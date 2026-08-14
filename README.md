# Save DedSec Project

This repository keeps the current DedSec Project ecosystem synchronized with Internet Archive while the live DedSec websites are progressively captured by the Wayback Machine.

## Fixed Architecture

Internet Archive working-tree synchronization and live-website Wayback capture processing are separate:

1. Current repository files and directories are mirrored first; Git history is excluded.
2. Every successful file upload or deletion is checkpointed immediately.
3. The file-sync job finishes without waiting for thousands of Wayback captures.
4. One serial Wayback job processes a limited resumable queue for the live websites only.
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
- **Praying Project:** https://archive.org/details/dedsec1121fk-praying-project-repository-snapshots
- **Offline Survival:** https://archive.org/details/dedsec1121fk-offline-survival-project-repository-snapshots
- **Hacking Guide Project:** https://archive.org/details/dedsec1121fk-hacking-guide-project-repository-snapshots
- **Save DedSec Project:** https://archive.org/details/dedsec1121fk-save-dedsec-project-repository-snapshots

This section is regenerated on every archive run from the target configuration in `.github/workflows/internet-archive.yml`.
<!-- PERMANENT_ARCHIVE_LINKS_END -->

## Incremental Internet Archive Mirror

The archive now operates in **working-tree-only mode**. The first successful run uploads every current file. Later runs compare SHA-256 hashes:

- New files are uploaded.
- Changed files replace their matching archive objects.
- Deleted repository files are deleted from the current mirror.
- Unchanged files are skipped.
- Missing remote mirror files are restored.
- `.git` is excluded completely.
- Git commit history, push history, Git bundles, commit pages and commit-pinned repository archives are not backed up.
- Any existing visible `git-history.bundle` from the previous design is deleted on the next successful sync.

Every target item contains only the current working-tree mirror and synchronization metadata:

```text
mirror/<original path>
manifest.json
SHA256SUMS.txt
archive-state/update.json
```

The Internet Archive checkpoint is updated after every successful file operation. Repository targets are not submitted to Wayback; Wayback is used only for the live DedSec websites.

A synchronized combined copy is stored here:

```text
update.json
```

If Internet Archive temporarily returns HTTP 503 during a first run, the workflow falls back to the GitHub `update.json` state or starts a safe initial sync. It never deletes unknown files without a trustworthy previous state.

## Resumable Wayback Queue

Wayback processing is restricted to the live DedSec websites. GitHub repository, commit, branch, tag, release and source-history URLs are not queued.

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
| Tuesday | 05:05 | GitHub profile, Corrupted Files, Pocket AI, Praying Project, Offline Survival, Hacking Guide Project and Save DedSec Project |
| Wednesday | 22:22 | DedSec Project main/backup + website source + both live websites |
| Friday | 12:12 | GitHub profile, Corrupted Files, Pocket AI, Praying Project, Offline Survival, Hacking Guide Project and Save DedSec Project |
| Saturday | 00:00 | DedSec Project main/backup + website source + both live websites |
| 1st & 3rd Sunday | 03:33 | GitHub profile, Corrupted Files, Pocket AI, Praying Project, Offline Survival, Hacking Guide Project and Save DedSec Project |
| 2nd & 4th Sunday | 03:00 | GitHub profile, Corrupted Files, Pocket AI, Praying Project, Offline Survival, Hacking Guide Project and Save DedSec Project |

If a month has a fifth Sunday, no Sunday backup is scheduled for that fifth occurrence.

### Monthly Backup Order Rotation

Scheduled repository backups run one target at a time so the configured order is meaningful.

- **January, March, May, July, September and November:** targets run in the exact order listed in the schedule above.
- **February, April, June, August, October and December:** the same target list runs in reverse order.
- **Manual runs:** keep the normal listed order.

For the DedSec/website group, the normal repository order is DedSec main → DedSec backup → website source/live websites; the reverse order starts with the website target. For the other-projects group, the normal order is GitHub profile → Corrupted Files → Pocket AI → Praying Project → Offline Survival → Hacking Guide Project → Save DedSec Project, and even-numbered months reverse that sequence.

## Official Websites

- **Main website:** https://ded-sec.space/
- **Backup website:** https://ded-sec.online/

## Repositories

- **Website source:** https://github.com/dedsec1121fk/dedsec1121fk.github.io
- **DedSec Project main:** https://github.com/dedsec1121fk/DedSec
- **DedSec Project backup:** https://github.com/sal-scar/DedSec
- **GitHub profile:** https://github.com/dedsec1121fk/dedsec1121fk
- **Corrupted Files Project:** https://github.com/dedsec1121fk/Corrupted-Files-Project
- **Pocket AI:** https://github.com/dedsec1121fk/Pocket-AI-Project
- **Praying Project:** https://github.com/dedsec1121fk/Praying-Project
- **Offline Survival Project:** https://github.com/dedsec1121fk/Offline-Survival-Project
- **Hacking Guide Project:** https://github.com/dedsec1121fk/Hacking-Guide-Project
- **Save DedSec Project:** https://github.com/dedsec1121fk/Save-DedSec-Project

## Automatic Archive Status

<!-- WEBSITES_ARCHIVE_STATUS_START -->
### DedSec Websites and Website Source

**Current file-sync status:** `complete`  
**Last complete or attempted save:** 2026-08-13 00:39:12 EEST  
**Current mirrored files:** 821  
**Latest file update:** 659 uploaded, 4 deleted, 162 unchanged.  
**Mirror verification:** `True`  
**Scheduled time(s):** Monday 11:11, Wednesday 22:22 and Saturday 00:00 Europe/Athens  
**Archive mode:** Current working-tree files/directories only; no Git history.  
**Wayback queue remaining:** 1537  
**Wayback captures accepted:** 697  

- [Internet Archive current mirror](https://archive.org/details/dedsec1121fk-dedsec-website-snapshots)
- [https://ded-sec.space Wayback history](https://web.archive.org/web/*/https://ded-sec.space/*)
- [https://ded-sec.online Wayback history](https://web.archive.org/web/*/https://ded-sec.online/*)

This section is generated from `update.json`.
<!-- WEBSITES_ARCHIVE_STATUS_END -->

<!-- DEDSEC_MAIN_ARCHIVE_STATUS_START -->
### DedSec Project Main Repository

**Current file-sync status:** `in_progress`  
**Last complete or attempted save:** 2026-08-04 10:52:40 EEST  
**Current mirrored files:** 589  
**Latest file update:** 0 uploaded, 0 deleted, 587 unchanged.  
**Mirror verification:** `True`  
**Scheduled time(s):** Monday 11:11, Wednesday 22:22 and Saturday 00:00 Europe/Athens  
**Archive mode:** Current working-tree files/directories only; no Git history.  

- [Internet Archive current mirror](https://archive.org/details/dedsec1121fk-dedsec-project-repository-snapshots)

This section is generated from `update.json`.
<!-- DEDSEC_MAIN_ARCHIVE_STATUS_END -->

<!-- DEDSEC_BACKUP_ARCHIVE_STATUS_START -->
### DedSec Project Backup Repository

**Current file-sync status:** `in_progress`  
**Last complete or attempted save:** 2026-08-07 09:05:38 EEST  
**Current mirrored files:** 588  
**Latest file update:** 0 uploaded, 0 deleted, 587 unchanged.  
**Mirror verification:** `True`  
**Scheduled time(s):** Monday 11:11, Wednesday 22:22 and Saturday 00:00 Europe/Athens  
**Archive mode:** Current working-tree files/directories only; no Git history.  

- [Internet Archive current mirror](https://archive.org/details/dedsec1121fk-dedsec-project-backup-repository-snapshots)

This section is generated from `update.json`.
<!-- DEDSEC_BACKUP_ARCHIVE_STATUS_END -->

<!-- GITHUB_PROFILE_ARCHIVE_STATUS_START -->
### DedSec GitHub Profile Repository

**Current file-sync status:** `in_progress`  
**Last complete or attempted save:** 2026-08-09 20:04:20 EEST  
**Current mirrored files:** 8  
**Latest file update:** 3 uploaded, 0 deleted, 6 unchanged.  
**Mirror verification:** `True`  
**Scheduled time(s):** Tuesday 05:05, Friday 12:12, 1st/3rd Sunday 03:33 and 2nd/4th Sunday 03:00 Europe/Athens  
**Archive mode:** Current working-tree files/directories only; no Git history.

- [Internet Archive current mirror](https://archive.org/details/dedsec1121fk-github-profile-repository-snapshots)

This section is generated from `update.json`.
<!-- GITHUB_PROFILE_ARCHIVE_STATUS_END -->

<!-- CORRUPTED_FILES_ARCHIVE_STATUS_START -->
### Corrupted Files Project

**Current file-sync status:** `failed`  
**Last complete or attempted save:** 2026-08-09 20:03:59 EEST  
**Current mirrored files:** 2141  
**Latest file update:** 0 uploaded, 0 deleted, 1721 unchanged.  
**Mirror verification:** `True`  
**Scheduled time(s):** Tuesday 05:05, Friday 12:12, 1st/3rd Sunday 03:33 and 2nd/4th Sunday 03:00 Europe/Athens  
**Archive mode:** Current working-tree files/directories only; no Git history.

- [Internet Archive current mirror](https://archive.org/details/dedsec1121fk-corrupted-files-project-repository-snapshots)

This section is generated from `update.json`.
<!-- CORRUPTED_FILES_ARCHIVE_STATUS_END -->

<!-- POCKET_AI_ARCHIVE_STATUS_START -->
### Pocket AI

**Current file-sync status:** `uploaded_unverified`  
**Last complete or attempted save:** 2026-08-14 14:55:20 EEST  
**Current mirrored files:** 128  
**Latest file update:** 54 uploaded, 1 deleted, 74 unchanged.  
**Mirror verification:** `False`  
**Scheduled time(s):** Tuesday 05:05, Friday 12:12, 1st/3rd Sunday 03:33 and 2nd/4th Sunday 03:00 Europe/Athens  
**Archive mode:** Current working-tree files/directories only; no Git history.

- [Internet Archive current mirror](https://archive.org/details/dedsec1121fk-pocket-ai-repository-snapshots)

This section is generated from `update.json`.
<!-- POCKET_AI_ARCHIVE_STATUS_END -->

<!-- PRAYING_PROJECT_ARCHIVE_STATUS_START -->
### Praying Project

**Current file-sync status:** `complete`  
**Last complete or attempted save:** 2026-08-14 14:28:19 EEST  
**Current mirrored files:** 74  
**Latest file update:** 74 uploaded, 0 deleted, 0 unchanged.  
**Mirror verification:** `True`  
**Scheduled time(s):** Tuesday 05:05, Friday 12:12, 1st/3rd Sunday 03:33 and 2nd/4th Sunday 03:00 Europe/Athens  
**Archive mode:** Current working-tree files/directories only; no Git history.

- [Internet Archive current mirror](https://archive.org/details/dedsec1121fk-praying-project-repository-snapshots)

This section is generated from `update.json`.
<!-- PRAYING_PROJECT_ARCHIVE_STATUS_END -->

<!-- OFFLINE_SURVIVAL_ARCHIVE_STATUS_START -->
### Offline Survival Project

**Current file-sync status:** `failed`  
**Last complete or attempted save:** 2026-08-09 20:03:43 EEST  
**Current mirrored files:** 1410  
**Latest file update:** 0 uploaded, 0 deleted, 1409 unchanged.  
**Mirror verification:** `True`  
**Scheduled time(s):** Tuesday 05:05, Friday 12:12, 1st/3rd Sunday 03:33 and 2nd/4th Sunday 03:00 Europe/Athens  
**Archive mode:** Current working-tree files/directories only; no Git history.

- [Internet Archive current mirror](https://archive.org/details/dedsec1121fk-offline-survival-project-repository-snapshots)

This section is generated from `update.json`.
<!-- OFFLINE_SURVIVAL_ARCHIVE_STATUS_END -->

<!-- HACKING_GUIDE_ARCHIVE_STATUS_START -->
### Hacking Guide Project

**Current file-sync status:** `failed`  
**Last complete or attempted save:** Not completed yet  
**Current mirrored files:** 6  
**Latest file update:** 0 uploaded, 0 deleted, 0 unchanged.  
**Mirror verification:** `False`  
**Scheduled time(s):** Tuesday 05:05, Friday 12:12, 1st/3rd Sunday 03:33 and 2nd/4th Sunday 03:00 Europe/Athens  
**Archive mode:** Current working-tree files/directories only; no Git history.

- [Internet Archive current mirror](https://archive.org/details/dedsec1121fk-hacking-guide-project-repository-snapshots)

This section is generated from `update.json`.
<!-- HACKING_GUIDE_ARCHIVE_STATUS_END -->

<!-- SAVE_DEDSEC_PROJECT_ARCHIVE_STATUS_START -->
### Save DedSec Project

**Current file-sync status:** `failed`  
**Last complete or attempted save:** 2026-08-14 13:36:42 EEST  
**Current mirrored files:** 5  
**Latest file update:** 5 uploaded, 0 deleted, 0 unchanged.  
**Mirror verification:** `False`  
**Scheduled time(s):** Tuesday 05:05, Friday 12:12, 1st/3rd Sunday 03:33 and 2nd/4th Sunday 03:00 Europe/Athens  
**Archive mode:** Current working-tree files/directories only; no Git history.

- [Internet Archive current mirror](https://archive.org/details/dedsec1121fk-save-dedsec-project-repository-snapshots)

This section is generated from `update.json`.
<!-- SAVE_DEDSEC_PROJECT_ARCHIVE_STATUS_END -->

