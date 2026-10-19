# v1.0.0 release audit — 2026-10-19

**Stage: A/B and marketing preparation complete; awaiting consolidated approval. No new push, public Release, directory submission, PR, social post or outreach has been executed.** This repository was already public. This document is a preparation snapshot, not the final publication report.

## Scope and decision

Ready for a **versioned GitHub/repository distribution release**, with explicit limits below. Not yet a ChatGPT, Claude or Skills.sh public-directory listing. Core discovery, evidence, fit/admission, policy-benefit and cost-comparison methods are retained; no new workspace database, MCP service, API dependency or automatic contact flow was added.

### Release fixes only

1. Refuse an installation/update destination that could replace the source checkout or recursively copy its references; ignore project update backups.
2. Reject non-object JSON, malformed field types, extreme integers and overflowing cost totals with controlled errors. Valid-input calculations and hard-condition decision logic are unchanged.
3. Build minimal allowlisted distribution packages and synchronized repository plugin copies, with deterministic ordering/timestamps, safe paths, licenses and checksums. Fit manifest field limits and add square original branding assets.
4. Document platform requirements, data handling, existing promotional note and evidence limits rather than claiming directory approval or stable performance gains.

The optional Dayweaver note was already requested before this release audit and is included in the reviewed changes. It is one labeled, opt-out invitation in a full report, not a ranking factor, signup requirement or automatic transfer/monitoring feature.

## A. Content, dependency, license and data review

- `SKILL.md`: scoped to solo/small-team workspaces, concrete space+plan, local source discovery, policy/eligibility evidence, unknown/conflicting conditions and actionable follow-up. No restaurant/industrial/lab compliance guarantee, invented subsidy, contact or application authority.
- Runtime helper, installer, updater and release builder use the shell/Python standard library. No pip/npm packages are runtime requirements. Python 3 is needed only for optional arithmetic or build/tests. Search/browser/document tools come from the authorized host.
- Optional installation clients have their own requirements: Skills CLI needs Node/npm, Codex/Claude plugin commands need those clients. They are not bundled dependencies. Local checks used Python 3.14, Skills CLI 1.7.2, Codex 0.159.2 and Claude Code 2.1.198 on macOS arm64.
- Existing **PolyForm Shield 1.0.0** and required Dayweaver notice are retained. Official plain text was fetched and compared: substantive/markdown-normalized text matches; whitespace differs. Every runtime/plugin/media ZIP carries LICENSE. Source-available, not OSI open source; not a blanket noncommercial license. GitHub currently detects license as “Other”. This is a packaging/content check, not a legal opinion.
- [Privacy](../../PRIVACY.md) and [third-party use](../../THIRD_PARTY.md): no bundled analytics/backend/credentials. No provider photo, raw external HTML/PDF corpus or workspace database ships. Original simulated fixtures are labeled; previous real-source evaluations are dated archives, not current offers. Third-party facts are short, linked paraphrases without endorsement or relicensing claims.
- Original artwork is separate marketing material, not fabricated app UI or a customer testimonial. Three [workspace demos](demos/README.md) have hypothetical briefs, real published sources, unresolved conditions and reproducible arithmetic; they are not a new effectiveness trial.

## B. Private data and repository hygiene

Gitleaks **8.30.1** was downloaded temporarily from its official GitHub release and checked against its published SHA-256 checksum. Full reachable Git history (3 existing commits) and the allowlisted current public export were scanned with redaction. **Exit 0, no secret findings.** Temporary tool binaries, raw research, full local logs, isolated configs and npm caches remain under ignored `.release-private/`; `dist/` is ignored and uploaded only as approved Release assets.

Filename/content probes found no local user-home absolute paths, credential files or cache artifacts in the public export. No public symlinks were found. Original evaluation logs already redact local paths; machine-private logs were not added. This is a bounded review and automated scan, not a guarantee that no sensitive data can ever exist. The staged/final file inventory must be checked again immediately before the approved push.

## C. Actual validation results

[verification.json](verification.json) records normalized commands, exit codes, scope and relevant failures. Full local logs remain private; no test result is invented.

| Check | Actual result |
|---|---|
| Python unit/regression/package/demo tests | **15 tests, exit 0** |
| Shell install/update tests | **Exit 0**, overwrite, unrelated target, symlink, self-update and recursive-copy protections |
| Skill Creator format validator | **Exit 0**, Skill valid (host validation utility; not a runtime dependency) |
| Clean exported tree, isolated HOME/config, unrelated current directory | Install/update/helper **exit 0**; no local absolute paths required |
| Claude plugin + repository catalog strict validation | Both **exit 0**; initial missing catalog-description warning was fixed |
| Isolated Claude local marketplace install/list/details | **Exit 0**, v1.0.0, one Skill, zero hooks/MCP/agents/LSP |
| Isolated Codex local marketplace install/list | **Exit 0**, v1.0.0 enabled |
| Skills CLI local discovery/install | **Exit 0**, finds one Skill, copied installation for Codex/Claude Code; installed runtime bytes checked |
| Portable plugin JSON Schema / field lengths / asset paths | **Exit 0**, local structural checks; not a portal upload or review |
| Deterministic packages and safe allowlists | Repeated builds have matching bytes/checksums in the same tested environment; helper, references and LICENSE present |
| Public pre-release `main` via Skills CLI | First two tries **exit 1** (HTTP/2/connection failures); third **exit 0**, real install with telemetry disabled. This checks existing `d672d04`, **not unpublished v1.0.0** |
| Skills.sh detail-page check | Request **exit 0 / HTTP 200**, but body says **404 / skill unavailable**. **Not listed** at this check; success status alone is not evidence |
| Git diff whitespace | **Exit 0** |

“Clean” means an allowlisted temporary export and empty temporary HOME/host configs on the existing macOS installation, with minimal environment for local commands. It does not mean a new operating-system VM. Linux/Windows and ChatGPT web runtime have not been tested. No new model-vs-model efficacy experiment was performed in this release phase; the existing mixed single Montréal pair remains the evidence limit.

## D. Packages and public files

Source of truth remains root `SKILL.md`, `references/` and the helper. `plugins/workspace-scout/` is generated from those sources. Catalogs: `.agents/plugins/marketplace.json` and `.claude-plugin/marketplace.json`.

Release attachments prepared in ignored `dist/`:

- `workspace-scout-skill-v1.0.0.zip`: minimal runtime Skill + license.
- `workspace-scout-openai-v1.0.0.zip`: portable Skills-only Plugin; logo/composer icon; no MCP, hooks, external services or UI screenshots.
- `workspace-scout-claude-v1.0.0.zip`: Claude manifest + Skill resources + branding/license.
- `workspace-scout-media-v1.0.0.zip`: original launch/research cards + license.
- `SHA256SUMS`: checksums; [manifest.json](manifest.json) preserves the approved package/runtime hashes.

Public source changes also include the installer/helper fixes and regression tests, VERSION, privacy/third-party notices, English-primary bilingual README, release notes/listing metadata, submission instructions, three demo briefs/reports/snapshots, community rules, outreach research and drafts. Existing source/history remains public. **No private research/cache/config/tool directories or raw provider pages are to be committed or attached.**

## E. Platform status and human steps

| Platform / channel | Status before approval | What remains |
|---|---|---|
| GitHub repository/Release | Existing [public repo](https://github.com/Nick-Zheng-Q/workspace-scout); CLI authenticated with ADMIN; v1.0.0 not created | Approved commit/push/tag, create Release/assets and verify public downloads |
| Skills CLI | Local candidate and existing public main install verified | Verify new public version after push; one genuine install, not an install campaign |
| Skills.sh detail page | [Checked route](https://skills.sh/nick-zheng-q/workspace-scout/workspace-scout) currently unavailable | Check indexing; do not guarantee ranking or claim our test as organic adoption |
| Codex/Claude repository plugins | Local installation verified, new catalogs not public yet | Push and verify remote installs; this is not central-directory approval |
| OpenAI public Plugins Directory | Skills-only ZIP ready, local checks only | [Portal](https://platform.openai.com/plugins): actual developer identity verification, org/project permissions and user attestations; no connected supported submission interface here |
| Claude Directory | Packet ready; CLI logged in, portal plan/permission not established | [Portal](https://claude.ai/directory/manage): existing paid plan under current docs, login and rights/policy confirmation; **no plan purchase** |
| Awesome Lists | Rules checked; no eligible agent-PR target among checked lists | Preserve packet; stars/adoption, license compatibility or human-only requirements prevent appropriate submission now |
| X / Reddit | Drafts only; no authenticated posting interface; Reddit rules not fully readable | Check actual account/rules; no scripted website posting or unsolicited mass outreach |
| Show HN | Human-only facts prepared | Current rules prohibit generated text and automated posting. Creator must independently author/post, not paste an AI draft |

Official requirements and exact portal actions are in [SUBMISSION.md](SUBMISSION.md); community rule sources are in [marketing/channels.md](marketing/channels.md). No payment is needed for the prepared GitHub/repository publication. A host model, web tool or third-party plan may have its own costs; this task buys none.

## Consolidated approval boundary

See [the execution plan](publish-plan.md). One approval authorizes the reviewed GitHub source/attachments, v1.0.0 tag/Release, legitimate public-install verification and accurate final status commit. Submit elsewhere only through available supported authenticated interfaces **and** current rules; otherwise retain ready materials and report the exact human action. It does not authorize paying, bypassing access controls, changing license, manufacturing traction, prohibited AI posts or bulk outreach. A material scope change or unanticipated legal attestation must not be silently accepted.
