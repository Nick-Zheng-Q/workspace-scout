# Overseas with/without-Skill comparison — 2026-10-19

## Result

**The revised Skill helped narrowly in this Montréal case, but did not establish more fully confirmed fits.** A reviewer given randomized answer labels and no condition mapping preferred the Skill answer for a specific, source-backed fee warning and an additional credible low-cost enquiry path. The baseline answer retained a more concrete two-location fallback. One pair does not establish consistent improvement, and a full-Skill/no-Skill comparison cannot isolate the new search guide's effect from the core instructions and evidence template.

## Design and scope

- **Request:** one solo software consultant, Plateau-Mont-Royal versus downtown Montréal; six desk weekdays and four one-hour private calls monthly; CAD 350 including mandatory charges; Canadian company, no university affiliation. [Exact prompt](overseas-ab-2026-10-19/request.txt).
- **Execution:** two fresh subagents with no inherited chat history and separate temporary directories. Baseline was instructed not to inspect workspace-specific Skills or the repository. The treatment received only the current runtime Skill and its resources, not prior reports, this rubric or example providers. Both inherited the same model/reasoning settings; the tool did not report the exact model name.
- **Budget:** each had 12 search queries and 16 page opens/clicks. Both used those ceilings. Finds on already retrieved pages were available without a separate ceiling: baseline used 0, Skill used 19. Thus this was not an equal-total-tool-call or equal-token-cost test.
- **Review:** outcome criteria were fixed before reading the results. A fresh reviewer saw randomized A/B answers, request and criteria only, then independently checked primary sources with 3 queries, 13 opens and 4 finds. Condition mapping and execution logs were withheld until after its written judgment; writing style could still allow guesses. [Criteria](overseas-ab-2026-10-19/review-criteria.md), [review](overseas-ab-2026-10-19/blind-review.md).
- **Frozen treatment:** runtime file hashes are in the [manifest](overseas-ab-2026-10-19/manifest.json). No runtime instruction was changed after the test. Skill/reference setup reads were omitted from the initial log and later supplied as a factual [addendum](overseas-ab-2026-10-19/setup-read-audit.json); original answers and logs were not revised.
- **Side effects:** no contact, submission, account creation or purchase. Both runs attempted the same host-required Directory setup; unavailable tooling did not lead either to install software or authenticate.

## Observable differences

| Outcome | No Skill — Answer A | Revised Skill — Answer B | Interpretation |
| --- | --- | --- | --- |
| Main published quantity-fitting plan | ECTO flex and its shorter-commitment variant | Same | No increase in proven providers or fully confirmed fits. Both found the useful French plan terms. |
| Specific potential entry charge | Generic question about joining/co-op fees | Located the published CAD 350 lifetime-share amount; flagged requirement, timing and refundability as unknown | A material enquiry improvement. It does **not** prove that the amount is compulsory or that a monthly budget necessarily fails. [Operator tariffs](https://ecto.coop/tous-les-tarifs/). |
| Downtown low-cost path | Café and municipal-library alternatives; no established incubator access | Also followed District 3 to its workspace, program and contact pages, with applicant and workload limits | A credible additional enquiry, not a confirmed free standalone desk/call-room entitlement. [Programs](https://www.district3.co/programs), [workspace](https://www.district3.co/about). |
| Budgeted fallback | Priced downtown café desk days plus separately rented Plateau meeting rooms, with travel caveat | More conditional same-site café illustration | Baseline advantage: a useful combination the Skill answer did not develop. No option's privacy and full compulsory charges were confirmed. |
| Evidence limits | Flagged CoWork access limits; café prices stated more directly | Explicitly distinguished indexed café claims from unread page bodies | Better disclosure in B; the raw access log shows blank extraction rather than verified full terms. It is not credited as extra supply. |
| Full affordable, available, private-call fit | 0 | 0 | Neither result is an approval, current inventory confirmation or all-in quote. |

Both used French and English queries, computed the compared monetary examples correctly, and did not assume a phone booth or library room automatically met the private-call requirement. Do not attribute those shared strengths to the Skill alone. The reviewer also noted a published personalized-plan/service-exchange invitation that neither answer developed; this remains a missed enquiry route, not grounds for a city-specific instruction.

## Artifacts and audit limits

- [Baseline answer](overseas-ab-2026-10-19/baseline-answer.md) and [query/access log](overseas-ab-2026-10-19/baseline-search-log.json).
- [Skill answer](overseas-ab-2026-10-19/with-skill-answer.md) and [query/access log](overseas-ab-2026-10-19/with-skill-search-log.json).
- [Independent review](overseas-ab-2026-10-19/blind-review.md) and [review research log](overseas-ab-2026-10-19/review-search-log.json).

Logs are execution-agent-maintained audits, not complete server-side transcripts. Public exports redact machine paths and replace tool-local references with recorded URLs where possible; unmapped references are marked unresolved. Original output/log hashes and normalization notes are retained in the manifest. Primary URLs can be rechecked, but the live web, result ranking and access failures are not deterministic.

This evaluates **one case, one run per condition, explicit Skill use**. It does not retest automatic invocation, worldwide coverage, all free workspace discovery, or the marginal contribution of `search-guide.md` alone. The Japanese and mainland-China prompts in the protocol were not run. No scores or candidate-count ranking are substituted for the source checks.

## Release decision

Keep the general international discovery changes and publish this mixed, narrowly favorable result alongside the earlier limitations. Do not add Montréal, ECTO, District 3 or a prescribed platform to the runtime guide. Preserve baseline strengths for future tests. Repeat with new cases before claiming stable superiority.

## 中文结论

本次蒙特利尔单案例中，使用 Skill 的结果略好：追查到具体的合作社份额收费，并补查了一个带资格与义务限制的市中心低价空间渠道；无 Skill 组的跨地点组合方案更具体。两组都没有确认全部费用、空余和通话私密性。因此只能说本次有局部帮助，不能证明新版搜索指导单独或稳定优于基线。原始答案、查询记录与盲评均已归档，运行时指南没有加入城市或运营方专用规则。
