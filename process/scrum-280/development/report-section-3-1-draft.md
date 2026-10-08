# 3.1 Repositories and hosting platforms

Draft for section 3.1 of the INCD report, per the skeleton: "the main repositories and distribution
channels, and what security controls each applies itself." Source identifiers in brackets resolve in
the source log; the full evidence, including the four-provider breakdown of the cloud gardens, is in
`landscape-platform-comparison.md`. Research cut-off 2026-10-06. Version 1, draft.

---

This section answers three questions about an open model before any threat is discussed: where its
file is published, which is the subject of 1.1; through which channels it reaches an organisation and in
what form, which is 1.2; and what each platform does to the file on the way, which Table 1 to Table 3
record and the last subsection interprets. Four properties are recorded for every platform, and they are the
columns of all three: governance, platform-side controls, guaranteed metadata, and distribution mechanism.

**Notation.** Terms fixed in the report's glossary are used as defined there and are not redefined here;
in this section they are producer, model repository, redistributor, platform-side control, guaranteed
metadata, distribution mechanism, inference server, in possession and by proxy. A bracketed identifier
such as [HF-18] names a row of the source log in section 3, and every factual statement carries one. A
cell or sentence that reads *not established* means that no page published by the platform states the
property; it is never inferred from another platform.

## The repositories

Published models live in three model repositories: the Hugging Face Hub, Kaggle Models and ModelScope. A producer that
attaches its file to a GitHub release is using a package registry, which 1.2 covers.

An entry holds the files, a commit history, a model card, a licence field and, where the producer
declares it, the relation to a parent model: fine-tune, adapter, merge or quantisation. Three facts
about that relation carry through the report. It is declared by the producer and verified by no
repository examined [HF-14, KG-05, MS-04]. Many producers do not declare it, since no repository
requires it [HF-15]. And a derivative is a different model from its parent, so a verdict on the parent
does not carry to the child.

Table 1 records the four properties for each of the three. The guaranteed metadata column lists only the fields
the platform enforces or verifies; a field the publisher fills in freely is marked not guaranteed.

[Table 1: the four model repositories; columns kind and what it hands you, governance, platform-side controls, guaranteed metadata, distribution mechanism; from the SCRUM-280 deliverable]

## Distribution channels beyond the repositories

Between the repository and the organisation that runs a model sit redistributors, which repackage a
published model for a particular way of running it. What they hand over is either a file or a key: the
organisation then holds the model in possession, running it on an inference server it operates, or by
proxy, calling a provider's copy through an API. The licence is the same in both cases; what differs is
what the organisation can inspect, what it is accountable for and which tests it can run at all. The
line runs through platforms, not between them: Hugging Face hands out files and sells an API over them
[HF-18], NVIDIA ships containers and hosts endpoints for the same models [CG-13], and the cloud gardens
do both [CG-01, CG-04, CG-08].

Table 2 records the same four properties for the redistributors, one row per kind the glossary names,
and Table 3 opens the cloud-garden row into its four providers, whose controls differ more than any
other group's. Together AI stands for the hosted inference providers; Fireworks, Groq and OpenRouter,
named beside it in the foundation document, were not examined.

[Table 2: the six redistributors, columns as Table 1; from the SCRUM-280 deliverable]

[Table 3: the four cloud model gardens, columns as Table 1; from the SCRUM-280 deliverable]



## What the platform controls establish, and what they do not

Three findings follow from Table 1 to Table 3.

**The controls act on the file, not on the model's behaviour.** Malware scanning compares each file
with signatures of known malicious files; pickle scanning reads the instruction stream of a pickle
checkpoint without loading it and lists the imports it would make, since loading a pickle can execute
code [HF-05, HF-06]. Conversion changes the container the numbers sit in [HF-10, CG-13], and signing
establishes who published a file and that it has not changed since [HF-11, GH-06, CG-12]. No platform
examined claims more, and one states the limit: a supported model has been tested for deployability, with no guarantee of the
absence of vulnerabilities or malicious code [CG-01].

**Almost every control is advisory.** The malware and pickle scanning in Table 1, ClamAV and the pickle
import scan on the Hugging Face Hub with the Protect AI and JFrog scans beside them, produces warnings and
badges, and a flagged file remains downloadable [HF-05, HF-06, HF-07, HF-08]. The blocking controls all
sit at the redistribution layer, in Table 2 and Table 3: Google's Model Garden blocks deployment of models
the Hugging Face scans marked unsafe [CG-01]; the newer Microsoft Foundry path runs its own mandatory
malware scan, refuses models requiring remote code execution and enforces safetensors only [CG-09]; and
AWS custom import and Together AI custom upload accept safetensors only [CG-07, TA-04]. Each applies to
the copy that platform serves, not to the file where it was published. Three platforms lean on the Hub's
hygiene rather than their own: Kaggle surfaces Hub repositories as links [LD-13], Microsoft Foundry hosts
a Hub collection [LD-27], and Google decides on the Hub's scan verdicts [LD-28, CG-01], so a weakness
there is not contained to the Hub.

**Provenance is declared, not verified.** Every repository records a licence field and, where the
producer supplies it, a parent-model relation; none verifies either [HF-14, KG-05, MS-04]. No
redistributor in Table 2 adds what the repository lacks: the Ollama library carries the licence as
optional free text and the parent as a comment [OL-05], GitHub releases and Docker Hub have no
model-specific field [GH-10, DK-01], and Together AI states nothing [TA-02, TA-03]. Digests and
signatures establish that a file has not changed since publication, not that it is what its model card
claims.

