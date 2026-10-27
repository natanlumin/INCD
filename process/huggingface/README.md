# Supply-chain and artefact-level threats: strategy

Item folder for the skeleton's 4.2. No Jira identifier yet; rename the folder and the task file to the
SCRUM number when the item is created (`scrumNNN.md`, PDF `~/Downloads/scrumNNN.pdf`). Per the item
convention, this README is the strategy and `hub-supply-chain-threats.md` is the task; the PDF is built from the
task only.

## What the item asks (as the skeleton states it)

4.2 Supply-chain and artefact-level threats: malicious serialisation, format exploits, repository
typosquatting, tampered weights and malicious adapters. Each threat carries its family, its level (model or
system), its orchestration complexity (access, skill, cost, detectability) and a confidence label. The
request that opened the folder adds two things the skeleton line does not name: third-party software that is
installed or executed while a model is loaded, and the security of the repositories themselves as a
dependency. Both are in the task as T7 and section 1.5.

## Plan

| # | Subtask | Hours | State |
|---|---|---|---|
| 1 | Reuse: pull every supply-chain fact already sourced in SCRUM-280 (platform controls, formats), the landscape serving document (loaders, engines, plugins, cache), SCRUM-284 (Q1.1 to Q1.3, e1.4 to e1.6) and SCRUM-286 (provenance fractions) | 2 | done |
| 2 | New sources: maintainer advisories for the loader defects (PyTorch, transformers, vLLM, llama.cpp, llama-cpp-python, picklescan), the Hub's account and token pages, the research on malicious models, typosquatting and naming | 3 | done, 27 rows |
| 3 | Draft: path table, seven threats, repository-controls table, threat table, orchestration table, controls table, hand-on to 4.3, 4.4, 4.5, 5.1, 6.1, 9.2 | 4 | done |
| 4 | Glossary lint and source lint against the style guide | 1 | done |
| 5 | Reviews: Dan on the threat ratings and the 4.4 boundary; Lior on the advisory reading | 1 | pending |

## Decisions taken in drafting

- **Threats, not risks.** The glossary reserves threat for an attack vector and forbids "risk" and
  "vulnerability" for it. The task says threat throughout; "published defect" is used for a CVE record,
  and the acronym is expanded once.
- **Seven threats, not five.** The skeleton's five are T1 to T6 (tampered weights became T6 tampering after
  publication, because the documented routes are the account, the revision and the copy, not the numbers).
  T7 (software installed or executed during loading) and section 1.5 (the repositories as a dependency) are
  the additions the request asked for.
- **The 4.4 boundary.** Plugins, custom operators and the compile cache are described here because the
  request asked for everything installed during loading, and are marked as 4.4's under the skeleton. The
  assembly editor cuts or cross-references.
- **Orchestration ratings carry the forecast label.** They are the authors' judgement; no source rates them.
- **Only advisories and research are cited for incidents.** Press coverage of malicious models and scanner
  bypasses is plentiful and excluded; the maintainer's own advisory is cited instead in every case.
- **One claim is held at "not established" on purpose**: whether a deleted Hub repository name can be taken
  by another account. The documentation states redirects on rename and nothing on deletion.

## Developer notes

- Source ids: SC-01 to SC-27 are new; everything else resolves to the earlier logs. Two SC rows post-date the
  landscape cut-off and are admitted by the addendum note in the task's section 2.
- Numbers quoted from research (91 malicious models, 44.9 per cent pickle, 1,574 squatting candidates) are the
  papers' own samples and are labelled as such; they are not ecosystem totals.
- The GGUF parser advisory cited is the 2025 one; the 2024 one the search was aimed at could not be found
  under a maintainer record and is logged as not found.
- The chapter uses Table 1 to Table 5 and no figure. A path figure (account, repository, mechanism, loader,
  with the seven threats on it) would help the lay reader and can be drawn from Table 1 at assembly.

## Restructure (26 to 27 October)

User decision: write the subsection top down and through the primary repository, the Hub, with a separate part
asking which threats transfer to other repositories, since not every repository has the same vectors. The task
file is `hub-supply-chain-threats.md`, complete on 27 October: Scope and Structure header; Hub introduction
(eight observations); Part 1 the Hub as an object (Table 1, eleven elements, guaranteed versus declared); Part 2
eight threats T1 to T8 by layer, defined once as bullets (Table 2); Part 3 eighteen Hub controls C1 to C18
(Tables 3 and 4); Part 4 transfer to Kaggle, ModelScope, Ollama, GitHub, NVIDIA and Docker Hub (Table 5); Part
5 ratings (Tables 6 and 7); Part 6 organisation-side controls (Table 8); source log SC-01 to SC-29; a closing
table of symbols from outside the document. Version 1 was superseded.

Export rules applied on the user's word: the task is export content for readers extracting security content,
so no drafting scaffolding in it (no authors, versions or dates, no skeleton hand-offs, no lifecycle mapping,
no assessment gaps, no pending-review notes; all of these live in this README); each part's introduction
stands alone with no forward references; glossary terms carry (SCRUM-281) at first use in each part; symbols
from outside the document are tabled once at the end; first table column wide and ids never split. Scope
decision (4.2 read through the primary repository) is pending Dan's agreement; Dan's five Hub-specific
judgements from version 1 carry over to Part 3 and Table 7.

## Files

- `hub-supply-chain-threats.md`: the task (the Hub-focused 4.2, Parts 1 to 6, source log, symbols table).
- Version 1 (`supply-chain-threats.md`, generic supply chain, 26 October) was superseded by the restructure and is not kept; its material is in the task and its hand-offs are below.
- `README.md`: this strategy.

## Hand-offs to the other skeleton sections (moved out of the task on 27 October)

The reader-facing Part 6 keeps the organisation-side controls (Table 8), the lifecycle mapping and the
assessment gaps. The hand-offs below are for assembly and for Dan, in skeleton numbers. T8's server-side
routes (plugins, custom operators, compile cache) are the system level of the boundary 4.4 draws, and the
skeleton places them there.

**To 4.3, model-integrity threats.** The artefact layer is the delivery mechanism for a model whose numbers
were altered; the alteration itself, and what it does, is that subsection's.

**To 4.4, inference-time and runtime threats.** T8's server-side routes, plugins, custom operators and the
compile cache, are the system level of the boundary 4.4 draws, and the skeleton places them there. The
loader's own release history, the defects in PyTorch, transformers and vLLM that T3 and T8 record, is a
dependency 4.4 should carry as its own.

**To 4.5, the segmentation.** The column mapping of Table 6: T3 keys on the pickle column, T4 on GGUF and
ONNX, T5 on the loader rather than the column, T6 on the adapter file kind, T1, T2, T7 and T8 on every cell.

**To 5.1, the control inventory.** Table 4 gave what the Hub does and what remains with the organisation.
Table 8 names the organisation-side controls that remain, what each establishes and what it does not;
maturity scoring is 5.2's.

**To 6.1 and 7.x.** The lifecycle mapping, below. **To 9.2.** The six gaps, below.

### Lifecycle mapping (moved out of the task on 27 October; for 6.1 and 7.x)

T3 to T6 are answered at Q1.3 by the static family on e1.4 and
e1.6, with the Hub's advisory scan as e1.5; T1 and T2 at Q1.1 and Q1.2 by the provenance family on e1.1 and
e1.3; T7 at Q3.4 and Q4.1 by the provenance family against the recorded revision; T8 at Q3.2 and Q3.4 by the
static family on the organisation's own deployment, and at Q4.1 thereafter. By proxy, all of them pass to
the serving provider, and the organisation holds only the provider's declaration.

### Assessment gaps (moved out of the task on 27 October; for 9.2)

Removed from the task because every row is either outside the Hub's plane or already stated in Parts 1 to 3.

Six questions have no control and no evidence that answers them today; they are assessment gaps.

- No scanner reads a compiled engine or a container's model for the payloads T3 to T5 describe.
- The Hub's scans are advisory and have been bypassed, so an unflagged file is not evidence; and their
  coverage is not fully documented: whether the third-party scans reach private repositories, and whether
  the pickle scan descends into archives, are both unstated [HF-07, HF-08, HF-06].
- The frequency of account takeover and of tampering after publication is unmeasured, on the Hub and
  everywhere else.
- The declared parent of an adapter, which decides which base it is tested with, is verified by no
  repository.
- Adoption of the optional controls, two-factor, commit signing, safetensors conversion and revision
  pinning, is unpublished, so the organisation cannot tell from a page whether a producer uses any of them.
- Availability is unassessed: no framework question today asks what the organisation sees when the
  repository it built on is renamed, transferred, made private or removed, or its owner's account is
  terminated, and the Hub's terms describe nothing for the dependent [HF-01, SC-05].


