# Execution plan — approved

**User approval received 2026-10-19.** This is the original plan; see [executed results](EXECUTION.md). Historical “not yet executed” labels below describe the preparation stage, not current status.

**Do not execute publishing steps before one explicit consolidated approval.** No remote push, Release, PR, directory submission or social post was made during preparation. The repository was already public before this request.

## 1. Final local checks, commit and GitHub release

Re-run the checks, rebuild packages and ensure their hashes match the approved manifest. Reject unexpected extra changes or an existing v1.0.0 tag/Release; never force-push or overwrite a public tag. If only a recorded transient network error recurs, retry in a bounded way; stop/report on permission or policy failure.

Planned commands, **not yet executed** (run from the repository root):

```sh
python3 scripts/build_release.py
python3 -m unittest discover -s tests -p 'test_*.py'
sh tests/test_install.sh
git diff --check
# Stage only reviewed source, generated plugin, release docs and media paths:
git add .gitignore README.md SKILL.md references/candidate-record.md install.sh scripts/check_candidates.py tests/test_check_candidates.py tests/test_install.sh VERSION PRIVACY.md THIRD_PARTY.md scripts/build_release.py tests/test_release.py .claude-plugin/marketplace.json .agents/plugins/marketplace.json plugins/workspace-scout release/v1.0.0
git commit -m "Release Workspace Scout v1.0.0"
git push origin main
git tag -a v1.0.0 -m "Workspace Scout v1.0.0"
git push origin refs/tags/v1.0.0
gh release create v1.0.0 dist/workspace-scout-skill-v1.0.0.zip dist/workspace-scout-openai-v1.0.0.zip dist/workspace-scout-claude-v1.0.0.zip dist/workspace-scout-media-v1.0.0.zip dist/SHA256SUMS --verify-tag --title "Workspace Scout v1.0.0" --notes-file release/v1.0.0/RELEASE_NOTES.md
gh release view v1.0.0 --json url,isDraft,isPrerelease,tagName,assets
```

Publication destination: [existing repository](https://github.com/Nick-Zheng-Q/workspace-scout). Expected Release route: `https://github.com/Nick-Zheng-Q/workspace-scout/releases/tag/v1.0.0` (**not created yet**). Verify public page and downloadable asset hashes before marking released. `dist/` is not committed: only the four approved ZIPs and checksum file become Release attachments. Private research/cache/auth directories never ship.

## 2. Public installation verification

Use isolated temporary homes/config directories and remove them afterwards; do not change the user's normal installed skills/plugins. Verify public Git commit/tag, Skills CLI install of one named Skill, Codex repository marketplace pinned to v1.0.0, Claude repository marketplace and component inventory. Compare installed runtime files with the published source.

```sh
npx skills@1.7.2 add Nick-Zheng-Q/workspace-scout --skill workspace-scout --agent codex claude-code --copy -y --json
codex plugin marketplace add Nick-Zheng-Q/workspace-scout --ref v1.0.0 --json
codex plugin add workspace-scout@workspace-scout-marketplace --json
claude plugin marketplace add Nick-Zheng-Q/workspace-scout
claude plugin install workspace-scout@workspace-scout-marketplace
```

The Skills command is **one genuine installation check**, not organic user adoption; default telemetry may contribute to indexing and must be disclosed as our own check. Do not repeat installs to inflate ranking. Inspect the public detail page independently; a working Git install, HTTP 200, prepared listing or submitted scan does not establish directory inclusion. If transport errors prevent verification, keep the actual failure/exit code and state unverified.

## 3. Directory submission and initial distribution

- The OpenAI and Claude directory packets and instructions are prepared in [SUBMISSION.md](SUBMISSION.md). Use only supported, already-authorized publishing interfaces. No such connected interface is present now; creator identity/plan/policy confirmations remain human steps at the exact linked portals. Do not request passwords or buy a plan. Keep materials ready if submission is unavailable.
- No checked Awesome List is currently eligible for an agent-submitted recommendation PR. Do not open inappropriate PRs/issues, bypass star/adoption thresholds or violate human-only rules. Save [the factual packet](marketing/awesome-submission.md); no PR acceptance is claimed.
- X and Reddit: retain drafts until both authenticated supported posting access and current rules are verified. No browser-script posting, unsolicited mass outreach or invented endorsements.
- Show HN: human-authored only. Do not post generated text or agent-written comments; approval cannot override the site's rules.
- Outreach: the researched professional shortlist is informational; do not mass-message or pay anyone.

## 4. Final report

Record each actual URL, normalized command, exit code, local versus public-version check, failure/retry, directory submission identifier and remaining human step. Add a dated execution result **after** the release commit; commit/push that status record without moving the immutable v1.0.0 tag. Report submitted versus accepted separately. Do not say every platform launched if only the GitHub package is public.
