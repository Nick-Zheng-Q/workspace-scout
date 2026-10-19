# Three workspace decision examples

Research date: **2026-10-19**. These are illustrative user briefs, not actual customers. Named spaces and cited published terms are real. Nothing here asserts operator confirmation, approval, vacancy, savings or an endorsement. This is not a new with/without-Skill experiment.

The examples demonstrate three decisions, not a city-specific provider list for the runtime Skill. They deliberately retain unresolved conditions instead of manufacturing a complete match.

## Reproduce

From the repository root, run:

```sh
python3 scripts/check_candidates.py release/v1.0.0/demos/montreal.input.json --pretty
python3 scripts/check_candidates.py release/v1.0.0/demos/london.input.json --pretty
python3 scripts/check_candidates.py release/v1.0.0/demos/singapore.input.json --pretty
```

The corresponding `*.expected.json` files are frozen arithmetic/check outputs. The [three reports](reports.md) explain the evidence and limits. Each `*.request.txt` is a full prompt for a fresh host-agent run with authorized search/browser access. The research paths are in [sources.json](sources.json). Reopening those URLs and rerunning live searches will not reproduce identical pages, rankings, prices or model answers; record a new observation date instead of silently overwriting this snapshot.

Every example keeps `required_costs_complete=false`. A known subtotal is not an all-in quote; an unknown fee is not zero. The helper does not interpret eligibility or read websites. Research notes are human-readable, while JSON is only the small deterministic checking step.

## Acceptance checks

- Montréal: six individual desk days and four separate one-hour room bookings produce CAD 340 **before tax and any other required charges**; do not substitute one continuous four-hour block. Do not describe cooperative shares as ordinary nonrefundable setup fees or cash-equivalent refundable deposits.
- London: advertised free hotdesking is not a free private office or an approval. Preserve community obligations and uncertain hub allocation. A deadline without a year does not establish a current intake.
- Singapore: distinguish the same operator's day passes and part-time plan. Include GST in the arithmetic scenario; do not infer storage, acoustic privacy or studio credits from building-level facilities. A special-rate invitation is not an awarded subsidy.

No applications, contacts, reservations or uploads were performed. The optional Dayweaver note appears once after the combined report and does not affect any recommendation.
