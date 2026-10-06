# INCD report

Working repository for the INCD engagement: **"Securing Open-Source AI Models: Threat Landscape,
Assessment Methodology and Acceptance Criteria."**

This repository holds the report and the process around it. It is deliberately separate from the
LuminAI product code: the code lives in the `luminai` repository and its pull requests, and nothing
here belongs there.

## What is in here

| Folder | Holds | State |
|---|---|---|
| `skeleton/` | the INCD table of contents, v0.2 of 12 September 2026. The target structure; the oracle for where everything goes | reference, not ours to edit |
| `governing/` | the style guide: glossary, citation policy and source-quality bar, figure and table style, the English QA passes | agreed; to be posted to the shared workspace |
| `foundation/` | the theory. The six-tests foundation paper, its two earlier editions, the content-organization master, and the open-weight ecosystems document | content agreed |
| `landscape/` | the sourced landscape research: platform comparison, producers, taxonomy evidence, source log | research complete at cut-off 2026-10-06 |
| `report-sections/` | drafted sections of the report itself, named by their skeleton number | 3.1 drafted |
| `process/` | Jira item drafts and decision sheets | LAND-1 drafted |
| `lay-package/` | the customer-facing explainer, cards, map, concept notes and writing brief | done |

## Map to the skeleton

Where the material answers a section of the report, and where it does not yet.

| Skeleton section | Covered by | State |
|---|---|---|
| 2.1 Scope and definitions | `foundation/open-weight-ecosystems.md`, `governing/` glossary | have |
| 2.4 Evidence standards and research cut-off | `governing/` citation policy; cut-off 2026-10-06 | have |
| 3.1 Repositories and hosting platforms | `report-sections/report-section-3-1-draft.md`, `landscape/` | drafted |
| 3.2 Model types, tasks and artefact formats | `landscape/` taxonomy evidence | awaiting the freeze |
| 3.3 Release trends and ecosystem growth | nothing | needs its own measurement |
| 3.4 Licensing and provenance in practice | `landscape/` producers table | partly; model-card completeness unmeasured |
| 3.5 Ecosystem outlook | nothing | blocked on INCD's scope question |
| 4.2 Supply-chain and artefact-level threats | `landscape/` format evidence | input only |
| 4.5 Threat x model-type matrix | the frozen taxonomy supplies both axes | blocked on the freeze |
| 5.3 Threat-to-control coverage | inherits the model-type axis from 4.5 | blocked |
| 6.2 Publicly attestable properties | `landscape/` controls and metadata columns | largely answered, undrafted |
| 7.x Testing and acceptance | `foundation/` six-tests papers | have, unmapped to 7.x |
| Appendix D Glossary | `governing/` | have |
| Appendix E Bibliography and source log | `landscape/` source log, about 120 entries | have, needs merging into one log |

## Rules this work runs under

- **Small to big.** The per-test papers are the source; the master and the foundation follow them.
  Never edit a paper to fit the master. Every change to a document carries its own justification.
- **Sources.** Every factual claim resolves to a dated source of a declared class. A claim with no
  source is marked *not established* and is never inferred from a neighbouring case.
- **Research cut-off 2026-10-06.** Sources after it are admitted only by an explicit addendum.
- **Theory text carries no results, no numbers and no file references.** Results are quoted only from
  the latest runs, and only in technical sections.
- **Door 1 is indicated, never measured, by the six tests.**

## Open decisions

1. **The taxonomy freeze.** Four questions for Dan, in `process/land-1-dan-decision-sheet.md`. Blocks
   sections 3.2, 4.5 and 5.3.
2. **Four claims in the ecosystems document** are contradicted by the sourced research: ModelScope
   described as a mirror, GitHub Models listed as live when it was retired on 30 July 2026, Kaggle
   credited with file hashes, and the producers table behind on Cohere and Gemma. Either the document
   is corrected or it stays frozen and `landscape/` carries the corrections.
3. **Duplication.** The foundation's section 2 and the ecosystems document are word for word the same,
   about 2,100 words. The glossaries have also drifted: the ecosystems document says *open-weight
   model*, the style guide says *open-source model*.
4. **INCD's own scope question** - whether classification and embedding models are in scope - decides
   which taxonomy rows survive, and therefore 3.5.
