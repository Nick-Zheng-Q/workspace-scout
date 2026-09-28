# 费用与硬条件检查脚本输入

运行：`python3 scripts/check_candidates.py path/to/candidates.json`。输出 JSON，可用 `--pretty` 阅读。只做算术和状态汇总；来源是否可靠、条款如何解释仍须人工核查。所有金额须采用同一货币（`currency`），按预计使用量折算成同一**月度**口径。

```json
{
  "currency": "CNY",
  "hard_requirements": ["周末使用", "设备过夜留置"],
  "budgets": {"monthly_max": 4000, "upfront_max": 10000},
  "candidates": [
    {
      "id": "space-a-fixed-desk",
      "required_costs_complete": false,
      "conditions": {"周末使用": "unknown", "设备过夜留置": "met"},
      "costs": [
        {"name": "工位", "kind": "recurring", "amount": 1800, "quantity": 1, "required": true},
        {"name": "每月预计会议室小时", "kind": "recurring", "amount": 80, "quantity": 8, "required": true},
        {"name": "押金", "kind": "deposit", "amount": 1800, "required": true},
        {"name": "待报价的储物柜", "kind": "recurring", "amount": null, "required": true}
      ]
    }
  ]
}
```

`kind` 仅允许 `recurring`（月度支出）、`upfront`（前期不可退）、`deposit`（可退押金）。`amount` 是非负单价，未知时用 `null`；`quantity` 为该月/该项目的非负数量，默认 1。`required:false` 项目不计入基础费用；优惠/补贴不要写成负金额，应在候选记录中另列条件情景。`upfront_max` 检查的是前期不可退支出加押金，**不含首月租金**，因此输出不是完整的签约现金需求。预算可省略；缺少预算时不做预算判定。

签约时需付现金须在候选记录另列，仅加总已证实签约时要付的押金、一次性费用、预付租金及其他预付款，逐项列式；脚本当前不计算它。不得把 `upfront_budget_status` 直接当作签约现金是否足够，也不得在付款时间未知时自行假定。

`required_costs_complete` 默认 `false`。只有已经核对该方案在用户使用方式下所有必要的月度及前期收费，才设为 `true`；否则已知小计即使低于预算也不能判定预算内。月度支出、前期不可退费用、可退押金三个类别都须各有一条 `required:true` 的记录；确认没有该类费用时，显式录入金额为 0 的记录。否则即使标为费用已核全，缺失类别仍为 `unknown`。该标志依赖证据，不是脚本能够自动证明的。

条件状态只允许 `met`、`unmet`、`unknown`、`conflict`，对应满足、不满足、未知、资料冲突。缺失的硬条件按未知处理。任何不满足为 `reject`；没有不满足但有未知或冲突为 `verify`；全部满足才是 `pass`。预算已知小计超限则判 `over`；未超限但有必需费用未知或收费范围未核全则判 `unknown`。只有 `required_costs_complete=true` 且已知费用未超限，才输出 `within_confirmed_scope`。
若尚未录入月度费用，月度预算状态也为 `unknown`；确认免费时请显式录入金额为 0 的月度费用项。
