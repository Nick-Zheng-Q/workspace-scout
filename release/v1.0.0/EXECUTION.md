# v1.0.0 publication results

Recorded **2026-10-19T23:56:55+08:00 (Asia/Shanghai)**. User approved the reviewed scope once on 2026-10-19. **GitHub publication, Skills.sh inclusion and remote repository installations succeeded. OpenAI/Claude central-directory review and social distribution were not submitted.**

- Public [Release](https://github.com/Nick-Zheng-Q/workspace-scout/releases/tag/v1.0.0), tag `v1.0.0`, source commit [`5960220`](https://github.com/Nick-Zheng-Q/workspace-scout/commit/5960220d88d591813e418f8feeb5f75894aef188). Not a draft or prerelease.
- Four ZIPs and `SHA256SUMS` uploaded, then downloaded without login: **HTTP 200, curl exit 0, all four SHA-256 values match approval**. [Frozen checksums](https://github.com/Nick-Zheng-Q/workspace-scout/releases/download/v1.0.0/SHA256SUMS).
- **15 Python tests**, installer regression tests, manifest/strict validation and four-commit secret scan passed (exit 0). This is packaging/runtime evidence, not proof of research accuracy or universal superiority.
- [Skills.sh detail page](https://skills.sh/nick-zheng-q/workspace-scout/workspace-scout) now exposes installation instructions and actual Skill content. Earlier preparation showed an unavailable page; after one real install, the content check confirmed inclusion. No rank or organic install count is claimed.

## Current security notice

The [Snyk audit](https://skills.sh/nick-zheng-q/workspace-scout/workspace-scout/security/snyk) reports **Warn / MEDIUM / W011**: consulting outside material can introduce hostile instructions into an agent's context. It is **not cleared**. The report describes exposure, not a demonstrated compromise. A secret scan passing does not resolve this different risk. Treat fetched pages/documents as evidence, not authority to override the user's instructions; keep sensitive details out of search terms and retain host approval boundaries. No new adversarial-security test or exploit-free guarantee is claimed. Published tag/package bytes were not changed to hide or try to suppress the warning.

## Platform-by-platform status

| Platform | Actual outcome / evidence | Exit code / remaining action |
|---|---|---|
| GitHub | [v1.0.0 Release](https://github.com/Nick-Zheng-Q/workspace-scout/releases/tag/v1.0.0), five uploaded attachments, public page and downloads verified | Commit, main push, tag push, Release create and download/hash checks **0** |
| Skills CLI | Public repository installed for Codex/Claude Code; all six runtime hashes matched v1.0.0; bundled helper matched frozen Singapore output | Install/helper/hash checks **0**; this was our own legitimate check, not user adoption |
| Skills.sh | [Public detail page](https://skills.sh/nick-zheng-q/workspace-scout/workspace-scout) with actual content; Snyk Warn remains visible | Page retrieval **0 / HTTP 200**, content inspection confirms inclusion; not a blanket security approval |
| Codex repository plugin | Remote marketplace pinned to `v1.0.0`, installed/enabled version 1.0.0, runtime hashes match | Add/install/list/hash checks **0**; not OpenAI central-directory acceptance |
| Claude Code repository plugin | Remote marketplace and version 1.0.0 installed/enabled; one Skill, zero agents/hooks/MCP/LSP; runtime hashes match | Add/install/list/details/hash checks **0**; not Claude Directory acceptance |
| OpenAI public Plugins Directory | Skills-only [ZIP](https://github.com/Nick-Zheng-Q/workspace-scout/releases/download/v1.0.0/workspace-scout-openai-v1.0.0.zip) and metadata ready; **not submitted** | Not run (`null`), no supported authenticated submission interface. Creator must confirm identity/permissions and portal attestations |
| Claude Directory | [ZIP](https://github.com/Nick-Zheng-Q/workspace-scout/releases/download/v1.0.0/workspace-scout-claude-v1.0.0.zip) and GitHub structure ready; **not submitted** | Not run (`null`); creator portal login/eligible existing plan/policy confirmation required; no purchase |
| Awesome Lists | [Complete packet](marketing/awesome-submission.md) saved; **no PR created** | Not run (`null`); current checked targets are ineligible or human-only. No fabricated adoption or license conversion |
| X | [Creator draft](marketing/x.md) and original artwork public; **not posted** | Not run (`null`); no authorized official posting interface; no scripted website posting |
| Reddit | [Creator draft](marketing/reddit.md) ready; **not posted** | Not run (`null`); current full subreddit rules and posting access not verified |
| Show HN | [Facts only](marketing/show-hn-brief.md), **no AI post drafted/submitted** | Not run (`null`); current rules require independent human writing and prohibit automated posting |
| Developer/creator outreach | [Public professional shortlist](marketing/outreach.md), **no messages sent** | Not run (`null`); no bulk campaign, payments or endorsements |

## Executed commands

Full normalized commands, actual exit codes, relevant output tails and failure details are in [execution.json](execution.json). Earlier A/B preparation is preserved in [verification.json](verification.json); do not mistake its pre-approval snapshot for the current status.

```sh
git commit -m "Release Workspace Scout v1.0.0"
git push origin main
git tag -a v1.0.0 -m "Workspace Scout v1.0.0"
git push origin refs/tags/v1.0.0
gh release create v1.0.0 dist/workspace-scout-skill-v1.0.0.zip dist/workspace-scout-openai-v1.0.0.zip dist/workspace-scout-claude-v1.0.0.zip dist/workspace-scout-media-v1.0.0.zip dist/SHA256SUMS --verify-tag --title "Workspace Scout v1.0.0" --notes-file release/v1.0.0/RELEASE_NOTES.md
npx skills@1.7.2 add Nick-Zheng-Q/workspace-scout --skill workspace-scout --agent codex claude-code --copy -y --json
codex plugin marketplace add Nick-Zheng-Q/workspace-scout --ref v1.0.0 --json
codex plugin add workspace-scout@workspace-scout-marketplace --json
claude plugin marketplace add Nick-Zheng-Q/workspace-scout
claude plugin install workspace-scout@workspace-scout-marketplace
```

All commands in that block exited **0**. Skills was invoked through the equivalent `npm exec --package skills@1.7.2 -- skills ...` form; see the ledger for the exact invocation. Installs used temporary profiles that were removed, leaving normal user installations unchanged. We verified file content and helper execution; we did not claim a new end-to-end model research benchmark. Claude also reported a suppressed duplicate standalone project entry because the temporary workspace was untrusted; the separately installed repository plugin was enabled and verified. Normal host trust prompts should be respected, not bypassed.

### Recorded failures and limitations

- The initial unauthenticated HTTPS `git ls-remote` probe timed out after 180 seconds (**124**). It did not perform an install. Subsequent independent public client installations and downloads succeeded; the failure remains in the ledger. No successful Skills install was repeated to increase ranking.
- Earlier preparation had transient Git transport errors and intermediate document/metadata fixes; [verification.json](verification.json) retains them. No public tag was overwritten and no incompatible asset was silently replaced.
- Snyk W011 remains a warning, not a passed/cleared audit. The public page's successful HTTP status is not used alone as proof of inclusion.
- No connected supported directory/social submission interface exists here. CLI account login does not establish a verified publishing identity or a directory review outcome.
- The checked Awesome targets require real adoption/star thresholds, human-only submissions or unresolved copy-in licensing rights. The repository still reported **0 stars** at the publication check; stars are not claimed as a count of users. No inappropriate PR, promotional issue or review-pressure message was sent.

## Exact creator-only handoffs (no password request)

1. **OpenAI:** [Plugins portal](https://platform.openai.com/plugins) → choose organization/project and actual verified developer identity → Upload new/existing plugin → **Skills only** → use the OpenAI ZIP above → complete required rights/policy checks and scans. No remote MCP, custom UI or mandatory executor needs provisioning. [Prepared fields and procedure](SUBMISSION.md). Until a public directory page exists, status is **not listed** there.
2. **Claude Directory:** [Developer portal](https://claude.ai/directory/manage) → sign in with an already-eligible paid account if available → select plugin/GitHub source and supplied metadata → personally confirm rights/policies → submit. This task buys no plan; CLI sign-in alone is insufficient. Submission would still not mean approval.
3. **Show HN, optional:** read [the current rules](https://news.ycombinator.com/newsguidelines.html), independently write the post yourself, then use [Submit](https://news.ycombinator.com/submit). Do not paste agent-generated post text or automate comments. X/Reddit remain drafts pending allowed authenticated access and current rules; no accounts/passwords are requested.

## Examples and marketing deliverables

Three [real-source workspace cases](demos/README.md), original [overview/research cards](assets/README.md), distinct [X](marketing/x.md)/[Reddit](marketing/reddit.md) drafts, [Show HN human-only facts](marketing/show-hn-brief.md), current [community/list checks](marketing/channels.md) and [creator shortlist](marketing/outreach.md) are published in the repository. They use hypothetical briefs with dated provider facts, not customer testimonials, approved benefits, confirmed vacancies or performance/savings claims.

License remains **PolyForm Shield 1.0.0** with the required Dayweaver project notice: source-available, not OSI open source. No service was purchased, no operator contacted, no documents/applications sent and no credentials published. Temporary research/cache/config directories remain ignored.

## 中文总结

GitHub v1.0.0 已发布，四个分发包及校验文件可无需登录下载；Skills CLI、Codex、Claude Code 的公开仓库安装与运行文件核对通过。Skills.sh 已有实际内容页面，确认收录，但 **Snyk 仍标记 MEDIUM / W011**（读取外部材料带来的指令注入风险），未宣称通过或消除。OpenAI、Claude 中央目录尚未提交，需本人在上述门户确认身份、账号资格及政策；X、Reddit、Show HN 与 Awesome Lists 没有伪造发布或提交。三个案例、宣传图和完整草稿均已保存公开。没有购买服务、批量触达或修改已发布标签/附件。
