# Submission material and exact handoff points

Prepared 2026-10-19. **Not submitted; no public directory approval claimed.** Existing GitHub CLI authentication is sufficient for repository publication; it does not verify a developer identity or authenticate any other directory. No purchase or new paid plan is authorized.

## Shared listing fields

Canonical metadata: [listing.json](listing.json). Name: **Workspace Scout**, slug `workspace-scout`, version `1.0.0`, suggested category **Productivity**. Keywords: workspace, coworking, office, solo-founder, small-business, incubator, location-research. English is primary; the README and release notes have Chinese supplements. Runtime instructions are currently Chinese and can be interpreted by multilingual host agents; no claim of a fully translated English instruction set is made.

Description: Discover specific workspace plans for solo founders and small teams. Compare practical fit, admission requirements, full costs, conditional support and exit terms, with dated evidence and questions to ask next.

Publisher source: `Nick-Zheng-Q` / [repository](https://github.com/Nick-Zheng-Q/workspace-scout). The directory publisher name must match the platform's actual verified identity; do not claim a verified Dayweaver business identity without completing verification.

License: **PolyForm Shield 1.0.0**, existing required Dayweaver project notice. Source-available, not OSI open source. Preserve this disclosure even if a directory only has a generic “Other license” choice.

Product disclosure: A Dayweaver project. A completed report includes one optional, labeled Dayweaver invitation, omitted if declined; no account is required and no data is automatically sent there. This does not influence space ranking or promise automatic monitoring.

Public URLs after the approved push:
- Website/source: https://github.com/Nick-Zheng-Q/workspace-scout
- Support: https://github.com/Nick-Zheng-Q/workspace-scout/issues
- Data handling: https://github.com/Nick-Zheng-Q/workspace-scout/blob/main/PRIVACY.md
- Terms/license: https://github.com/Nick-Zheng-Q/workspace-scout/blob/main/LICENSE
- Demo: https://github.com/Nick-Zheng-Q/workspace-scout/blob/main/release/v1.0.0/demos/README.md

## OpenAI / ChatGPT + Codex public Plugins Directory

Package: `dist/workspace-scout-openai-v1.0.0.zip`, root portable `plugin.json`, square SVG branding and `skills/workspace-scout/`. **Choose Skills only.** There is no remote MCP, custom UI, app registration, hook or mandatory local execution requirement. Authorized host search/browser tools are needed for new discovery. Python is optional: without a local executor, the workflow still works, with manual arithmetic and explicit limits. Do not add an MCP merely to submit.

Local checks cover portable manifest schema, documented field lengths, square assets, safe ZIP paths and resource completeness; **only the portal can validate its scans/review**. No `interface.screenshots` are included: the separate media cards are not MCP UI screenshots.

Exact entry: [OpenAI Plugins portal](https://platform.openai.com/plugins). [Official submission procedure](https://developers.openai.com/plugins/deploy/submission). The owner must select the organization/project, complete individual or business verification and have owner or Apps Management Write permissions. No connected supported upload/submission tool is available in this session. Do not ask for passwords, identity documents or secrets in chat.

After identity/access is ready: Upload new/existing plugin → Skills only → upload ZIP → select actual verified identity → review metadata and skill scan findings → submit when required scans pass. User-only attestations must be completed by the user. Save submission identifier/status; report **submitted**, not listed, until a publicly accessible directory page exists. If scan fixes materially alter the approved scope or require a license change, stop for direction; do not silently relicense.

## Claude Plugin repository and Directory

Repository source: `.claude-plugin/marketplace.json` → `plugins/workspace-scout/`. The plugin has `.claude-plugin/plugin.json` and `skills/workspace-scout/`; no symlinks, hooks or servers. Both plugin and marketplace pass Claude Code strict validation and isolated local installation.

After the approved push:

```sh
claude plugin marketplace add Nick-Zheng-Q/workspace-scout
claude plugin install workspace-scout@workspace-scout-marketplace
```

Directory package: `dist/workspace-scout-claude-v1.0.0.zip`. Suggested category/keywords use shared metadata; follow the portal's actual allowed values. Entry: [Claude directory developer portal](https://claude.ai/directory/manage), [official publication guide](https://code.claude.com/docs/en/plugins/publish). A paid claude.ai plan is required for directory submission under current documentation; this task will **not buy one**. Claude CLI sign-in does not prove portal plan, identity or publishing permissions. There is no connected supported directory-submission interface here. The creator must log in, confirm rights/policies and provide the GitHub/package fields the portal asks for. Record actual submission status; local marketplace availability is not a directory listing.

## Skills.sh

Documented/tested command (CLI 1.7.2):

```sh
npx skills add Nick-Zheng-Q/workspace-scout --skill workspace-scout
```

For deterministic local verification, use `npx skills@1.7.2` and `--agent codex claude-code --copy -y --json`. Telemetry was disabled during preparation. The public pre-release `main` installation was checked separately from the unpublished v1.0.0 package. See [verification.json](verification.json) for failures and retries. [CLI docs](https://skills.sh/docs/cli), [FAQ](https://skills.sh/docs/faq).

Skills.sh derives discovery/ranking from installation telemetry; there is no guaranteed manual acceptance or rank. After approval, perform one genuine public-version installation check (not an install campaign), disclose that it is our own verification, and inspect the public detail page. Do not fabricate install counts, call preparatory tests organic adoption, or claim listing from an HTTP 200/error-shell page alone. If indexing has not happened, report pending/unconfirmed and retain materials.

## Social and Awesome lists

[Channel rules and eligibility](marketing/channels.md), [X draft](marketing/x.md), [Reddit draft](marketing/reddit.md), [Show HN human-only facts](marketing/show-hn-brief.md), [list submission facts](marketing/awesome-submission.md), [professional outreach research](marketing/outreach.md).

No authenticated supported X/Reddit posting interface is currently available. Do not script their websites. Show HN prohibits generated text/automated posting, and some list maintainers prohibit agent submissions. Current checked PR targets do not meet eligibility or licensing requirements; do not spam them. These are rule/access limitations, not completed submissions.
