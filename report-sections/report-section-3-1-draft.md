# 3.1 Repositories and hosting platforms

Draft for section 3.1 of the INCD report, per the skeleton: "the main repositories and distribution
channels, and what security controls each applies itself." Source identifiers in brackets resolve in
the source log; the full evidence, including the four-provider breakdown of the cloud gardens, is in
`landscape-platform-comparison.md`. Research cut-off 2026-10-06. Version 1, draft.

---

This section answers three questions about an open model before any threat is discussed: where its
file is published, which is the subject of 1.1; through which channels it reaches an organisation and in
what form, which is 1.2; and what each platform does to the file on the way, which Table 1 and Table 2
record in 1.3 and 1.4 interprets. Four properties are recorded for every platform, and they are the
columns of Table 1: governance, platform-side controls, guaranteed metadata, and distribution mechanism.

**Notation.** Terms fixed in the report's glossary are used as defined there and are not redefined here;
in this section they are producer, model repository, redistributor, platform-side control, guaranteed
metadata, distribution mechanism, inference server, in possession and by proxy. A bracketed identifier
such as [HF-18] names a row of the source log in section 3, and every factual statement carries one. A
cell or sentence that reads *not established* means that no page published by the platform states the
property; it is never inferred from another platform.

## The repositories

Published models live in a small number of model repositories that host the files, their metadata and
their revision history: the Hugging Face Hub, the largest and the ecosystem's default address; Kaggle
Models and ModelScope for most of the rest; plain GitHub releases and the package registries for the
remainder.

An entry holds the files, a commit history, a model card, a licence field and, where the producer
declares it, the relation to a parent model. The declared relations, fine-tune, adapter, merge and
quantisation, link entries into a tree in which a popular base model may have thousands of descendants.
Three properties of that tree carry through the report. The relation is declared by the producer and
verified by no repository examined [HF-14, KG-05, MS-04]. Many producers do not declare it, since no
repository requires it [HF-15]. And a derivative is a different model from its parent, so a verdict on
the parent does not carry to the child.

What each repository does to the files it hosts is in Table 1, and the range is wide. The Hugging Face
Hub scans every file at every commit and extracts the imports of every pickle file [HF-05, HF-06].
Kaggle and ModelScope document no scanning, signing or conversion at all [KG-04, MS-02, MS-05]. The
Ollama library and GitHub verify digests but document no review of content [OL-03, OL-09, GH-05, GH-10].

Two cautions. ModelScope documents no mirroring of the Hugging Face Hub; its re-uploads are ordinary
user uploads carrying ModelScope's own hashes, so provenance must be re-established rather than assumed
to carry across [MS-04, MS-07]. GitHub Models, the hosted catalogue beside GitHub releases, was retired
on 30 July 2026 [GH-11] and appears here only because earlier material refers to it.

## Distribution channels beyond the repositories

Between the repository and the organisation that runs a model sit redistributors, which repackage a
published model for a particular way of running it. What they hand over is either a file or a key: the
organisation then holds the model in possession, running it on an inference server it operates, or by
proxy, calling a provider's copy through an API. The licence is the same in both cases. What differs is
what the organisation can inspect, what it is accountable for, which of the risks in Chapter 4 are its
own and, in section 7.4, which tests it can run at all. The line runs through platforms, not between
them: Hugging Face hands out files and sells an API over them [HF-18], NVIDIA ships containers and hosts
endpoints for the same models [CG-13], and the cloud gardens do both [CG-01, CG-04, CG-08].

Five kinds of redistributor, each placed in Table 1 by what it hands over:

- **Cloud model gardens.** Google's Model Garden, Amazon Bedrock with SageMaker JumpStart, Microsoft
  Foundry and NVIDIA's NGC: provider-curated catalogues with no community publishing path, deploying a
  copy the provider often optimises or quantises [CG-01, CG-03, CG-07, CG-09, CG-13]. Their controls
  differ more than any other group's, which is why Table 2 breaks them out.
- **Packaged inference microservices.** NVIDIA's NIM: the model, an inference server and a serving API
  in one container, available to pull or to call [CG-13].
- **Local inference servers with their own libraries.** Ollama and the llama.cpp family, distributing
  quantised GGUF files for a workstation or a single server [OL-01, OL-06]; the one channel whose default
  artefact is a derivative rather than the producer's original.
- **Deployment and orchestration platforms.** Manage the accelerators and the serving workloads; the
  organisation chooses the model and the serving stack.
- **Hosted inference providers.** Open models behind a pay-per-token API; the organisation never handles
  the file.

## The comparison

The table below summarises the platforms on the four dimensions the report uses throughout: governance,
the controls the platform applies itself, the metadata it guarantees, and the mechanism by which the
file reaches the organisation. Every cell resolves to a dated source in the log. A cell that reads *not
established* means that no page published by the platform states the property; it is left as such and
is never inferred from another platform, because the platforms differ precisely where an inference
would be convenient.

[Table: condensed platform comparison - one row per platform, columns: kind and what it hands you;
governance; platform-side controls; guaranteed metadata; distribution mechanism. Full version with
source identifiers per cell, and the four-provider cloud-garden breakdown, in Appendix A.]

## What the platform controls establish, and what they do not

Three findings follow from the comparison, and each one shapes a later chapter.

**The controls act on the file as an artefact, not on the model as a behaviour.** Scanning looks for
executable content and known malware signatures; conversion changes the container the numbers sit in;
signing establishes who published a file and that it has not changed since. None of these examines what
the model does when it runs. No platform examined claims otherwise, and one states the limit explicitly,
noting that a model designated as supported has been tested for deployability but carries no guarantee
of the absence of vulnerabilities or malicious code [CG-01]. This is the boundary that section 6.3
builds on: the properties discoverable only by testing are precisely those the platform layer cannot
reach.

**Almost every control is advisory.** The scanners described in this section produce badges, warnings
and reports; a flagged file generally remains downloadable. Two documented exceptions exist, both at
the redistribution layer rather than the repository layer: Google's Model Garden blocks deployment of
models that the upstream repository's scanners deem unsafe, while flagging rather than blocking those
it deems suspicious or capable of executing remote code [CG-01]; and the newer Microsoft Foundry path
refuses models requiring remote code execution and enforces a safetensors-only rule on the collection
it manages [CG-09]. The practical consequence for Chapter 5 is that a control inventory built on
platform scanning inherits an advisory posture by default, and an organisation that wants a blocking
posture must impose it itself.

**Provenance is declared, not verified.** Every repository examined records a licence field and, where
the publisher supplies it, a parent-model relation; none verifies either [HF-14, KG-05, MS-04]. The
digests and signatures that do exist establish that a file has not changed since it was published; they
say nothing about whether the published file is what its model card claims. This is the gap that
Chapter 6 divides into publicly attestable properties and properties discoverable only by testing, and
it is the reason the acceptance criteria in Chapter 7 cannot rest on repository metadata alone.
