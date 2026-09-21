<div align="center">
  <h1>Save DedSec Project</h1>
  <p><strong>Internet Archive · Software Heritage · Wayback preservation controller</strong></p>
</div>

---
<a id="english-readme"></a>
# Save DedSec Project

> **Για να μεταβείτε στην πλήρη Ελληνική έκδοση, συνεχίστε [Πατώντας Εδώ](#greek-readme).**

This repository keeps the current DedSec Project ecosystem synchronized with Internet Archive and Software Heritage, preserves the APK dependencies used by the local Save DedSec Project backup, and progressively captures the live DedSec websites with the Wayback Machine.

<h2>Table of Contents</h2>
* Fixed Architecture
* Forking This Archive Controller
* Permanent Internet Archive Links
* Software Heritage Links
* Compact Internet Archive Working-Tree Archive
* Resumable Wayback Queue
* Backup Schedule
* Official Websites
* Repositories
* APK Preservation
* Automatic Archive Status

<details>
<summary><strong>Fixed Architecture</strong></summary>


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

</details>
<details>
<summary><strong>Forking This Archive Controller</strong></summary>


Fork owners can configure their own Internet Archive credentials and item identifiers by following [Fork Instructions](Fork%20Instructions.md). The fork guide is bilingual in English and Greek.

</details>
<details>
<summary><strong>Permanent Internet Archive Links</strong></summary>

<!-- PERMANENT_ARCHIVE_LINKS_START -->
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
- **Ghost Project:** https://archive.org/details/dedsec1121fk-ghost-project-repository-snapshots
- **Save DedSec Project:** https://archive.org/details/dedsec1121fk-save-dedsec-project-repository-snapshots
- **APK dependencies:** https://archive.org/details/dedsec1121fk-dedsec-project-apk-backups

This section is regenerated on every archive run from the target configuration in `.github/workflows/internet-archive.yml`.
<!-- PERMANENT_ARCHIVE_LINKS_END -->

</details>

<details>
<summary><strong>Software Heritage Links</strong></summary>

<!-- SOFTWARE_HERITAGE_LINKS_START -->
Software Heritage Save Code Now requests are submitted during one workflow run, but their archive links are resolved only on later runs. This gives Software Heritage time to ingest each repository before a link is published here.

- **DedSec main:** [Software Heritage archive](https://archive.softwareheritage.org/browse/origin/?origin_url=https%3A%2F%2Fgithub.com%2Fdedsec1121fk%2FDedSec) · [latest snapshot](https://archive.softwareheritage.org/swh:1:snp:9398c186b5c5727ca1b2acbe482010bffeb45d94/) · `full`
- **DedSec backup:** [Software Heritage archive](https://archive.softwareheritage.org/browse/origin/?origin_url=https%3A%2F%2Fgithub.com%2Fsal-scar%2FDedSec) · [latest snapshot](https://archive.softwareheritage.org/swh:1:snp:a4185f5487b9f54a85989033e5f1d9daa214f84a/) · `full`
- **Websites:** [Software Heritage archive](https://archive.softwareheritage.org/browse/origin/?origin_url=https%3A%2F%2Fgithub.com%2Fdedsec1121fk%2Fdedsec1121fk.github.io) · [latest snapshot](https://archive.softwareheritage.org/swh:1:snp:0fdf2bb2c142cdb402cb4fbe9f55bebb9386a24b/) · `full`
- **Website mirror:** [Software Heritage archive](https://archive.softwareheritage.org/browse/origin/?origin_url=https%3A%2F%2Fgithub.com%2Fsal-scar%2Fded-sec) · [latest snapshot](https://archive.softwareheritage.org/swh:1:snp:29edba7c972de18149294255d58688b6951daa20/) · `full`
- **GitHub profile:** [Software Heritage archive](https://archive.softwareheritage.org/browse/origin/?origin_url=https%3A%2F%2Fgithub.com%2Fdedsec1121fk%2Fdedsec1121fk) · [latest snapshot](https://archive.softwareheritage.org/swh:1:snp:0fc90da064ef8052b56fa6eedb878a88205173af/) · `full`
- **Corrupted Files:** [Software Heritage archive](https://archive.softwareheritage.org/browse/origin/?origin_url=https%3A%2F%2Fgithub.com%2Fdedsec1121fk%2FCorrupted-Files-Project) · [latest snapshot](https://archive.softwareheritage.org/swh:1:snp:a9c7391b498b3cda67cfdd5158d8bc7d4eee6675/) · `full`
- **Pocket AI:** [Software Heritage archive](https://archive.softwareheritage.org/browse/origin/?origin_url=https%3A%2F%2Fgithub.com%2Fdedsec1121fk%2FPocket-AI-Project) · [latest snapshot](https://archive.softwareheritage.org/swh:1:snp:10b3547fa34d0969398029647aed7ec4f1fe0a2d/) · `full`
- **Praying Project:** [Software Heritage archive](https://archive.softwareheritage.org/browse/origin/?origin_url=https%3A%2F%2Fgithub.com%2Fdedsec1121fk%2FPraying-Project) · [latest snapshot](https://archive.softwareheritage.org/swh:1:snp:0b111d36cd347ed8f4d2a23468b79ed950f86623/) · `full`
- **Offline Survival:** [Software Heritage archive](https://archive.softwareheritage.org/browse/origin/?origin_url=https%3A%2F%2Fgithub.com%2Fdedsec1121fk%2FOffline-Survival-Project) · [latest snapshot](https://archive.softwareheritage.org/swh:1:snp:74463bfb99413ef5d50df7cfae4845aa83fde5ed/) · `full`
- **Hacking Guide Project:** [Software Heritage archive](https://archive.softwareheritage.org/browse/origin/?origin_url=https%3A%2F%2Fgithub.com%2Fdedsec1121fk%2FHacking-Guide-Project) · [latest snapshot](https://archive.softwareheritage.org/swh:1:snp:ad11139d5d05cae40aa4d08997f31dc69b9323a7/) · `full`
- **Language Project:** [Software Heritage archive](https://archive.softwareheritage.org/browse/origin/?origin_url=https%3A%2F%2Fgithub.com%2Fdedsec1121fk%2FLanguage-Project) · [latest snapshot](https://archive.softwareheritage.org/swh:1:snp:7a5abba3c29b0260dd5ba46ac103006862a6886d/) · `full`
- **Ghost Project:** no confirmed Software Heritage snapshot yet
- **Save DedSec Project:** [Software Heritage archive](https://archive.softwareheritage.org/browse/origin/?origin_url=https%3A%2F%2Fgithub.com%2Fdedsec1121fk%2FSave-DedSec-Project) · [latest snapshot](https://archive.softwareheritage.org/swh:1:snp:560216cea159f7a7a59780c595bf67470fa760d9/) · `full`

Last checked: `2026-09-21T09:38:01Z`.

<!-- SOFTWARE_HERITAGE_LINKS_END -->

</details>
<details>
<summary><strong>Compact Internet Archive Working-Tree Archive</strong></summary>


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

</details>
<details>
<summary><strong>Resumable Wayback Queue</strong></summary>


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

</details>
<details>
<summary><strong>Backup Schedule</strong></summary>


All scheduled times use `Europe/Athens`.

| Day | Greece time | Archive targets |
|---|---:|---|
| Monday | 11:11 | DedSec Project main/backup + website source + website mirror + both live websites |
| Tuesday | 05:05 | GitHub profile, Corrupted Files, Pocket AI, Praying Project, Offline Survival, Hacking Guide Project, Language Project, Ghost Project and Save DedSec Project |
| Wednesday | 22:22 | DedSec Project main/backup + website source + website mirror + both live websites |
| Friday | 12:12 | GitHub profile, Corrupted Files, Pocket AI, Praying Project, Offline Survival, Hacking Guide Project, Language Project, Ghost Project and Save DedSec Project |
| Saturday | 00:00 | DedSec Project main/backup + website source + website mirror + both live websites |
| 1st & 3rd Sunday | 03:33 | GitHub profile, Corrupted Files, Pocket AI, Praying Project, Offline Survival, Hacking Guide Project, Language Project, Ghost Project and Save DedSec Project |
| 2nd & 4th Sunday | 03:00 | GitHub profile, Corrupted Files, Pocket AI, Praying Project, Offline Survival, Hacking Guide Project, Language Project, Ghost Project and Save DedSec Project |

If a month has a fifth Sunday, no Sunday backup is scheduled for that fifth occurrence.

### Monthly Backup Order Rotation

Scheduled repository backups run one target at a time so the configured order is meaningful.

- **January, March, May, July, September and November:** targets run in the exact order listed in the schedule above.
- **February, April, June, August, October and December:** the same target list runs in reverse order.
- **Manual runs:** keep the normal listed order.

For the DedSec/website group, the normal repository order is DedSec main → DedSec backup → website source/live websites → website mirror; the reverse order starts with the website mirror. For the other-projects group, the normal order is GitHub profile → Corrupted Files → Pocket AI → Praying Project → Offline Survival → Hacking Guide Project → Language Project → Ghost Project → Save DedSec Project, and even-numbered months reverse that sequence.

</details>
<details>
<summary><strong>Official Websites</strong></summary>


- **Main website:** https://ded-sec.space/
- **Backup website:** https://ded-sec.online/

</details>
<details>
<summary><strong>Repositories</strong></summary>


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
- **Ghost Project:** https://github.com/dedsec1121fk/Ghost-Project
- **Save DedSec Project:** https://github.com/dedsec1121fk/Save-DedSec-Project

</details>
<details>
<summary><strong>APK Preservation</strong></summary>

<!-- APK_ARCHIVE_STATUS_START -->
The same four APK dependencies used by the local `Settings.py` Save DedSec Project backup are checked on every workflow run.

- [Internet Archive APK collection](https://archive.org/details/dedsec1121fk-dedsec-project-apk-backups)
- **F-Droid.apk:** `985f5181d48bb6bafd54083a048b391271e0ab28385881cc41294fb01a222762` (12426276 bytes)
- **Termux.apk:** `fdd476982cd74f2f00aac12d3683b1fa260a0b2d146411b94e09d773be3a7b56` (114920926 bytes)
- **Termux_API.apk:** `4497dbbf81906df52e59ed387a5223d225aa0de3aca817cc557a621e4dadda44` (3956196 bytes)
- **Termux_Styling.apk:** `799a53f096c28e2aafae918f5ab91de500526bc5461030dbceea4e89bf56b68f` (32930486 bytes)

Last checked: `2026-09-21T10:29:52Z`.

<!-- APK_ARCHIVE_STATUS_END -->

</details>
<details>
<summary><strong>Automatic Archive Status</strong></summary>


<details>
<summary><strong>DedSec Project Main Repository</strong></summary>

<!-- DEDSEC_MAIN_ARCHIVE_STATUS_START -->
**Current archive status:** `complete`  
**Last complete or attempted save:** 2026-09-21 12:41:12 EEST  
**Current working-tree files:** 209  
**Latest working-tree change:** 2 changed/added, 0 deleted, 207 unchanged.  
**Compact archive uploaded this run:** `True`  
**Archive verification:** `True`  
**Scheduled time(s):** Monday 11:11, Wednesday 22:22 and Saturday 00:00 Europe/Athens  
**Archive mode:** One current `current-working-tree.tar.gz` plus manifest/checksums/state; `.git`, commits and push history are excluded.
**Legacy pre-migration mirror objects still visible:** 589. They are frozen and are not used for future backups.  

- [Internet Archive working-tree archive](https://archive.org/details/dedsec1121fk-dedsec-project-repository-snapshots)

This section is generated from `update.json`.
<!-- DEDSEC_MAIN_ARCHIVE_STATUS_END -->

</details>

<details>
<summary><strong>DedSec Project Backup Repository</strong></summary>

<!-- DEDSEC_BACKUP_ARCHIVE_STATUS_START -->
**Current archive status:** `complete`  
**Last complete or attempted save:** 2026-09-21 12:45:00 EEST  
**Current working-tree files:** 209  
**Latest working-tree change:** 2 changed/added, 0 deleted, 207 unchanged.  
**Compact archive uploaded this run:** `True`  
**Archive verification:** `True`  
**Scheduled time(s):** Monday 11:11, Wednesday 22:22 and Saturday 00:00 Europe/Athens  
**Archive mode:** One current `current-working-tree.tar.gz` plus manifest/checksums/state; `.git`, commits and push history are excluded.
**Legacy pre-migration mirror objects still visible:** 588. They are frozen and are not used for future backups.  

- [Internet Archive working-tree archive](https://archive.org/details/dedsec1121fk-dedsec-project-backup-repository-snapshots)

This section is generated from `update.json`.
<!-- DEDSEC_BACKUP_ARCHIVE_STATUS_END -->

</details>

<details>
<summary><strong>DedSec Websites and Website Source</strong></summary>

<!-- WEBSITES_ARCHIVE_STATUS_START -->
**Current archive status:** `complete`  
**Last complete or attempted save:** 2026-09-21 12:48:33 EEST  
**Current working-tree files:** 808  
**Latest working-tree change:** 496 changed/added, 2 deleted, 312 unchanged.  
**Compact archive uploaded this run:** `True`  
**Archive verification:** `True`  
**Scheduled time(s):** Monday 11:11, Wednesday 22:22 and Saturday 00:00 Europe/Athens  
**Archive mode:** One current `current-working-tree.tar.gz` plus manifest/checksums/state; `.git`, commits and push history are excluded.
**Legacy pre-migration mirror objects still visible:** 821. They are frozen and are not used for future backups.  
**Wayback queue remaining:** 1711  
**Wayback captures accepted:** 1334  

- [Internet Archive working-tree archive](https://archive.org/details/dedsec1121fk-dedsec-website-snapshots)
- [https://ded-sec.space Wayback history](https://web.archive.org/web/*/https://ded-sec.space/*)
- [https://ded-sec.online Wayback history](https://web.archive.org/web/*/https://ded-sec.online/*)

This section is generated from `update.json`.
<!-- WEBSITES_ARCHIVE_STATUS_END -->

</details>

<details>
<summary><strong>DedSec Website Mirror Repository</strong></summary>

<!-- DEDSEC_WEBSITE_MIRROR_ARCHIVE_STATUS_START -->
**Current archive status:** `complete`  
**Last complete or attempted save:** 2026-09-21 12:52:18 EEST  
**Current working-tree files:** 808  
**Latest working-tree change:** 496 changed/added, 2 deleted, 312 unchanged.  
**Compact archive uploaded this run:** `True`  
**Archive verification:** `True`  
**Scheduled time(s):** Monday 11:11, Wednesday 22:22 and Saturday 00:00 Europe/Athens  
**Archive mode:** One current `current-working-tree.tar.gz` plus manifest/checksums/state; `.git`, commits and push history are excluded.

- [Internet Archive working-tree archive](https://archive.org/details/dedsec1121fk-dedsec-website-mirror-repository-snapshots)

This section is generated from `update.json`.
<!-- DEDSEC_WEBSITE_MIRROR_ARCHIVE_STATUS_END -->

</details>

<details>
<summary><strong>DedSec GitHub Profile Repository</strong></summary>

<!-- GITHUB_PROFILE_ARCHIVE_STATUS_START -->
**Current archive status:** `complete`  
**Last complete or attempted save:** 2026-09-21 12:55:31 EEST  
**Current working-tree files:** 54  
**Latest working-tree change:** 35 changed/added, 0 deleted, 19 unchanged.  
**Compact archive uploaded this run:** `True`  
**Archive verification:** `True`  
**Scheduled time(s):** Tuesday 05:05, Friday 12:12, 1st/3rd Sunday 03:33 and 2nd/4th Sunday 03:00 Europe/Athens  
**Archive mode:** One current `current-working-tree.tar.gz` plus manifest/checksums/state; `.git`, commits and push history are excluded.
**Legacy pre-migration mirror objects still visible:** 8. They are frozen and are not used for future backups.  

- [Internet Archive working-tree archive](https://archive.org/details/dedsec1121fk-github-profile-repository-snapshots)

This section is generated from `update.json`.
<!-- GITHUB_PROFILE_ARCHIVE_STATUS_END -->

</details>

<details>
<summary><strong>Corrupted Files Project</strong></summary>

<!-- CORRUPTED_FILES_ARCHIVE_STATUS_START -->
**Current archive status:** `complete`  
**Last complete or attempted save:** 2026-09-21 12:57:26 EEST  
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

</details>

<details>
<summary><strong>Pocket AI</strong></summary>

<!-- POCKET_AI_ARCHIVE_STATUS_START -->
**Current archive status:** `complete`  
**Last complete or attempted save:** 2026-09-21 12:59:10 EEST  
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

</details>

<details>
<summary><strong>Praying Project</strong></summary>

<!-- PRAYING_PROJECT_ARCHIVE_STATUS_START -->
**Current archive status:** `complete`  
**Last complete or attempted save:** 2026-09-21 13:02:45 EEST  
**Current working-tree files:** 1502  
**Latest working-tree change:** 1 changed/added, 0 deleted, 1501 unchanged.  
**Compact archive uploaded this run:** `True`  
**Archive verification:** `True`  
**Scheduled time(s):** Tuesday 05:05, Friday 12:12, 1st/3rd Sunday 03:33 and 2nd/4th Sunday 03:00 Europe/Athens  
**Archive mode:** One current `current-working-tree.tar.gz` plus manifest/checksums/state; `.git`, commits and push history are excluded.
**Legacy pre-migration mirror objects still visible:** 74. They are frozen and are not used for future backups.  

- [Internet Archive working-tree archive](https://archive.org/details/dedsec1121fk-praying-project-repository-snapshots)

This section is generated from `update.json`.
<!-- PRAYING_PROJECT_ARCHIVE_STATUS_END -->

</details>

<details>
<summary><strong>Offline Survival Project</strong></summary>

<!-- OFFLINE_SURVIVAL_ARCHIVE_STATUS_START -->
**Current archive status:** `complete`  
**Last complete or attempted save:** 2026-09-21 13:04:33 EEST  
**Current working-tree files:** 921  
**Latest working-tree change:** 0 changed/added, 0 deleted, 921 unchanged.  
**Compact archive uploaded this run:** `False`  
**Archive verification:** `True`  
**Scheduled time(s):** Tuesday 05:05, Friday 12:12, 1st/3rd Sunday 03:33 and 2nd/4th Sunday 03:00 Europe/Athens  
**Archive mode:** One current `current-working-tree.tar.gz` plus manifest/checksums/state; `.git`, commits and push history are excluded.
**Legacy pre-migration mirror objects still visible:** 1410. They are frozen and are not used for future backups.  

- [Internet Archive working-tree archive](https://archive.org/details/dedsec1121fk-offline-survival-project-repository-snapshots)

This section is generated from `update.json`.
<!-- OFFLINE_SURVIVAL_ARCHIVE_STATUS_END -->

</details>

<details>
<summary><strong>Hacking Guide Project</strong></summary>

<!-- HACKING_GUIDE_ARCHIVE_STATUS_START -->
**Current archive status:** `complete`  
**Last complete or attempted save:** 2026-09-21 13:06:21 EEST  
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

</details>

<details>
<summary><strong>Language Project</strong></summary>

<!-- LANGUAGE_PROJECT_ARCHIVE_STATUS_START -->
**Current archive status:** `complete`  
**Last complete or attempted save:** 2026-09-21 13:08:20 EEST  
**Current working-tree files:** 10753  
**Latest working-tree change:** 0 changed/added, 0 deleted, 10753 unchanged.  
**Compact archive uploaded this run:** `False`  
**Archive verification:** `True`  
**Scheduled time(s):** Tuesday 05:05, Friday 12:12, 1st/3rd Sunday 03:33 and 2nd/4th Sunday 03:00 Europe/Athens  
**Archive mode:** One current `current-working-tree.tar.gz` plus manifest/checksums/state; `.git`, commits and push history are excluded.

- [Internet Archive working-tree archive](https://archive.org/details/dedsec1121fk-language-project-repository-snapshots)

This section is generated from `update.json`.
<!-- LANGUAGE_PROJECT_ARCHIVE_STATUS_END -->

</details>

<details>
<summary><strong>Ghost Project</strong></summary>

<!-- GHOST_PROJECT_ARCHIVE_STATUS_START -->
**Current archive status:** `uploaded_unverified`  
**Last complete or attempted save:** 2026-09-21 13:25:38 EEST  
**Current working-tree files:** 372  
**Latest working-tree change:** 372 changed/added, 0 deleted, 0 unchanged.  
**Compact archive uploaded this run:** `True`  
**Archive verification:** `False`  
**Scheduled time(s):** Tuesday 05:05, Friday 12:12, 1st/3rd Sunday 03:33 and 2nd/4th Sunday 03:00 Europe/Athens  
**Archive mode:** One current `current-working-tree.tar.gz` plus manifest/checksums/state; `.git`, commits and push history are excluded.

- [Internet Archive working-tree archive](https://archive.org/details/dedsec1121fk-ghost-project-repository-snapshots)

This section is generated from `update.json`.
<!-- GHOST_PROJECT_ARCHIVE_STATUS_END -->

</details>

<details>
<summary><strong>Save DedSec Project</strong></summary>

<!-- SAVE_DEDSEC_PROJECT_ARCHIVE_STATUS_START -->
**Current archive status:** `complete`  
**Last complete or attempted save:** 2026-09-21 13:29:07 EEST  
**Current working-tree files:** 7  
**Latest working-tree change:** 4 changed/added, 0 deleted, 3 unchanged.  
**Compact archive uploaded this run:** `True`  
**Archive verification:** `True`  
**Scheduled time(s):** Tuesday 05:05, Friday 12:12, 1st/3rd Sunday 03:33 and 2nd/4th Sunday 03:00 Europe/Athens  
**Archive mode:** One current `current-working-tree.tar.gz` plus manifest/checksums/state; `.git`, commits and push history are excluded.
**Legacy pre-migration mirror objects still visible:** 5. They are frozen and are not used for future backups.  

- [Internet Archive working-tree archive](https://archive.org/details/dedsec1121fk-save-dedsec-project-repository-snapshots)

This section is generated from `update.json`.
<!-- SAVE_DEDSEC_PROJECT_ARCHIVE_STATUS_END -->

</details>

</details>

---
<a id="greek-readme"></a>
# Save DedSec Project — Ελληνικά

> **Για να επιστρέψετε στην πλήρη Αγγλική έκδοση, συνεχίστε [Πατώντας Εδώ](#english-readme).**

Αυτό το repository διατηρεί το τρέχον οικοσύστημα DedSec Project συγχρονισμένο με το Internet Archive και το Software Heritage, διατηρεί τα APK dependencies που χρησιμοποιεί το τοπικό backup του Save DedSec Project και αποθηκεύει σταδιακά τους live ιστοτόπους DedSec μέσω του Wayback Machine.

<h2>Περιεχόμενα</h2>
* Σταθερή Αρχιτεκτονική
* Fork αυτού του Archive Controller
* Μόνιμοι Σύνδεσμοι Internet Archive
* Σύνδεσμοι Software Heritage
* Compact Archive του Working Tree στο Internet Archive
* Resumable Wayback Queue
* Πρόγραμμα Backup
* Επίσημοι Ιστότοποι
* Repositories
* Διατήρηση APK
* Αυτόματη Κατάσταση Archive

<details>
<summary><strong>Σταθερή Αρχιτεκτονική</strong></summary>


Ο συγχρονισμός του working tree στο Internet Archive, η διατήρηση του source code στο Software Heritage, η διατήρηση των APK και η επεξεργασία των Wayback captures για τους live ιστοτόπους είναι ξεχωριστές διαδικασίες:

1. Κάθε repository γίνεται checkout με `fetch-depth: 1`· το πλήρες Git history δεν γίνεται ποτέ fetch από αυτόν τον controller.
2. Το `.git` εξαιρείται από inventory, manifests, checksums και δημιουργία archive στο Internet Archive.
3. Ολόκληρο το τρέχον working tree πακετάρεται σε ένα deterministic `current-working-tree.tar.gz` για κάθε repository target του Internet Archive.
4. Το Internet Archive λαμβάνει το πολύ το compact TAR.GZ, `manifest.json`, `SHA256SUMS.txt` και ένα state checkpoint για κάθε repository target, αντί για εκατοντάδες ή χιλιάδες uploads ανά αρχείο.
5. Τα τέσσερα APK dependencies που ορίζονται από την τρέχουσα ρουτίνα `Settings.py` του Save DedSec Project κατεβαίνουν ξεχωριστά και συγχρονίζονται σε ένα dedicated software item στο Internet Archive μόνο όταν αλλάζουν τα hashes τους.
6. Κάθε δημόσιο Git repository παρακολουθείται από το Software Heritage. Τα repositories που επιλέγονται για ένα run λαμβάνουν Save Code Now request, εκτός αν υπάρχει ήδη ενεργό ή πολύ πρόσφατο request· οι σύνδεσμοι ελέγχονται και δημοσιεύονται σκόπιμα μόνο σε επόμενα workflow runs.
7. Τα repository archive files αντικαθίστανται με `x-archive-keep-old-version:0`, ώστε το Internet Archive να μην δημιουργεί αντίγραφα `history/files/` όταν γίνεται overwrite των τρεχόντων objects.
8. Τα repository targets δεν υποβάλλονται ποτέ στο Wayback. Μόνο οι δύο live ιστοσελίδες DedSec χρησιμοποιούν το resumable Wayback queue.

Αυτός ο σχεδιασμός αφαιρεί το burst από requests ανά αρχείο που προκαλούσε σφάλματα Internet Archive `503 SlowDown` και αποτρέπει επίσης την απόρριψη μεμονωμένων προβληματικών PDF κατά το upload: αρχεία όπως τα PDF διατηρούνται byte-for-byte μέσα στο TAR.GZ αντί να ανεβαίνουν ως ανεξάρτητα objects στο Internet Archive.

</details>
<details>
<summary><strong>Fork αυτού του Archive Controller</strong></summary>


Οι ιδιοκτήτες forks μπορούν να ρυθμίσουν τα δικά τους Internet Archive credentials και item identifiers ακολουθώντας τις [Οδηγίες Fork](Fork%20Instructions.md). Το αρχείο οδηγιών είναι πλήρως δίγλωσσο σε Αγγλικά και Ελληνικά.

</details>
<details>
<summary><strong>Μόνιμοι Σύνδεσμοι Internet Archive</strong></summary>

<!-- PERMANENT_ARCHIVE_LINKS_EL_START -->
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
- **Ghost Project:** https://archive.org/details/dedsec1121fk-ghost-project-repository-snapshots
- **Save DedSec Project:** https://archive.org/details/dedsec1121fk-save-dedsec-project-repository-snapshots
- **APK dependencies:** https://archive.org/details/dedsec1121fk-dedsec-project-apk-backups

Αυτή η ενότητα δημιουργείται ξανά σε κάθε archive run από τη ρύθμιση στόχων στο `.github/workflows/internet-archive.yml`.
<!-- PERMANENT_ARCHIVE_LINKS_EL_END -->

</details>

<details>
<summary><strong>Σύνδεσμοι Software Heritage</strong></summary>

<!-- SOFTWARE_HERITAGE_LINKS_EL_START -->
Τα αιτήματα Software Heritage Save Code Now υποβάλλονται σε ένα workflow run, αλλά οι σύνδεσμοι του archive επιβεβαιώνονται μόνο σε επόμενα runs. Έτσι δίνεται χρόνος στο Software Heritage να εισάγει κάθε repository πριν δημοσιευτεί εδώ ο σύνδεσμος.

- **DedSec main:** [archive στο Software Heritage](https://archive.softwareheritage.org/browse/origin/?origin_url=https%3A%2F%2Fgithub.com%2Fdedsec1121fk%2FDedSec) · [τελευταίο snapshot](https://archive.softwareheritage.org/swh:1:snp:9398c186b5c5727ca1b2acbe482010bffeb45d94/) · `full`
- **DedSec backup:** [archive στο Software Heritage](https://archive.softwareheritage.org/browse/origin/?origin_url=https%3A%2F%2Fgithub.com%2Fsal-scar%2FDedSec) · [τελευταίο snapshot](https://archive.softwareheritage.org/swh:1:snp:a4185f5487b9f54a85989033e5f1d9daa214f84a/) · `full`
- **Websites:** [archive στο Software Heritage](https://archive.softwareheritage.org/browse/origin/?origin_url=https%3A%2F%2Fgithub.com%2Fdedsec1121fk%2Fdedsec1121fk.github.io) · [τελευταίο snapshot](https://archive.softwareheritage.org/swh:1:snp:0fdf2bb2c142cdb402cb4fbe9f55bebb9386a24b/) · `full`
- **Website mirror:** [archive στο Software Heritage](https://archive.softwareheritage.org/browse/origin/?origin_url=https%3A%2F%2Fgithub.com%2Fsal-scar%2Fded-sec) · [τελευταίο snapshot](https://archive.softwareheritage.org/swh:1:snp:29edba7c972de18149294255d58688b6951daa20/) · `full`
- **GitHub profile:** [archive στο Software Heritage](https://archive.softwareheritage.org/browse/origin/?origin_url=https%3A%2F%2Fgithub.com%2Fdedsec1121fk%2Fdedsec1121fk) · [τελευταίο snapshot](https://archive.softwareheritage.org/swh:1:snp:0fc90da064ef8052b56fa6eedb878a88205173af/) · `full`
- **Corrupted Files:** [archive στο Software Heritage](https://archive.softwareheritage.org/browse/origin/?origin_url=https%3A%2F%2Fgithub.com%2Fdedsec1121fk%2FCorrupted-Files-Project) · [τελευταίο snapshot](https://archive.softwareheritage.org/swh:1:snp:a9c7391b498b3cda67cfdd5158d8bc7d4eee6675/) · `full`
- **Pocket AI:** [archive στο Software Heritage](https://archive.softwareheritage.org/browse/origin/?origin_url=https%3A%2F%2Fgithub.com%2Fdedsec1121fk%2FPocket-AI-Project) · [τελευταίο snapshot](https://archive.softwareheritage.org/swh:1:snp:10b3547fa34d0969398029647aed7ec4f1fe0a2d/) · `full`
- **Praying Project:** [archive στο Software Heritage](https://archive.softwareheritage.org/browse/origin/?origin_url=https%3A%2F%2Fgithub.com%2Fdedsec1121fk%2FPraying-Project) · [τελευταίο snapshot](https://archive.softwareheritage.org/swh:1:snp:0b111d36cd347ed8f4d2a23468b79ed950f86623/) · `full`
- **Offline Survival:** [archive στο Software Heritage](https://archive.softwareheritage.org/browse/origin/?origin_url=https%3A%2F%2Fgithub.com%2Fdedsec1121fk%2FOffline-Survival-Project) · [τελευταίο snapshot](https://archive.softwareheritage.org/swh:1:snp:74463bfb99413ef5d50df7cfae4845aa83fde5ed/) · `full`
- **Hacking Guide Project:** [archive στο Software Heritage](https://archive.softwareheritage.org/browse/origin/?origin_url=https%3A%2F%2Fgithub.com%2Fdedsec1121fk%2FHacking-Guide-Project) · [τελευταίο snapshot](https://archive.softwareheritage.org/swh:1:snp:ad11139d5d05cae40aa4d08997f31dc69b9323a7/) · `full`
- **Language Project:** [archive στο Software Heritage](https://archive.softwareheritage.org/browse/origin/?origin_url=https%3A%2F%2Fgithub.com%2Fdedsec1121fk%2FLanguage-Project) · [τελευταίο snapshot](https://archive.softwareheritage.org/swh:1:snp:7a5abba3c29b0260dd5ba46ac103006862a6886d/) · `full`
- **Ghost Project:** δεν υπάρχει ακόμη επιβεβαιωμένο snapshot στο Software Heritage
- **Save DedSec Project:** [archive στο Software Heritage](https://archive.softwareheritage.org/browse/origin/?origin_url=https%3A%2F%2Fgithub.com%2Fdedsec1121fk%2FSave-DedSec-Project) · [τελευταίο snapshot](https://archive.softwareheritage.org/swh:1:snp:560216cea159f7a7a59780c595bf67470fa760d9/) · `full`

Τελευταίος έλεγχος: `2026-09-21T09:38:01Z`.

<!-- SOFTWARE_HERITAGE_LINKS_EL_END -->

</details>
<details>
<summary><strong>Compact Archive του Working Tree στο Internet Archive</strong></summary>


Το archive λειτουργεί σε **working-tree-only mode**. Τα Git metadata και το history δεν αποτελούν inputs διατήρησης. Σε κάθε run, το workflow κάνει inventory του τρέχοντος checkout, υπολογίζει SHA-256 hashes και συγκρίνει το snapshot του working tree με την προηγούμενη κατάσταση.

Όταν αλλάζει το snapshot, ενημερώνεται το target item με:

```text
current-working-tree.tar.gz
manifest.json
SHA256SUMS.txt
archive-state/update.json
```

Όταν το snapshot δεν έχει αλλάξει, το μεγάλο TAR.GZ δεν ανεβαίνει ξανά· ανανεώνεται μόνο το compact state που χρειάζεται το workflow. Το archive είναι deterministic, άρα ίδιο περιεχόμενο working tree παράγει ίδια archive bytes.

Ιδιότητες ασφάλειας και ιδιωτικότητας:

- Οι φάκελοι και τα αρχεία `.git` εξαιρούνται σε κάθε βάθος, μαζί με nested submodules.
- Git commits, branches, reflogs, push history, Git bundles, commit pages και commit-pinned GitHub archives δεν αρχειοθετούνται.
- Η αντικατάσταση ή διαγραφή objects στο Internet Archive χρησιμοποιεί ρητά `x-archive-keep-old-version:0`.
- Υπάρχοντα `git-history.bundle`, `history/files/` objects και παλιά timestamped history archives καθαρίζονται σε μικρά περιορισμένα batches ώστε η εκκαθάριση να μην ξαναδημιουργήσει το παλιό request storm.
- Παλιά `mirror/` objects από τον προηγούμενο σχεδιασμό δεν ενημερώνονται πλέον. Δεν μπορούν να καταγράψουν μελλοντικά pushes και αναφέρονται ως legacy objects μέχρι να αφαιρεθούν ξεχωριστά.
- Τα item metadata διορθώνονται μέσω του Internet Archive Metadata API ώστε να μην ισχυρίζονται πλέον ότι διατηρείται Git history.
- Private Sponsors-Only repositories δεν δημοσιεύονται από αυτόν τον public archive controller· μόνο public repository targets στέλνονται στο Internet Archive και στο Software Heritage.

Ένα συγχρονισμένο συνδυασμένο αντίγραφο κατάστασης αποθηκεύεται σε αυτό το repository ως:

```text
update.json
```

Πριν από S3 writes, το workflow ελέγχει το queue-capacity endpoint του Internet Archive και περιμένει όταν το item/account είναι πάνω από το όριο. Τα uploads χρησιμοποιούν επίσης μεγαλύτερα retry windows για προσωρινές καταστάσεις `429`/`503`.

</details>
<details>
<summary><strong>Resumable Wayback Queue</strong></summary>


Η επεξεργασία Wayback περιορίζεται στους live ιστοτόπους DedSec. URLs από GitHub repositories, commits, branches, tags, releases και source history δεν μπαίνουν στο queue.

Ένα σειριακό Wayback job:

- Επεξεργάζεται το πολύ 120 URLs ανά workflow run.
- Τρέχει για έως τρεις ώρες.
- Γράφει Internet Archive state checkpoint κάθε 20 επεξεργασμένα URLs αντί μετά από κάθε URL.
- Γράφει ένα τελικό checkpoint στο τέλος του batch.
- Αντιμετωπίζει active-session limits και HTTP 429/500/502/503/504 ως προσωρινά.
- Αφήνει τα μη ολοκληρωμένα URLs στο queue για το επόμενο run.
- Παραλείπεται εσωτερικά όταν το επιλεγμένο backup group δεν περιέχει website target.
- Δεν αποτυγχάνει τη διατήρηση repository files απλώς επειδή το Wayback είναι απασχολημένο.

</details>
<details>
<summary><strong>Πρόγραμμα Backup</strong></summary>


Όλες οι προγραμματισμένες ώρες χρησιμοποιούν `Europe/Athens`.

| Ημέρα | Ώρα Ελλάδας | Archive targets |
|---|---:|---|
| Δευτέρα | 11:11 | DedSec Project main/backup + website source + website mirror + και οι δύο live ιστοσελίδες |
| Τρίτη | 05:05 | GitHub profile, Corrupted Files, Pocket AI, Praying Project, Offline Survival, Hacking Guide Project, Language Project, Ghost Project and Save DedSec Project |
| Τετάρτη | 22:22 | DedSec Project main/backup + website source + website mirror + και οι δύο live ιστοσελίδες |
| Παρασκευή | 12:12 | GitHub profile, Corrupted Files, Pocket AI, Praying Project, Offline Survival, Hacking Guide Project, Language Project, Ghost Project and Save DedSec Project |
| Σάββατο | 00:00 | DedSec Project main/backup + website source + website mirror + και οι δύο live ιστοσελίδες |
| 1η & 3η Κυριακή | 03:33 | GitHub profile, Corrupted Files, Pocket AI, Praying Project, Offline Survival, Hacking Guide Project, Language Project, Ghost Project and Save DedSec Project |
| 2η & 4η Κυριακή | 03:00 | GitHub profile, Corrupted Files, Pocket AI, Praying Project, Offline Survival, Hacking Guide Project, Language Project, Ghost Project and Save DedSec Project |

Αν ένας μήνας έχει πέμπτη Κυριακή, δεν προγραμματίζεται Sunday backup για αυτή την πέμπτη εμφάνιση.

### Μηνιαία Εναλλαγή Σειράς Backup

Τα προγραμματισμένα repository backups τρέχουν ένα target τη φορά, ώστε η ρυθμισμένη σειρά να έχει σημασία.

- **Ιανουάριος, Μάρτιος, Μάιος, Ιούλιος, Σεπτέμβριος και Νοέμβριος:** τα targets τρέχουν με την ακριβή σειρά του παραπάνω προγράμματος.
- **Φεβρουάριος, Απρίλιος, Ιούνιος, Αύγουστος, Οκτώβριος και Δεκέμβριος:** η ίδια λίστα targets τρέχει με αντίστροφη σειρά.
- **Manual runs:** κρατούν την κανονική σειρά.

Για το DedSec/website group, η κανονική σειρά repositories είναι DedSec main → DedSec backup → website source/live websites → website mirror· η αντίστροφη σειρά ξεκινά από το website mirror. Για το other-projects group, η κανονική σειρά είναι GitHub profile → Corrupted Files → Pocket AI → Praying Project → Offline Survival → Hacking Guide Project → Language Project → Ghost Project → Save DedSec Project, και οι ζυγοί μήνες αντιστρέφουν αυτή τη σειρά.

</details>
<details>
<summary><strong>Επίσημοι Ιστότοποι</strong></summary>


- **Κύριος ιστότοπος:** https://ded-sec.space/
- **Backup ιστότοπος:** https://ded-sec.online/

</details>
<details>
<summary><strong>Repositories</strong></summary>


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
- **Ghost Project:** https://github.com/dedsec1121fk/Ghost-Project
- **Save DedSec Project:** https://github.com/dedsec1121fk/Save-DedSec-Project

</details>
<details>
<summary><strong>Διατήρηση APK</strong></summary>

<!-- APK_ARCHIVE_STATUS_EL_START -->
Τα ίδια τέσσερα APK dependencies που χρησιμοποιεί το τοπικό backup του Save DedSec Project μέσω `Settings.py` ελέγχονται σε κάθε workflow run.

- [Συλλογή APK στο Internet Archive](https://archive.org/details/dedsec1121fk-dedsec-project-apk-backups)
- **F-Droid.apk:** `985f5181d48bb6bafd54083a048b391271e0ab28385881cc41294fb01a222762` (12426276 bytes)
- **Termux.apk:** `fdd476982cd74f2f00aac12d3683b1fa260a0b2d146411b94e09d773be3a7b56` (114920926 bytes)
- **Termux_API.apk:** `4497dbbf81906df52e59ed387a5223d225aa0de3aca817cc557a621e4dadda44` (3956196 bytes)
- **Termux_Styling.apk:** `799a53f096c28e2aafae918f5ab91de500526bc5461030dbceea4e89bf56b68f` (32930486 bytes)

Τελευταίος έλεγχος: `2026-09-21T10:29:52Z`.

<!-- APK_ARCHIVE_STATUS_EL_END -->

</details>
<details>
<summary><strong>Αυτόματη Κατάσταση Archive</strong></summary>


<details>
<summary><strong>DedSec Project Main Repository</strong></summary>

<!-- GREEK_DEDSEC_MAIN_ARCHIVE_STATUS_START -->
**Τρέχουσα κατάσταση αρχειοθέτησης:** `complete`  
**Τελευταία ολοκληρωμένη ή επιχειρούμενη αποθήκευση:** 2026-09-21 12:41:12 EEST  
**Αρχεία τρέχοντος working tree:** 209  
**Τελευταία αλλαγή working tree:** 2 αλλαγμένα/προστέθηκαν, 0 διαγράφηκαν, 207 αμετάβλητα.  
**Ανέβηκε compact archive σε αυτό το run:** `True`  
**Επαλήθευση archive:** `True`  
**Προγραμματισμένες ώρες:** Monday 11:11, Wednesday 22:22 and Saturday 00:00 Europe/Athens  
**Λειτουργία αρχειοθέτησης:** Ένα τρέχον `current-working-tree.tar.gz` μαζί με manifest/checksums/state· τα `.git`, commits και push history εξαιρούνται.
**Παλιότερα mirror objects πριν τη μετάβαση που παραμένουν ορατά:** 589. Είναι παγωμένα και δεν χρησιμοποιούνται για μελλοντικά backups.  

- [Working-tree archive στο Internet Archive](https://archive.org/details/dedsec1121fk-dedsec-project-repository-snapshots)

Αυτή η ενότητα δημιουργείται από το `update.json`.
<!-- GREEK_DEDSEC_MAIN_ARCHIVE_STATUS_END -->

</details>

<details>
<summary><strong>DedSec Project Backup Repository</strong></summary>

<!-- GREEK_DEDSEC_BACKUP_ARCHIVE_STATUS_START -->
**Τρέχουσα κατάσταση αρχειοθέτησης:** `complete`  
**Τελευταία ολοκληρωμένη ή επιχειρούμενη αποθήκευση:** 2026-09-21 12:45:00 EEST  
**Αρχεία τρέχοντος working tree:** 209  
**Τελευταία αλλαγή working tree:** 2 αλλαγμένα/προστέθηκαν, 0 διαγράφηκαν, 207 αμετάβλητα.  
**Ανέβηκε compact archive σε αυτό το run:** `True`  
**Επαλήθευση archive:** `True`  
**Προγραμματισμένες ώρες:** Monday 11:11, Wednesday 22:22 and Saturday 00:00 Europe/Athens  
**Λειτουργία αρχειοθέτησης:** Ένα τρέχον `current-working-tree.tar.gz` μαζί με manifest/checksums/state· τα `.git`, commits και push history εξαιρούνται.
**Παλιότερα mirror objects πριν τη μετάβαση που παραμένουν ορατά:** 588. Είναι παγωμένα και δεν χρησιμοποιούνται για μελλοντικά backups.  

- [Working-tree archive στο Internet Archive](https://archive.org/details/dedsec1121fk-dedsec-project-backup-repository-snapshots)

Αυτή η ενότητα δημιουργείται από το `update.json`.
<!-- GREEK_DEDSEC_BACKUP_ARCHIVE_STATUS_END -->

</details>

<details>
<summary><strong>DedSec Websites and Website Source</strong></summary>

<!-- GREEK_WEBSITES_ARCHIVE_STATUS_START -->
**Τρέχουσα κατάσταση αρχειοθέτησης:** `complete`  
**Τελευταία ολοκληρωμένη ή επιχειρούμενη αποθήκευση:** 2026-09-21 12:48:33 EEST  
**Αρχεία τρέχοντος working tree:** 808  
**Τελευταία αλλαγή working tree:** 496 αλλαγμένα/προστέθηκαν, 2 διαγράφηκαν, 312 αμετάβλητα.  
**Ανέβηκε compact archive σε αυτό το run:** `True`  
**Επαλήθευση archive:** `True`  
**Προγραμματισμένες ώρες:** Monday 11:11, Wednesday 22:22 and Saturday 00:00 Europe/Athens  
**Λειτουργία αρχειοθέτησης:** Ένα τρέχον `current-working-tree.tar.gz` μαζί με manifest/checksums/state· τα `.git`, commits και push history εξαιρούνται.
**Παλιότερα mirror objects πριν τη μετάβαση που παραμένουν ορατά:** 821. Είναι παγωμένα και δεν χρησιμοποιούνται για μελλοντικά backups.  
**Υπόλοιπο Wayback queue:** 1711  
**Wayback captures που έγιναν δεκτά:** 1334  

- [Working-tree archive στο Internet Archive](https://archive.org/details/dedsec1121fk-dedsec-website-snapshots)
- [Ιστορικό Wayback για https://ded-sec.space](https://web.archive.org/web/*/https://ded-sec.space/*)
- [Ιστορικό Wayback για https://ded-sec.online](https://web.archive.org/web/*/https://ded-sec.online/*)

Αυτή η ενότητα δημιουργείται από το `update.json`.
<!-- GREEK_WEBSITES_ARCHIVE_STATUS_END -->

</details>

<details>
<summary><strong>DedSec Website Mirror Repository</strong></summary>

<!-- GREEK_DEDSEC_WEBSITE_MIRROR_ARCHIVE_STATUS_START -->
**Τρέχουσα κατάσταση αρχειοθέτησης:** `complete`  
**Τελευταία ολοκληρωμένη ή επιχειρούμενη αποθήκευση:** 2026-09-21 12:52:18 EEST  
**Αρχεία τρέχοντος working tree:** 808  
**Τελευταία αλλαγή working tree:** 496 αλλαγμένα/προστέθηκαν, 2 διαγράφηκαν, 312 αμετάβλητα.  
**Ανέβηκε compact archive σε αυτό το run:** `True`  
**Επαλήθευση archive:** `True`  
**Προγραμματισμένες ώρες:** Monday 11:11, Wednesday 22:22 and Saturday 00:00 Europe/Athens  
**Λειτουργία αρχειοθέτησης:** Ένα τρέχον `current-working-tree.tar.gz` μαζί με manifest/checksums/state· τα `.git`, commits και push history εξαιρούνται.

- [Working-tree archive στο Internet Archive](https://archive.org/details/dedsec1121fk-dedsec-website-mirror-repository-snapshots)

Αυτή η ενότητα δημιουργείται από το `update.json`.
<!-- GREEK_DEDSEC_WEBSITE_MIRROR_ARCHIVE_STATUS_END -->

</details>

<details>
<summary><strong>DedSec GitHub Profile Repository</strong></summary>

<!-- GREEK_GITHUB_PROFILE_ARCHIVE_STATUS_START -->
**Τρέχουσα κατάσταση αρχειοθέτησης:** `complete`  
**Τελευταία ολοκληρωμένη ή επιχειρούμενη αποθήκευση:** 2026-09-21 12:55:31 EEST  
**Αρχεία τρέχοντος working tree:** 54  
**Τελευταία αλλαγή working tree:** 35 αλλαγμένα/προστέθηκαν, 0 διαγράφηκαν, 19 αμετάβλητα.  
**Ανέβηκε compact archive σε αυτό το run:** `True`  
**Επαλήθευση archive:** `True`  
**Προγραμματισμένες ώρες:** Tuesday 05:05, Friday 12:12, 1st/3rd Sunday 03:33 and 2nd/4th Sunday 03:00 Europe/Athens  
**Λειτουργία αρχειοθέτησης:** Ένα τρέχον `current-working-tree.tar.gz` μαζί με manifest/checksums/state· τα `.git`, commits και push history εξαιρούνται.
**Παλιότερα mirror objects πριν τη μετάβαση που παραμένουν ορατά:** 8. Είναι παγωμένα και δεν χρησιμοποιούνται για μελλοντικά backups.  

- [Working-tree archive στο Internet Archive](https://archive.org/details/dedsec1121fk-github-profile-repository-snapshots)

Αυτή η ενότητα δημιουργείται από το `update.json`.
<!-- GREEK_GITHUB_PROFILE_ARCHIVE_STATUS_END -->

</details>

<details>
<summary><strong>Corrupted Files Project</strong></summary>

<!-- GREEK_CORRUPTED_FILES_ARCHIVE_STATUS_START -->
**Τρέχουσα κατάσταση αρχειοθέτησης:** `complete`  
**Τελευταία ολοκληρωμένη ή επιχειρούμενη αποθήκευση:** 2026-09-21 12:57:26 EEST  
**Αρχεία τρέχοντος working tree:** 2148  
**Τελευταία αλλαγή working tree:** 0 αλλαγμένα/προστέθηκαν, 0 διαγράφηκαν, 2148 αμετάβλητα.  
**Ανέβηκε compact archive σε αυτό το run:** `False`  
**Επαλήθευση archive:** `True`  
**Προγραμματισμένες ώρες:** Tuesday 05:05, Friday 12:12, 1st/3rd Sunday 03:33 and 2nd/4th Sunday 03:00 Europe/Athens  
**Λειτουργία αρχειοθέτησης:** Ένα τρέχον `current-working-tree.tar.gz` μαζί με manifest/checksums/state· τα `.git`, commits και push history εξαιρούνται.
**Παλιότερα mirror objects πριν τη μετάβαση που παραμένουν ορατά:** 2141. Είναι παγωμένα και δεν χρησιμοποιούνται για μελλοντικά backups.  

- [Working-tree archive στο Internet Archive](https://archive.org/details/dedsec1121fk-corrupted-files-project-repository-snapshots)

Αυτή η ενότητα δημιουργείται από το `update.json`.
<!-- GREEK_CORRUPTED_FILES_ARCHIVE_STATUS_END -->

</details>

<details>
<summary><strong>Pocket AI</strong></summary>

<!-- GREEK_POCKET_AI_ARCHIVE_STATUS_START -->
**Τρέχουσα κατάσταση αρχειοθέτησης:** `complete`  
**Τελευταία ολοκληρωμένη ή επιχειρούμενη αποθήκευση:** 2026-09-21 12:59:10 EEST  
**Αρχεία τρέχοντος working tree:** 128  
**Τελευταία αλλαγή working tree:** 0 αλλαγμένα/προστέθηκαν, 0 διαγράφηκαν, 128 αμετάβλητα.  
**Ανέβηκε compact archive σε αυτό το run:** `False`  
**Επαλήθευση archive:** `True`  
**Προγραμματισμένες ώρες:** Tuesday 05:05, Friday 12:12, 1st/3rd Sunday 03:33 and 2nd/4th Sunday 03:00 Europe/Athens  
**Λειτουργία αρχειοθέτησης:** Ένα τρέχον `current-working-tree.tar.gz` μαζί με manifest/checksums/state· τα `.git`, commits και push history εξαιρούνται.
**Παλιότερα mirror objects πριν τη μετάβαση που παραμένουν ορατά:** 128. Είναι παγωμένα και δεν χρησιμοποιούνται για μελλοντικά backups.  

- [Working-tree archive στο Internet Archive](https://archive.org/details/dedsec1121fk-pocket-ai-repository-snapshots)

Αυτή η ενότητα δημιουργείται από το `update.json`.
<!-- GREEK_POCKET_AI_ARCHIVE_STATUS_END -->

</details>

<details>
<summary><strong>Praying Project</strong></summary>

<!-- GREEK_PRAYING_PROJECT_ARCHIVE_STATUS_START -->
**Τρέχουσα κατάσταση αρχειοθέτησης:** `complete`  
**Τελευταία ολοκληρωμένη ή επιχειρούμενη αποθήκευση:** 2026-09-21 13:02:45 EEST  
**Αρχεία τρέχοντος working tree:** 1502  
**Τελευταία αλλαγή working tree:** 1 αλλαγμένα/προστέθηκαν, 0 διαγράφηκαν, 1501 αμετάβλητα.  
**Ανέβηκε compact archive σε αυτό το run:** `True`  
**Επαλήθευση archive:** `True`  
**Προγραμματισμένες ώρες:** Tuesday 05:05, Friday 12:12, 1st/3rd Sunday 03:33 and 2nd/4th Sunday 03:00 Europe/Athens  
**Λειτουργία αρχειοθέτησης:** Ένα τρέχον `current-working-tree.tar.gz` μαζί με manifest/checksums/state· τα `.git`, commits και push history εξαιρούνται.
**Παλιότερα mirror objects πριν τη μετάβαση που παραμένουν ορατά:** 74. Είναι παγωμένα και δεν χρησιμοποιούνται για μελλοντικά backups.  

- [Working-tree archive στο Internet Archive](https://archive.org/details/dedsec1121fk-praying-project-repository-snapshots)

Αυτή η ενότητα δημιουργείται από το `update.json`.
<!-- GREEK_PRAYING_PROJECT_ARCHIVE_STATUS_END -->

</details>

<details>
<summary><strong>Offline Survival Project</strong></summary>

<!-- GREEK_OFFLINE_SURVIVAL_ARCHIVE_STATUS_START -->
**Τρέχουσα κατάσταση αρχειοθέτησης:** `complete`  
**Τελευταία ολοκληρωμένη ή επιχειρούμενη αποθήκευση:** 2026-09-21 13:04:33 EEST  
**Αρχεία τρέχοντος working tree:** 921  
**Τελευταία αλλαγή working tree:** 0 αλλαγμένα/προστέθηκαν, 0 διαγράφηκαν, 921 αμετάβλητα.  
**Ανέβηκε compact archive σε αυτό το run:** `False`  
**Επαλήθευση archive:** `True`  
**Προγραμματισμένες ώρες:** Tuesday 05:05, Friday 12:12, 1st/3rd Sunday 03:33 and 2nd/4th Sunday 03:00 Europe/Athens  
**Λειτουργία αρχειοθέτησης:** Ένα τρέχον `current-working-tree.tar.gz` μαζί με manifest/checksums/state· τα `.git`, commits και push history εξαιρούνται.
**Παλιότερα mirror objects πριν τη μετάβαση που παραμένουν ορατά:** 1410. Είναι παγωμένα και δεν χρησιμοποιούνται για μελλοντικά backups.  

- [Working-tree archive στο Internet Archive](https://archive.org/details/dedsec1121fk-offline-survival-project-repository-snapshots)

Αυτή η ενότητα δημιουργείται από το `update.json`.
<!-- GREEK_OFFLINE_SURVIVAL_ARCHIVE_STATUS_END -->

</details>

<details>
<summary><strong>Hacking Guide Project</strong></summary>

<!-- GREEK_HACKING_GUIDE_ARCHIVE_STATUS_START -->
**Τρέχουσα κατάσταση αρχειοθέτησης:** `complete`  
**Τελευταία ολοκληρωμένη ή επιχειρούμενη αποθήκευση:** 2026-09-21 13:06:21 EEST  
**Αρχεία τρέχοντος working tree:** 334  
**Τελευταία αλλαγή working tree:** 0 αλλαγμένα/προστέθηκαν, 0 διαγράφηκαν, 334 αμετάβλητα.  
**Ανέβηκε compact archive σε αυτό το run:** `False`  
**Επαλήθευση archive:** `True`  
**Προγραμματισμένες ώρες:** Tuesday 05:05, Friday 12:12, 1st/3rd Sunday 03:33 and 2nd/4th Sunday 03:00 Europe/Athens  
**Λειτουργία αρχειοθέτησης:** Ένα τρέχον `current-working-tree.tar.gz` μαζί με manifest/checksums/state· τα `.git`, commits και push history εξαιρούνται.
**Παλιότερα mirror objects πριν τη μετάβαση που παραμένουν ορατά:** 6. Είναι παγωμένα και δεν χρησιμοποιούνται για μελλοντικά backups.  

- [Working-tree archive στο Internet Archive](https://archive.org/details/dedsec1121fk-hacking-guide-project-repository-snapshots)

Αυτή η ενότητα δημιουργείται από το `update.json`.
<!-- GREEK_HACKING_GUIDE_ARCHIVE_STATUS_END -->

</details>

<details>
<summary><strong>Language Project</strong></summary>

<!-- GREEK_LANGUAGE_PROJECT_ARCHIVE_STATUS_START -->
**Τρέχουσα κατάσταση αρχειοθέτησης:** `complete`  
**Τελευταία ολοκληρωμένη ή επιχειρούμενη αποθήκευση:** 2026-09-21 13:08:20 EEST  
**Αρχεία τρέχοντος working tree:** 10753  
**Τελευταία αλλαγή working tree:** 0 αλλαγμένα/προστέθηκαν, 0 διαγράφηκαν, 10753 αμετάβλητα.  
**Ανέβηκε compact archive σε αυτό το run:** `False`  
**Επαλήθευση archive:** `True`  
**Προγραμματισμένες ώρες:** Tuesday 05:05, Friday 12:12, 1st/3rd Sunday 03:33 and 2nd/4th Sunday 03:00 Europe/Athens  
**Λειτουργία αρχειοθέτησης:** Ένα τρέχον `current-working-tree.tar.gz` μαζί με manifest/checksums/state· τα `.git`, commits και push history εξαιρούνται.

- [Working-tree archive στο Internet Archive](https://archive.org/details/dedsec1121fk-language-project-repository-snapshots)

Αυτή η ενότητα δημιουργείται από το `update.json`.
<!-- GREEK_LANGUAGE_PROJECT_ARCHIVE_STATUS_END -->

</details>

<details>
<summary><strong>Ghost Project</strong></summary>

<!-- GREEK_GHOST_PROJECT_ARCHIVE_STATUS_START -->
**Τρέχουσα κατάσταση αρχειοθέτησης:** `uploaded_unverified`  
**Τελευταία ολοκληρωμένη ή επιχειρούμενη αποθήκευση:** 2026-09-21 13:25:38 EEST  
**Αρχεία τρέχοντος working tree:** 372  
**Τελευταία αλλαγή working tree:** 372 αλλαγμένα/προστέθηκαν, 0 διαγράφηκαν, 0 αμετάβλητα.  
**Ανέβηκε compact archive σε αυτό το run:** `True`  
**Επαλήθευση archive:** `False`  
**Προγραμματισμένες ώρες:** Tuesday 05:05, Friday 12:12, 1st/3rd Sunday 03:33 and 2nd/4th Sunday 03:00 Europe/Athens  
**Λειτουργία αρχειοθέτησης:** Ένα τρέχον `current-working-tree.tar.gz` μαζί με manifest/checksums/state· τα `.git`, commits και push history εξαιρούνται.

- [Working-tree archive στο Internet Archive](https://archive.org/details/dedsec1121fk-ghost-project-repository-snapshots)

Αυτή η ενότητα δημιουργείται από το `update.json`.
<!-- GREEK_GHOST_PROJECT_ARCHIVE_STATUS_END -->

</details>

<details>
<summary><strong>Save DedSec Project</strong></summary>

<!-- GREEK_SAVE_DEDSEC_PROJECT_ARCHIVE_STATUS_START -->
**Τρέχουσα κατάσταση αρχειοθέτησης:** `complete`  
**Τελευταία ολοκληρωμένη ή επιχειρούμενη αποθήκευση:** 2026-09-21 13:29:07 EEST  
**Αρχεία τρέχοντος working tree:** 7  
**Τελευταία αλλαγή working tree:** 4 αλλαγμένα/προστέθηκαν, 0 διαγράφηκαν, 3 αμετάβλητα.  
**Ανέβηκε compact archive σε αυτό το run:** `True`  
**Επαλήθευση archive:** `True`  
**Προγραμματισμένες ώρες:** Tuesday 05:05, Friday 12:12, 1st/3rd Sunday 03:33 and 2nd/4th Sunday 03:00 Europe/Athens  
**Λειτουργία αρχειοθέτησης:** Ένα τρέχον `current-working-tree.tar.gz` μαζί με manifest/checksums/state· τα `.git`, commits και push history εξαιρούνται.
**Παλιότερα mirror objects πριν τη μετάβαση που παραμένουν ορατά:** 5. Είναι παγωμένα και δεν χρησιμοποιούνται για μελλοντικά backups.  

- [Working-tree archive στο Internet Archive](https://archive.org/details/dedsec1121fk-save-dedsec-project-repository-snapshots)

Αυτή η ενότητα δημιουργείται από το `update.json`.
<!-- GREEK_SAVE_DEDSEC_PROJECT_ARCHIVE_STATUS_END -->

</details>

</details>
