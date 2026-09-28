# Workspace Scout

面向个人创业者和小团队的工作空间发现、适配评估与入驻条件核查 Skill。它帮助 agent 从运营方供给、园区或孵化器申请项目及用户已有材料中，找出**具体空间＋具体使用或入驻方案**，核查实际用途、资格、费用和退出条件，再给出值得联系的少数候选。

**状态：公开测试版。** 已通过格式、脚本和安装测试，并做过少量跨城市对照；这些测试尚未证明它能稳定地比不使用 Skill 的 agent 找到更多当前可申请的扶持空间。不要把输出当作已确认的空余、报价、政策资格或入驻批准。

## 适用范围

- 软件、设计、咨询、内容制作等个人或小团队的办公空间；可记录接待、拍摄、录音、设备留置等特殊要求。
- 支持从零寻找，也支持审查已有的园区资料、报价、申请说明和合同草稿。
- 不直接判断餐饮门店、生产车间、实验室等专门行业的合规性。
- 不自动提交申请、发送资料、签约或联系运营方。

核心方法见 [SKILL.md](SKILL.md)；搜索方向见 [references/search-guide.md](references/search-guide.md)。

## 安装

需要能够读取本地 Skill 的 Codex 环境，以及用于费用检查的 Python 3（仅在运行该脚本时需要）。从本仓库目录运行：

```sh
./install.sh
```

默认安装到 `~/.agents/skills/workspace-scout`。如需仅供当前项目使用，运行 `./install.sh --project`，安装到**本仓库**的 `.agents/skills/workspace-scout`。也可指定其他 Skill 目录：

```sh
./install.sh --dest-dir /path/to/skills
```

安装脚本只复制运行 Skill 所需的文件及许可证；不会更改现有同名安装。安装后可直接提出工作空间问题，由宿主 agent 根据 Skill 描述决定是否调用，或显式使用 `$workspace-scout`。实际搜索能力取决于宿主 agent 已获准使用的工具。

## 更新

先获取本仓库的新版本（例如通过 Git 拉取），再在**同一个本地仓库目录**运行：

```sh
./update.sh
```

如果安装时用了 `--project` 或 `--dest-dir`，更新时传入相同参数。`update.sh` **不会联网下载新版**；它用当前仓库内容替换已安装版本，并把旧版备份到安装目录旁的 `workspace-scout-backups`。它会拒绝替换符号链接或无法识别的同名目录。

## 费用检查脚本

可选脚本只核算已输入的金额与硬条件状态，**不会验证来源真实性或自动补齐漏报费用**：

```sh
python3 scripts/check_candidates.py path/to/input.json --pretty
```

输入格式见 [references/check-input.md](references/check-input.md)。

## 测试

```sh
sh tests/test_install.sh
python3 -m unittest discover -s tests -p 'test_*.py'
```

格式检查可用 Codex 的 `skill-creator` Skill 附带的 `quick_validate.py`。搜索效果的测试方法与结果保存在 [tests/eval](tests/eval)；历史报告沿用当时的 `workspace-select` 名称；其中的网页和报价仅用于复盘，不代表今天仍可申请或适用。

## 使用时的边界

每次检索都应从用户当前业务和可接受区域出发，不把前海、福田或 OPC 当作默认条件。新闻和第三方房源可以提供线索，但具体资格、现价、名额和包含服务应回到对应发布方或运营方核实。未确认的免费工位、补贴或优惠不能直接抵减基础预算。用户联系或申请前，应再次核对当期条款。

## 许可证

本项目使用 [PolyForm Shield License 1.0.0](LICENSE)，并在许可证末尾列有须保留的 Dayweaver 项目声明。该条款允许在许可范围内使用、转载和修改，但不允许用本软件提供与许可方及其相关产品竞争的产品。它**不是 OSI 定义的开源许可证**；准确表述应是「源码公开」。

这份标准条款限制的是竞争性产品使用，**不保证涵盖一切“为竞品导流”的行为**，也不能阻止他人独立重写类似方法。如果打算以许可证处理具体导流争议，或希望把 Dayweaver 某一业务明确纳入保护范围，发布前应由法律专业人士结合实际权利主体和产品范围审阅。
