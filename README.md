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

## Weekly Schedule

All groups run Wednesday, Friday and Sunday using `Europe/Athens`.

| Greece time | Archive group |
|---|---|
| 08:00 | DedSec Project main and backup repositories |
| 13:50 | Main website, backup website and website source |
| 19:30 | GitHub profile, Corrupted Files, Pocket AI and Offline Survival |

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

## Automatic Archive Status

<!-- WEBSITES_ARCHIVE_STATUS_START -->
### DedSec Websites and Website Source

**Current file-sync status:** `complete`  
**Last complete or attempted save:** 2026-08-03 10:33:58 EEST  
**Current mirrored files:** 789  
**Latest file update:** 0 uploaded, 0 deleted, 789 unchanged.  
**Mirror verification:** `True`  
**Wayback queue remaining:** 2931  
**Wayback captures accepted:** 309  
**Scheduled window:** Wednesday, Friday and Sunday, 13:50–18:50 Europe/Athens  
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

**Current file-sync status:** `complete`  
**Last complete or attempted save:** 2026-08-03 10:35:20 EEST  
**Current mirrored files:** 587  
**Latest file update:** 0 uploaded, 0 deleted, 587 unchanged.  
**Mirror verification:** `True`  
**Wayback queue remaining:** 205  
**Wayback captures accepted:** 209  
**Scheduled window:** Wednesday, Friday and Sunday, 08:00–13:00 Europe/Athens  
**Resume mode:** File uploads and Wayback URLs are checkpointed separately.

- [Internet Archive current mirror](https://archive.org/details/dedsec1121fk-dedsec-project-repository-snapshots)
- [Wayback Machine capture history](https://web.archive.org/web/*/https://github.com/dedsec1121fk/DedSec*)
- [Last archived commit](https://github.com/dedsec1121fk/DedSec/commit/160a769d7c173da58ec9268c8263c0d947b01c31)

This section is generated from `update.json`.
<!-- DEDSEC_MAIN_ARCHIVE_STATUS_END -->

<!-- DEDSEC_BACKUP_ARCHIVE_STATUS_START -->
### DedSec Project Backup Repository

**Current file-sync status:** `complete`  
**Last complete or attempted save:** 2026-08-03 10:49:08 EEST  
**Current mirrored files:** 587  
**Latest file update:** 0 uploaded, 0 deleted, 587 unchanged.  
**Mirror verification:** `True`  
**Wayback queue remaining:** 995  
**Wayback captures accepted:** 206  
**Scheduled window:** Wednesday, Friday and Sunday, 08:00–13:00 Europe/Athens  
**Resume mode:** File uploads and Wayback URLs are checkpointed separately.

- [Internet Archive current mirror](https://archive.org/details/dedsec1121fk-dedsec-project-backup-repository-snapshots)
- [Wayback Machine capture history](https://web.archive.org/web/*/https://github.com/sal-scar/DedSec*)
- [Last archived commit](https://github.com/sal-scar/DedSec/commit/28dbb1cb4a8d1df28c34b9aad8096a1cc90b2b28)

This section is generated from `update.json`.
<!-- DEDSEC_BACKUP_ARCHIVE_STATUS_END -->

<!-- GITHUB_PROFILE_ARCHIVE_STATUS_START -->
### DedSec GitHub Profile Repository

**Current file-sync status:** `complete`  
**Last complete or attempted save:** 2026-08-03 10:37:41 EEST  
**Current mirrored files:** 8  
**Latest file update:** 6 uploaded, 0 deleted, 2 unchanged.  
**Mirror verification:** `True`  
**Wayback queue remaining:** 6  
**Wayback captures accepted:** 89  
**Scheduled window:** Wednesday, Friday and Sunday, 19:30–23:30 Europe/Athens  
**Resume mode:** File uploads and Wayback URLs are checkpointed separately.

- [Internet Archive current mirror](https://archive.org/details/dedsec1121fk-github-profile-repository-snapshots)
- [Wayback Machine capture history](https://web.archive.org/web/*/https://github.com/dedsec1121fk/dedsec1121fk*)
- [Last archived commit](https://github.com/dedsec1121fk/dedsec1121fk/commit/55d90fdade89623e6b5fee9220dc32abfc4c04ac)

This section is generated from `update.json`.
<!-- GITHUB_PROFILE_ARCHIVE_STATUS_END -->

<!-- CORRUPTED_FILES_ARCHIVE_STATUS_START -->
### Corrupted Files Project

**Current file-sync status:** `complete`  
**Last complete or attempted save:** 2026-08-03 10:35:07 EEST  
**Current mirrored files:** 1721  
**Latest file update:** 0 uploaded, 0 deleted, 1721 unchanged.  
**Mirror verification:** `True`  
**Wayback queue remaining:** 3309  
**Wayback captures accepted:** 143  
**Scheduled window:** Wednesday, Friday and Sunday, 19:30–23:30 Europe/Athens  
**Resume mode:** File uploads and Wayback URLs are checkpointed separately.

- [Internet Archive current mirror](https://archive.org/details/dedsec1121fk-corrupted-files-project-repository-snapshots)
- [Wayback Machine capture history](https://web.archive.org/web/*/https://github.com/dedsec1121fk/Corrupted-Files-Project*)
- [Last archived commit](https://github.com/dedsec1121fk/Corrupted-Files-Project/commit/d6a37ae50dec7a6934a0ad6e868a548a0d87abe8)

This section is generated from `update.json`.
<!-- CORRUPTED_FILES_ARCHIVE_STATUS_END -->

<!-- POCKET_AI_ARCHIVE_STATUS_START -->
### Pocket AI

**Current file-sync status:** `complete`  
**Last complete or attempted save:** 2026-08-03 10:36:36 EEST  
**Current mirrored files:** 128  
**Latest file update:** 0 uploaded, 0 deleted, 128 unchanged.  
**Mirror verification:** `True`  
**Wayback queue remaining:** 111  
**Wayback captures accepted:** 160  
**Scheduled window:** Wednesday, Friday and Sunday, 19:30–23:30 Europe/Athens  
**Resume mode:** File uploads and Wayback URLs are checkpointed separately.

- [Internet Archive current mirror](https://archive.org/details/dedsec1121fk-pocket-ai-repository-snapshots)
- [Wayback Machine capture history](https://web.archive.org/web/*/https://github.com/dedsec1121fk/Pocket-AI*)
- [Last archived commit](https://github.com/dedsec1121fk/Pocket-AI/commit/8f468aa3aa4e0078544458bde0b9c8ab5cb64127)

This section is generated from `update.json`.
<!-- POCKET_AI_ARCHIVE_STATUS_END -->

<!-- OFFLINE_SURVIVAL_ARCHIVE_STATUS_START -->
### Offline Survival Project

**Current file-sync status:** `complete`  
**Last complete or attempted save:** 2026-08-03 10:36:08 EEST  
**Current mirrored files:** 1409  
**Latest file update:** 0 uploaded, 0 deleted, 1409 unchanged.  
**Mirror verification:** `True`  
**Wayback queue remaining:** 2659  
**Wayback captures accepted:** 170  
**Scheduled window:** Wednesday, Friday and Sunday, 19:30–23:30 Europe/Athens  
**Resume mode:** File uploads and Wayback URLs are checkpointed separately.

- [Internet Archive current mirror](https://archive.org/details/dedsec1121fk-offline-survival-project-repository-snapshots)
- [Wayback Machine capture history](https://web.archive.org/web/*/https://github.com/dedsec1121fk/Offline-Survival-Project*)
- [Last archived commit](https://github.com/dedsec1121fk/Offline-Survival-Project/commit/80bff10df9f28093ea965ae4043e781d7a52dc87)

This section is generated from `update.json`.
<!-- OFFLINE_SURVIVAL_ARCHIVE_STATUS_END -->
