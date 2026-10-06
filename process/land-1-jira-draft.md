# LAND-1 draft description (v1, 2026-10-06)

Proposed replacement text for the Jira item "Map repositories, hosting platforms and the model
taxonomy". Changes against the current description are listed at the end with their justification.

---

## Description

Two things the rest of the report depends on. First, where open-source models actually live and move:
Hugging Face, Kaggle, ModelScope, Ollama/GGUF, GitHub releases, cloud model gardens - governance,
platform-side controls, guaranteed metadata, distribution mechanism. Second, the working segmentation:
model types (quantised, classification, generative, embedding, multimodal, adapters) crossed with
artefact formats (pickle, safetensors, GGUF, ONNX).

Where it lands in the report: section 3.1 (repositories and hosting platforms) and section 3.2 (model
types, tasks and artefact formats). The remaining sections of Chapter 3 - 3.3 release trends, 3.4
licensing and provenance, 3.5 ecosystem outlook - are the rest of deliverable 1a and are tracked
separately; this item does not close them.

Research state: the desk research for both outputs is complete as of the research cut-off 2026-10-06,
in `sabre/docs/landscape-platform-comparison.md`. It holds the filled platform comparison table, a
four-provider breakdown of the cloud gardens, per-cell evidence for every taxonomy cell with Hugging
Face Hub counts, and the source log in Appendix E format (about 120 entries, classes S1 and S4). What
remains is the agreement with Dan, the prose, and the corrections to the documents the research
contradicted.

Downstream: the threat x model-type matrix (4.5), the threat-to-control coverage matrix (5.3) and the
acceptance criteria per test family and trust tier (7.5) use the taxonomy's row and column labels
verbatim. Section 6.2 (publicly attestable properties) and section 4.2 (supply-chain and artefact-level
threats) cite this item's platform table rather than re-researching the platforms.

Open dependency: INCD's first question for the engagement - whether "open-source AI model" covers
classification and embedding models or language models only - changes which taxonomy rows survive. The
table is therefore structured as core rows (generative, instruct and base) plus extended rows, so a
narrower answer is a row subset rather than a rebuild.

## ACCEPTANCE CRITERIA

1. Drafted subsection 3.1 with the platform comparison table, every claim carrying a dated source that
   resolves in the report's single source log (Appendix E). A cell with no source reads "not
   established" and is never inferred from another platform.
2. Drafted subsection 3.2 with the taxonomy table, agreed with Dan as the single segmentation used
   consistently across Parts I-IV, carrying a version number and a freeze date.
3. The agreement with Dan covers four points, each recorded in the item: the rule distinguishing common
   from possible-but-uncommon from not-applicable; whether the container/image column is an artefact
   format or a packaging layer described in 3.1; whether the generative-base row may inherit its values
   from the generative-instruct row; and whether the pickle column carries a "legacy, falling" marker.
4. Row and column labels published to LAND-2, THR-2 and THR-3, with a note on how "not established"
   is to be rendered in a downstream matrix cell.
5. The research cut-off date stated in section 2.4.

## SEQUENCING

Wave 1. Startable now - no outstanding predecessors. Blocks LAND-2, THR-2, THR-3. Criterion 2 must be
met before S2, since every later matrix keys off the taxonomy.

## EFFORT SPLIT

Natan 1.5d planned. Desk research complete (2026-10-06); approximately 0.5d remains, distributed across
the subtasks below. The assignee is accountable for the item; the split is how capacity was planned.

## Subtasks

| # | Subtask | Output | Est. |
|---|---|---|---|
| 1 | Taxonomy session with Dan | the four decisions in AC-3 recorded; table frozen at v1.0 with its date | 1.5h incl. prep |
| 2 | Apply the accepted corrections to the foundation paper, the ecosystems document and the style guide | eleven sourced corrections, decided one by one | 1h |
| 3 | Draft section 3.1 | about two pages: platforms in the in-possession / by-proxy frame, the comparison table, what the controls do not do, gardens as redistributors. Folds today's table into the existing ecosystems text rather than drafting from scratch | 2h |
| 4 | Draft section 3.2 | about 1.5 pages: the two axes, the reading rules, the frozen table, and the format risk notes that Chapter 4 picks up (pickle executes on load; a multimodal GGUF is a pair of files; an adapter is not runnable alone) | 1.5h |
| 5 | Merge the source log into the report's Appendix E; write the 2.4 cut-off sentence | one log, one cut-off | 0.5h |
| 6 | Hand-off note to LAND-2, THR-2, THR-3 | frozen labels plus the "not established" convention | 0.5h |

---

## Changes against the current description, with justification

| # | Change | Justification |
|---|---|---|
| 1 | Named the target sections 3.1 and 3.2 | the current text says what to produce but not where it goes; the skeleton has five sections in Chapter 3 and the item covers two |
| 2 | Stated that 3.3, 3.4 and 3.5 are out of scope and tracked separately | the acceptance criteria name only the platform table and the taxonomy, so the item as written cannot close deliverable 1a; saying so prevents a silent scope gap |
| 3 | Recorded the research as complete with its cut-off and artefact | the work exists; leaving the item worded as if nothing had been done would mis-state the remaining effort |
| 4 | Expanded "agreed with Dan" into four named decisions | without a written rule for the cell values, six cells of the taxonomy are arguable, and an agreement that does not fix the rule will not hold through Parts I-IV |
| 5 | Added the core-rows / extended-rows structure and the INCD scope dependency | INCD's own open question decides whether two of the seven rows survive; structuring for it now avoids a rebuild after S2 |
| 6 | Named the downstream consumers, including 6.2 and 4.2 | the item already says it blocks three others; 6.2 and 4.2 are answered largely by this table, and saying so stops the platforms being researched twice |
| 7 | Added the "not established" convention to the acceptance criteria and the hand-off | it is the rule that keeps an unsourced cell from becoming an inferred claim in a downstream matrix |
