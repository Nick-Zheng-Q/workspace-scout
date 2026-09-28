#!/bin/sh
# Install this checkout's runtime Skill files. Run from any directory.
set -eu

usage() {
  echo "Usage: $0 [--project | --dest-dir DIR]" >&2
  echo "       $0 --update [--project | --dest-dir DIR]" >&2
  exit 2
}

mode=install
if [ "${1-}" = "--update" ]; then
  mode=update
  shift
fi

source_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd -P)
dest_dir=${HOME:?}/.agents/skills
case "${1-}" in
  '') ;;
  --project)
    dest_dir=$source_dir/.agents/skills
    shift
    ;;
  --dest-dir)
    [ "$#" -ge 2 ] && [ -n "$2" ] || usage
    dest_dir=$2
    shift 2
    ;;
  *) usage ;;
esac
[ "$#" -eq 0 ] || usage

for file in SKILL.md LICENSE references/candidate-record.md references/check-input.md references/search-guide.md scripts/check_candidates.py; do
  [ -f "$source_dir/$file" ] || { echo "Missing source file: $source_dir/$file" >&2; exit 1; }
done
grep -qx 'name: workspace-scout' "$source_dir/SKILL.md" || {
  echo "Source SKILL.md is not workspace-scout" >&2
  exit 1
}

mkdir -p "$dest_dir"
dest_dir=$(CDPATH= cd -- "$dest_dir" && pwd -P)
target=$dest_dir/workspace-scout
if [ -L "$target" ]; then
  echo "Refusing to replace symlink: $target" >&2
  exit 1
fi
if [ "$mode" = install ]; then
  if [ -e "$target" ]; then
    echo "Already installed: $target; run update.sh instead" >&2
    exit 1
  fi
else
  if [ ! -f "$target/SKILL.md" ] || ! grep -qx 'name: workspace-scout' "$target/SKILL.md"; then
    echo "No workspace-scout installation found at $target; run install.sh first" >&2
    exit 1
  fi
fi

stage=$(mktemp -d "$dest_dir/.workspace-scout-stage.XXXXXX")
cleanup() {
  if [ -n "$stage" ] && [ -d "$stage" ]; then rm -rf -- "$stage"; fi
}
trap cleanup EXIT HUP INT TERM
cp "$source_dir/SKILL.md" "$stage/SKILL.md"
cp "$source_dir/LICENSE" "$stage/LICENSE"
cp -R "$source_dir/references" "$stage/references"
mkdir "$stage/scripts"
cp "$source_dir/scripts/check_candidates.py" "$stage/scripts/check_candidates.py"

if [ "$mode" = install ]; then
  mv -- "$stage" "$target"
  stage=
  echo "Installed workspace-scout: $target"
else
  backup_dir=$(dirname -- "$dest_dir")/workspace-scout-backups
  mkdir -p "$backup_dir"
  backup=$backup_dir/workspace-scout-$(date +%Y%m%d-%H%M%S)-$$
  mv -- "$target" "$backup"
  if ! mv -- "$stage" "$target"; then
    mv -- "$backup" "$target"
    echo "Update failed; original installation restored" >&2
    exit 1
  fi
  stage=
  echo "Updated workspace-scout: $target"
  echo "Previous version backed up: $backup"
fi
