# Save DedSec Project

This repository keeps the current DedSec Project ecosystem synchronized with Internet Archive and progressively captured by the Wayback Machine.

## Fixed Architecture

Internet Archive file synchronization and Wayback capture processing are separate:

1. Repository files are mirrored first.
2. Every successful file upload or deletion is checkpointed immediately.
3. The file-sync job finishes without waiting for thousands of Wayback captures.
4. One serial Wayback job processes a limited resumable queue.
5. Remaining Wayback URLs continue during the next scheduled or manual run.

This prevents Wayback rate limits from canceling otherwise successful repository backups.

## Forking This Archive Controller

Fork owners can configure their own Internet Archive credentials and item identifiers by following [Fork Instructions](Fork%20Instructions.md).

<!-- PERMANENT_ARCHIVE_LINKS_START -->
## Permanent Internet Archive Links

- **DedSec main:** https://archive.org/details/dedsec1121fk-dedsec-project-repository-snapshots
- **DedSec backup:** https://archive.org/details/dedsec1121fk-dedsec-project-backup-repository-snapshots
- **Websites:** https://archive.org/details/dedsec1121fk-dedsec-website-snapshots
- **GitHub profile:** https://archive.org/details/dedsec1121fk-github-profile-repository-snapshots
- **Corrupted Files:** https://archive.org/details/dedsec1121fk-corrupted-files-project-repository-snapshots
- **Pocket AI:** https://archive.org/details/dedsec1121fk-pocket-ai-repository-snapshots
- **Offline Survival:** https://archive.org/details/dedsec1121fk-offline-survival-project-repository-snapshots
- **Hacking Guide Project:** https://archive.org/details/dedsec1121fk-hacking-guide-project-repository-snapshots
- **Save DedSec Project:** https://archive.org/details/dedsec1121fk-save-dedsec-project-repository-snapshots

This section is regenerated on every archive run from the target configuration in `.github/workflows/internet-archive.yml`.
<!-- PERMANENT_ARCHIVE_LINKS_END -->

## Incremental Internet Archive Mirror

The first successful run uploads every current file. Later runs use SHA-256 hashes:

- New files are uploaded.
- Changed files replace their matching archive objects.
- Deleted repository files are deleted from the current mirror.
- Unchanged files are skipped.
- Missing remote mirror files are restored.
- Git history is stored in `git-history.bundle`.

Every target item contains:

```text
mirror/<original path>
git-history.bundle
manifest.json
SHA256SUMS.txt
archive-state/update.json
```

The Internet Archive checkpoint is updated after every successful file operation.

A synchronized combined copy is stored here:

```text
update.json
```

If Internet Archive temporarily returns HTTP 503 during a first run, the workflow falls back to the GitHub `update.json` state or starts a safe initial sync. It never deletes unknown files without a trustworthy previous state.

## Resumable Wayback Queue

Wayback URLs are not submitted in parallel anymore.

A single job:

- Processes at most 360 URLs per workflow run.
- Runs for at most three hours.
- Checkpoints after every processed URL.
- Treats active-session limits and HTTP 429/500/502/503/504 as temporary.
- Leaves unfinished URLs in the queue for the next run.
- Does not fail the Internet Archive file backup merely because Wayback is busy.

## Backup Schedule

All scheduled times use `Europe/Athens`.

| Day | Greece time | Archive targets |
|---|---:|---|
| Monday | 11:11 | DedSec Project main/backup + website source + both live websites |
| Tuesday | 05:05 | GitHub profile, Corrupted Files, Pocket AI, Offline Survival, Hacking Guide Project and Save DedSec Project |
| Wednesday | 22:22 | DedSec Project main/backup + website source + both live websites |
| Friday | 12:12 | GitHub profile, Corrupted Files, Pocket AI, Offline Survival, Hacking Guide Project and Save DedSec Project |
| Saturday | 00:00 | DedSec Project main/backup + website source + both live websites |
| 1st & 3rd Sunday | 03:33 | GitHub profile, Corrupted Files, Pocket AI, Offline Survival, Hacking Guide Project and Save DedSec Project |
| 2nd & 4th Sunday | 03:00 | GitHub profile, Corrupted Files, Pocket AI, Offline Survival, Hacking Guide Project and Save DedSec Project |

If a month has a fifth Sunday, no Sunday backup is scheduled for that fifth occurrence.

### Monthly Backup Order Rotation

Scheduled repository backups run one target at a time so the configured order is meaningful.

- **January, March, May, July, September and November:** targets run in the exact order listed in the schedule above.
- **February, April, June, August, October and December:** the same target list runs in reverse order.
- **Manual runs:** keep the normal listed order.

For the DedSec/website group, the normal repository order is DedSec main → DedSec backup → website source/live websites; the reverse order starts with the website target. For the other-projects group, the normal order is GitHub profile → Corrupted Files → Pocket AI → Offline Survival → Hacking Guide Project → Save DedSec Project, and even-numbered months reverse that sequence.

## Official Websites

- **Main website:** https://ded-sec.space/
- **Backup website:** https://ded-sec.online/

## Repositories

- **Website source:** https://github.com/dedsec1121fk/dedsec1121fk.github.io
- **DedSec Project main:** https://github.com/dedsec1121fk/DedSec
- **DedSec Project backup:** https://github.com/sal-scar/DedSec
- **GitHub profile:** https://github.com/dedsec1121fk/dedsec1121fk
- **Corrupted Files Project:** https://github.com/dedsec1121fk/Corrupted-Files-Project
- **Pocket AI:** https://github.com/dedsec1121fk/Pocket-AI
- **Offline Survival Project:** https://github.com/dedsec1121fk/Offline-Survival-Project
- **Hacking Guide Project:** https://github.com/dedsec1121fk/Hacking-Guide-Project
- **Save DedSec Project:** https://github.com/dedsec1121fk/Save-DedSec-Project

## Automatic Archive Status

<!-- WEBSITES_ARCHIVE_STATUS_START -->
### DedSec Websites and Website Source

**Current file-sync status:** `in_progress`  
**Last complete or attempted save:** 2026-08-04 10:51:33 EEST  
**Current mirrored files:** 825  
**Latest file update:** 0 uploaded, 0 deleted, 789 unchanged.  
**Mirror verification:** `True`  
**Wayback queue remaining:** 2555  
**Wayback captures accepted:** 685  
**Scheduled time(s):** Monday 11:11, Wednesday 22:22 and Saturday 00:00 Europe/Athens  
**Resume mode:** File uploads and Wayback URLs are checkpointed separately.

- [Internet Archive current mirror](https://archive.org/details/dedsec1121fk-dedsec-website-snapshots)
- [Wayback Machine capture history](https://web.archive.org/web/*/https://github.com/dedsec1121fk/dedsec1121fk.github.io*)
- [Last archived commit](https://github.com/dedsec1121fk/dedsec1121fk.github.io/commit/243e2386e60a00133b257f1d8a593be737432077)
- [https://ded-sec.space Wayback history](https://web.archive.org/web/*/https://ded-sec.space/*)
- [https://ded-sec.online Wayback history](https://web.archive.org/web/*/https://ded-sec.online/*)

This section is generated from `update.json`.
<!-- WEBSITES_ARCHIVE_STATUS_END -->

<!-- DEDSEC_MAIN_ARCHIVE_STATUS_START -->
### DedSec Project Main Repository

**Current file-sync status:** `in_progress`  
**Last complete or attempted save:** 2026-08-04 10:52:40 EEST  
**Current mirrored files:** 587  
**Latest file update:** 0 uploaded, 0 deleted, 587 unchanged.  
**Mirror verification:** `True`  
**Wayback queue remaining:** 30  
**Wayback captures accepted:** 387  
**Scheduled time(s):** Monday 11:11, Wednesday 22:22 and Saturday 00:00 Europe/Athens  
**Resume mode:** File uploads and Wayback URLs are checkpointed separately.

- [Internet Archive current mirror](https://archive.org/details/dedsec1121fk-dedsec-project-repository-snapshots)
- [Wayback Machine capture history](https://web.archive.org/web/*/https://github.com/dedsec1121fk/DedSec*)
- [Last archived commit](https://github.com/dedsec1121fk/DedSec/commit/160a769d7c173da58ec9268c8263c0d947b01c31)

This section is generated from `update.json`.
<!-- DEDSEC_MAIN_ARCHIVE_STATUS_END -->

<!-- DEDSEC_BACKUP_ARCHIVE_STATUS_START -->
### DedSec Project Backup Repository

**Current file-sync status:** `in_progress`  
**Last complete or attempted save:** 2026-08-07 09:05:38 EEST  
**Current mirrored files:** 587  
**Latest file update:** 0 uploaded, 0 deleted, 587 unchanged.  
**Mirror verification:** `True`  
**Wayback queue remaining:** 819  
**Wayback captures accepted:** 385  
**Scheduled time(s):** Monday 11:11, Wednesday 22:22 and Saturday 00:00 Europe/Athens  
**Resume mode:** File uploads and Wayback URLs are checkpointed separately.

- [Internet Archive current mirror](https://archive.org/details/dedsec1121fk-dedsec-project-backup-repository-snapshots)
- [Wayback Machine capture history](https://web.archive.org/web/*/https://github.com/sal-scar/DedSec*)
- [Last archived commit](https://github.com/sal-scar/DedSec/commit/28dbb1cb4a8d1df28c34b9aad8096a1cc90b2b28)

This section is generated from `update.json`.
<!-- DEDSEC_BACKUP_ARCHIVE_STATUS_END -->

<!-- GITHUB_PROFILE_ARCHIVE_STATUS_START -->
### DedSec GitHub Profile Repository

**Current file-sync status:** `complete`  
**Last complete or attempted save:** 2026-08-09 20:04:20 EEST  
**Current mirrored files:** 9  
**Latest file update:** 3 uploaded, 0 deleted, 6 unchanged.  
**Mirror verification:** `True`  
**Wayback queue remaining:** 0  
**Wayback captures accepted:** 135  
**Scheduled time(s):** Tuesday 05:05, Friday 12:12, 1st/3rd Sunday 03:33 and 2nd/4th Sunday 03:00 Europe/Athens  
**Resume mode:** File uploads and Wayback URLs are checkpointed separately.

- [Internet Archive current mirror](https://archive.org/details/dedsec1121fk-github-profile-repository-snapshots)
- [Wayback Machine capture history](https://web.archive.org/web/*/https://github.com/dedsec1121fk/dedsec1121fk*)
- [Last archived commit](https://github.com/dedsec1121fk/dedsec1121fk/commit/b072d5b01c0e9055df005a0fb54dd6cc77f46362)

This section is generated from `update.json`.
<!-- GITHUB_PROFILE_ARCHIVE_STATUS_END -->

<!-- CORRUPTED_FILES_ARCHIVE_STATUS_START -->
### Corrupted Files Project

**Current file-sync status:** `complete`  
**Last complete or attempted save:** 2026-08-09 20:03:59 EEST  
**Current mirrored files:** 1721  
**Latest file update:** 0 uploaded, 0 deleted, 1721 unchanged.  
**Mirror verification:** `True`  
**Wayback queue remaining:** 3174  
**Wayback captures accepted:** 278  
**Scheduled time(s):** Tuesday 05:05, Friday 12:12, 1st/3rd Sunday 03:33 and 2nd/4th Sunday 03:00 Europe/Athens  
**Resume mode:** File uploads and Wayback URLs are checkpointed separately.

- [Internet Archive current mirror](https://archive.org/details/dedsec1121fk-corrupted-files-project-repository-snapshots)
- [Wayback Machine capture history](https://web.archive.org/web/*/https://github.com/dedsec1121fk/Corrupted-Files-Project*)
- [Last archived commit](https://github.com/dedsec1121fk/Corrupted-Files-Project/commit/d6a37ae50dec7a6934a0ad6e868a548a0d87abe8)

This section is generated from `update.json`.
<!-- CORRUPTED_FILES_ARCHIVE_STATUS_END -->

<!-- POCKET_AI_ARCHIVE_STATUS_START -->
### Pocket AI

**Current file-sync status:** `complete`  
**Last complete or attempted save:** 2026-08-09 20:03:39 EEST  
**Current mirrored files:** 128  
**Latest file update:** 0 uploaded, 0 deleted, 128 unchanged.  
**Mirror verification:** `True`  
**Wayback queue remaining:** 0  
**Wayback captures accepted:** 274  
**Scheduled time(s):** Tuesday 05:05, Friday 12:12, 1st/3rd Sunday 03:33 and 2nd/4th Sunday 03:00 Europe/Athens  
**Resume mode:** File uploads and Wayback URLs are checkpointed separately.

- [Internet Archive current mirror](https://archive.org/details/dedsec1121fk-pocket-ai-repository-snapshots)
- [Wayback Machine capture history](https://web.archive.org/web/*/https://github.com/dedsec1121fk/Pocket-AI*)
- [Last archived commit](https://github.com/dedsec1121fk/Pocket-AI/commit/8f468aa3aa4e0078544458bde0b9c8ab5cb64127)

This section is generated from `update.json`.
<!-- POCKET_AI_ARCHIVE_STATUS_END -->

<!-- OFFLINE_SURVIVAL_ARCHIVE_STATUS_START -->
### Offline Survival Project

**Current file-sync status:** `complete`  
**Last complete or attempted save:** 2026-08-09 20:03:43 EEST  
**Current mirrored files:** 1409  
**Latest file update:** 0 uploaded, 0 deleted, 1409 unchanged.  
**Mirror verification:** `True`  
**Wayback queue remaining:** 2527  
**Wayback captures accepted:** 302  
**Scheduled time(s):** Tuesday 05:05, Friday 12:12, 1st/3rd Sunday 03:33 and 2nd/4th Sunday 03:00 Europe/Athens  
**Resume mode:** File uploads and Wayback URLs are checkpointed separately.

- [Internet Archive current mirror](https://archive.org/details/dedsec1121fk-offline-survival-project-repository-snapshots)
- [Wayback Machine capture history](https://web.archive.org/web/*/https://github.com/dedsec1121fk/Offline-Survival-Project*)
- [Last archived commit](https://github.com/dedsec1121fk/Offline-Survival-Project/commit/80bff10df9f28093ea965ae4043e781d7a52dc87)

This section is generated from `update.json`.
<!-- OFFLINE_SURVIVAL_ARCHIVE_STATUS_END -->

<!-- HACKING_GUIDE_ARCHIVE_STATUS_START -->
### Hacking Guide Project

**Current file-sync status:** `not_started`  
**Last complete or attempted save:** Not completed yet  
**Current mirrored files:** 0  
**Latest file update:** 0 uploaded, 0 deleted, 0 unchanged.  
**Mirror verification:** `False`  
**Wayback queue remaining:** 0  
**Wayback captures accepted:** 0  
**Scheduled time(s):** Tuesday 05:05, Friday 12:12, 1st/3rd Sunday 03:33 and 2nd/4th Sunday 03:00 Europe/Athens  
**Resume mode:** File uploads and Wayback URLs are checkpointed separately.

- [Internet Archive current mirror](https://archive.org/details/dedsec1121fk-hacking-guide-project-repository-snapshots)
- [Wayback Machine capture history](https://web.archive.org/web/*/https://github.com/dedsec1121fk/Hacking-Guide-Project*)

This section is generated from `update.json` after the first archive run.
<!-- HACKING_GUIDE_ARCHIVE_STATUS_END -->

<!-- SAVE_DEDSEC_PROJECT_ARCHIVE_STATUS_START -->
### Save DedSec Project

**Current file-sync status:** `not_started`  
**Last complete or attempted save:** Not completed yet  
**Current mirrored files:** 0  
**Latest file update:** 0 uploaded, 0 deleted, 0 unchanged.  
**Mirror verification:** `False`  
**Wayback queue remaining:** 0  
**Wayback captures accepted:** 0  
**Scheduled time(s):** Tuesday 05:05, Friday 12:12, 1st/3rd Sunday 03:33 and 2nd/4th Sunday 03:00 Europe/Athens  
**Resume mode:** File uploads and Wayback URLs are checkpointed separately.

- [Internet Archive current mirror](https://archive.org/details/dedsec1121fk-save-dedsec-project-repository-snapshots)
- [Wayback Machine capture history](https://web.archive.org/web/*/https://github.com/dedsec1121fk/Save-DedSec-Project*)

This section is generated from `update.json` after the first archive run.
<!-- SAVE_DEDSEC_PROJECT_ARCHIVE_STATUS_END -->

