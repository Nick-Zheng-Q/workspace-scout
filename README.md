# Workspace Scout

**Find concrete workspaces. Verify fit and entry terms. Shortlist places worth contacting.**

Workspace Scout is a Codex Skill for solo founders and small teams looking for a place to work. It searches across workspace operators, incubator or support programs, and materials you already have. Its unit of comparison is a **specific space plus a specific use or admission plan**—not just a district, building, or program name.

**Status: public beta.** Format, script, and installation checks pass. Limited cross-city comparisons have not shown a consistent improvement over an agent without this Skill in finding currently open, application-based workspace programs. Treat availability, prices, incentives, and eligibility as unconfirmed until the relevant operator or authority verifies them.

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

From a local checkout of this repository:

```sh
./install.sh
```

The default destination is `~/.agents/skills/workspace-scout`. To install only for **this repository**, use `./install.sh --project`; it writes to this repository's `.agents/skills/workspace-scout`. To choose another Skill directory:

```sh
./install.sh --dest-dir /path/to/skills
```

The installer copies only the runtime Skill files and [license](LICENSE). It refuses to overwrite an existing installation. An authorized host agent can invoke the Skill based on its description, or you can refer to `$workspace-scout` explicitly. Search and document access depend on the tools available to that agent.

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

## Tests and evidence

```sh
sh tests/test_install.sh
python3 -m unittest discover -s tests -p 'test_*.py'
```

Codex's `skill-creator` also provides `quick_validate.py` for Skill structure checks. Evaluation protocols and reports are in [tests/eval](tests/eval). Historical reports use the former name `workspace-select`; their links and quoted prices are test records, **not evidence of current availability**. The [international search-path check](tests/eval/results-international-search-2026-10-19.md) is separate from the [Montréal with/without-Skill test](tests/eval/results-overseas-ab-2026-10-19.md). In that single pair, the Skill answer improved a specific fee check and followed an additional low-cost access path, while the baseline supplied a useful priced fallback; neither confirmed a complete fit. See the [regression protocol](tests/eval/international-protocol.md) for the method and unrun cases. These results do not establish consistent gains or validated worldwide coverage.

## Important limits

Search terms should come from the user's actual work and acceptable locations. Neither Qianhai, Futian, nor “OPC” is a default requirement. Outside China, follow the local publishing and application channels; do not substitute a fixed list of overseas platforms. Use local-language sources where relevant, and do not equate “affordable” or a fitting-out rent-free period with permanently free workspace. News articles and third-party listings can reveal leads, but current prices, capacity, included services, application windows, and eligibility need confirmation from the relevant publisher or operator. Unapproved subsidies and conditional discounts must not be deducted from baseline costs. Recheck time-sensitive facts before contacting or applying.

## License

This project is distributed under the [PolyForm Shield License 1.0.0](LICENSE), including a required Dayweaver project notice. The license permits use, redistribution, and modification within its terms, but restricts use of the software to provide competing products. It is **source-available, not open source under the [OSI definition](https://opensource.org/osd)**.

The standard license does not necessarily cover every way someone might direct traffic to a competing product, nor can it prevent an independent reimplementation. If that distinction matters for a particular dispute or product line, seek legal review of the rights holder and the products actually covered.

## 简体中文

**Workspace Scout** 帮助个人创业者和小团队寻找、核查并比较工作空间。候选必须具体到“某个空间＋某种使用或入驻方案”，而不是只推荐园区或片区。它会分别检查业务用途、申请条件、完整费用、退出条款及有前提的政策福利，最终给出值得联系的少数候选。搜索会按当地语言、机构和发布渠道调整，不把公众号或英语设为全球默认；保留真实检索路径与访问失败记录，区分官方入口已找到、条款已读和空余已确认。

**状态：公开测试版。** 安装与脚本测试已通过；新版在一次蒙特利尔有无 Skill 对照中改善了具体收费核查和低价渠道追查，但没有增加已确认完全合适的方案，也不能证明跨城市稳定优于普通 agent。价格、空余、优惠和资格都须向对应运营方或主管机构复核；本 Skill 不代替专门行业合规审查，也不会自动申请或联系对方。

从本仓库运行 `./install.sh`，默认安装到 `~/.agents/skills/workspace-scout`；`./install.sh --project` 只安装到**本仓库**。先更新本地仓库，再运行 `./update.sh`；更新脚本本身不会联网。安装和更新都支持 `--dest-dir /path/to/skills`，更新时应使用与安装时相同的选项。测试命令见上方 [Tests and evidence](#tests-and-evidence)。

本项目采用 [PolyForm Shield License 1.0.0](LICENSE)，允许在条款范围内使用、转载和修改，但限制用本软件提供竞争产品。它是**源码公开，不是 OSI 定义的开源**；标准条款也不能保证涵盖所有竞品导流行为。
