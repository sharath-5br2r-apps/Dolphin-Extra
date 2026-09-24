#!/usr/bin/env python3
"""Convert Dolphin-Extra's raw build.json into the unified release manifest."""
import json
import os
import re
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path


def apk_metadata(path):
    result = {"min_sdk": None, "version_code": None, "densities": [], "native_libraries": []}
    tools = [shutil.which("aapt2"), shutil.which("aapt")]
    android_home = os.environ.get("ANDROID_HOME", "")
    if android_home:
        tools += sorted(Path(android_home).glob("build-tools/*/aapt2"), reverse=True)
        tools += sorted(Path(android_home).glob("build-tools/*/aapt"), reverse=True)
    tool = next((str(candidate) for candidate in tools if candidate), None)
    if not tool:
        return result
    output = subprocess.run([tool, "dump", "badging", str(path)], capture_output=True,
                            text=True, check=False).stdout
    patterns = {
        "min_sdk": r"(?:sdkVersion|minSdkVersion):'([^']+)'",
        "version_code": r"versionCode='([^']+)'",
        "densities": r"densities: '([^']+)'",
        "native_libraries": r"native-code: '([^']+)'",
    }
    for key, pattern in patterns.items():
        match = re.search(pattern, output)
        if match:
            result[key] = match.group(1).split() if key.endswith("s") else match.group(1)
    return result


def main():
    build = os.environ.get("NEXT_VER_CODE", "").strip()
    if not build:
        raise SystemExit("NEXT_VER_CODE is required")
    channel = "beta" if os.environ.get("IS_PRERELEASE", "false").lower() == "true" else "stable"
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    raw = json.loads(Path("build.json").read_text(encoding="utf-8"))
    files = {}
    for info in raw.values():
        assets = info.get("assets", [])
        for asset in assets:
            filename = asset["name"]
            lower = filename.lower()
            if not lower.endswith((".apk", ".apkm", ".xapk", ".apks", ".zip")):
                continue
            is_apk = lower.endswith((".apk", ".apkm", ".xapk", ".apks"))
            apk = apk_metadata(Path("release-files") / filename) if is_apk else {}
            arch = asset.get("arch")
            if not arch or arch == "universal":
                if "x86_64" in filename.lower():
                    arch = "x86_64"
                elif "arm64-v8a" in filename.lower() or "aarch64" in filename.lower():
                    arch = "arm64-v8a"
                elif "arm-v7a" in filename.lower() or "armeabi-v7a" in filename.lower():
                    arch = "arm"
                else:
                    arch = "universal"
            record = {
                "name": "dolphin-extra",
                "version": info.get("version", ""),
                "appKey": "dolphin-extra",
                "appName": "Dolphin Extra",
                "arch": arch,
                "fileType": "APK" if is_apk else "Module",
                "brandKey": None,
                "brandName": None,
                "variant": None,
                "subVariant": None,
                "packageName": (info.get("package_name") or "org.dolphinemu.dolphinemu") if is_apk else None,
                "patchSources": [],
                "changelogUrls": info.get("changelog_urls", []),
                "changelogs": info.get("changelogs", []),
                "appliedPatches": asset.get("appliedPatches", []),
                "skippedPatches": asset.get("skippedPatches", []),
                "failedPatches": asset.get("failedPatches", []),
                "originBuild": build,
                "publishedAt": now,
            }
            if is_apk:
                record.update({
                    "densities": apk.get("densities", []),
                    "nativeLibraries": apk.get("native_libraries", []),
                    "minSdk": apk.get("min_sdk"),
                    "versionCode": apk.get("version_code"),
                })
            files[filename] = {key: value for key, value in record.items() if value is not None and value != []}
    manifest = {"schema": 1, "kind": "build",
                "meta": {"build": build, "channel": channel, "publishedAt": now},
                "files": files}
    out = Path("temp/manifest/build.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(manifest, separators=(",", ":")), encoding="utf-8")
    Path("release-files/build.json").write_text(out.read_text(encoding="utf-8"), encoding="utf-8")
    print(f"Wrote {out} with {len(files)} file entries")


if __name__ == "__main__":
    main()
