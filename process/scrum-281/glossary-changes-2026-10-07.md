# Glossary and citation-policy changes, 2026-10-07 (style guide v1.1 → v1.2, §1 and §2)

Decisions behind them: the glossary holds the report's vocabulary in the Jira's and skeleton's words;
the six tests and the doors are the demonstration set's vocabulary and move out; evidence rules belong
to the citation policy; the landscape research of 2026-10-06 corrected three entries and added terms.

| # | Change | Justification |
|---|---|---|
| 1 | §1.4 "Threat model and assessment" (doors, indicated vs measured, two halves, work factor, band, Robust/Sensitive/Fragile, reconnaissance) and §1.5 "The six tests" moved to `foundation/demonstration-terms.md` | user decision: the six tests and the three doors are an experiment we ran, not fundamental vocabulary; the Jira author knows only that there is advisor code in LuminAI |
| 2 | Nine lay rows moved out of §1.3 (refusal vector, internal state, the model's "no", a push inside, meaning direction, how big a push, whether the push grows, fluent compliance, committee of specialists) | same decision; these are the explainer words for the six tests |
| 3 | New §1.4 "Assessment vocabulary" with 19 terms taken from the skeleton's chapter and section titles (threat, threat family, model-level vs system-level, backdoor, data poisoning, control, control maturity, trust tier, lifecycle stage, attestable vs testable property, test family, black-box / white-box qualification, metric, acceptance criterion, attack-orchestration complexity, gap, demonstration set) | the chapters on threats, controls, assessment and acceptance need fixed words and the skeleton already supplies them |
| 4 | Confidence label, research cut-off and framework identifiers are not in §1 | overlap with the citation policy; definitions of evidence rules live in §2 only |
| 5 | §1.1 "mirror": ModelScope removed from the anchor; "avoid" now states that no mirroring process is documented and that its re-uploads are user uploads with their own hashes | landscape research, source log MS-04 / MS-07: a mirroring or syncing process is not established |
| 6 | §1.1 "model garden": anchors renamed to Gemini Enterprise Agent Platform (formerly Vertex AI) and Microsoft Foundry (formerly Azure AI Foundry) | both products were renamed; the old names appear only in material written before the rename |
| 7 | §1.1 new rows: producer, redistributor, in possession, by proxy | the ecosystems document and the landscape work use all four and the glossary is the document that fixes terms once |
| 8 | §1.1 new rows: inference server, compiled engine; "container image" moved here from §1.2 Axis B | serving study of 2026-10-06: an engine and a container are received in place of a weight file but are not ways of storing parameters, so they are distribution, not format |
| 9 | §1.2 "multimodal model" replaced by "modality", a qualifier on a model type | taxonomy rebuild: multimodal says what goes in, classification says what comes out; listing them as alternative rows is why vision-language models never fitted |
| 10 | §1.2 intro rewritten: rows are content, columns are file manner, qualifiers named; row set and values marked as pending the freeze with Dan | reflects the rebuilt taxonomy without pre-empting the freeze |
| 11 | §1.2 "base model" now defined as the pre-training-stage release without a trained refusal behaviour, as well as the root of derivatives | the safeguard exists only in the instruct variant; the old definition (no recorded parent) did not say so |
| 12 | §1.2 "adapter" and "quantised model" state where they sit (file kind that changes the row; qualifier on the columns) | taxonomy rebuild |
| 13 | §1.2 Axis B: pickle (extension is a convention), GGUF (multimodal is two files), ONNX (can name native code) gained the facts Chapter 4 picks up | landscape deliverable §3, sources LD-31 to LD-38 |
| 14 | §1.2 note on the Jira list rewritten to place each of the six named kinds | the six names are kept; only their place in the table changes |
| 15 | §1.3 "abliterated model" loses "the weight-surgery attack done once"; "safeguard" redefined without reference to the tests | demonstration vocabulary out of the glossary |
| 16 | §1.1 "platform-side control" and "guaranteed metadata" gained an avoid clause each (a control that only flags; a declared parent relation is not verified) | the two findings of the platform comparison that most often get misread |
| 17 | Header and §5 mapping row updated; version 1.2 | bookkeeping |
| 18 | §2.1: seven classes S1–S7 collapsed to four, A–D: standards, specifications and official publications (incl. government and regulator); research, with preprints folded in as a labelled case; vendor and platform documentation; press as the floor that never supports a claim | user decision 2026-10-07: S4–S7 were local to our project; arXiv does not deserve its own row; a government deliverable needs a short ladder |
| 19 | §2.1: own measurement and practitioner interviews removed from the ladder; admitted under the rules of the chapter that produces them | they are evidence the report produces, not external sources |
| 20 | §2.2: new rule 4 ("not established" is a value, never inferred) and rule 6 (confidence labelling: established / emerging / forecast) | the first was applied throughout the landscape work but never written; the second is asked for by the skeleton's evidence-standards and forecast sections |
| 21 | §2.2 rules 3, 5, 10 neutralised: "SABRE", "door 1" and the named paper replaced by "measured data", "the demonstration set", "a threat that was not itself run" | demonstration vocabulary out of the governing text |
| 22a | §2.1 class C renamed "own documentation" and defined by reference to §1.1, examples list removed | the list duplicated the platforms table; the row stays only for the weight it carries (self-reported) |
| 22b | §2.1 reduced to two classes: C (own documentation) merged into A as the official statement of the party about what it owns; D (press) replaced by one exclusion sentence | user: C and D are redundant; a party's own documentation is official for that party, and a class that never supports a claim is a rule, not a class |
| 22c | §2.2 rule 7 now states the cut-off date, 6 October 2026 | subtask 2 asks for the date; it was stated in the landscape documents but not in the policy |
| 22d | §2 restructured into five labelled parts (minimum standard; source classes incl. exclusions and report-produced evidence; confidence labels; research cut-off; source log and citation form), one per deliverable of SCRUM-281 subtask 2; the ten-rule list dissolved into those parts | the subtask and the section must correspond one to one so that each deliverable can be checked off against a subsection |
| 22e | §1.2 Axis B and §1.1 container image: the owner of each format's specification added to the technical-anchor cell | the owner of a specification is a fact about the format and belongs in the glossary; §2.2 class A then says only "format specifications" |
| 23 | §1.4 rewritten from 18 rows to 9: threat family, model-level vs system-level and orchestration complexity folded into threat; control maturity into control; black-box / white-box into test family; attestable and testable merged; backdoor, data poisoning and metric removed; technical-anchor column dropped | one row per thing the report talks about; the split rows were one idea each, and the anchors restated the term |
| 24 | §1.2 Axis A rewritten with Takes in / Gives out columns in plain data types; technical anchors (decoder-only, causal LM, bi-encoder, PEFT, GPTQ...) dropped | user: a reader does not know what a decoder is; input and output data types explain a model type better than any sentence |
| 25 | §1.3 from 16 rows to 9: lay doubles (compressed copy, retrained copy, stripped fork) merged into quantised, fine-tuned, abliterated; weight averaging, SLERP, TIES folded into merged model; derivative row cut to one sentence; safeguard and guard as one pair row | the report uses the skeleton's technical words; one row per thing |
| 26 | §1.1 from 18 rows to 12: model hub and mirror folded into repository; model garden and package registry into redistributor as kinds; gated model into platform-side control; container image and compiled engine into one row, received instead of a file; lead sentence dropped | one row per thing; the folded rows were kinds or details of another row |
| 22 | §2.1 mapping line S1→A, S2/S3→B, S4→C, S7→D, S5→measured, S6→interview; §6 references updated | the landscape source logs (about 150 rows) are tagged S1/S4 and are re-labelled mechanically when merged into the single log |

Not changed in this pass, pending: §4.3 QA pass 3 "door lint" (demonstration term, to move with the
doors); §6.1 taxonomy table (replaced by the frozen table after the Dan session); re-labelling the
existing source logs when they are merged.

## Removed from the governing text on 2026-10-07, kept here

- Source-log verification tags used in the landscape research: *checked* (the page states the claim), *partial* (implied, gap named), *not established* (no page states it, after the searches named).
- Framework-identifier trap: ATLAS T0018 is "Manipulate AI Model", not "Backdoor"; a backdoor trigger is T0043.004.
- Mapping of the old source classes in existing logs: S1 and S4 to Official, S2 and S3 to Research, S7 to motivating only, S5 and S6 own evidence outside the ladder.
- Measured-data log fields: demonstration set, technique, version, run identifier, date (belongs with the demonstration appendix).
