# Save DedSec Project

This repository keeps the current DedSec Project ecosystem synchronized with Internet Archive and Software Heritage, preserves the APK dependencies used by the local Save DedSec Project backup, and progressively captures the live DedSec websites with the Wayback Machine.

## Fixed Architecture

Internet Archive working-tree synchronization, Software Heritage source preservation, APK preservation and live-website Wayback capture processing are separate:

1. Each repository is checked out with `fetch-depth: 1`; full Git history is never fetched by this controller.
2. `.git` is excluded from Internet Archive inventory, manifests, checksums and archive creation.
3. The complete current working tree is packed into one deterministic `current-working-tree.tar.gz` for each Internet Archive repository target.
4. Internet Archive receives at most the compact TAR.GZ, `manifest.json`, `SHA256SUMS.txt` and one state checkpoint for repository targets instead of hundreds or thousands of per-file uploads.
5. The four APK dependencies defined by the current `Settings.py` Save DedSec Project routine are downloaded separately and synchronized to one dedicated Internet Archive software item only when their hashes change.
6. Every public Git repository is tracked with Software Heritage. Repositories selected for a run receive a Save Code Now request unless an active or very recent request already exists; links from that request are intentionally checked and published only by later workflow runs.
7. Repository archive files are replaced with `x-archive-keep-old-version:0`, so Internet Archive is instructed not to create `history/files/` copies when current objects are overwritten.
8. Repository targets are never submitted to Wayback. Only the two live DedSec websites use the resumable Wayback queue.


This design removes the per-file request burst that caused Internet Archive `503 SlowDown` errors and also prevents malformed individual PDFs from being rejected during upload: files such as PDFs are preserved byte-for-byte inside the TAR.GZ rather than uploaded as standalone Internet Archive objects.

## Forking This Archive Controller

Fork owners can configure their own Internet Archive credentials and item identifiers by following [Fork Instructions](Fork%20Instructions.md).

<!-- PERMANENT_ARCHIVE_LINKS_START -->
## Permanent Internet Archive Links

- **DedSec main:** https://archive.org/details/dedsec1121fk-dedsec-project-repository-snapshots
- **DedSec backup:** https://archive.org/details/dedsec1121fk-dedsec-project-backup-repository-snapshots
- **Websites:** https://archive.org/details/dedsec1121fk-dedsec-website-snapshots
- **Website mirror:** https://archive.org/details/dedsec1121fk-dedsec-website-mirror-repository-snapshots
- **GitHub profile:** https://archive.org/details/dedsec1121fk-github-profile-repository-snapshots
- **Corrupted Files:** https://archive.org/details/dedsec1121fk-corrupted-files-project-repository-snapshots
- **Pocket AI:** https://archive.org/details/dedsec1121fk-pocket-ai-repository-snapshots
- **Praying Project:** https://archive.org/details/dedsec1121fk-praying-project-repository-snapshots
- **Offline Survival:** https://archive.org/details/dedsec1121fk-offline-survival-project-repository-snapshots
- **Hacking Guide Project:** https://archive.org/details/dedsec1121fk-hacking-guide-project-repository-snapshots
- **Language Project:** https://archive.org/details/dedsec1121fk-language-project-repository-snapshots
- **Save DedSec Project:** https://archive.org/details/dedsec1121fk-save-dedsec-project-repository-snapshots
- **APK dependencies:** https://archive.org/details/dedsec1121fk-dedsec-project-apk-backups

This section is regenerated on every archive run from the target configuration in `.github/workflows/internet-archive.yml`.
<!-- PERMANENT_ARCHIVE_LINKS_END -->

<!-- SOFTWARE_HERITAGE_LINKS_START -->
## Software Heritage Links

Software Heritage Save Code Now requests are submitted during one workflow run, but their archive links are resolved only on later runs. This gives Software Heritage time to ingest each repository before a link is published here.

- **DedSec main:** [Software Heritage archive](https://archive.softwareheritage.org/browse/origin/?origin_url=https%3A%2F%2Fgithub.com%2Fdedsec1121fk%2FDedSec) · [latest snapshot](https://archive.softwareheritage.org/swh:1:snp:19fb93418982d1f79459a4afe75854c29c00839b/) · `full`
- **DedSec backup:** [Software Heritage archive](https://archive.softwareheritage.org/browse/origin/?origin_url=https%3A%2F%2Fgithub.com%2Fsal-scar%2FDedSec) · [latest snapshot](https://archive.softwareheritage.org/swh:1:snp:6bacd1ebe8e09aff30f6e25784a3210784f887dc/) · `full`
- **Websites:** [Software Heritage archive](https://archive.softwareheritage.org/browse/origin/?origin_url=https%3A%2F%2Fgithub.com%2Fdedsec1121fk%2Fdedsec1121fk.github.io) · [latest snapshot](https://archive.softwareheritage.org/swh:1:snp:c259b5c43362a6b775e92012d0fe762c566486c4/) · `full`
- **Website mirror:** [Software Heritage archive](https://archive.softwareheritage.org/browse/origin/?origin_url=https%3A%2F%2Fgithub.com%2Fsal-scar%2Fded-sec) · [latest snapshot](https://archive.softwareheritage.org/swh:1:snp:05e7ec480d81318c2466947d9ae8cb6744bf7751/) · `full`
- **GitHub profile:** [Software Heritage archive](https://archive.softwareheritage.org/browse/origin/?origin_url=https%3A%2F%2Fgithub.com%2Fdedsec1121fk%2Fdedsec1121fk) · [latest snapshot](https://archive.softwareheritage.org/swh:1:snp:fffaf29c526af7df9f512af5ccf499fa0e62ee8a/) · `full`
- **Corrupted Files:** [Software Heritage archive](https://archive.softwareheritage.org/browse/origin/?origin_url=https%3A%2F%2Fgithub.com%2Fdedsec1121fk%2FCorrupted-Files-Project) · [latest snapshot](https://archive.softwareheritage.org/swh:1:snp:a9c7391b498b3cda67cfdd5158d8bc7d4eee6675/) · `full`
- **Pocket AI:** [Software Heritage archive](https://archive.softwareheritage.org/browse/origin/?origin_url=https%3A%2F%2Fgithub.com%2Fdedsec1121fk%2FPocket-AI-Project) · [latest snapshot](https://archive.softwareheritage.org/swh:1:snp:10b3547fa34d0969398029647aed7ec4f1fe0a2d/) · `full`
- **Praying Project:** [Software Heritage archive](https://archive.softwareheritage.org/browse/origin/?origin_url=https%3A%2F%2Fgithub.com%2Fdedsec1121fk%2FPraying-Project) · [latest snapshot](https://archive.softwareheritage.org/swh:1:snp:e02371e7ee55132c4f79bd0330efcf62ab38938e/) · `full`
- **Offline Survival:** [Software Heritage archive](https://archive.softwareheritage.org/browse/origin/?origin_url=https%3A%2F%2Fgithub.com%2Fdedsec1121fk%2FOffline-Survival-Project) · [latest snapshot](https://archive.softwareheritage.org/swh:1:snp:2e09b6077bc459898406430982d83b9ebcf8369b/) · `full`
- **Hacking Guide Project:** [Software Heritage archive](https://archive.softwareheritage.org/browse/origin/?origin_url=https%3A%2F%2Fgithub.com%2Fdedsec1121fk%2FHacking-Guide-Project) · [latest snapshot](https://archive.softwareheritage.org/swh:1:snp:ad11139d5d05cae40aa4d08997f31dc69b9323a7/) · `full`
- **Language Project:** [Software Heritage archive](https://archive.softwareheritage.org/browse/origin/?origin_url=https%3A%2F%2Fgithub.com%2Fdedsec1121fk%2FLanguage-Project) · [latest snapshot](https://archive.softwareheritage.org/swh:1:snp:7a5abba3c29b0260dd5ba46ac103006862a6886d/) · `full`
- **Save DedSec Project:** [Software Heritage archive](https://archive.softwareheritage.org/browse/origin/?origin_url=https%3A%2F%2Fgithub.com%2Fdedsec1121fk%2FSave-DedSec-Project) · [latest snapshot](https://archive.softwareheritage.org/swh:1:snp:0e16b6792419158c5dd646d94f4c6cbe1ddfc665/) · `full`

Last checked: `2026-08-25T03:08:22Z`.

<!-- SOFTWARE_HERITAGE_LINKS_END -->

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
- Private Sponsors-Only repositories are not published by this public archive controller; only public repository targets are sent to Internet Archive and Software Heritage.

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
| Monday | 11:11 | DedSec Project main/backup + website source + website mirror + both live websites |
| Tuesday | 05:05 | GitHub profile, Corrupted Files, Pocket AI, Praying Project, Offline Survival, Hacking Guide Project, Language Project and Save DedSec Project |
| Wednesday | 22:22 | DedSec Project main/backup + website source + website mirror + both live websites |
| Friday | 12:12 | GitHub profile, Corrupted Files, Pocket AI, Praying Project, Offline Survival, Hacking Guide Project, Language Project and Save DedSec Project |
| Saturday | 00:00 | DedSec Project main/backup + website source + website mirror + both live websites |
| 1st & 3rd Sunday | 03:33 | GitHub profile, Corrupted Files, Pocket AI, Praying Project, Offline Survival, Hacking Guide Project, Language Project and Save DedSec Project |
| 2nd & 4th Sunday | 03:00 | GitHub profile, Corrupted Files, Pocket AI, Praying Project, Offline Survival, Hacking Guide Project, Language Project and Save DedSec Project |

If a month has a fifth Sunday, no Sunday backup is scheduled for that fifth occurrence.

### Monthly Backup Order Rotation

Scheduled repository backups run one target at a time so the configured order is meaningful.

- **January, March, May, July, September and November:** targets run in the exact order listed in the schedule above.
- **February, April, June, August, October and December:** the same target list runs in reverse order.
- **Manual runs:** keep the normal listed order.

For the DedSec/website group, the normal repository order is DedSec main → DedSec backup → website source/live websites → website mirror; the reverse order starts with the website mirror. For the other-projects group, the normal order is GitHub profile → Corrupted Files → Pocket AI → Praying Project → Offline Survival → Hacking Guide Project → Language Project → Save DedSec Project, and even-numbered months reverse that sequence.

## Official Websites

- **Main website:** https://ded-sec.space/
- **Backup website:** https://ded-sec.online/

## Repositories

- **Website source:** https://github.com/dedsec1121fk/dedsec1121fk.github.io
- **Website mirror:** https://github.com/sal-scar/ded-sec
- **DedSec Project main:** https://github.com/dedsec1121fk/DedSec
- **DedSec Project backup:** https://github.com/sal-scar/DedSec
- **GitHub profile:** https://github.com/dedsec1121fk/dedsec1121fk
- **Corrupted Files Project:** https://github.com/dedsec1121fk/Corrupted-Files-Project
- **Pocket AI:** https://github.com/dedsec1121fk/Pocket-AI-Project
- **Praying Project:** https://github.com/dedsec1121fk/Praying-Project
- **Offline Survival Project:** https://github.com/dedsec1121fk/Offline-Survival-Project
- **Hacking Guide Project:** https://github.com/dedsec1121fk/Hacking-Guide-Project
- **Language Project:** https://github.com/dedsec1121fk/Language-Project
- **Save DedSec Project:** https://github.com/dedsec1121fk/Save-DedSec-Project

<!-- APK_ARCHIVE_STATUS_START -->
## APK Preservation

The same four APK dependencies used by the local `Settings.py` Save DedSec Project backup are checked on every workflow run.

- [Internet Archive APK collection](https://archive.org/details/dedsec1121fk-dedsec-project-apk-backups)
- **F-Droid.apk:** `985f5181d48bb6bafd54083a048b391271e0ab28385881cc41294fb01a222762` (12426276 bytes)
- **Termux.apk:** `fdd476982cd74f2f00aac12d3683b1fa260a0b2d146411b94e09d773be3a7b56` (114920926 bytes)
- **Termux_API.apk:** `4497dbbf81906df52e59ed387a5223d225aa0de3aca817cc557a621e4dadda44` (3956196 bytes)
- **Termux_Styling.apk:** `799a53f096c28e2aafae918f5ab91de500526bc5461030dbceea4e89bf56b68f` (32930486 bytes)

Last checked: `2026-08-25T03:27:38Z`.

<!-- APK_ARCHIVE_STATUS_END -->

## Automatic Archive Status

<!-- WEBSITES_ARCHIVE_STATUS_START -->
### DedSec Websites and Website Source

**Current archive status:** `complete`  
**Last complete or attempted save:** 2026-08-24 12:08:57 EEST  
**Current working-tree files:** 829  
**Latest working-tree change:** 18 changed/added, 0 deleted, 811 unchanged.  
**Compact archive uploaded this run:** `True`  
**Archive verification:** `True`  
**Scheduled time(s):** Monday 11:11, Wednesday 22:22 and Saturday 00:00 Europe/Athens  
**Archive mode:** One current `current-working-tree.tar.gz` plus manifest/checksums/state; `.git`, commits and push history are excluded.
**Legacy pre-migration mirror objects still visible:** 821. They are frozen and are not used for future backups.  
**Wayback queue remaining:** 1595  
**Wayback captures accepted:** 1082  

- [Internet Archive working-tree archive](https://archive.org/details/dedsec1121fk-dedsec-website-snapshots)
- [https://ded-sec.space Wayback history](https://web.archive.org/web/*/https://ded-sec.space/*)
- [https://ded-sec.online Wayback history](https://web.archive.org/web/*/https://ded-sec.online/*)

This section is generated from `update.json`.
<!-- WEBSITES_ARCHIVE_STATUS_END -->

<!-- DEDSEC_MAIN_ARCHIVE_STATUS_START -->
### DedSec Project Main Repository

**Current archive status:** `complete`  
**Last complete or attempted save:** 2026-08-24 12:16:02 EEST  
**Current working-tree files:** 209  
**Latest working-tree change:** 3 changed/added, 0 deleted, 206 unchanged.  
**Compact archive uploaded this run:** `True`  
**Archive verification:** `True`  
**Scheduled time(s):** Monday 11:11, Wednesday 22:22 and Saturday 00:00 Europe/Athens  
**Archive mode:** One current `current-working-tree.tar.gz` plus manifest/checksums/state; `.git`, commits and push history are excluded.
**Legacy pre-migration mirror objects still visible:** 589. They are frozen and are not used for future backups.  

- [Internet Archive working-tree archive](https://archive.org/details/dedsec1121fk-dedsec-project-repository-snapshots)

This section is generated from `update.json`.
<!-- DEDSEC_MAIN_ARCHIVE_STATUS_END -->

<!-- DEDSEC_BACKUP_ARCHIVE_STATUS_START -->
### DedSec Project Backup Repository

**Current archive status:** `complete`  
**Last complete or attempted save:** 2026-08-24 12:12:27 EEST  
**Current working-tree files:** 209  
**Latest working-tree change:** 3 changed/added, 0 deleted, 206 unchanged.  
**Compact archive uploaded this run:** `True`  
**Archive verification:** `True`  
**Scheduled time(s):** Monday 11:11, Wednesday 22:22 and Saturday 00:00 Europe/Athens  
**Archive mode:** One current `current-working-tree.tar.gz` plus manifest/checksums/state; `.git`, commits and push history are excluded.
**Legacy pre-migration mirror objects still visible:** 588. They are frozen and are not used for future backups.  

- [Internet Archive working-tree archive](https://archive.org/details/dedsec1121fk-dedsec-project-backup-repository-snapshots)

This section is generated from `update.json`.
<!-- DEDSEC_BACKUP_ARCHIVE_STATUS_END -->

<!-- GITHUB_PROFILE_ARCHIVE_STATUS_START -->
### DedSec GitHub Profile Repository

**Current archive status:** `complete`  
**Last complete or attempted save:** 2026-08-25 06:26:55 EEST  
**Current working-tree files:** 20  
**Latest working-tree change:** 8 changed/added, 0 deleted, 12 unchanged.  
**Compact archive uploaded this run:** `True`  
**Archive verification:** `True`  
**Scheduled time(s):** Tuesday 05:05, Friday 12:12, 1st/3rd Sunday 03:33 and 2nd/4th Sunday 03:00 Europe/Athens  
**Archive mode:** One current `current-working-tree.tar.gz` plus manifest/checksums/state; `.git`, commits and push history are excluded.
**Legacy pre-migration mirror objects still visible:** 8. They are frozen and are not used for future backups.  

- [Internet Archive working-tree archive](https://archive.org/details/dedsec1121fk-github-profile-repository-snapshots)

This section is generated from `update.json`.
<!-- GITHUB_PROFILE_ARCHIVE_STATUS_END -->

<!-- CORRUPTED_FILES_ARCHIVE_STATUS_START -->
### Corrupted Files Project

**Current archive status:** `complete`  
**Last complete or attempted save:** 2026-08-25 06:23:36 EEST  
**Current working-tree files:** 2148  
**Latest working-tree change:** 0 changed/added, 0 deleted, 2148 unchanged.  
**Compact archive uploaded this run:** `False`  
**Archive verification:** `True`  
**Scheduled time(s):** Tuesday 05:05, Friday 12:12, 1st/3rd Sunday 03:33 and 2nd/4th Sunday 03:00 Europe/Athens  
**Archive mode:** One current `current-working-tree.tar.gz` plus manifest/checksums/state; `.git`, commits and push history are excluded.
**Legacy pre-migration mirror objects still visible:** 2141. They are frozen and are not used for future backups.  

- [Internet Archive working-tree archive](https://archive.org/details/dedsec1121fk-corrupted-files-project-repository-snapshots)

This section is generated from `update.json`.
<!-- CORRUPTED_FILES_ARCHIVE_STATUS_END -->

<!-- POCKET_AI_ARCHIVE_STATUS_START -->
### Pocket AI

**Current archive status:** `complete`  
**Last complete or attempted save:** 2026-08-25 06:21:47 EEST  
**Current working-tree files:** 128  
**Latest working-tree change:** 0 changed/added, 0 deleted, 128 unchanged.  
**Compact archive uploaded this run:** `False`  
**Archive verification:** `True`  
**Scheduled time(s):** Tuesday 05:05, Friday 12:12, 1st/3rd Sunday 03:33 and 2nd/4th Sunday 03:00 Europe/Athens  
**Archive mode:** One current `current-working-tree.tar.gz` plus manifest/checksums/state; `.git`, commits and push history are excluded.
**Legacy pre-migration mirror objects still visible:** 128. They are frozen and are not used for future backups.  

- [Internet Archive working-tree archive](https://archive.org/details/dedsec1121fk-pocket-ai-repository-snapshots)

This section is generated from `update.json`.
<!-- POCKET_AI_ARCHIVE_STATUS_END -->

<!-- PRAYING_PROJECT_ARCHIVE_STATUS_START -->
### Praying Project

**Current archive status:** `complete`  
**Last complete or attempted save:** 2026-08-25 06:19:55 EEST  
**Current working-tree files:** 74  
**Latest working-tree change:** 1 changed/added, 0 deleted, 73 unchanged.  
**Compact archive uploaded this run:** `True`  
**Archive verification:** `True`  
**Scheduled time(s):** Tuesday 05:05, Friday 12:12, 1st/3rd Sunday 03:33 and 2nd/4th Sunday 03:00 Europe/Athens  
**Archive mode:** One current `current-working-tree.tar.gz` plus manifest/checksums/state; `.git`, commits and push history are excluded.
**Legacy pre-migration mirror objects still visible:** 74. They are frozen and are not used for future backups.  

- [Internet Archive working-tree archive](https://archive.org/details/dedsec1121fk-praying-project-repository-snapshots)

This section is generated from `update.json`.
<!-- PRAYING_PROJECT_ARCHIVE_STATUS_END -->

<!-- OFFLINE_SURVIVAL_ARCHIVE_STATUS_START -->
### Offline Survival Project

**Current archive status:** `complete`  
**Last complete or attempted save:** 2026-08-25 06:16:33 EEST  
**Current working-tree files:** 807  
**Latest working-tree change:** 0 changed/added, 0 deleted, 807 unchanged.  
**Compact archive uploaded this run:** `False`  
**Archive verification:** `True`  
**Scheduled time(s):** Tuesday 05:05, Friday 12:12, 1st/3rd Sunday 03:33 and 2nd/4th Sunday 03:00 Europe/Athens  
**Archive mode:** One current `current-working-tree.tar.gz` plus manifest/checksums/state; `.git`, commits and push history are excluded.
**Legacy pre-migration mirror objects still visible:** 1410. They are frozen and are not used for future backups.  

- [Internet Archive working-tree archive](https://archive.org/details/dedsec1121fk-offline-survival-project-repository-snapshots)

This section is generated from `update.json`.
<!-- OFFLINE_SURVIVAL_ARCHIVE_STATUS_END -->

<!-- HACKING_GUIDE_ARCHIVE_STATUS_START -->
### Hacking Guide Project

**Current archive status:** `complete`  
**Last complete or attempted save:** 2026-08-25 06:14:41 EEST  
**Current working-tree files:** 334  
**Latest working-tree change:** 0 changed/added, 0 deleted, 334 unchanged.  
**Compact archive uploaded this run:** `False`  
**Archive verification:** `True`  
**Scheduled time(s):** Tuesday 05:05, Friday 12:12, 1st/3rd Sunday 03:33 and 2nd/4th Sunday 03:00 Europe/Athens  
**Archive mode:** One current `current-working-tree.tar.gz` plus manifest/checksums/state; `.git`, commits and push history are excluded.
**Legacy pre-migration mirror objects still visible:** 6. They are frozen and are not used for future backups.  

- [Internet Archive working-tree archive](https://archive.org/details/dedsec1121fk-hacking-guide-project-repository-snapshots)

This section is generated from `update.json`.
<!-- HACKING_GUIDE_ARCHIVE_STATUS_END -->

<!-- SAVE_DEDSEC_PROJECT_ARCHIVE_STATUS_START -->
### Save DedSec Project

**Current archive status:** `complete`  
**Last complete or attempted save:** 2026-08-25 06:11:02 EEST  
**Current working-tree files:** 7  
**Latest working-tree change:** 2 changed/added, 0 deleted, 5 unchanged.  
**Compact archive uploaded this run:** `True`  
**Archive verification:** `True`  
**Scheduled time(s):** Tuesday 05:05, Friday 12:12, 1st/3rd Sunday 03:33 and 2nd/4th Sunday 03:00 Europe/Athens  
**Archive mode:** One current `current-working-tree.tar.gz` plus manifest/checksums/state; `.git`, commits and push history are excluded.
**Legacy pre-migration mirror objects still visible:** 5. They are frozen and are not used for future backups.  

- [Internet Archive working-tree archive](https://archive.org/details/dedsec1121fk-save-dedsec-project-repository-snapshots)

This section is generated from `update.json`.
<!-- SAVE_DEDSEC_PROJECT_ARCHIVE_STATUS_END -->

<!-- DEDSEC_WEBSITE_MIRROR_ARCHIVE_STATUS_START -->
### DedSec Website Mirror Repository

**Current archive status:** `complete`  
**Last complete or attempted save:** 2026-08-24 12:05:28 EEST  
**Current working-tree files:** 829  
**Latest working-tree change:** 18 changed/added, 0 deleted, 811 unchanged.  
**Compact archive uploaded this run:** `True`  
**Archive verification:** `True`  
**Scheduled time(s):** Monday 11:11, Wednesday 22:22 and Saturday 00:00 Europe/Athens  
**Archive mode:** One current `current-working-tree.tar.gz` plus manifest/checksums/state; `.git`, commits and push history are excluded.

- [Internet Archive working-tree archive](https://archive.org/details/dedsec1121fk-dedsec-website-mirror-repository-snapshots)

This section is generated from `update.json`.
<!-- DEDSEC_WEBSITE_MIRROR_ARCHIVE_STATUS_END -->

<!-- LANGUAGE_PROJECT_ARCHIVE_STATUS_START -->
### Language Project

**Current archive status:** `complete`  
**Last complete or attempted save:** 2026-08-25 06:12:56 EEST  
**Current working-tree files:** 10753  
**Latest working-tree change:** 0 changed/added, 0 deleted, 10753 unchanged.  
**Compact archive uploaded this run:** `False`  
**Archive verification:** `True`  
**Scheduled time(s):** Tuesday 05:05, Friday 12:12, 1st/3rd Sunday 03:33 and 2nd/4th Sunday 03:00 Europe/Athens  
**Archive mode:** One current `current-working-tree.tar.gz` plus manifest/checksums/state; `.git`, commits and push history are excluded.

- [Internet Archive working-tree archive](https://archive.org/details/dedsec1121fk-language-project-repository-snapshots)

This section is generated from `update.json`.
<!-- LANGUAGE_PROJECT_ARCHIVE_STATUS_END -->
