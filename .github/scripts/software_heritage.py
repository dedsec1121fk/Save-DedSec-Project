#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import pathlib
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone

API_ROOT = "https://archive.softwareheritage.org/api/1"
ARCHIVE_ROOT = "https://archive.softwareheritage.org"
OUTPUT = pathlib.Path(os.environ.get("SWH_STATE_PATH", "software-heritage.json"))
PREVIOUS_STATE_PATH = pathlib.Path(
    os.environ.get("SWH_PREVIOUS_STATE_PATH", "controller/update.json")
)
RETRYABLE = {408, 425, 429, 500, 502, 503, 504}
USER_AGENT = "Save-DedSec-Project Software-Heritage sync"


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def parse_json_env(name: str) -> list[dict]:
    try:
        value = json.loads(os.environ.get(name, "[]"))
    except json.JSONDecodeError:
        return []
    return value if isinstance(value, list) else []


def load_previous_records() -> dict[str, dict]:
    try:
        payload = json.loads(PREVIOUS_STATE_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}

    software_state = payload.get("software_heritage", {})
    records = software_state.get("repositories", {}) if isinstance(software_state, dict) else {}
    if not isinstance(records, dict):
        return {}
    return {
        str(repository): record
        for repository, record in records.items()
        if isinstance(record, dict)
    }


def github_origin(repository: str) -> str:
    return f"https://github.com/{repository.strip().strip('/')}"


def browse_url(origin: str) -> str:
    return ARCHIVE_ROOT + "/browse/origin/?" + urllib.parse.urlencode({"origin_url": origin})


def snapshot_browse_url(swhid: str) -> str | None:
    value = str(swhid or "").strip()
    if not value:
        return None
    return f"{ARCHIVE_ROOT}/{value}/"


def retry_delay(attempt: int, retry_after: str | None = None) -> int:
    if retry_after and retry_after.isdigit():
        return min(120, max(1, int(retry_after)))
    return min(60, 4 * (2 ** min(attempt - 1, 4)))


def request_json(method: str, url: str, *, attempts: int = 4, allow_404: bool = False):
    last_error: BaseException | None = None
    for attempt in range(1, attempts + 1):
        request = urllib.request.Request(
            url,
            data=b"" if method == "POST" else None,
            method=method,
            headers={
                "Accept": "application/json",
                "User-Agent": USER_AGENT,
                "Cache-Control": "no-cache",
            },
        )
        try:
            with urllib.request.urlopen(request, timeout=90) as response:
                return json.load(response)
        except urllib.error.HTTPError as error:
            if allow_404 and error.code == 404:
                return None
            last_error = error
            if error.code == 429:
                raise RuntimeError(
                    "Software Heritage rate limit reached; retry on the next workflow run"
                ) from error
            if error.code not in RETRYABLE:
                raise
            delay = retry_delay(attempt, error.headers.get("Retry-After"))
            print(f"Software Heritage HTTP {error.code}; retrying in {delay}s.")
            time.sleep(delay)
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as error:
            last_error = error
            delay = retry_delay(attempt)
            print(f"Software Heritage temporary error; retrying in {delay}s.")
            time.sleep(delay)
    raise RuntimeError(f"Software Heritage request failed: {last_error!r}")


def latest_save_request(origin: str) -> dict | None:
    url = API_ROOT + "/origin/save/?" + urllib.parse.urlencode(
        {"visit_type": "git", "origin_url": origin}
    )
    payload = request_json("GET", url, allow_404=True)
    if not isinstance(payload, list) or not payload:
        return None
    return max(payload, key=lambda item: str(item.get("save_request_date") or ""))


def request_save(origin: str) -> dict:
    url = API_ROOT + "/origin/save/?" + urllib.parse.urlencode(
        {"visit_type": "git", "origin_url": origin}
    )
    payload = request_json("POST", url)
    return payload if isinstance(payload, dict) else {}


def latest_visit(origin: str) -> dict | None:
    encoded = urllib.parse.quote(origin, safe=":/")
    url = (
        f"{API_ROOT}/origin/{encoded}/visit/latest/"
        "?require_snapshot=true&visit_type=git"
    )
    payload = request_json("GET", url, allow_404=True)
    return payload if isinstance(payload, dict) else None


def parse_datetime(value: object) -> datetime | None:
    text = str(value or "").strip()
    if not text:
        return None
    try:
        return datetime.fromisoformat(text.replace("Z", "+00:00"))
    except ValueError:
        return None


def request_is_recent(request: dict | None) -> bool:
    if not request:
        return False
    when = parse_datetime(request.get("save_request_date"))
    if when is None:
        return False
    return (datetime.now(timezone.utc) - when).total_seconds() < 3600


def active_request(request: dict | None) -> bool:
    if not request:
        return False
    return str(request.get("save_task_status") or "").strip().lower() in {
        "not created",
        "pending",
        "scheduled",
        "running",
    }


def normalize_targets(targets: list[dict]) -> list[dict]:
    seen: set[str] = set()
    normalized: list[dict] = []
    for target in targets:
        repository = str(target.get("repository") or "").strip().strip("/")
        if not repository or repository in seen:
            continue
        seen.add(repository)
        normalized.append(target)
    return normalized


def previous_record_needs_link_check(record: dict | None) -> bool:
    if not isinstance(record, dict) or not record:
        return False
    return bool(
        record.get("save_request_date")
        or record.get("save_requested_this_run")
        or record.get("awaiting_link_check")
        or record.get("snapshot_swhid")
    )


def carry_confirmed_snapshot(record: dict | None) -> tuple[str | None, str | None]:
    if not isinstance(record, dict):
        return None, None
    swhid = str(record.get("snapshot_swhid") or "").strip() or None
    url = str(record.get("snapshot_url") or "").strip() or None
    if swhid and not url:
        url = snapshot_browse_url(swhid)
    return swhid, url


def main() -> int:
    all_targets = normalize_targets(parse_json_env("ALL_TARGETS"))
    selected_repositories = {
        str(target.get("repository") or "").strip().strip("/")
        for target in parse_json_env("SELECTED_TARGETS")
    }
    previous_records = load_previous_records()

    state: dict = {
        "schema_version": 2,
        "checked_at_utc": utc_now(),
        "service": "Software Heritage",
        "link_resolution_policy": (
            "Save requests made in the current workflow run are not resolved into README links "
            "until a later workflow run."
        ),
        "repositories": {},
    }

    for target in all_targets:
        repository = str(target.get("repository") or "").strip().strip("/")
        origin = github_origin(repository)
        previous_record = previous_records.get(repository, {})
        previous_swhid, previous_snapshot_url = carry_confirmed_snapshot(previous_record)
        record = {
            "repository": repository,
            "title": target.get("archive_label") or target.get("title") or repository,
            "origin_url": origin,
            "browse_url": browse_url(origin),
            "selected_this_run": repository in selected_repositories,
            "save_requested_this_run": False,
            "save_request_status": None,
            "save_task_status": None,
            "save_request_date": None,
            "link_checked_this_run": False,
            "link_check_basis": "previous_run_only",
            "awaiting_link_check": False,
            "latest_visit_date": previous_record.get("latest_visit_date"),
            "latest_visit_status": previous_record.get("latest_visit_status"),
            "snapshot_swhid": previous_swhid,
            "snapshot_url": previous_snapshot_url,
            "error": None,
        }

        try:
            # Resolve only requests that were already present in the controller state
            # before this workflow started. Never use a Save Code Now request made
            # later in this same run to publish a Software Heritage README link.
            if previous_record_needs_link_check(previous_record):
                record["link_checked_this_run"] = True
                visit = latest_visit(origin)
                if visit:
                    record["latest_visit_date"] = visit.get("date")
                    record["latest_visit_status"] = visit.get("status")
                    snapshot = str(visit.get("snapshot") or "").strip()
                    request_time = parse_datetime(previous_record.get("save_request_date"))
                    visit_time = parse_datetime(visit.get("date"))
                    visit_is_new_enough = (
                        request_time is None
                        or visit_time is None
                        or visit_time >= request_time
                    )
                    if snapshot and visit_is_new_enough:
                        record["snapshot_swhid"] = f"swh:1:snp:{snapshot}"
                        record["snapshot_url"] = snapshot_browse_url(
                            record["snapshot_swhid"]
                        )
                    elif snapshot and not record.get("snapshot_swhid"):
                        # A snapshot exists, but it predates the request from the
                        # previous workflow run. Keep waiting rather than publish
                        # a stale link as if the new preservation had completed.
                        record["awaiting_link_check"] = True

            # The save-request status check is used only to avoid duplicate requests.
            # It does not authorize publishing a new link in the current run.
            previous_request = latest_save_request(origin)
            current_request = previous_request

            if repository in selected_repositories and not (
                active_request(previous_request) or request_is_recent(previous_request)
            ):
                current_request = request_save(origin)
                record["save_requested_this_run"] = True
                record["awaiting_link_check"] = True
                # Keep calls gentle when several repositories are selected.
                time.sleep(2)
            elif previous_record_needs_link_check(previous_record) and not record.get("snapshot_swhid"):
                record["awaiting_link_check"] = True

            if isinstance(current_request, dict):
                record["save_request_status"] = current_request.get("save_request_status")
                record["save_task_status"] = current_request.get("save_task_status")
                record["save_request_date"] = current_request.get("save_request_date")

            # Even if the POST response happens to expose snapshot fields, intentionally
            # ignore them here. The next workflow run is responsible for link resolution.
            if record["save_requested_this_run"]:
                record["awaiting_link_check"] = True

        except Exception as error:
            record["error"] = f"{type(error).__name__}: {error}"
            print(f"::warning title=Software Heritage::{repository}: {record['error']}")

        state["repositories"][repository] = record

    OUTPUT.write_text(
        json.dumps(state, indent=2, ensure_ascii=False, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(f"Software Heritage state written to {OUTPUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
