import hashlib
import importlib.util
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("build_release", ROOT / "scripts/build_release.py")
module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(module)


class ReleaseTests(unittest.TestCase):
    def test_checked_in_plugin_mirror_and_metadata(self):
        for relative in module.RUNTIME:
            self.assertEqual((ROOT / relative).read_bytes(),
                (ROOT / "plugins/workspace-scout/skills/workspace-scout" / relative).read_bytes())
        meta = json.loads((ROOT / "plugins/workspace-scout/plugin.json").read_text())
        self.assertEqual(meta["version"], (ROOT / "VERSION").read_text().strip())
        ui = meta["extensions"]["com.openai"]["interface"]
        self.assertLessEqual(len(ui["displayName"]), 30)
        self.assertLessEqual(len(ui["shortDescription"]), 30)
        self.assertTrue(all(len(p) <= 128 for p in ui["defaultPrompt"]))

    def test_demo_arithmetic_snapshots(self):
        for name in ("montreal", "london", "singapore"):
            base = ROOT / "release/v1.0.0/demos"
            result = subprocess.run([sys.executable, str(ROOT / "scripts/check_candidates.py"),
                str(base / f"{name}.input.json")], capture_output=True, text=True, check=True)
            self.assertEqual(json.loads(result.stdout), json.loads((base / f"{name}.expected.json").read_text()))

    def test_reproducible_allowlisted_packages_and_mirrors(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for relative in module.RUNTIME + ["VERSION", "release/v1.0.0/listing.json", "release/v1.0.0/assets/icon.svg"]:
                dest = root / relative
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(ROOT / relative, dest)
            (root / ".env").write_text("MUST_NOT_SHIP=private")
            module.build(root)
            sums = (root / "dist/SHA256SUMS").read_bytes()
            module.build(root)
            self.assertEqual(sums, (root / "dist/SHA256SUMS").read_bytes())
            for relative in module.RUNTIME:
                self.assertEqual((ROOT / relative).read_bytes(),
                    (root / "plugins/workspace-scout/skills/workspace-scout" / relative).read_bytes())
            for package in (root / "dist").glob("*.zip"):
                with zipfile.ZipFile(package) as z:
                    self.assertTrue(all(not n.startswith("/") and ".." not in Path(n).parts for n in z.namelist()))
                    self.assertFalse(any(".env" in n or "tests/" in n or "release-private" in n for n in z.namelist()))
                    self.assertTrue(any(n.endswith("LICENSE") for n in z.namelist()))
            with zipfile.ZipFile(root / "dist/workspace-scout-openai-v1.0.0.zip") as z:
                self.assertIn("plugin.json", z.namelist())
                manifest = json.loads(z.read("plugin.json"))
                self.assertNotIn("screenshots", manifest["extensions"]["com.openai"]["interface"])
                self.assertFalse(any("mcp" in n or "hooks" in n for n in z.namelist()))

    def test_cli_bad_input_is_controlled(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "bad.json"
            p.write_text("[]")
            r = subprocess.run([sys.executable, str(ROOT / "scripts/check_candidates.py"), str(p)], capture_output=True, text=True)
            self.assertEqual(r.returncode, 2)
            self.assertIn("input must be an object", r.stderr)
            self.assertNotIn("Traceback", r.stderr)
