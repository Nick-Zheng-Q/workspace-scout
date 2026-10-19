#!/usr/bin/env python3
"""Build allowlisted, deterministic runtime/plugin packages. No network or publishing."""
import argparse
import hashlib
import json
import shutil
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RUNTIME = ["SKILL.md", "LICENSE", "references/candidate-record.md", "references/check-input.md",
           "references/search-guide.md", "scripts/check_candidates.py"]
URL = "https://github.com/Nick-Zheng-Q/workspace-scout"


def write_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def archive(path, files):
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for name, source in sorted(files.items()):
            info = zipfile.ZipInfo(name, date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            z.writestr(info, source.read_bytes())


def build(root=ROOT):
    version = (root / "VERSION").read_text().strip()
    release = root / "release" / f"v{version}"
    meta = json.loads((release / "listing.json").read_text())
    if meta["version"] != version:
        raise ValueError("VERSION and listing version differ")
    for field, limit in (("display_name", 30), ("short_description", 30), ("default_prompt", 128)):
        if not isinstance(meta[field], str) or not 0 < len(meta[field]) <= limit:
            raise ValueError(f"{field} exceeds the submission limit or is empty")
    plugin = root / "plugins/workspace-scout"
    # Generated files only. Authoring remains at the repository root.
    if plugin.is_symlink():
        raise ValueError("plugin destination must not be a symlink")
    if plugin.exists():
        shutil.rmtree(plugin)
    skill = plugin / "skills/workspace-scout"
    for relative in RUNTIME:
        target = skill / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(root / relative, target)
    (plugin / "assets").mkdir()
    shutil.copyfile(release / "assets/icon.svg", plugin / "assets/icon.svg")
    shutil.copyfile(root / "LICENSE", plugin / "LICENSE")
    common = {"name": meta["name"], "version": version, "description": meta["description"],
              "author": {"name": "Nick-Zheng-Q", "url": "https://github.com/Nick-Zheng-Q"},
              "homepage": URL, "repository": URL, "license": "PolyForm-Shield-1.0.0",
              "keywords": meta["keywords"]}
    interface = {"displayName": meta["display_name"], "shortDescription": meta["short_description"],
                 "longDescription": meta["description"] + " " + meta["disclosure"],
                 "developerName": "Nick-Zheng-Q", "category": meta["category"],
                 "capabilities": ["Compare workspaces"], "defaultPrompt": [meta["default_prompt"]],
                 "logo": "./assets/icon.svg", "composerIcon": "./assets/icon.svg",
                 "websiteURL": URL, "supportURL": URL + "/issues"}
    write_json(plugin / "plugin.json", {"$schema": "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json",
                **common, "extensions": {"com.openai": {"interface": interface}}})
    write_json(plugin / ".codex-plugin/plugin.json", {**common, "skills": "./skills/", "interface": interface})
    write_json(plugin / ".claude-plugin/plugin.json", common)
    (plugin / "README.md").write_text("# Workspace Scout\n\n" + meta["description"] + "\n\n" + meta["disclosure"] +
        "\n\nRequires host-authorized web search and browsing for discovery. No mandatory MCP or account. "
        "Python 3 is optional for the bundled arithmetic helper; without it, compare costs manually. "
        "No hooks, automatic contact, payment or background data collection.\n\n" +
        "Source, installation, evidence and support: " + URL + "\n", encoding="utf-8")
    write_json(root / ".claude-plugin/marketplace.json", {"name": "workspace-scout-marketplace",
        "owner": {"name": "Nick-Zheng-Q"}, "metadata": {"description": "Workspace research for solo founders and small teams"}, "plugins": [{"name": meta["name"],
        "source": "./plugins/workspace-scout", "description": meta["description"]}]})
    write_json(root / ".agents/plugins/marketplace.json", {"name": "workspace-scout-marketplace",
        "interface": {"displayName": "Workspace Scout"},
        "plugins": [{"name": meta["name"], "source": {"source": "local", "path": "./plugins/workspace-scout"},
        "policy": {"installation": "AVAILABLE", "authentication": "ON_INSTALL"}, "category": meta["category"]}]})
    dist = root / "dist"
    dist.mkdir(exist_ok=True)
    archive(dist / f"workspace-scout-skill-v{version}.zip", {"workspace-scout/" + f: root / f for f in RUNTIME})
    plugin_files = {p.relative_to(plugin).as_posix(): p for p in plugin.rglob("*") if p.is_file()}
    # Each plugin format has its own clean package, not conflicting client overlays.
    for platform in ("openai", "claude"):
        files = {n: p for n, p in plugin_files.items() if
                 not (platform == "openai" and (n.startswith(".claude-plugin/") or n.startswith(".codex-plugin/")))
                 and not (platform == "claude" and (n == "plugin.json" or n.startswith(".codex-plugin/")))}
        archive(dist / f"workspace-scout-{platform}-v{version}.zip", files)
    marketing = {p.relative_to(release).as_posix(): p for p in (release / "assets").glob("*") if p.is_file()}
    if len(marketing) > 1:
        marketing["LICENSE"] = root / "LICENSE"
        archive(dist / f"workspace-scout-media-v{version}.zip", marketing)
    artifacts = sorted(dist.glob(f"workspace-scout-*-v{version}.zip"))
    sums = "".join(f"{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.name}\n" for p in artifacts)
    (dist / "SHA256SUMS").write_text(sums, encoding="ascii")
    print(sums, end="")


if __name__ == "__main__":
    argparse.ArgumentParser(description=__doc__).parse_args()
    build()
