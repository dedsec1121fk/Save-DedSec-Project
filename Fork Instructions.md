# Fork Instructions

This repository can be forked and used as an independent archive controller for the DedSec Project ecosystem. Each fork must use its own Internet Archive credentials and archive item identifiers. Software Heritage Save Code Now requests for public Git repositories do not require the Internet Archive credentials.

## 1. Fork The Repository

Fork this repository into your GitHub account. Open the fork itself before configuring anything; secrets added to the original repository are not inherited by forks.

Then open the **Actions** tab in your fork and enable workflows when GitHub asks you to do so.

## 2. Create Internet Archive Credentials

1. Create or sign in to an Internet Archive account.
2. Open the Internet Archive S3-like API keys page:
   https://archive.org/account/s3.php
3. Copy the **Access Key** and **Secret Key**.

Keep both values private. Do not paste them into the workflow, README, issues, commits, or Actions logs.

## 3. Add The Keys As GitHub Actions Secrets

Inside your fork, open:

**Settings → Secrets and variables → Actions → Secrets → New repository secret**

Create these two repository secrets using the exact names below:

| Secret name | Value |
|---|---|
| `Internet_Archive_1` | Your Internet Archive **Access Key** |
| `Internet_Archive_2` | Your Internet Archive **Secret Key** |

The workflow already reads them here:

```yaml
IA_ACCESS_KEY: ${{ secrets.Internet_Archive_1 }}
IA_SECRET_KEY: ${{ secrets.Internet_Archive_2 }}
```

GitHub secret names are case-insensitive, but using the exact names above avoids configuration mistakes. Secret values cannot be viewed again after they are saved.

## 4. Give The Workflow Permission To Update The Fork

Open:

**Settings → Actions → General → Workflow permissions**

Select **Read and write permissions**, then save the setting. The workflow needs this permission to update `update.json`, refresh the generated archive links and status sections in `README.md`, and push the checkpoint commit back to the fork.

The workflow also declares:

```yaml
permissions:
  contents: write
```

Both the repository setting and the workflow permission must allow the write operation.

## 5. Replace The Internet Archive Item Identifiers

The identifiers currently in `.github/workflows/internet-archive.yml` belong to the original archive setup. A different Internet Archive account normally cannot update items owned by another account.

Open `.github/workflows/internet-archive.yml`, find every `ia_item` entry, and replace its value with a unique identifier owned by your Internet Archive account. A practical format is to prefix every identifier with your Internet Archive or GitHub username.

Example:

```python
"ia_item": "yourname-dedsec-project-repository-snapshots",
```

Change all twelve repository/website target identifiers:

- DedSec websites and website source
- DedSec website mirror repository
- DedSec Project main repository
- DedSec Project backup repository
- GitHub profile repository
- Corrupted Files Project
- Pocket AI
- Praying Project
- Offline Survival Project
- Hacking Guide Project
- Language Project
- Save DedSec Project

After any `ia_item` value changes, the **Permanent Internet Archive Links** section in `README.md` is regenerated automatically on the next workflow run. You do not need to edit those README links manually.

The APK collection uses a separate identifier in the `sync-apks` job:

```yaml
APK_IA_ITEM_IDENTIFIER: dedsec1121fk-dedsec-project-apk-backups
```

Replace that value with another unique Internet Archive identifier owned by your account as well.

## 6. Optional: Change What The Fork Archives

By default, the controller continues archiving the original DedSec Project repositories and websites. To archive your own repository copies instead, change the corresponding `repository` and `sites` values in the target definitions inside `.github/workflows/internet-archive.yml`.

Do not change the marker values unless you also intentionally replace the matching generated status blocks in `README.md`.

Software Heritage targets are derived from each configured `repository` value. A Save Code Now request made in the current workflow run is not turned into a README link immediately. A later workflow run checks whether Software Heritage has finished ingesting the repository and only then publishes the confirmed origin/snapshot links in `README.md`.

## 7. Run The First Archive

1. Open the **Actions** tab.
2. Select **Incrementally Archive Entire DedSec Ecosystem**.
3. Choose **Run workflow**.
4. Select `all` for the archive group.
5. Start the run and inspect each job.

A successful run should:

- Upload or synchronize the configured Internet Archive repository/website items and the APK collection.
- Resolve Software Heritage links only for requests already recorded by an earlier workflow run, then request Save Code Now for the selected current-run targets when appropriate.
- Store each target checkpoint as `archive-state/update.json`.
- Refresh the combined root `update.json`.
- Refresh the generated Internet Archive, Software Heritage, APK and status sections in `README.md`.
- Commit the updated state and README back to your fork.

## Scheduled Target Order

Scheduled runs are intentionally serial. January, March, May, July, September and November use the target order defined in the workflow; February, April, June, August, October and December use the reverse order. Manual runs keep the normal listed order.

## Troubleshooting

### `Missing Internet_Archive_1` Or `Missing Internet_Archive_2`

One or both repository secrets are absent, empty, or were added to a different repository. Add them to the fork that is actually running the workflow.

### Internet Archive Upload Is Rejected

Confirm that every `ia_item` uses a unique identifier your Internet Archive account can create or modify. Do not leave the original maintainer's identifiers unchanged unless your account has explicit write access to those items.

### Git Push Is Rejected

Confirm **Settings → Actions → General → Workflow permissions → Read and write permissions** is enabled in the fork. Also keep `update.json` at the repository root; do not move generated state into `.github/workflows/`, because updates in that protected directory require additional workflow-level authorization.

### Secrets Are Missing In A Pull Request Workflow

GitHub does not pass normal Actions secrets to workflows triggered from another fork's pull request. Run the scheduled or manual workflow directly inside your own fork instead.

## Security Rules

- Never commit Internet Archive keys to Git.
- Never place keys in repository variables; use encrypted Actions secrets.
- Never print either key in workflow output.
- Rotate both Internet Archive keys immediately if either value is exposed.
- Review workflow changes before running them, because a modified workflow can access configured repository secrets.
- Keep private Sponsors-Only repositories out of public archive target lists unless you intentionally want their contents published. The provided workflow archives only public repositories and APK dependencies.

## Working-Tree-Only Security Model

This controller intentionally archives only the files and directories present in each repository's current checked-out working tree. It does not upload `.git`, create Git bundles, archive commit pages, or queue repository history in Wayback. If a secret existed only in an older Git commit and is no longer present in the current working tree, this controller will not newly back up that old commit. Secrets still present in current files can still be archived and must be removed before a backup run.
