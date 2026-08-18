#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import html
import json
import os
import pathlib
import re
import shutil
import subprocess
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone

ITEM = os.environ.get("APK_IA_ITEM_IDENTIFIER", "dedsec1121fk-dedsec-project-apk-backups")
ACCESS_KEY = os.environ.get("IA_ACCESS_KEY", "")
SECRET_KEY = os.environ.get("IA_SECRET_KEY", "")
OUTPUT = pathlib.Path(os.environ.get("APK_STATE_PATH", "apks.json"))
USER_AGENT = "Save-DedSec-Project APK preservation"
RETRYABLE = {408, 425, 429, 500, 502, 503, 504}

APK_SOURCES = [
    {"filename": "F-Droid.apk", "type": "direct", "url": "https://f-droid.org/F-Droid.apk"},
    {"filename": "Termux.apk", "type": "fdroid_package", "package": "com.termux"},
    {"filename": "Termux_API.apk", "type": "fdroid_package", "package": "com.termux.api"},
    {"filename": "Termux_Styling.apk", "type": "fdroid_package", "package": "com.termux.styling"},
]


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def sha256_file(path: pathlib.Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def fetch_bytes(url: str, *, timeout: int = 120) -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return response.read()


def resolve_fdroid_package(package: str) -> str:
    page_url = f"https://f-droid.org/packages/{urllib.parse.quote(package, safe='')}/"
    text = fetch_bytes(page_url, timeout=90).decode("utf-8", "replace")
    patterns = [
        r'href="([^"]+\.apk)"[^>]*>\s*Download APK',
        r'href="([^"]*' + re.escape(package) + r'[^"]*\.apk)"',
        r'href="([^"]+\.apk)"',
    ]
    for pattern in patterns:
        match = re.search(pattern, text, flags=re.IGNORECASE | re.DOTALL)
        if not match:
            continue
        value = html.unescape(match.group(1).strip())
        return urllib.parse.urljoin("https://f-droid.org/", value)
    raise RuntimeError(f"Unable to resolve F-Droid APK for {package}")


def download(url: str, path: pathlib.Path) -> None:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=180) as response, path.open("wb") as output:
        shutil.copyfileobj(response, output, length=1024 * 1024)


def validate_apk(path: pathlib.Path) -> None:
    if path.stat().st_size < 10_000:
        raise RuntimeError("downloaded file is too small to be a valid APK")
    with path.open("rb") as stream:
        magic = stream.read(4)
    if magic != b"PK\x03\x04":
        raise RuntimeError("downloaded file does not have the expected APK/ZIP signature")


def fetch_previous_manifest() -> dict | None:
    item = urllib.parse.quote(ITEM, safe="")
    url = f"https://archive.org/download/{item}/manifest.json?ts={int(time.time())}"
    request = urllib.request.Request(
        url,
        headers={"Accept": "application/json", "Cache-Control": "no-cache", "User-Agent": USER_AGENT},
    )
    try:
        with urllib.request.urlopen(request, timeout=90) as response:
            payload = json.load(response)
        return payload if isinstance(payload, dict) else {}
    except urllib.error.HTTPError as error:
        if error.code == 404:
            return {}
        print(f"::warning title=APK manifest::HTTP {error.code}; remote APK state is unavailable, so uploads will be deferred.")
        return None
    except Exception as error:
        print(f"::warning title=APK manifest::{type(error).__name__}: {error}; uploads will be deferred.")
        return None


def check_capacity() -> bool:
    if not ACCESS_KEY:
        return False
    query = urllib.parse.urlencode({"check_limit": "1", "accesskey": ACCESS_KEY, "bucket": ITEM})
    try:
        with urllib.request.urlopen(
            urllib.request.Request(f"https://s3.us.archive.org/?{query}", headers={"User-Agent": USER_AGENT}),
            timeout=60,
        ) as response:
            payload = json.load(response)
        return str(payload.get("over_limit", "0")) != "1"
    except Exception:
        return False


def wait_for_capacity() -> None:
    for attempt in range(1, 7):
        if check_capacity():
            return
        delay = min(180, 20 + attempt * 10)
        print(f"Internet Archive APK item is busy; retrying capacity check in {delay}s.")
        time.sleep(delay)
    raise RuntimeError("Internet Archive capacity remained unavailable for APK preservation")


def remote_url(name: str) -> str:
    return (
        "https://s3.us.archive.org/"
        + urllib.parse.quote(ITEM, safe="")
        + "/"
        + urllib.parse.quote(name, safe="/~._-()")
    )


def upload(path: pathlib.Path, remote_name: str, *, metadata: bool = False) -> None:
    wait_for_capacity()
    args = [
        "curl", "--silent", "--show-error", "--fail-with-body", "--location", "--location-trusted",
        "--retry", "8", "--retry-connrefused", "--retry-max-time", "3600", "--connect-timeout", "45",
        "--header", f"Authorization: LOW {ACCESS_KEY}:{SECRET_KEY}",
        "--header", "x-amz-auto-make-bucket:1",
        "--header", "x-archive-ignore-preexisting-bucket:1",
        "--header", "x-archive-keep-old-version:0",
        "--header", "x-archive-queue-derive:0",
    ]
    if metadata:
        args.extend([
            "--header", "x-archive-meta-title:DedSec Project APK Preservation",
            "--header", "x-archive-meta-creator:DedSec Project",
            "--header", "x-archive-meta-mediatype:software",
            "--header", "x-archive-meta-description:Current APK dependencies used by the Save DedSec Project local backup routine.",
            "--header", "x-archive-meta-subject:DedSec Project; Termux; F-Droid; APK; software preservation",
        ])
    args.extend(["--upload-file", str(path), remote_url(remote_name)])
    subprocess.run(args, check=True)
    time.sleep(10)


def main() -> int:
    if not ACCESS_KEY or not SECRET_KEY:
        raise SystemExit("Internet Archive credentials are required for APK preservation")

    previous = fetch_previous_manifest()
    remote_manifest_reliable = previous is not None
    previous = previous or {}
    previous_files = previous.get("files", {}) if isinstance(previous.get("files"), dict) else {}

    state = {
        "schema_version": 1,
        "checked_at_utc": utc_now(),
        "ia_item": ITEM,
        "archive_url": f"https://archive.org/details/{ITEM}",
        "files": {},
        "changed": [],
        "failures": [],
        "uploaded": False,
        "remote_manifest_reliable": remote_manifest_reliable,
    }

    with tempfile.TemporaryDirectory(prefix="dedsec-apks-") as temp_dir:
        root = pathlib.Path(temp_dir)
        for source in APK_SOURCES:
            filename = source["filename"]
            target = root / filename
            try:
                url = source["url"] if source["type"] == "direct" else resolve_fdroid_package(source["package"])
                download(url, target)
                validate_apk(target)
                digest = sha256_file(target)
                metadata = {
                    "source_url": url,
                    "sha256": digest,
                    "size": target.stat().st_size,
                }
                state["files"][filename] = metadata
                old = previous_files.get(filename, {}) if isinstance(previous_files.get(filename), dict) else {}
                if old.get("sha256") != digest:
                    state["changed"].append(filename)
            except Exception as error:
                state["failures"].append({"filename": filename, "error": f"{type(error).__name__}: {error}"})
                print(f"::warning title=APK download::{filename}: {error}")

        complete_set = len(state["files"]) == len(APK_SOURCES) and not state["failures"]
        if complete_set and not remote_manifest_reliable:
            print("::warning title=APK preservation::Remote manifest could not be checked; APK uploads were deferred to avoid unnecessary Internet Archive writes.")
        elif complete_set:
            manifest = {
                "schema_version": 1,
                "generated_at_utc": utc_now(),
                "source": "Settings.py PROJECT_SAVE_APK_SOURCES",
                "files": state["files"],
            }
            manifest_path = root / "manifest.json"
            manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
            checksum_path = root / "SHA256SUMS.txt"
            checksum_path.write_text(
                "".join(f"{entry['sha256']}  {name}\n" for name, entry in sorted(state["files"].items())),
                encoding="utf-8",
            )

            if state["changed"] or not previous_files:
                first_write = not bool(previous_files)
                for filename in state["changed"] or list(state["files"]):
                    upload(root / filename, filename, metadata=first_write)
                    first_write = False
                upload(manifest_path, "manifest.json", metadata=first_write)
                upload(checksum_path, "SHA256SUMS.txt")
                state["uploaded"] = True
            else:
                print("APK hashes are unchanged; Internet Archive uploads skipped.")
        else:
            print("::warning title=APK preservation::One or more APK downloads failed; remote APK state was left unchanged.")

    OUTPUT.write_text(json.dumps(state, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    print(f"APK preservation state written to {OUTPUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
