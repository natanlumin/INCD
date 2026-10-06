# Where open models live and move, and what they are

**LAND-1 deliverable.** Covers the two halves of the Jira item: where open-source models actually live
and move, with each platform's governance, platform-side controls, guaranteed metadata and
distribution mechanism; and the working segmentation of model types against artefact formats.

Research cut-off and access date 2026-10-06. Source identifiers resolve in the log at the end and in
`../landscape/landscape-platform-comparison.md`. Draft 1.

---

## 1. Why the same four questions do not fit every platform

A platform comparison that asks the same questions of every row produces a table full of cells that
are true but pointless. Before the comparison, it is worth saying which questions each platform can
even answer, because the differences are not small.

The first question is what the platform hands over. A platform that hands over a file can be asked
what formats it carries, what kinds of model, and what those models do. A platform that hands over an
API key cannot: the organisation never sees a file, so the file's format is not a property of
anything it holds. The second question is how much choice the platform leaves. A repository that
accepts any upload in any format has a wide and genuinely informative format profile. A package
registry built around one format has a format profile of one line, and asking about it tells the
reader nothing they could not infer from the name.

This is why the dimensions below are applied selectively, and why a cell may read *not applicable*
with a reason rather than being filled for symmetry.

| Platform | What it hands over | Is the format question informative? | Are modality, type and task informative? |
|---|---|---|---|
| Hugging Face Hub | files | Yes. The widest format range of any platform here, and the only one where the choice of format is routinely the publisher's | Yes. The broadest coverage, and the only platform with a published task taxonomy |
| Kaggle Models | files | Yes, but narrower, and framework rather than format is the enumerated field | Partly |
| ModelScope | files | Yes | Yes |
| Ollama library | files, one format | No. The library is built around a single quantised format, so the answer is one line and carries no information | Partly. The set is narrow and shaped by what the runtime can execute |
| GitHub releases | files, any content | No. There is no model convention at all, so the format is whatever the publisher attached | No |
| Cloud model gardens | a deployment into the customer's account, or a provider-hosted endpoint | Partly. The provider selects and often converts, so the format reflects the provider's choice rather than the publisher's | Yes, but the catalogue is curated, so coverage describes the provider's selection |
| Hosted inference providers | an API key | No. No file is received | Partly. Only what the provider has chosen to offer, and only as a menu |

Two rows deserve the emphasis. **Ollama is the clearest case of a dimension collapsing**: the format
question has one answer, and the interesting question in its place is what the runtime can execute at
all. **The hosted providers are the clearest case of a dimension disappearing**: with no file, format
is not merely uninformative but meaningless, and the organisation's exposure shifts entirely to what
the provider discloses, which section 5 of the ecosystems document shows is usually nothing.

## 2. The platforms

<!-- PLATFORM PROFILES -->

## 3. Artefact formats

<!-- FORMATS -->

## 4. The segmentation

<!-- TAXONOMY -->

## 5. Source log

<!-- LOG -->
