# Skill 自动触发隔离测试（2026-09-23）

依据 [OpenAI 官方 Build skills 文档](https://learn.chatgpt.com/docs/build-skills)，Codex 会从仓库的 `.agents/skills` 等位置发现 Skill，并可根据 `description` 隐式调用。为避免改动用户全局配置，本次在 `/private/tmp` 下建临时 Git 项目，将当前 Skill 复制到 `.agents/skills/workspace-select/`，使用 `codex exec --ephemeral -s read-only` 运行两个**没有提及 Skill 名称**的提示。没有联网找房源或修改实际项目。

| 测试 | 输入概述 | 运行记录 |
| --- | --- | --- |
| 正向 | 两人在厦门思明／湖里找设计咨询工作空间；只要搜索方向，不联网 | Codex 命令记录明确读取 `.agents/skills/workspace-select/SKILL.md`，随后读取 `references/search-guide.md`；答复也按两区的运营方直供、申请型空间及免费工位核查展开。**触发成功。** |
| 负向 | 厦门小餐馆店面，问排烟、消防和食品许可，不联网 | 命令记录没有读取上述 Skill 或搜索指南。**未误触发。** |

这是**一正一负的最小触发检查**，不能证明各种自然语言请求均能稳定触发，也不验证搜索结果质量。当前项目只有根目录的 `SKILL.md`，尚未放入本项目 `.agents/skills/workspace-select/` 或用户 Skill 目录；因此本次成功说明**按官方位置安装后**可触发，不表示当前工程目录本身已自动启用。
