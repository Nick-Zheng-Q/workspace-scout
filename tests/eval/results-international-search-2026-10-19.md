# International search-path check — 2026-10-19

## Scope and limits

A manual, live check of source-discovery paths during the international guidance revision, not an isolated agent evaluation or an A/B comparison. No operator was contacted, account created, application submitted, or purchase made. The probes below tested source attribution, local-language discovery, unavailable pages, and distinctions between types of concessions. They did not produce a complete workspace shortlist or confirm inventory, applicant eligibility, booking success, or total cost. The cities and operators are evidence for these probes, **not a maintained directory or preferred providers**.

The web tool returned search-index text for some pages but could not fetch their bodies. This report preserves that distinction. All observations refer to 2026-10-19; a later reader must recheck them.

## Actual queries and source paths

These are the decisive queries and click paths actually used, not a claim to record every returned result or measure search recall.

| Probe | Actual queries | Follow-up | Observed access and conclusion |
| --- | --- | --- | --- |
| London | `site.london.gov.uk affordable workspace providers directory workspace apply` (literal query, not a correctly formed `site:` filter); then `site:camdencollective.co.uk apply membership free coworking eligibility` | City Hall index named Camden Collective → exact operator query → [operator hotdesking page](https://camdencollective.co.uk/hotdesking) → its Apply Now link | [City Hall body](https://www.london.gov.uk/programmes-strategies/shaping-local-places/places-work) returned 403, so only its indexed text was available. Operator body was readable. Its application link redirected to an external form that the tool could not read. Operator identity and link provenance were checked; form contents and successful submission were **not** checked. |
| Berlin | `site:berlin.de Gründungszentren Coworking Arbeitsplätze Bewerbung`; `site:hu-berlin.de Startup Inkubator Coworking Bewerbung Arbeitsplätze`; `site:tu.berlin gruenden coworking start up arbeitsplätze`; `site:tu.berlin/entrepreneurship "Inkubationsprozess" "Aufnahme"` | Native-language results → [TU room offer](https://www.tu.berlin/entrepreneurship/startup-support/raum-zum-starten), [startup support](https://www.tu.berlin/entrepreneurship/startup-support/) and an [English overview](https://www.tu.berlin/en/topics/entrepreneurship/eins) | Those body fetches returned 403. German index results exposed potentially relevant university and program leads; they did **not** establish readable current admission terms or an applicant-specific room. Stop at an unverified lead, not “no Berlin spaces” or “free access confirmed.” |
| Singapore | `site:jtc.gov.sg LaunchPad coworking startup space apply`; `site:n9offices.com Ayer Rajah coworking day pass`; `site:n9offices.com "Ayer Rajah"` | JTC estate overview → [specific One-North property page](https://www.jtc.gov.sg/find-space/launchpad--onenorth) → its Apply for Space link | Property body was readable; the linked government form only exposed a JavaScript requirement. No attributable N9 plan was established in these queries. The readable property page and unread form are separate observations, not proof of a working application or an available room. |

## What these paths support

- **London:** The [operator page](https://camdencollective.co.uk/hotdesking) distinguishes free hotdesking from subsidised lockable offices. It describes community obligations and says applications are being accepted. A linked external form is not automatically unofficial, but capacity and applicant approval remain unconfirmed. The probe did not inspect form fields or submit them.
- **Berlin:** German search-index results contained named institutions, space descriptions and program references. No comparison against an English-only search was run. Because body access failed, this check supports adding a local-language and access-status workflow—not a verified conclusion about the university's current offer or eligibility. Search-index crawl freshness is not a current application deadline.
- **Singapore:** The [property page](https://www.jtc.gov.sg/find-space/launchpad--onenorth) describes a fitting-out rent-free period and requests availability enquiries; that is not permanently free coworking. It also distinguishes unit types and gives local incorporation conditions. None of those facts establishes the unknown user's qualification or a priced, available office plan.

## Supported changes and remaining tests

The guide now follows locally appropriate institutions and terminology, accepts operator-authorized external entry points with limited claims, and records unread sources rather than treating fetch errors as absent supply. The general instructions do not name these operators or require an English source, WeChat, LinkedIn, a university, or a particular domain suffix in every search.

The [international regression protocol](international-protocol.md) contains fresh Montréal, Osaka and Guangzhou cases. **Those agent runs have not been executed.** The installer and Python unit tests validate packaging and arithmetic/constraint behavior only. This report does not establish that the revised Skill improves discovery quality or works reliably worldwide.


## Later paired test on 2026-10-19

The Montréal with/without-Skill pair was subsequently [run and reviewed](results-overseas-ab-2026-10-19.md). The earlier paragraph describes the state at the time of this source-path check; Osaka and Guangzhou remain unrun. The later pair does not turn this source-access probe into an agent evaluation.
