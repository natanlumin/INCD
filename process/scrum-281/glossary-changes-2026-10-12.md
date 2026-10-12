# Glossary changes, 2026-10-12 (style guide v1.2 → v1.3, §1)

Decision behind them: the lifecycle assessment framework (SCRUM-284) needed two terms that every later
section touching by-proxy assessment, method coverage and acceptance criteria will also need. A term used
outside one item is not that item's local notation; it is added here first, per the glossary's own rule.
User decision of 12 October 2026.

| # | Change | Justification |
|---|---|---|
| 1 | §1.1 new row: serving provider, the platform or redistributor that runs the copy of a model a key opens and returns its outputs; answers for the endpoint, never for the model; a producer serving its own API holds both roles | the glossary had producer for the model's maker and used "provider" only loosely for the serving side; the framework's who-answers column needs the two parties named apart, and "provider" alone was being read as the model's maker |
| 2 | §1.1 "by proxy": "a provider's copy" now reads "a serving provider's copy"; avoid clause likewise | consistency with change 1 |
| 3 | §1.4 new row: outputs and internals, the two things a testable property can be measured on; outputs black-box through a file or a key, internals white-box and needing the file | the attestable and testable row defined testable as one thing; the access line of the framework splits it, and the split decides which test families survive by proxy |
| 4 | Header: version 1.3, change note | bookkeeping |

Applied to `governing/report-style-guide-and-glossary.md` and to `scrum281.md` here. The copy in the
shared workspace package (`sabre/docs/`) is not yet updated.
