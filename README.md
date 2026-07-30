# Save DedSec Project

This repository automatically preserves the current DedSec Project ecosystem in Internet Archive and Wayback Machine.

## Incremental and Resumable Synchronization

The first successful run uploads every current file. Later runs calculate SHA-256 hashes and synchronize only the differences:

- New files are uploaded.
- Changed files replace their matching Internet Archive objects.
- Files deleted from GitHub are deleted from the Internet Archive mirror.
- Unchanged files are skipped.
- Missing remote mirror files are detected and restored.
- The stable `git-history.bundle` is replaced only when repository history changes.

Every successful file upload or deletion is checkpointed in the target Internet Archive item as:

```text
archive-state/update.json
```

A synchronized readable copy is committed here as:

```text
.github/workflows/update.json
```

Resume is **file-level**. If a job stops, the next run skips all checkpointed files and continues with the remaining files. A file interrupted in the middle may need to restart, but previously completed files do not.

## Weekly Schedule

All groups run on **Wednesday, Friday and Sunday** using the `Europe/Athens` timezone.

| Greece time | Archive group | Maximum duration |
|---|---|---|
| 08:00 | DedSec Project main and backup repositories | 5 hours |
| 13:50 | Main website, backup website and website source | 5 hours |
| 19:30 | GitHub profile, Corrupted Files, Pocket AI and Offline Survival | 4 hours |

Repositories in the same group run in parallel.

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

## Internet Archive Storage Layout

Each repository uses its own Internet Archive item:

```text
mirror/<original repository path>
git-history.bundle
manifest.json
SHA256SUMS.txt
wayback-report.json
archive-state/update.json
```

The `mirror/` tree always represents the latest fully synchronized working tree. Timestamped packages created by older workflow versions are removed only after the new mirror passes verification.

## Permanent Archive Links

- **Websites:** https://archive.org/details/dedsec1121fk-dedsec-website-snapshots
- **DedSec main:** https://archive.org/details/dedsec1121fk-dedsec-project-repository-snapshots
- **DedSec backup:** https://archive.org/details/dedsec1121fk-dedsec-project-backup-repository-snapshots
- **GitHub profile:** https://archive.org/details/dedsec1121fk-github-profile-repository-snapshots
- **Corrupted Files:** https://archive.org/details/dedsec1121fk-corrupted-files-project-repository-snapshots
- **Pocket AI:** https://archive.org/details/dedsec1121fk-pocket-ai-repository-snapshots
- **Offline Survival:** https://archive.org/details/dedsec1121fk-offline-survival-project-repository-snapshots

## Automatic Archive Status

<!-- WEBSITES_ARCHIVE_STATUS_START -->
### DedSec Websites and Website Source

**Current synchronization status:** `not_started`  
**Last complete save:** Not completed yet.  
**Scheduled window:** Wednesday, Friday and Sunday, 13:50–18:50 Europe/Athens.  
**Resume mode:** File-level.

- [Internet Archive current mirror](https://archive.org/details/dedsec1121fk-dedsec-website-snapshots)
- [Main website Wayback history](https://web.archive.org/web/*/https://ded-sec.space/*)
- [Backup website Wayback history](https://web.archive.org/web/*/https://ded-sec.online/*)
<!-- WEBSITES_ARCHIVE_STATUS_END -->

<!-- DEDSEC_MAIN_ARCHIVE_STATUS_START -->
### DedSec Project Main Repository

**Current synchronization status:** `not_started`  
**Last complete save:** Not completed yet.  
**Scheduled window:** Wednesday, Friday and Sunday, 08:00–13:00 Europe/Athens.  
**Resume mode:** File-level.

- [Internet Archive current mirror](https://archive.org/details/dedsec1121fk-dedsec-project-repository-snapshots)
- [Wayback history](https://web.archive.org/web/*/https://github.com/dedsec1121fk/DedSec*)
<!-- DEDSEC_MAIN_ARCHIVE_STATUS_END -->

<!-- DEDSEC_BACKUP_ARCHIVE_STATUS_START -->
### DedSec Project Backup Repository

**Current synchronization status:** `not_started`  
**Last complete save:** Not completed yet.  
**Scheduled window:** Wednesday, Friday and Sunday, 08:00–13:00 Europe/Athens.  
**Resume mode:** File-level.

- [Internet Archive current mirror](https://archive.org/details/dedsec1121fk-dedsec-project-backup-repository-snapshots)
- [Wayback history](https://web.archive.org/web/*/https://github.com/sal-scar/DedSec*)
<!-- DEDSEC_BACKUP_ARCHIVE_STATUS_END -->

<!-- GITHUB_PROFILE_ARCHIVE_STATUS_START -->
### DedSec GitHub Profile Repository

**Current synchronization status:** `not_started`  
**Last complete save:** Not completed yet.  
**Scheduled window:** Wednesday, Friday and Sunday, 19:30–23:30 Europe/Athens.  
**Resume mode:** File-level.

- [Internet Archive current mirror](https://archive.org/details/dedsec1121fk-github-profile-repository-snapshots)
- [Wayback history](https://web.archive.org/web/*/https://github.com/dedsec1121fk/dedsec1121fk*)
<!-- GITHUB_PROFILE_ARCHIVE_STATUS_END -->

<!-- CORRUPTED_FILES_ARCHIVE_STATUS_START -->
### Corrupted Files Project

**Current synchronization status:** `not_started`  
**Last complete save:** Not completed yet.  
**Scheduled window:** Wednesday, Friday and Sunday, 19:30–23:30 Europe/Athens.  
**Resume mode:** File-level.

- [Internet Archive current mirror](https://archive.org/details/dedsec1121fk-corrupted-files-project-repository-snapshots)
- [Wayback history](https://web.archive.org/web/*/https://github.com/dedsec1121fk/Corrupted-Files-Project*)
<!-- CORRUPTED_FILES_ARCHIVE_STATUS_END -->

<!-- POCKET_AI_ARCHIVE_STATUS_START -->
### Pocket AI

**Current synchronization status:** `not_started`  
**Last complete save:** Not completed yet.  
**Scheduled window:** Wednesday, Friday and Sunday, 19:30–23:30 Europe/Athens.  
**Resume mode:** File-level.

- [Internet Archive current mirror](https://archive.org/details/dedsec1121fk-pocket-ai-repository-snapshots)
- [Wayback history](https://web.archive.org/web/*/https://github.com/dedsec1121fk/Pocket-AI*)
<!-- POCKET_AI_ARCHIVE_STATUS_END -->

<!-- OFFLINE_SURVIVAL_ARCHIVE_STATUS_START -->
### Offline Survival Project

**Current synchronization status:** `not_started`  
**Last complete save:** Not completed yet.  
**Scheduled window:** Wednesday, Friday and Sunday, 19:30–23:30 Europe/Athens.  
**Resume mode:** File-level.

- [Internet Archive current mirror](https://archive.org/details/dedsec1121fk-offline-survival-project-repository-snapshots)
- [Wayback history](https://web.archive.org/web/*/https://github.com/dedsec1121fk/Offline-Survival-Project*)
<!-- OFFLINE_SURVIVAL_ARCHIVE_STATUS_END -->
