# SCRUM-288 (THR-3): model-integrity and inference-time threats, strategy

Item folder for SCRUM-288, THR-3 in the plan (epic SCRUM-266). Per the item convention this README is the strategy and `scrum288.md` is the task; the
PDF is built from the task only. Natan drafts, Dan reviews for security correctness.

## What the Jira asks, and where the task answers it

| Jira requirement | Where in `scrum288.md` |
|---|---|
| Threats to the model itself: training-data poisoning; backdoors and trojan triggers; fine-tune and LoRA tampering; quantisation-induced drift and quantisation-triggered backdoors; merge contamination | Part 2, T9 to T14, one entry each, in the Jira's words and order |
| Threats at use: prompt injection, direct and indirect; jailbreaks; model and training-data extraction; membership inference; agentic and tool-use abuse | Part 3, T15 to T21, one entry each, in the Jira's words and order |
| Drafted subsections | Part 2 (skeleton 4.3) and Part 3 (skeleton 4.4) |
| Distinguishing what is demonstrated in literature from what is theoretical | intro Table 1 row 1; Part 1.3 defines the three statuses; every entry carries a "Demonstrated" and a "Theoretical" paragraph; Table 3 gives the status per threat |
| Each threat tagged with the lifecycle stage it enters at | intro Table 1 row 2; Part 1.4 defines the tag and where each family enters; every entry carries "Enters at"; Table 3 |
| The model-level versus system-level boundary stated explicitly | intro Table 1 row 3; Part 1.5 states the boundary as a test and what it decides (criterion timing, who answers by proxy, which control); Part 4 applies it threat by threat (Table 4) |
| Every threat listed enters the ADV-2 classification cycle | intro Table 1 row 4; Part 1.2 Table 2 lists all thirteen; Table 3 is the register, one row per threat with the fields ADV-2 records; all thirteen ids are handed over |

## Pending fixes from the user's remarks (apply after the remarks round is complete)

1. **DONE 16 Nov. Reference the numbers in the register bullet** ("One register for the whole threat landscape"): give the
   source of "eight", "T1 to T8" and "twenty-one" at the point of use, i.e. the supply-chain and
   artefact-level threats document, Part 2 (`process/huggingface/hub-supply-chain-threats.md`), and say that
   the thirteen are the Jira's list with three pairs split (1.2). User, 16 Nov: "provide reference; don't do
   it now, fix after we complete the remarks".
2. **DONE 16 Nov. Part 2 opening bullet list** repeats Table 2's definitions; replace with a pointer to Table 2 (rule:
   threats defined once).
3. **DONE 16 Nov. Where the thirteen threats come from (1.2, Table 2).** Add a reference for each threat's origin: a
   "Named in" column with the framework entries that name it (OWASP Top 10 for LLM Applications 2025, MITRE
   ATLAS 2026.09, NIST AI 100-2 E2025), each verified against the source, and "named by no framework" where
   that is the case (to check for quantisation and merging). User, 16 Nov.
5. **Audit 16 Nov, wording and accuracy fixes:** [a, DONE] T9 "Demonstrated. Four results, each on models the
   researchers trained themselves" is wrong for Carlini et al. (datasets, not models); [b, DONE] classification row
   of T9 and T10 marked "not established" although NIST 2.3 and the predictive-AI poisoning literature cover
   it; [c, DONE] "threat classification cycle" to use the report structure's term, threat classification and decision
   cycle (section 2.3), with reference; [e, DONE] Table 3 caption still dated and omits NIST; [f, DONE as (a): kept as the finished paper's statement; COMPLETION CHECK before Dan's review: every Table 2 threat has an entry in Part 2 or 3, a row in Part 4 and a row in Table 3] 1.2's "every threat ... has
   an entry and a row" true only when Parts 2 to 5 are complete; [d, DONE] inference-time "Enters at" must name one
   stage (S4) with S3 as where exposure is fixed.
6. **DONE 16 Nov (TH-13 PICCOLO, TH-14 TDC2023). T10 literature**: add PICCOLO (IEEE S&P 2022) and the Trojan Detection Challenge, after verification.

## Acceptance criteria, state on 16 November

| Criterion | State |
|---|---|
| Drafted subsections | 2 of 13 threats drafted (T9, T10); Part 1 frame complete |
| Demonstrated in literature versus theoretical | in place for T9, T10; frame defines the three statuses |
| Each threat tagged with the lifecycle stage it enters at | in place for T9, T10, in SCRUM-284's S, Q and e notation |
| Model-level versus system-level boundary stated explicitly | stated as a test in 1.4; Part 4 (applied per threat) to write |
| Every threat enters the ADV-2 classification cycle | register Table 3 has 2 of 13 rows; Disposition column left for ADV-2 |
| Dan reviews for security correctness | pending; subtask 5 |

## Bound to the existing files

| File | What this item takes from it | Where |
|---|---|---|
| `governing/report-style-guide-and-glossary.md` (SCRUM-281) | the three threat families; model level and system level; lifecycle stage; derivatives incl. abliterated model; confidence labels; Official and Research classes | throughout; tagged (SCRUM-281) at first use per part |
| `process/scrum-284/` (ASM-1) | S1 to S4, Qn.k, en.k; declared evidence; Table 1 for what exists by proxy; e2.4 and e2.5 trigger probes at Q2.2; S4 as the only stage that sees inference-time threats | "Enters at" line of every entry; 1.3 |
| `process/scrum-280/` (LAND-1) | Table 4 row and column labels; file kinds | "Applies to"; 1.5 |
| `process/scrum-286/` | Table 2 derivative counts; Table 6 training-data field at 13 per cent | Part 2 intro; T9 |
| `process/huggingface/` (4.2) | T1 to T8 numbering continued; T3 versus T10 separation; T6 adapters as the route for T11; T8 serving routes for the boundary part | scope, Part 2, T10, Part 4 |
| `landscape/serving-and-compiled-artefacts.md` | plugins, custom operators, compile cache as system level | Part 4 |
| root `README.md` | skeleton map rows 4.3 and 4.4 now point here | done |

## Plan (Jira subtasks, in the Jira's words)

| Subtask | Delivers | Estimate | State |
|---|---|---|---|
| Analyse the threats to the model itself | the six model-integrity entries with status, stage and level | Natan 0.5d | 2 of 6 drafted |
| Analyse the threats at use | the seven inference-time entries with status, stage and level | Natan 0.5d | to write |
| State the model-level versus system-level boundary | the boundary test and its application to every threat | Natan 0.25d | test stated; application to write |
| Hand every threat to the classification cycle | the register table, one row per threat | Natan 0.25d | 2 of 13 rows |
| Review for security correctness | Dan's review of the entries, statuses and the boundary | Dan 0.5d | pending |

## Decisions taken in drafting

- **Every claim cited at the point of use (user, 16 Nov: "extremely cardinal").** Prose cites (Authors,
  venue year) or (Authors year, preprint) plus the log id; frameworks by name plus id. The work must read as
  holistic: no claim depends on a time, a run or our own measurement.
- **Era-agnostic text (user, 16 Nov).** The task carries no counts or dates from a particular pull or run.
  Ecosystem facts are stated as findings with a pointer to the SCRUM-286 section that measures them; the
  numbers live there. Dates and versions remain only where the citation policy requires them: framework
  editions, the verification date in a framework table's caption, and the source log.

- **Thirteen threats, exactly the Jira's list, numbered T9 to T21.** The numbering continues the 4.2 Hub
  task's T1 to T8, so that 4.2 and THR-3 form one threat register for ADV-2 and Appendix A. M and I were
  rejected: ASM-1 (SCRUM-284) already uses M, Mi for an assessment method. The Jira's paired items are split
  where the pair has different evidence, stage or level: prompt injection into direct (T15) and indirect
  (T16); extraction into model (T18) and training-data (T19); quantisation into drift (T12) and triggered
  backdoors (T13). The full list: T9 training-data poisoning, T10 backdoors and trojan triggers, T11 fine-tune
  and LoRA tampering (abliteration inside), T12 quantisation-induced drift, T13 quantisation-triggered
  backdoors, T14 merge contamination; T15 direct prompt injection, T16 indirect prompt injection, T17
  jailbreaks, T18 model extraction, T19 training-data extraction, T20 membership inference, T21 agentic and
  tool-use abuse. Jira-facing text uses the names only, never the numbers. Nothing outside
  the list was added. Inversion, which the skeleton's 4.4 line names, is treated inside T19, because it
  recovers training data. Abliteration is treated inside T11, because it is a published tampering of the
  safeguard by a weight edit.
- **Demonstrated versus theoretical is a separate axis from the confidence label.** The label (established,
  emerging, forecast) says how well the claim is sourced; the status (observed in deployment, demonstrated in
  research, theoretical) says what the source shows. A peer-reviewed lab result is established and
  demonstrated in research, not observed.
- **Enters at = ASM-1's lifecycle stage (SCRUM-284, `process/scrum-284/`).** The tag is one of ASM-1's four
  stages, S1 selection, S2 adjustment, S3 deployment, S4 runtime detection, plus the ASM-1 question at which
  the threat is first answerable (e.g. Q1.6 behaviour and safeguard at selection; Q2.2 and Q2.3 after an
  adjustment; Q3.2 what surrounds the model; Q4.2 inputs arriving in service). A threat introduced upstream,
  in the producer's training or a third party's derivative, enters the organisation at S1; the entry also
  names who introduces it. ASM-1's access line (in possession or by proxy) is carried per threat, since by
  proxy only black-box behaviour and declared statements exist (ASM-1 Table 1).
- **The boundary is a test, not a list.** Model level: the threat travels with the file and is present in any
  deployment of it. System level: it exists because of what surrounds the model. Most inference-time threats
  have a model-level susceptibility and a system-level consequence, and the task says which part is which.
- **Applies to = LAND-1's segmentation, verbatim.** LAND-1 (worked in `process/scrum-280/`, section 2,
  Table 4) is the single segmentation every later matrix keys off. The "applies to" column of the register
  uses its row labels (classification, embedding, generative model; the modality qualifier) and its column
  labels (pickle checkpoint, safetensors, GGUF, ONNX), and its two file kinds (quantised model, adapter) plus
  the glossary's merged model. Table 4 is still pending the freeze with Dan, so the column is marked as keyed
  to the proposed table and is re-read at the freeze. Expected shape: model-integrity threats key on the rows
  and the file kinds, not the format columns, since the alteration is in the numbers whatever the container;
  T13 is the exception, demonstrated on GGUF quantisation types specifically.
- **The demonstration set is not cited.** Theory text carries no results; the demonstration evidence belongs
  in Appendix B.

## Hand-offs (for assembly; kept out of the task)

- **From 4.2 (process/huggingface):** the artefact layer is the delivery mechanism for T9 to T14; the 4.2
  task handed "the alteration itself, and what it does" to this item. T8's server-side routes (plugins,
  custom operators, compile cache) were handed to 4.4 as system level; they are not in the THR-3 Jira list,
  so the task's boundary section names them as system level and points back to 4.2 rather than adding a
  fourteenth threat. Dan to rule.
- **To THR-1 (4.1):** the framework column of Table 3 (OWASP 2025, MITRE ATLAS) is given with its
  verification date; THR-1 owns the alignment and may replace it.
- **To THR-4 (blocked by this item):** Table 3 and Table 4.
- **To ADV-2 (2.3 and Appendix A):** the thirteen register rows; the disposition column is ADV-2's to fill.
- **To 4.5:** the "applies to" column of Table 3 keys on LAND-1's Table 4; re-read it when Table 4 is frozen.
- **To 4.6:** orchestration ratings are not in the THR-3 Jira and are not drafted here (user, 16 Nov).
- **Serving-side routes from 4.2 T8** (plugins, custom operators, compile cache): one paragraph in the
  boundary part as system level, pointing back to 4.2; not a threat of THR-3 (user to confirm).
- **Demonstration set (Appendix B, 7.x):** Ob2-4, Amnesia and Nudge bear on T11 directly, T12 and T14 as a
  parent-against-derivative comparison, T17 as the white-box counterpart. CORRECTION 16 Nov: SABRE on dev also
  has a white-box backdoor family, `sabre/src/attacks/whitebox/backdoor/` (since 2026-10-13/21): TriggerSearch
  (GCG-style search against the base), VocabTriggerSweep (base-free), PICCOLO trigger inversion for classifiers,
  DefectionProbeBimodality (trigger-agnostic direction), SelfDisclosedTriggers, payload and target inversion,
  and quantised-variant checks (QuantBehaviorDeltaMatrix, QuantNoiseSensitivity). These bear on T9 and T10
  (trigger search), T13 (quantised variants against full precision) and T11 (fine-tune against base).
  Thresholds are marked uncalibrated in the code; no result to quote until a validated run. Still none on T15,
  T16, T18 to T21. Not cited in the task.
- **Literature to add to T10 (verify first):** PICCOLO, Liu et al., IEEE S&P 2022, trigger inversion for NLP
  classifiers (the SABRE check's source); the Trojan Detection Challenge results; these support "a search can
  find a trigger" beside TH-12's "detectors are fragile".
- **To 9.2:** the assessment gaps named in Parts 2 and 3 (no detector for an unknown trigger; quantisation
  behaviour not inherited from the parent's assessment; membership inference unreliable on generative models).

## Glossary additions needed (SCRUM-281 first, then this task)

The task uses these terms, which the governing glossary does not yet hold: backdoor and trigger, prompt
injection (direct, indirect), jailbreak, model extraction, training-data extraction, membership inference,
agent and tool use. Each is defined at first use in the task; per the style guide they must be added to the
glossary before assembly.

## Notation, aligned with the repository

| Symbol | Meaning | Taken from |
|---|---|---|
| T9 to T21 | the thirteen threats | continues T1 to T8 of `process/huggingface/hub-supply-chain-threats.md` |
| S1 to S4, Qn.k, en.k, H | stage, question, evidence item, access line | ASM-1, `process/scrum-284/stage-tables.md`, Notation |
| F1 to F4 | test families: static, dynamic, behavioural, provenance | ASM-1 |
| in possession, by proxy | access state | glossary (SCRUM-281) section 1.1 |
| model level, system level | the threat's level | glossary section 1.4, threat row |
| established, emerging, forecast | confidence label | glossary section 2.3 |
| Official, Research | source class | glossary section 2.2 |
| row and column labels of "applies to" | model type x artefact format, plus file kinds | LAND-1, `process/scrum-280/scrum280.md` Table 4 and Table 6 |
| (SCRUM-281) after a term | glossary term, first use per part | the 4.2 task's convention |
| TH-nn | this item's source rows | new prefix; earlier prefixes (HF, SC, TX, LC, SV, EC) resolve to their logs |
| observed in deployment, demonstrated in research, theoretical | demonstration status | new in this item, defined in Part 1; proposed for the glossary |

Register columns (Table 3) extend the 4.2 Table 6 header in its order: Threat | Family | Enters at (stage, question) | Level | Organisation exposed | Applies to | Status | Label | Framework | Sources | Disposition (ADV-2, empty).

## Files

- `scrum288.md`: the task.
- `subtask_1.md` to `subtask_5.md`: Jira subtask texts, in the Jira's words.
- `README.md`: this strategy.
