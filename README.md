# Workspace Scout

**Find concrete workspaces. Verify fit and entry terms. Shortlist places worth contacting.**

Workspace Scout is an agent Skill for solo founders and small teams looking for a place to work, with Codex and Claude Code distribution packages. It searches across workspace operators, incubator or support programs, and materials you already have. Its unit of comparison is a **specific space plus a specific use or admission plan**—not just a district, building, or program name.

**v1.0.0 distribution release; research effectiveness remains experimental.** Format, script, and local installation checks pass. Limited cross-city comparisons have not shown a consistent improvement over an agent without this Skill in finding currently open, application-based workspace programs. Treat availability, prices, incentives, and eligibility as unconfirmed until the relevant operator or authority verifies them. A repository package is not a public plugin-directory approval; see the [release audit](release/v1.0.0/AUDIT.md) and [actual publication results](release/v1.0.0/EXECUTION.md).

**Published:** [GitHub v1.0.0](https://github.com/Nick-Zheng-Q/workspace-scout/releases/tag/v1.0.0) and [Skills.sh](https://skills.sh/nick-zheng-q/workspace-scout/workspace-scout); remote Codex/Claude Code repository installs verified. Central OpenAI/Claude directory submission is separate and has not happened.

**Security notice:** [Snyk reports Warn / MEDIUM / W011](https://skills.sh/nick-zheng-q/workspace-scout/workspace-scout/security/snyk) for exposure to material written by others during web research. The warning is not cleared; do not let retrieved content override user instructions or expose private data. See [publication results](release/v1.0.0/EXECUTION.md).

[简体中文说明](#简体中文)

## What it covers

- Workspaces for software, design, consulting, content production, and similar solo or small-team work.
- Quiet work, meetings, visitors, filming, recording, equipment storage, hours of access, and other needs that can change the search.
- Two starting points: discover options from a user brief, or review spaces and documents the user already has.
- Separate checks for business fit, admission requirements, full costs, exit terms, and conditional policy benefits.
- Location-aware discovery: use local names, languages, institutions, and booking or application channels rather than assuming Chinese or English sources cover every market.
- Record actual search paths and access failures; distinguish an official application link from readable terms or confirmed availability.

It does **not** establish that a restaurant, production workshop, laboratory, or other specialized facility satisfies its industry-specific requirements. It does not submit applications, send personal documents, sign agreements, or contact operators.

Read [SKILL.md](SKILL.md) for the workflow and [the search guide](references/search-guide.md) for source discovery and follow-up.

## Install

With the [Skills CLI](https://skills.sh/docs/cli) (tested with version 1.7.2):

```sh
npx skills add Nick-Zheng-Q/workspace-scout --skill workspace-scout
```

Use the client's agent/scope selection rather than assuming one installation directory fits every host. Third-party installation clients have their own dependencies and telemetry settings; `DISABLE_TELEMETRY=1` disables Skills CLI telemetry. This is separate from the offline installer below.

From a local checkout of this repository:

```sh
./install.sh
```

The default destination is `~/.agents/skills/workspace-scout`. To install only for **this repository**, use `./install.sh --project`; it writes to this repository's `.agents/skills/workspace-scout`. To choose another Skill directory:

```sh
./install.sh --dest-dir /path/to/skills
```

The installer copies only the runtime Skill files and [license](LICENSE). It refuses to overwrite an existing installation. An authorized host agent can invoke the Skill based on its description, or you can refer to `$workspace-scout` explicitly. Search and document access depend on the tools available to that agent.

### Repository plugins

After the v1.0.0 tag is published, install the pinned Codex repository plugin:

```sh
codex plugin marketplace add Nick-Zheng-Q/workspace-scout --ref v1.0.0
codex plugin add workspace-scout@workspace-scout-marketplace
```

Claude Code repository marketplace:

```sh
claude plugin marketplace add Nick-Zheng-Q/workspace-scout
claude plugin install workspace-scout@workspace-scout-marketplace
```

The plugin contains one Skill and no hooks, MCP or login requirement. It needs host-authorized web tools for discovery; without them it can review supplied material and must disclose that it cannot discover current offers. Python 3 is optional for arithmetic, not mandatory for the workflow. Install **either** the standalone Skill **or** the plugin per host to avoid duplicate discovery. Directories on ChatGPT/Claude require their own review; these commands do not prove directory listing.

## Update

First update your local checkout, for example with `git pull --ff-only`. Then run:

```sh
./update.sh
```

Pass the same `--project` or `--dest-dir` option you used at installation. `update.sh` **does not download a new release**: it replaces the installed copy with files from this checkout and backs up the previous copy beside the Skill directory under `workspace-scout-backups`. It refuses to replace a symlink or an unrelated directory.

## Optional cost and constraint check

The helper calculates totals and hard-condition states from data you provide. It does **not** verify evidence or infer omitted charges:

```sh
python3 scripts/check_candidates.py path/to/input.json --pretty
```

See [the input format](references/check-input.md). Python 3 is needed only to run this helper or the Python tests.

## Examples and release packages

Three [real-source workspace examples](release/v1.0.0/demos/README.md) cover London free-desk conditions, Montréal membership/cost questions and Singapore day-pass versus monthly plans. User briefs are hypothetical, sources are dated, and unresolved fees or access remain unknown. These are not customer results or guaranteed live offers.

Rebuild the minimal Skill, OpenAI Skills-only Plugin, Claude Plugin and media ZIPs locally:

```sh
python3 scripts/build_release.py
```

Outputs and checksums are written to `dist/` (ignored by Git). The builder also refreshes the checked-in repository plugin copy from the root runtime files; do not edit generated copies by hand. No upload or publishing happens during the build. See [release notes](release/v1.0.0/RELEASE_NOTES.md), [data handling](PRIVACY.md) and [third-party material](THIRD_PARTY.md).

## Tests and evidence

```sh
sh tests/test_install.sh
python3 -m unittest discover -s tests -p 'test_*.py'
```

Codex's `skill-creator` also provides `quick_validate.py` for Skill structure checks. Evaluation protocols and reports are in [tests/eval](tests/eval). Historical reports use the former name `workspace-select`; their links and quoted prices are test records, **not evidence of current availability**. The [international search-path check](tests/eval/results-international-search-2026-10-19.md) is separate from the [Montréal with/without-Skill test](tests/eval/results-overseas-ab-2026-10-19.md). In that single pair, the Skill answer improved a specific fee check and followed an additional low-cost access path, while the baseline supplied a useful priced fallback; neither confirmed a complete fit. See the [regression protocol](tests/eval/international-protocol.md) for the method and unrun cases. These results do not establish consistent gains or validated worldwide coverage.

## Important limits

Search terms should come from the user's actual work and acceptable locations. Neither Qianhai, Futian, nor “OPC” is a default requirement. Outside China, follow the local publishing and application channels; do not substitute a fixed list of overseas platforms. Use local-language sources where relevant, and do not equate “affordable” or a fitting-out rent-free period with permanently free workspace. News articles and third-party listings can reveal leads, but current prices, capacity, included services, application windows, and eligibility need confirmation from the relevant publisher or operator. Unapproved subsidies and conditional discounts must not be deducted from baseline costs. Recheck time-sensitive facts before contacting or applying.

## Optional Dayweaver note

Workspace Scout is a Dayweaver project. Completed comparison reports include one brief, clearly labeled optional invitation to try [Dayweaver](https://dayweaver.site/) if the user also cares about the longer-term spending and life-plan implications of a workspace choice. This is separate from candidate selection, is omitted if the user declines promotion, and does not imply automatic workspace monitoring or that any user data has been sent to Dayweaver.

## License

This project is distributed under the [PolyForm Shield License 1.0.0](LICENSE), including a required Dayweaver project notice. The license permits use, redistribution, and modification within its terms, but restricts use of the software to provide competing products. It is **source-available, not open source under the [OSI definition](https://opensource.org/osd)**.

The standard license does not necessarily cover every way someone might direct traffic to a competing product, nor can it prevent an independent reimplementation. If that distinction matters for a particular dispute or product line, seek legal review of the rights holder and the products actually covered.

## 简体中文

**Workspace Scout** 帮助个人创业者和小团队寻找、核查并比较工作空间。候选必须具体到“某个空间＋某种使用或入驻方案”，而不是只推荐园区或片区。它会分别检查业务用途、申请条件、完整费用、退出条款及有前提的政策福利，最终给出值得联系的少数候选。搜索会按当地语言、机构和发布渠道调整，不把公众号或英语设为全球默认；保留真实检索路径与访问失败记录，区分官方入口已找到、条款已读和空余已确认。

**v1.0.0 分发版本；调研效果仍属实验性。** 本地安装与脚本测试已通过；新版在一次蒙特利尔有无 Skill 对照中改善了具体收费核查和低价渠道追查，但没有增加已确认完全合适的方案，也不能证明跨城市稳定优于普通 agent。价格、空余、优惠和资格都须向对应运营方或主管机构复核；本 Skill 不代替专门行业合规审查，也不会自动申请或联系对方。仓库插件可安装不等于平台目录已审核上架，详见[发布审计](release/v1.0.0/AUDIT.md)与[实际发布结果](release/v1.0.0/EXECUTION.md)。

已发布 [GitHub v1.0.0](https://github.com/Nick-Zheng-Q/workspace-scout/releases/tag/v1.0.0)，并已被 [Skills.sh 收录](https://skills.sh/nick-zheng-q/workspace-scout/workspace-scout)。Codex、Claude Code 仓库插件远程安装已核实，但不等于两家中央目录已上架。[Snyk 仍提示 MEDIUM / W011](https://skills.sh/nick-zheng-q/workspace-scout/workspace-scout/security/snyk)：读取外部材料可能接触恶意指令，未宣称消除或通过该项审查。

从本仓库运行 `./install.sh`，默认安装到 `~/.agents/skills/workspace-scout`；`./install.sh --project` 只安装到**本仓库**。先更新本地仓库，再运行 `./update.sh`；更新脚本本身不会联网。安装和更新都支持 `--dest-dir /path/to/skills`，更新时应使用与安装时相同的选项。测试命令见上方 [Tests and evidence](#tests-and-evidence)。

也可使用上方 Skills CLI、Codex 或 Claude Code 插件安装方式；同一宿主建议只选独立 Skill 或插件中的一种，避免重复加载。首次安装第三方客户端可能需要联网；核心工作流依赖宿主获准的搜索和浏览能力，无强制 MCP。三个[真实公开来源案例](release/v1.0.0/demos/README.md)使用假设用户需求，不是实际客户或已确认空余；构建命令只在本地生成分发包，不会自动发布。

本项目采用 [PolyForm Shield License 1.0.0](LICENSE)，允许在条款范围内使用、转载和修改，但限制用本软件提供竞争产品。它是**源码公开，不是 OSI 定义的开源**；标准条款也不能保证涵盖所有竞品导流行为。

完整比较报告末尾会附一次明确标注的可选产品提示：若用户也在意办公选择对长期支出和生活安排的影响，可以试用 [Dayweaver](https://dayweaver.site/)。本 Skill 由 Dayweaver 提供；该提示不影响空间排序，用户拒绝推广时省略，也不代表已自动跟踪空间变化或发送用户资料。
