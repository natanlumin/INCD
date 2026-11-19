# SCRUM-290 (ASM-3): survey and compare assessment tooling, strategy

Item folder for SCRUM-290, ASM-3 in the plan (epic SCRUM-266). Per the item convention this README is the
strategy and `scrum290.md` is the task; the HTML is built from the task only. Natan drafts (0.5d), Dan reviews
(0.25d). Skeleton section: 6.4 assessment tooling. Wave 3; blocked by ASM-1 (SCRUM-284, Done); blocks ADV-4 (SCRUM-305). Sprint 15, 3 story points,
labels deliverable-1c, incd, research, wa-asm, wave-3; reporter Dan Klein.

## What the Jira asks

Desk survey across categories: artefact and format scanners, red-team and adversarial frameworks, guardrail
layers, runtime monitors, provenance verifiers. Compared on coverage, lifecycle stage, maturity, licensing and
operational fit. Desk-based, no hands-on evaluation at this stage.

## Definition of done (acceptance criteria), state on 18 November

| Criterion | Where in `scrum290.md` | State |
|---|---|---|
| Survey across the five named categories | Part 2 opens with a bridge to the earlier documents; 2.1 in three groups by the object read (file, shipped code, packages and container, after SCRUM-284 section M "scanners (file, format, code)"); 2.1 to 2.5 in the Jira's order; 2.6 white-box analysis as a sixth category (Decision 3) | met (5 of 5, plus 1) |
| Compared on coverage, lifecycle stage, maturity, licensing, operational fit | 1.3 defines each comparison dimension and its scale (maturity: stable, pre-release, research code, dormant, retired); Tables 3 to 8 per category; Table 9 has one column per comparison dimension | met (5 of 5) |
| Desk-based, no hands-on evaluation | 1.4; every tool fact cited to its documentation, TL-01 to TL-48; performance only from papers (SC-18, TH-12, TH-14, TH-50, TH-53) | met |
| Comparison table with a stated evaluation date and version | Part 3, Table 9: 36 rows; evaluation date 18 November 2026 in the caption; version per row; version and licence per source-log row | met |
| Any tool proposed for the ADV-4 (SCRUM-305) demonstration set is justified from this table | Part 5, Table 11: eleven proposals on four stated conditions, each from its Table 9 row with its threats; every tool not proposed listed with the condition it fails | met |
| Blocked by ASM-1 | SCRUM-284 drafted; stage-tables.md section M, "Tooling kind to stage", gives the placement rule used here | met |
| Dan reviews (0.25d) | subtask 5 | pending |

## Notation and content bound to the earlier items

| In `scrum290.md` | Taken from | Used for |
|---|---|---|
| S1 to S4; Qn.k; en.k (Table 12 annex) | SCRUM-284, stage tables | the Stages column of Table 9; placement of each category (Table 2) |
| static, dynamic, behavioural, provenance | SCRUM-281 1.4; SCRUM-284 1.4, Table 3 | the test family of each category (Table 2) |
| tooling kind to stage | SCRUM-284, stage-tables.md section M | Table 2 repeats it unchanged; Part 3 adds the tools as rows under it, as section M asks |
| guard is a control, not a method | SCRUM-284 1.4; glossary "safeguard and guard" | 2.3 framing |
| T1 to T8; SC-15, SC-16, SC-18, SC-24, SC-26 | 4.2 supply-chain document | coverage of scanners and verifiers |
| T9 to T21; TH-12, TH-13, TH-14, TH-50, TH-51, TH-53 | SCRUM-288 | coverage; limits of backdoor scanners; AgentDojo |
| P1 to P6; D1 to D5 | SCRUM-289 | coverage: properties column of Table 9, rows of Table 10 |
| classification, embedding, generative rows | SCRUM-280, Table 4 | coverage by row; the embedding gap |
| HF-05 to HF-08; C4 to C7 | SCRUM-280; 4.2 document | the Hub's own scans as platform-side controls |
| gap; demonstration set; established, emerging; Official, Research | SCRUM-281 | Part 4, Part 5, claim labels, source classes |
| new ids TL-01 to TL-48 | this item | source log, same columns as SCRUM-288 and SCRUM-289 |

Completion check run 18 Nov: every TL id cited has a row and every row is cited; T9 to T21 each have a row in
Table 10; every Qn.k and en.k used is in the annex, Table 12; no em or en dashes; HTML rebuilt.

## Inputs, bound to the existing files

| From | What this item takes |
|---|---|
| ASM-1, `process/scrum-284/` | S1 to S4, Qn.k, en.k; test families F1 static, F2 dynamic, F3 behavioural, F4 provenance; the mapping rule (a method maps to every stage holding the evidence kind it reads, where its access need is met); `stage-tables.md` section M, the tooling-kind-to-stage table, whose rows this item fills; guards are controls, assessed with the model, not methods |
| THR-3, `process/scrum-288/` | threats T9 to T21, statuses, the boundary; TH-13 PICCOLO, TH-53 BAIT, TH-12, TH-14 for backdoor-scanner limits; TH-51 AgentDojo |
| ASM-2, `process/scrum-289/` | attestable properties P1 to P6 and testable properties D1 to D5; which tools read which property |
| 4.2 item, `process/huggingface/` | T1 to T8; Hub scanners C4 to C7; picklescan bypasses SC-15, SC-16; PickleBall SC-18; model signing SC-24; CycloneDX SC-25; ModelScan SC-26 |
| LAND-1, `process/scrum-280/` | Table 10 segmentation: classification, embedding, generative rows; formats pickle, safetensors, GGUF, ONNX |
| Glossary, SCRUM-281 | test family, control, guard, demonstration set, confidence labels, source classes |

## Rules this item runs under (same as SCRUM-288, SCRUM-289)

- Notation of the earlier items unchanged; new source ids use the prefix TL-nn; earlier ids resolve to their
  own logs.
- Every claim cited at the point of use. Tool facts are cited to the tool's own documentation (class
  Official); research results to the paper (Authors, venue year).
- The one date in the task is the evaluation date the Jira asks for, stated once in the Table 9 caption and in
  the source log. No counts from our own runs; popularity measures (stars, downloads) are not used, because
  they change with the day they are read.
- The demonstration set is named as the report's (SCRUM-281 term); no internal tool names in the task.
- No Jira ids, no drafting scaffolding in the task.

## Decisions

1. **Evaluation date** is the day versions and licences were read from the tools' release records:
   18 November 2026. This is later than the research cut-off (6 October 2026); the cut-off governs the
   literature, the evaluation date governs the versions. Settled: the DoD asks only that the evaluation date be stated.
2. **Scope: tools with a public version and licence.** Commercial services publish neither a version nor
   their method; they are named only where the platform documents them (Hub scanners C6, C7) and are not
   rows of the table, because a row without a version would fail the criterion.
3. **White-box analysis** (F2 in ASM-1's table) is not a Jira category but holds the only tools that read for
   hidden triggers (T10). It is surveyed as a sixth category, presented as one of the categories without an "added" label (user, 18
   Nov), so that T10 and the internals half of Q2.3 are not left without a row.
4. **Guardrail layers** are surveyed as the Jira asks, and placed as ASM-1 places guards: a control assessed
   with the model, not a method that assesses it.

## Files

- `scrum290.md`: the task. `scrum290.html`: its readable build.
- `subtask_1.md` to `subtask_5.md`: the Jira subtasks.
- `README.md`: this strategy.
