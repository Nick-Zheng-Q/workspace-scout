#!/bin/sh
set -eu

repo=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd -P)
tmp=$(mktemp -d "${TMPDIR:-/tmp}/workspace-scout-install-test.XXXXXX")
trap 'rm -rf -- "$tmp"' EXIT HUP INT TERM

mkdir -p "$tmp/source/scripts" "$tmp/source/references"
cp "$repo/install.sh" "$repo/update.sh" "$repo/SKILL.md" "$repo/LICENSE" "$tmp/source/"
cp "$repo"/references/*.md "$tmp/source/references/"
cp "$repo/scripts/check_candidates.py" "$tmp/source/scripts/"
mkdir "$tmp/dest"

"$tmp/source/install.sh" --dest-dir "$tmp/dest" > "$tmp/install.out"
[ -f "$tmp/dest/workspace-scout/SKILL.md" ]
[ -f "$tmp/dest/workspace-scout/LICENSE" ]
grep -q 'PolyForm Shield License 1.0.0' "$tmp/dest/workspace-scout/LICENSE"
[ -f "$tmp/dest/workspace-scout/references/search-guide.md" ]
[ -f "$tmp/dest/workspace-scout/scripts/check_candidates.py" ]
[ ! -f "$tmp/dest/workspace-scout/scripts/install.sh" ]
if "$tmp/source/install.sh" --dest-dir "$tmp/dest" > /dev/null 2>&1; then
  echo "Install should refuse to overwrite" >&2
  exit 1
fi

printf '\nTEST_UPDATE_MARKER\n' >> "$tmp/source/references/search-guide.md"
"$tmp/source/update.sh" --dest-dir "$tmp/dest" > "$tmp/update.out"
grep -q TEST_UPDATE_MARKER "$tmp/dest/workspace-scout/references/search-guide.md"
backup=$(find "$tmp/workspace-scout-backups" -mindepth 1 -maxdepth 1 -type d | head -1)
[ -n "$backup" ]
if grep -q TEST_UPDATE_MARKER "$backup/references/search-guide.md"; then
  echo "Backup should contain the previous version" >&2
  exit 1
fi

mkdir -p "$tmp/other/workspace-scout"
printf 'not a skill\n' > "$tmp/other/workspace-scout/SKILL.md"
if "$tmp/source/update.sh" --dest-dir "$tmp/other" > /dev/null 2>&1; then
  echo "Update should refuse an unrelated directory" >&2
  exit 1
fi

"$tmp/source/install.sh" --project > /dev/null
[ -f "$tmp/source/.agents/skills/workspace-scout/SKILL.md" ]
"$tmp/source/update.sh" --project > /dev/null

mkdir -p "$tmp/symlinks"
ln -s "$tmp/dest/workspace-scout" "$tmp/symlinks/workspace-scout"
if "$tmp/source/update.sh" --dest-dir "$tmp/symlinks" > /dev/null 2>&1; then
  echo "Update should refuse a symlinked installation" >&2
  exit 1
fi

echo "Installer tests passed"
