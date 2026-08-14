# Save DedSec Project

This repository keeps the current DedSec Project ecosystem synchronized with Internet Archive while the live DedSec websites are progressively captured by the Wayback Machine.

## Fixed Architecture

Internet Archive working-tree synchronization and live-website Wayback capture processing are separate:

1. Each repository is checked out with `fetch-depth: 1`; full Git history is never fetched.
2. `.git` is excluded from inventory, manifests, checksums and archive creation.
3. The complete current working tree is packed into one deterministic `current-working-tree.tar.gz`.
4. Internet Archive receives at most the compact TAR.GZ, `manifest.json`, `SHA256SUMS.txt` and one state checkpoint instead of hundreds or thousands of per-file uploads.
5. The same archive filename is replaced with `x-archive-keep-old-version:0`, so Internet Archive is instructed not to create `history/files/` copies when it is overwritten.
6. Repository targets are never submitted to Wayback. Only the two live DedSec websites use the resumable Wayback queue.

This design removes the per-file request burst that caused Internet Archive `503 SlowDown` errors and also prevents malformed individual PDFs from being rejected during upload: files such as PDFs are preserved byte-for-byte inside the TAR.GZ rather than uploaded as standalone Internet Archive objects.

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

## Compact Internet Archive Working-Tree Archive

The archive operates in **working-tree-only mode**. Git metadata and history are not preservation inputs. On every run the workflow inventories the current checkout, calculates SHA-256 hashes and compares the resulting working-tree snapshot with the previous state.

When the snapshot changes, the target item is updated with:

```text
current-working-tree.tar.gz
manifest.json
SHA256SUMS.txt
archive-state/update.json
```

When the snapshot has not changed, the large TAR.GZ is not uploaded again; only the compact state required by the workflow is refreshed. The archive is deterministic, so identical working-tree content produces identical archive bytes.

Security/privacy properties:

- `.git` directories and `.git` files are excluded at every depth, including nested submodules.
- Git commits, branches, reflogs, push history, Git bundles, commit pages and commit-pinned GitHub archives are not archived.
- Replacing or deleting Internet Archive objects explicitly uses `x-archive-keep-old-version:0`.
- Existing visible `git-history.bundle`, `history/files/` objects and legacy timestamped history archives are cleaned in small bounded batches so cleanup cannot recreate the old request storm.
- Old `mirror/` objects from the previous design are no longer updated. They cannot capture future pushes and are reported as legacy objects until separately removed.
- Item metadata is corrected through the Internet Archive Metadata API so it no longer claims that Git history is preserved.

A synchronized combined state copy is stored in this repository as:

```text
update.json
```

Before S3 writes, the workflow checks Internet Archive's queue-capacity endpoint and waits when the item/account is over limit. Uploads also use extended retry windows for temporary `429`/`503` conditions.

## Resumable Wayback Queue

Wayback processing is restricted to the live DedSec websites. GitHub repository, commit, branch, tag, release and source-history URLs are not queued.

A single serial Wayback job:

- Processes at most 120 URLs per workflow run.
- Runs for at most three hours.
- Writes its Internet Archive state checkpoint every 20 processed URLs instead of after every URL.
- Writes one final checkpoint at the end of the batch.
- Treats active-session limits and HTTP 429/500/502/503/504 as temporary.
- Leaves unfinished URLs in the queue for the next run.
- Is skipped internally when the selected backup group contains no website target.
- Does not fail repository file preservation merely because Wayback is busy.

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

**Current archive status:** `complete`  
**Last complete or attempted save:** 2026-08-13 00:39:12 EEST  
**Current working-tree files:** 821  
**Latest working-tree change:** 659 changed/added, 4 deleted, 162 unchanged.  
**Compact archive uploaded this run:** `False`  
**Archive verification:** `True`  
**Scheduled time(s):** Monday 11:11, Wednesday 22:22 and Saturday 00:00 Europe/Athens  
**Archive mode:** One current `current-working-tree.tar.gz` plus manifest/checksums/state; `.git`, commits and push history are excluded.
**Wayback queue remaining:** 1537  
**Wayback captures accepted:** 697  

- [Internet Archive working-tree archive](https://archive.org/details/dedsec1121fk-dedsec-website-snapshots)
- [https://ded-sec.space Wayback history](https://web.archive.org/web/*/https://ded-sec.space/*)
- [https://ded-sec.online Wayback history](https://web.archive.org/web/*/https://ded-sec.online/*)

This section is generated from `update.json`.
<!-- WEBSITES_ARCHIVE_STATUS_END -->

<!-- DEDSEC_MAIN_ARCHIVE_STATUS_START -->
### DedSec Project Main Repository

**Current archive status:** `in_progress`  
**Last complete or attempted save:** 2026-08-04 10:52:40 EEST  
**Current working-tree files:** 589  
**Latest working-tree change:** 0 changed/added, 0 deleted, 587 unchanged.  
**Compact archive uploaded this run:** `False`  
**Archive verification:** `True`  
**Scheduled time(s):** Monday 11:11, Wednesday 22:22 and Saturday 00:00 Europe/Athens  
**Archive mode:** One current `current-working-tree.tar.gz` plus manifest/checksums/state; `.git`, commits and push history are excluded.

- [Internet Archive working-tree archive](https://archive.org/details/dedsec1121fk-dedsec-project-repository-snapshots)

This section is generated from `update.json`.
<!-- DEDSEC_MAIN_ARCHIVE_STATUS_END -->

<!-- DEDSEC_BACKUP_ARCHIVE_STATUS_START -->
### DedSec Project Backup Repository

**Current archive status:** `in_progress`  
**Last complete or attempted save:** 2026-08-07 09:05:38 EEST  
**Current working-tree files:** 588  
**Latest working-tree change:** 0 changed/added, 0 deleted, 587 unchanged.  
**Compact archive uploaded this run:** `False`  
**Archive verification:** `True`  
**Scheduled time(s):** Monday 11:11, Wednesday 22:22 and Saturday 00:00 Europe/Athens  
**Archive mode:** One current `current-working-tree.tar.gz` plus manifest/checksums/state; `.git`, commits and push history are excluded.

- [Internet Archive working-tree archive](https://archive.org/details/dedsec1121fk-dedsec-project-backup-repository-snapshots)

This section is generated from `update.json`.
<!-- DEDSEC_BACKUP_ARCHIVE_STATUS_END -->

<!-- GITHUB_PROFILE_ARCHIVE_STATUS_START -->
### DedSec GitHub Profile Repository

**Current archive status:** `complete`  
**Last complete or attempted save:** 2026-08-09 20:04:20 EEST  
**Current working-tree files:** 9  
**Latest working-tree change:** 3 changed/added, 0 deleted, 6 unchanged.  
**Compact archive uploaded this run:** `False`  
**Archive verification:** `True`  
**Scheduled time(s):** Tuesday 05:05, Friday 12:12, 1st/3rd Sunday 03:33 and 2nd/4th Sunday 03:00 Europe/Athens  
**Archive mode:** One current `current-working-tree.tar.gz` plus manifest/checksums/state; `.git`, commits and push history are excluded.

- [Internet Archive working-tree archive](https://archive.org/details/dedsec1121fk-github-profile-repository-snapshots)

This section is generated from `update.json`.
<!-- GITHUB_PROFILE_ARCHIVE_STATUS_END -->

<!-- CORRUPTED_FILES_ARCHIVE_STATUS_START -->
### Corrupted Files Project

**Current archive status:** `complete`  
**Last complete or attempted save:** 2026-08-09 20:03:59 EEST  
**Current working-tree files:** 1721  
**Latest working-tree change:** 0 changed/added, 0 deleted, 1721 unchanged.  
**Compact archive uploaded this run:** `False`  
**Archive verification:** `True`  
**Scheduled time(s):** Tuesday 05:05, Friday 12:12, 1st/3rd Sunday 03:33 and 2nd/4th Sunday 03:00 Europe/Athens  
**Archive mode:** One current `current-working-tree.tar.gz` plus manifest/checksums/state; `.git`, commits and push history are excluded.

- [Internet Archive working-tree archive](https://archive.org/details/dedsec1121fk-corrupted-files-project-repository-snapshots)

This section is generated from `update.json`.
<!-- CORRUPTED_FILES_ARCHIVE_STATUS_END -->

<!-- POCKET_AI_ARCHIVE_STATUS_START -->
### Pocket AI

**Current archive status:** `complete`  
**Last complete or attempted save:** 2026-08-09 20:03:39 EEST  
**Current working-tree files:** 128  
**Latest working-tree change:** 0 changed/added, 0 deleted, 128 unchanged.  
**Compact archive uploaded this run:** `False`  
**Archive verification:** `True`  
**Scheduled time(s):** Tuesday 05:05, Friday 12:12, 1st/3rd Sunday 03:33 and 2nd/4th Sunday 03:00 Europe/Athens  
**Archive mode:** One current `current-working-tree.tar.gz` plus manifest/checksums/state; `.git`, commits and push history are excluded.

- [Internet Archive working-tree archive](https://archive.org/details/dedsec1121fk-pocket-ai-repository-snapshots)

This section is generated from `update.json`.
<!-- POCKET_AI_ARCHIVE_STATUS_END -->

<!-- PRAYING_PROJECT_ARCHIVE_STATUS_START -->
### Praying Project

**Current archive status:** `not_started`  
**Last complete or attempted save:** Not completed yet  
**Current working-tree files:** 0  
**Latest working-tree change:** 0 changed/added, 0 deleted, 0 unchanged.  
**Compact archive uploaded this run:** `False`  
**Archive verification:** `False`  
**Scheduled time(s):** Tuesday 05:05, Friday 12:12, 1st/3rd Sunday 03:33 and 2nd/4th Sunday 03:00 Europe/Athens  
**Archive mode:** One current `current-working-tree.tar.gz` plus manifest/checksums/state; `.git`, commits and push history are excluded.

- [Internet Archive working-tree archive](https://archive.org/details/dedsec1121fk-praying-project-repository-snapshots)

This section is generated from `update.json`.
<!-- PRAYING_PROJECT_ARCHIVE_STATUS_END -->

<!-- OFFLINE_SURVIVAL_ARCHIVE_STATUS_START -->
### Offline Survival Project

**Current archive status:** `complete`  
**Last complete or attempted save:** 2026-08-09 20:03:43 EEST  
**Current working-tree files:** 1409  
**Latest working-tree change:** 0 changed/added, 0 deleted, 1409 unchanged.  
**Compact archive uploaded this run:** `False`  
**Archive verification:** `True`  
**Scheduled time(s):** Tuesday 05:05, Friday 12:12, 1st/3rd Sunday 03:33 and 2nd/4th Sunday 03:00 Europe/Athens  
**Archive mode:** One current `current-working-tree.tar.gz` plus manifest/checksums/state; `.git`, commits and push history are excluded.

- [Internet Archive working-tree archive](https://archive.org/details/dedsec1121fk-offline-survival-project-repository-snapshots)

This section is generated from `update.json`.
<!-- OFFLINE_SURVIVAL_ARCHIVE_STATUS_END -->

<!-- HACKING_GUIDE_ARCHIVE_STATUS_START -->
### Hacking Guide Project

**Current archive status:** `not_started`  
**Last complete or attempted save:** Not completed yet  
**Current working-tree files:** 0  
**Latest working-tree change:** 0 changed/added, 0 deleted, 0 unchanged.  
**Compact archive uploaded this run:** `False`  
**Archive verification:** `False`  
**Scheduled time(s):** Tuesday 05:05, Friday 12:12, 1st/3rd Sunday 03:33 and 2nd/4th Sunday 03:00 Europe/Athens  
**Archive mode:** One current `current-working-tree.tar.gz` plus manifest/checksums/state; `.git`, commits and push history are excluded.

- [Internet Archive working-tree archive](https://archive.org/details/dedsec1121fk-hacking-guide-project-repository-snapshots)

This section is generated from `update.json`.
<!-- HACKING_GUIDE_ARCHIVE_STATUS_END -->

<!-- SAVE_DEDSEC_PROJECT_ARCHIVE_STATUS_START -->
### Save DedSec Project

**Current archive status:** `not_started`  
**Last complete or attempted save:** Not completed yet  
**Current working-tree files:** 0  
**Latest working-tree change:** 0 changed/added, 0 deleted, 0 unchanged.  
**Compact archive uploaded this run:** `False`  
**Archive verification:** `False`  
**Scheduled time(s):** Tuesday 05:05, Friday 12:12, 1st/3rd Sunday 03:33 and 2nd/4th Sunday 03:00 Europe/Athens  
**Archive mode:** One current `current-working-tree.tar.gz` plus manifest/checksums/state; `.git`, commits and push history are excluded.

- [Internet Archive working-tree archive](https://archive.org/details/dedsec1121fk-save-dedsec-project-repository-snapshots)

This section is generated from `update.json`.
<!-- SAVE_DEDSEC_PROJECT_ARCHIVE_STATUS_END -->

