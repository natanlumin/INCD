# 3.1 Repositories and hosting platforms

Draft for section 3.1 of the INCD report, per the skeleton: "the main repositories and distribution
channels, and what security controls each applies itself." Source identifiers in brackets resolve in
the source log; the full evidence, including the four-provider breakdown of the cloud gardens, is in
`landscape-platform-comparison.md`. Research cut-off 2026-10-06. Version 1, draft.

---

An open model is not a product bought from one vendor. It is a file that moves through an ecosystem of
publishers, repositories, redistributors, runtimes and hosted providers, changing hands and sometimes
changing form at each step. This section describes where the file lives, how it reaches an
organisation, and what each platform along the way does to it.

One distinction frames the whole chapter, and it is the one most often lost when an organisation says
it uses open models. **An open model in possession** means the organisation holds the file and runs it
on accelerators it pays for, choosing and operating the serving software. **An open model by proxy**
means the organisation holds an API key to a provider's copy of the same file: it sends requests,
receives answers, and never touches the file or the software that serves it. The licence is identical
in both cases. What differs is possession, and with it what the organisation can inspect, what it is
accountable for, and which of the risks in Chapter 4 are its own. The distinction recurs in section 7.4,
where it decides which tests an organisation is able to run at all.

The distinction cuts across platforms rather than between them, and it is not always visible from the
name. Hugging Face hosts files and also sells a hosted API over those same files [HF-18]. NVIDIA
publishes containers an organisation can pull and run, and hosts endpoints serving the same models
[CG-13]. The cloud gardens do both, depending on which deployment option the customer picks [CG-01,
CG-04, CG-08]. The useful question is never "is this platform open" but "does this platform hand me a
file or a key".

## The repositories

Published models live in a small number of repositories that host the files, their metadata and their
revision history. The Hugging Face Hub is the largest and functions as the default address of the
ecosystem; Kaggle Models and ModelScope hold most of the rest, with plain GitHub releases and the
package registries for the remainder.

A repository entry contains the files themselves, a commit history, a model card written by the
publisher, a licence field, and, where the publisher declares it, the relation to a parent model. The
declared relations - fine-tune, adapter, merge, quantisation - link entries into a tree, so that a
popular base model may have thousands of descendants. Three properties of that tree matter for the rest
of the report. The relation is declared by the publisher and not verified by the repository: no
platform examined states that it checks whether a file said to derive from a given parent actually does
[HF-14, KG-05, MS-04]. Many publishers do not declare it at all, since no repository requires it
[HF-15]. And a derivative is a different model from its parent, so a verdict on the parent does not
carry to the child.

Repositories do apply controls of their own, and they differ more than their similar appearance
suggests. The Hugging Face Hub scans every file at every commit with an antivirus engine, extracts and
displays the import list of every pickle file, and adds two third-party scanners across all public
repositories [HF-05, HF-06, HF-07, HF-08]. It offers conversion of pickled weights into a safe
container format through a service that opens a pull request the repository owner must merge [HF-10],
and it supports optional signed commits, which establish origin rather than safety [HF-06, HF-11].
Kaggle and ModelScope document no scanning, signing or conversion of model files at all; Kaggle's
acceptable-use policy prohibits distributing malicious files but describes no mechanism, and
ModelScope's international terms state expressly that user content is not verified or approved
[KG-04, KG-02, MS-02, MS-05]. The Ollama library verifies each layer's digest on download but documents
no review of what is pushed [OL-03, OL-09]. GitHub computes a digest for every release asset and offers
opt-in immutable releases with a signed attestation over the tag, commit and asset digests, but
documents no malware scanning of the assets themselves [GH-05, GH-06, GH-10].

Two of these platforms warrant a note. ModelScope is commonly described as a mirror of the Hugging Face
Hub; its own documentation describes no mirroring or syncing process, and the organisation that holds
most of the re-uploaded models publishes them as ordinary user uploads, with ModelScope's own hashes
[MS-04, MS-07]. Provenance must therefore be re-established rather than assumed to carry across. And
GitHub Models, the catalogue of hosted endpoints that sat beside GitHub releases, was fully retired on
30 July 2026 [GH-11]; it appears here only because material written before that date refers to it.

## Distribution channels beyond the repositories

Between the repository and the organisation that runs a model sit redistributors, which repackage a
published model for a particular way of running it. They fall into five kinds, and each changes what
the organisation receives.

**Cloud model gardens.** The major providers curate catalogues that deploy into a customer's account in
a few clicks: Google's Model Garden, Amazon Bedrock with its marketplace and SageMaker JumpStart, the
Microsoft Foundry catalogue, and NVIDIA's NGC. The provider selects what to list, often optimises or
quantises the model, and hosts the copy the customer deploys [CG-01, CG-03, CG-07, CG-09, CG-13]. None
of the four offers a community publishing path. Their platform-side controls differ more than any other
group examined, which is why section 3.1 of the appendix table breaks them out: at one end, no
pre-listing scanning of marketplace or catalogue models is documented at all [CG-04, CG-06]; at the
other, container images and model files are both signed, with a software bill of materials and
vulnerability-exchange documents retrievable by image digest [CG-11].

**Packaged inference microservices.** NVIDIA's NIM distributes models as containers bundling the file,
an optimised runtime and a serving API. The same model is available as a container to pull or as a
hosted endpoint to call, which places one product on both sides of the possession line [CG-13].

**Local runtimes with their own libraries.** Ollama and the wider llama.cpp family distribute models in
the GGUF format, usually quantised, through libraries of their own and run them on a workstation or a
single server [OL-01, OL-06]. They are the entry point for most individual and small-team use, and the
only channel in this section where the default artefact is a compressed derivative rather than the
publisher's original.

**Deployment and orchestration platforms.** Platforms that manage fleets of accelerators and the
deployment of serving workloads onto them. The organisation chooses the model and the serving stack;
the platform provisions and operates the infrastructure.

**Hosted inference providers.** Services that serve open models behind a pay-per-token API. The
organisation sends requests and receives answers exactly as it would with a closed commercial model,
and never handles the file.

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
