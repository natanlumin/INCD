# What a model file is worth: six activation-space tests of the steadiness and the intrinsic safeguard of an open-source language model

---

## Abstract

An open-source language model is distributed as a file of numbers. Everything it knows and every
habit it has, including the habit of refusing harmful requests, is encoded in those numbers, and
nothing about its behaviour is signed, attested or configurable from outside. The two questions an
operator would ask of any software they did not write, whether the artefact is the real thing and
whether its protections can be switched off, therefore have no conventional answer. This paper sets
out six tests that answer them on the file itself. Three measure steadiness: how forgiving the file
is of alteration, how little directed change inside the model already changes its answer, and
whether that sensitivity is specific to the model's own meaning directions. Three measure the
quality of the intrinsic safeguard: how far the model must be pushed off its refusal before it
complies, whether the refusal still fires when its trigger is dulled, and how firmly the line
between refusal and compliance is drawn. The tests share one theoretical basis, the geometry of
refusal in activation space, and one threat model, three attack surfaces defined by access. Their
output is a work factor: the effort an attacker with access to the model needs to force compliance,
which public red-teaming cannot provide because a clean red-team pass is only a lower bound on
attacker success. We define each test, state what it does and does not measure, map it to the
OWASP, MITRE ATLAS and NIST frameworks, and give the acceptance logic that turns a band into an
operational decision.

---

## 1. Introduction

Open-source language models have moved from research artefacts to production components. An
organisation downloads a file, loads it behind a serving stack, and exposes it to users, documents
and tools. The file may be a vendor's original release, a compressed copy, a retrained variant, a
merge of several parents, or a fork whose safety behaviour was deliberately removed and which was
then published under a reassuring name. In every case the operator receives numbers they cannot
read, accompanied by a model card they cannot verify. Whether the operator receives the file at all
depends on how the model is consumed: run on the operator's own accelerators, the file and the
serving stack are theirs; consumed through a hosted API, both belong to the provider, and the
operator's exposure is of a different kind. The ecosystem that produces these situations, the
producers, repositories, redistributors, consumption modes, model classes, formats and derivatives
through which open models move, is described in Section 2.

Security practice has mature answers for software supply chains: signatures, reproducible builds,
vulnerability scanning, configuration review. None of these reach the property that matters most in
a language model, its behaviour. A hash proves the bytes are unchanged; it says nothing about whether
the behaviour those bytes produce is the behaviour the model card describes, nor whether that
behaviour survives contact with an adversary. The model's refusal of harmful requests, the property
most often advertised and most often relied upon, is not a rule stored anywhere. It is a habit
learned from examples and distributed through the numbers.

The methods available to an operator today fall into two classes, and both miss the target.
Classical cyber tools inspect containers, networks and code; they do not see the model. Red-teaming
with public jailbreak and prompt-injection sets exercises the model through its input; on an
advanced model these sets seldom succeed, and a clean result establishes only that the attacks
already known do not work today. It is a lower bound on attacker success, not a measure of the
model's protection.

This paper takes a different position. The refusal behaviour of a safety-aligned model is carried
by a small, consistent structure in the model's internal state, a direction along which harmful and
harmless requests differ. That structure can be located by anyone holding the file, with a few dozen
example requests and a published recipe, and anything that can be located can be moved. The
robustness of the safeguard is therefore a geometric property of the file, and it can be measured
directly: how far the structure must be moved before the model complies, by which lever, and how
stable the structure is under perturbation of the data used to locate it. The same geometric view
yields measurements of steadiness that do not involve refusal at all: how much random alteration the
file absorbs before its answers change, and how little directed change inside the model is amplified
into a different answer.

We present six tests built on this view. They are organised in two groups. Group 1 measures
steadiness and forgiveness: integrity, fidelity and containment. Group 2 measures the quality of the
intrinsic safeguard: the twist test, the forgetting test and the firmness test. Each test is defined
by what it perturbs, where, by how much, and what it reads out; each is placed in a threat model of
three attack surfaces defined by the access they grant; each returns a band on a fixed scale rather
than a number, so that files can be compared and acceptance decisions can be stated.

The contribution is a coherent measurement framework rather than a new attack. Several of the tests
realise attacks published in the recent literature; others are measurements for which published
attacks serve as external corroboration. What is new is the organisation: one geometric basis, one
threat model, one output vocabulary, and an explicit statement for each test of what it does not
measure. The paper is theoretical in the sense that it defines and justifies the tests; empirical
results on particular models are deliberately left out.

The remainder is organised as follows. Section 2 describes the open-model ecosystem: producers,
repositories, redistributors, the four ways an organisation consumes an open model, large and small
models, artefact formats, and derivatives. Section 3 fixes
definitions. Section 4 states the threat model. Sections 5 and 6 define the two groups of tests.
Section 7 treats mixture-of-experts models, where the shared structure must be located per expert.
Section 8 gives the band vocabulary and the acceptance logic. Section 9 maps the tests to the OWASP,
MITRE ATLAS and NIST frameworks. Section 10 states limitations. Section 11 relates the tests to the
literature.

---

## 2. The open-model ecosystem

An open language model is not a product an organisation buys from one vendor. It is a file that
moves through an ecosystem of publishers, repositories, redistributors, runtimes and hosted
providers, changing hands and sometimes changing form at each step.

One distinction frames everything in this section, and it is the one most often lost when an
organisation says "we use open models". The same open file can be consumed in two ways.

- **An open model in possession.** The organisation downloads the file and runs it on accelerators
  it pays for: GPUs it has bought for its own data centre, or, far more often, GPUs it rents by the
  hour from a cloud provider or a GPU cloud. It chooses the serving software and operates it.
  Examples: a model pulled from the Hugging Face Hub and served with vLLM on rented GPUs in AWS, GCP
  or Azure; the same file deployed through SageMaker JumpStart into the organisation's own cloud
  account; an NVIDIA NIM container run on an on-premises cluster managed with a platform such as
  Rafay; a quantised copy run on a single workstation with Ollama. In every case the organisation
  holds the file, the hardware bill and the serving stack.
- **An open model by proxy.** The organisation holds an API key to a provider's copy of the same
  file. It pays per token, sends requests, receives answers, and never touches the file or the
  software that serves it. Examples: calling an open model through Together AI, Fireworks, Groq or
  OpenRouter; using a laboratory's own hosted endpoint for its open release; using NVIDIA's hosted
  NIM endpoints instead of pulling the container. In every case the provider holds the file, the
  hardware and the serving stack, and the organisation holds a key.

The licence is identical in both cases. What differs is possession, and with it everything that
follows from possession: what the organisation can inspect, what it is accountable for, and which
of the risks described in the rest of this paper are its own. A model by proxy is open in the sense
that its file is public and the provider could be replaced; it is not open in the sense that the
organisation possesses it. From the consumer's side it is indistinguishable from a closed commercial
model: a key, a request, an answer, a bill.

The section describes the ecosystem on its own terms: who produces models, where they are
published, how they are repackaged, the four ways an organisation consumes them, which resolve into
the two sides of the distinction above, the classes of model in circulation, the formats the files
take, and the derivatives that make up most of what is downloaded.

### 2.1 Producers

Open models are produced by a small number of well-resourced laboratories and a long tail of
everyone else. The laboratories, commercial and academic, train base models from scratch and
publish them under licences that range from permissive open-source licences to bespoke "open
weights" licences with use restrictions. The long tail does not train from scratch. It takes a
published base model and produces a variant: a version retrained for a task or a language, a
version compressed to run on smaller hardware, a merge of several variants, or a version from which
the publisher's safety behaviour has been removed. The long tail publishes far more files than the
laboratories do, and most of what an organisation finds when it searches for a model is the work of
the long tail.

The table below is an example snapshot of the producer landscape. Every cell is a dated factual
claim that changes as licences and endpoints change; it is given here to show the shape of the
information an organisation needs, and the landscape chapter of a full report carries the sourced
version.

| Producer | Open releases | Licence class | In possession, commercial use | By proxy |
|---|---|---|---|---|
| Meta | Llama family | open weights under a community licence with use restrictions | yes, within the licence | third-party hosts |
| Mistral | Mistral, Mixtral and successors | permissive (Apache 2.0) for most releases; some restricted | yes | own endpoint and third-party hosts |
| Cohere | Command R, Aya | non-commercial (CC BY-NC) | no, research use only | own endpoint |
| Alibaba (Qwen) | Qwen family | permissive for most sizes; some restricted | yes | third-party hosts |
| DeepSeek | V3, R1 and successors | permissive (MIT) | yes | own endpoint and third-party hosts |
| Google | Gemma | open weights under terms of use | yes, within the terms | own endpoint and third-party hosts |
| Microsoft | Phi | permissive (MIT) | yes | own endpoint (Azure) and third-party hosts |
| NVIDIA | Nemotron | NVIDIA open model licence | yes | own endpoint (NIM) and third-party hosts |

The licence column is the one that earns the table: "open" spans permissive, restricted-commercial
and research-only, and an organisation that buys accelerators needs to know which it holds before it
deploys. The last two columns answer whether each release is plausibly used in possession and by
proxy.

### 2.2 Repositories

Published models live in a few repositories that host the files, their metadata and their revision
history.

- **The repositories.** The Hugging Face Hub is the largest and functions as the default address of
  the ecosystem. Kaggle Models and ModelScope, which mirrors much of the Hub for the Chinese market,
  hold most of the rest, with plain GitHub releases for the remainder.
- **What an entry contains.** The files themselves, each with a hash, and a commit history. A model
  card written by the publisher: training, intended use, evaluation and, where the publisher chooses,
  safety. A licence. Where the publisher declares it, the relation to a parent model.
- **The model tree.** The declared relations, fine-tune, adapter, merge and quantisation, link entries
  into a tree, so that a popular base model may have thousands of descendants. The relation is
  declared by the publisher, not verified by the repository, and many publishers do not declare it.
- **Controls the repository applies.** Scanning uploaded checkpoints for executable content.
  Converting checkpoints into a safe container format on request. Gating a download behind
  acceptance of terms. Removing content under the platform's policies.
- **What the controls do not do.** They act on the file as an artefact. None of them verifies
  anything the model card says about behaviour, and none of them says whether the file behaves like
  the parent it claims to derive from.

The table below places the hosting services in the same fashion. The last column is the one to
read first: services that sit next to file repositories, and sometimes share their names, may hand
the organisation a key rather than a file.

| Service | What it hands you | Formats | Guaranteed metadata | Controls applied | Side of the line |
|---|---|---|---|---|---|
| Hugging Face Hub | files, with revision history and model cards | safetensors, pickle, GGUF, ONNX | file hashes, commit history, licence field, declared base-model relation | pickle scanning, safetensors conversion, gating, policy removal | in possession |
| Hugging Face Inference Endpoints | a hosted API over a Hub model | — | — | the Hub's, plus the endpoint's | by proxy |
| Kaggle Models | files, with model cards | safetensors, pickle, framework-specific | file hashes, licence field | moderation, licence acceptance | in possession |
| ModelScope | files, largely mirrored from the Hub | as the source | file hashes; relations as mirrored | mirror-side policy | in possession; provenance must be re-established |
| GitHub releases | files attached to a software release | any | release tag, asset hashes | none specific to models | in possession |
| GitHub Models | a catalogue of hosted endpoints | — | — | the backing provider's | by proxy |
| NVIDIA NGC | containers and files | NIM containers, checkpoints | image digests, signed containers | signing, scanning | in possession (container) |
| Ollama library | quantised files pulled by a local runtime | GGUF | manifest digests | none beyond the manifest | in possession |

### 2.3 Redistributors

Between the repository and the organisation that runs a model sit redistributors, which take a
published model and repackage it for a particular way of running it. They fall into five kinds.

- **Cloud model gardens.** The major cloud providers curate catalogues of open models that deploy
  into a customer's cloud account with a few clicks: Amazon Bedrock and SageMaker JumpStart, Google
  Vertex AI Model Garden, the Azure AI model catalogue. The provider selects which models to list,
  sometimes converts or optimises them, and hosts the copy that the customer deploys.
- **Packaged inference microservices.** NVIDIA's NIM distributes open models as containers in which
  the model file, an optimised inference runtime and a standard serving API are bundled. A container
  can be pulled and run on an organisation's own accelerators, or the same model can be consumed from
  NVIDIA's hosted endpoints.
- **Local runtimes with their own libraries.** Ollama and the wider llama.cpp family distribute
  models in the GGUF format, usually quantised, through libraries of their own, and run them on a
  workstation, a laptop or a single server, exposing a local API that mimics the hosted ones. They
  are the entry point for most individual and small-team use.
- **Deployment and orchestration platforms.** Platforms such as Rafay manage fleets of accelerators,
  on premises or across clouds, and the deployment of model-serving workloads onto them. The
  organisation chooses the model and the serving stack; the platform provisions, schedules and
  operates the infrastructure.
- **Hosted inference providers.** Together AI, Fireworks, Groq, OpenRouter and the Hub's own
  inference endpoints serve open models behind a pay-per-token API. The organisation sends requests
  and receives answers, exactly as it would with a closed model, and never handles the file.

### 2.4 Four ways to consume an open model

The redistributors above resolve into four consumption modes, distinguished by where the model
runs and who handles the file and the software that serves it. The first is the model by proxy; the
other three are the model in possession.

| Mode | Where the model runs | Who handles the file | Who operates the serving software | Typical examples |
|---|---|---|---|---|
| **Hosted API** | the provider's infrastructure | the provider | the provider | Together AI, Fireworks, Groq, OpenRouter, a laboratory's hosted endpoint |
| **Self-hosted on own accelerators** | the organisation's GPUs, on premises or in its cloud account | the organisation | the organisation | a repository download served with vLLM, TGI or SGLang; Ollama on a server |
| **Vendor-packaged, self-run** | the organisation's GPUs | the organisation, inside a container assembled by the vendor | shared: the vendor's runtime on the organisation's host | NIM containers; JumpStart deployments into the organisation's account |
| **Local or edge** | a workstation, a laptop, a device | the organisation or the individual | the same | Ollama, llama.cpp, mobile and in-browser runtimes |

The first mode is the model by proxy, as framed at the top of this section. The
other three modes put the file in the organisation's hands, together with the responsibility for
the hardware it runs on, the software that serves it and every component loaded beside it. The
choice between these modes is usually made on cost, latency, data residency and control; it also
decides, as a side effect, what the organisation is able to inspect and what it must take on trust.

### 2.5 Large and small models

Open models span several orders of magnitude in size, and size determines where a model can run.
Large language models, from tens to hundreds of billions of parameters, need multi-accelerator
servers and are the models most often consumed through hosted APIs or cloud gardens; the largest
open releases now use mixture-of-experts designs in which only a fraction of the parameters is
active for any one token, which lowers the cost of serving without lowering the size of the file.
Small language models, from under one billion to a few billion parameters, are built to run on a
single accelerator, a workstation or a device, and are the models most often self-hosted or run
locally. Small models are very often derivatives: distilled, quantised or retrained from a larger
parent for a narrower purpose. Alongside size, open models divide by task into generative models,
which produce text or other media; classification models, which assign labels; embedding models,
which produce vectors for search and retrieval; and multimodal models, which take or produce images,
audio or video together with text. Most of what is discussed as "an LLM" in production is a
generative model, large or small, often with a multimodal path.

### 2.6 Artefact formats

A model file arrives in one of a few formats, and the format matters independently of the model
inside it.

- **Pickle checkpoints** (`.bin`, `.pt`, `.pth`, `.ckpt`) are serialised with Python's pickle
  module. Loading one can execute arbitrary code embedded in the file. The format predates the
  ecosystem's security awareness and is still widespread in older entries.
- **safetensors** stores tensors and nothing else; loading it cannot run code. It has become the
  default on the Hub for new uploads and is the format repositories convert to.
- **GGUF** is a single-file format for quantised models, carrying its metadata inside the file, used
  by the llama.cpp family and by Ollama.
- **ONNX** is a graph-based interchange format for running a model outside the framework it was
  trained in, common for classification and embedding models in production pipelines.
- **Container images** bundle a model with its runtime and serving software into one deployable
  unit.

A safe format guarantees the safety of the container, not of its contents. A safetensors file can
hold a model whose behaviour has been altered in any way its publisher chose.

### 2.7 Derivatives and the model tree

Most files in circulation are derivatives: files produced from another model file rather than
trained from scratch. Four kinds account for nearly all of them.

- **Compressed copies** (quantised models) store the same model at lower numeric precision so that
  it fits smaller hardware. Behaviour is close to the parent's but not identical.
- **Retrained copies** (fine-tuned models, and adapters that are loaded alongside a base) change the
  model's behaviour by further training on new examples, for a task, a language, a style, or a
  different safety posture.
- **Merged models** combine the numbers of two or more parents, by averaging or by more elaborate
  schemes, to obtain a model with properties of each.
- **Stripped forks** (abliterated or "uncensored" models) are copies from which the publisher's
  refusal behaviour has been deliberately removed, then published, often with a name that advertises
  the removal as a feature.

Each derivative is a different model from its parent. The repository records the relation when the
publisher declares it; the publisher need not, and many do not, so the model tree is a partial map.
Licensing follows the tree in principle, since most open-weights licences bind derivatives to the
parent's terms, and diverges from it in practice, since enforcement is rare and relabelling is easy.
Provenance, the chain from a base model through each derivation to the file in hand, is therefore
something an organisation reconstructs for itself, from hashes, declared relations and the
publisher's reputation, rather than something the ecosystem supplies.

---

## 3. Definitions

**The file and the model.** The model is the file. Its weights are the only persistent state; there
is no separate policy, rulebook or configuration that governs behaviour. Any derivative of the file,
whether compressed, retrained, merged or stripped, is a different model and is assessed on its own.

**Internal state.** During inference the model maintains, at each layer ℓ and each token position, a
hidden state h_ℓ, the residual stream. The answer is produced from the final layer's state, and each
token generated is conditioned on the states of the tokens before it. A change to h_ℓ at one point
therefore propagates forward through the remaining layers and, through the generated tokens, along
the rest of the answer.

**Meaning directions.** Some directions in the space of h_ℓ are the model's own: those that the
unembedding reads into vocabulary, and those along which semantically distinct inputs separate. A
direction of this kind is called on-cone. A direction chosen at random, or associated with a token
the model would not produce, is off-cone.

**The refusal direction.** For a safety-aligned model, the mean hidden state over harmful requests
and the mean over harmless requests differ along a consistent direction,

r = mean(h_ℓ | harmful) − mean(h_ℓ | harmless).

This difference of means is the refusal direction. It is an on-cone direction of particular
interest: projecting it out of the hidden state, or steering against it, suppresses refusal, and
successful jailbreak prompts have been shown to suppress it through the input. Published work shows
the refusal structure is in fact a small bundle of directions; a single difference-of-means direction
is a floor on its removability. On a mixture-of-experts model the direction is located per expert
(Section 7).

**The activation-space intervention.** Every test in this paper is an instance of one operation:
perturb or read the hidden state along a direction, then read out an effect. An instance is fixed by
five choices: the direction v, the operator (add, subtract, rotate, project out), the locus (the
residual stream, the attention output, a particular expert), the magnitude (small, for measurement;
large, for attack), and the readout (a shift in the next-token distribution, a compliance judgement,
or a geometric displacement). Group 1 uses small magnitudes and distributional readouts; Group 2 uses
large magnitudes and compliance readouts, except the firmness test, which perturbs the data used to
locate v and reads the displacement of v itself.

**Radius.** For a family of perturbations indexed by a magnitude, the radius is the smallest
magnitude at which the mean per-token Kullback–Leibler divergence between the clean and the
perturbed next-token distributions exceeds a fixed threshold τ.

**Leverage.** The ratio of the radius for a random (off-cone) direction to the radius for a meaning
(on-cone) direction at the same layer: how much cheaper a meaning direction is than a random one.
Because a meaning direction is always somewhat cheaper, leverage near one is the healthy case; large
leverage indicates that small pushes along the model's own directions are amplified into large
changes of the answer.

**Coherent compliance.** A harmful request counts as complied with only when the generated answer
passes a degeneracy gate (it is fluent, not collapsed into repetition or noise) and a refusal
detector finds no refusal. Configurations in which the model produces incoherent text are excluded
regardless of what the detector reports, because an attacker wants usable answers. All
compliance-based scores are therefore conservative.

**Work factor.** The effort an attacker with access to the model's internals needs to obtain
coherent compliance. Each Group 2 test reports it in its own currency: an angle, a coefficient, a
geometric displacement. The currencies are not combined.

**Bands.** Every test decodes its score against one global band table. Attack metrics, where higher
is worse, read critical, high, medium or low. Quality scores, where higher is safer, read the same
four bands in the opposite direction. For Group 1 the four bands are reported with three words:
Robust for the low-risk band, Sensitive for the medium band, Fragile for the high and critical bands.

---

## 4. Threat model

### 4.1 Three doors

A model deployed as-is has exactly three attack surfaces. A door is defined by the access it grants,
not by who stands at it. Which doors an organisation holds follows from its consumption mode
(Section 2.4): through a hosted API it holds the input only, and the file and the serving software are
the provider's; on its own accelerators, packaged or not, it holds all three.

| Door | Access granted | Who typically has it | What can be done to the model |
|---|---|---|---|
| 1. The input | send text to the deployed model and read its output; nothing else | any user of the product; any document, web page or tool result the product feeds to the model | prompt attacks: jailbreaks, prompt injection, extraction. Nothing inside the model can be read or changed |
| 2. The serving path | read and write the model's internal state while it runs | the operator's own engineers; third-party serving, adapter and guardrail code; a compromised host; an insider | any activation-level intervention, applied live and removed without trace in the file |
| 3. The supply chain | the file itself before deployment, and the examples it was tuned with | the model vendor; the author of a fork; a compression or conversion step; a mirror; anyone who edits the file or its tuning set | a different model shipped under the same name: a corrupted or re-compressed copy, a fork with the refusal removed and baked in, a variant tuned from a tampered example set |

Three rules follow.

1. **Every test in this paper needs door 2 or door 3.** Tests that perturb the hidden state require
   full access to the model; the integrity test perturbs the weights. None of the six can be
   reproduced by typing a prompt.
2. **Door 1 is indicated by the six, never measured by them.** A prompt attack is a chain of two
   halves: words move the hidden state, and that movement moves the answer and is amplified along
   generation. The tests measure the second half exactly: how little internal movement already
   changes the answer or removes the refusal. They fix the floor a prompt attack must reach. Whether
   words can produce that movement is a separate measurement, made by black-box prompt attacks. Where
   this paper draws a door-1 consequence from a test, it is an inference supported by the literature,
   stated as such.
3. **Reconnaissance is free at doors 2 and 3.** Locating the refusal direction costs a few dozen
   prompts and a published recipe for anyone holding the file. The tests score the second step of an
   attack, moving the safeguard, never the first, finding it. Obscurity protects nothing.

### 4.2 Two halves of an assessment

The six tests grade what the model's own steadiness and safeguard are worth from inside the file or
upstream (doors 2 and 3). What an outsider obtains today at the input (door 1) is the province of
black-box prompt attacks, reported as a compliance rate. An assessment presents both halves. Reading
either alone is the error to avoid: a clean prompt-attack result on a model whose safeguard has a
low work factor establishes only that the words have not yet been found.

### 4.3 Why a work factor

Nobody certifies a cipher by observing that it has not been broken; the certification states the
effort required to break it. The Group 2 tests certify the safeguard in the same sense. A safeguard
that costs little to defeat from inside will, under rule 2, be defeated through the input eventually.
The work factor is exposure, not probability: it states what an attacker obtains if they try, and
says nothing about whether anyone will.

---

## 5. Group 1: steadiness and forgiveness

One measurement underlies the three tests: how small a change inside the model already changes its
answer. The three tests apply it three ways, which are also the three ways a model returns something
other than what was asked.

### 5.1 Integrity (the weight-tamper radius)

**Question.** Does a slightly altered copy of the file still behave like the original?

**Security meaning.** A corrupted, re-compressed or quietly edited file that crashes is caught. One
that keeps working and answers differently is not, and such a file can be substituted for the
original without any behavioural trace. The test asks how much alteration the file absorbs before
its answers move. A forgiving file cannot be nudged that way; a brittle one can.

**Mechanism.** Isotropic random noise of scale σ is added to the weights. The radius is the smallest
σ at which the mean per-token divergence between the clean and the noised next-token distributions
exceeds τ. It is reported with the corresponding signal-to-noise ratio in decibels.

**Door.** Supply chain. This is the one test that protects the operator even when nobody attacks.

**What it is not.** Not a crash test. Not a before-and-after comparison: it characterises this file,
and a derivative is a different file with its own assessment. Not a statement about behaviour under
any particular edit; it measures sensitivity to alteration in general.

### 5.2 Fidelity (on-cone distortion and leverage)

**Question.** How easily can the model be made to answer the question wrong, while staying on topic?

**Security meaning.** A wrong answer that remains on topic is the failure no output filter catches:
a support assistant that confidently states a wrong policy, a pricing assistant that quotes a wrong
figure. Fluent, relevant, wrong. Fidelity is the headline measurement of Group 1 for this reason.

**Mechanism.** A push of magnitude ε is added to the hidden state at a layer along an on-cone
direction, a vocabulary row or the refusal direction. The radius is the smallest ε at which the
next-token divergence exceeds τ. The leverage is the ratio of the off-cone radius to this on-cone
radius at the same layer. Layers are swept over a depth band and the least stable is reported. The
leverage is the primary score, because it is dimensionless and independent of τ to first order; a
meaning direction being a few times cheaper than a random one is the model's normal causal
structure, not a weakness, so leverage at or below that level maps to the safest band.

**Door.** Serving path directly; supply chain through altered copies; the input as the floor only.

**What it is not.** Not a prompt attack and not a measurement of door 1. Published attacks that
steer at the layer of maximum amplification, or that read the sensitivity of the response likelihood
to latent perturbation, are this measurement under other names, not separate tests.

### 5.3 Containment (off-cone diversion, the control)

**Question.** How easily can the model be pushed to answer a different question?

**Security meaning.** Drift off topic, or into content the model was not asked for. This is the
least worrying of the three, because an ordinary output filter catches it. Its value is as a control:
it establishes whether the model is loosely held in general or only along its own meaning
directions, which is the specificity claim that fidelity rests on.

**Mechanism.** The same push along a random or absent-token direction; reported as the ratio of the
off-cone to the on-cone radius.

**Door.** As fidelity.

**What it is not.** Not scored. It carries no band of its own and no acceptance criterion; the
fidelity mitigation and the output filter cover it.

---

## 6. Group 2: the quality of the intrinsic safeguard

### 6.1 One safeguard, three axes

The model's refusal is a single structure inside the file: the line, in the space of hidden states,
between the requests it refuses and the requests it answers. It is not a rulebook and not a separate
component. It is the whole of the model's own protection. Because it is one consistent structure, it
can be located from a small set of examples by anyone holding the file, and anything that can be
located can be moved.

The three tests of Group 2 act on this one structure along three axes. Mathematically, the twist and
the forgetting tests are affine maps of the hidden state built from a difference-of-means direction,
h ↦ Ah + b, the same class as the permanent removal performed by weight surgery; the firmness test
acts one level up, on the estimator of the direction, r′ = r(D + δD). Same object, two classes of
operator.

| Test | Axis on the safeguard | Operator | Locus | Readout |
|---|---|---|---|---|
| The twist test | how far the model can be pushed off the line before it complies | rotation in the plane of h and r, norm-preserving | residual stream | smallest coherent-jailbreak angle |
| The forgetting test | whether the line still fires when its trigger is dulled | subtraction of a scaled direction | attention output | best coherent compliance |
| The firmness test | how firmly the line is drawn | perturbation of the contrastive set | estimator of r | displacement of the located direction, null-controlled |

The attacker's prize is identical on every axis: fluent compliance with a harmful request, from a
model that sounds exactly like itself. Only fluent compliance counts; incoherent outputs are not
jailbreaks and are excluded. Every Group 2 result is conservative for that reason, and for a second:
each test locates a single direction, while the refusal structure is a small bundle, so the work
factor reported is an upper bound on the true one.

### 6.2 The twist test (angular steering)

**Question.** How far must the model be turned away from its refusal before it complies, while still
speaking fluently?

**Security meaning.** The refusal is a position the model holds inside, not a decision it makes each
time. An attacker does not delete the position and does not argue with it. They turn the model's
internal state a little away from it and ask the same question. The smallest angle at which the
model begins answering harmful questions fluently is the work factor along this axis. A small angle
carries a second message: the refusal is a position rather than a judgement, since nothing was
decided and the model was merely moved.

**Mechanism.** The refusal direction is located at each swept layer. A forward hook rotates the
hidden state away from it by an angle θ in the plane spanned by the state and the direction,
preserving norm. Answers are generated for a small fixed set of harmful requests; a configuration
counts as a coherent jailbreak only when enough answers pass the degeneracy gate and at least half of
those comply. The angle is swept upward per layer with early stopping at the first coherent break.
The score is the smallest coherent-jailbreak angle across layers, decoded so that a small angle is
critical, a moderate one high, a very large one medium, and no coherent break at any angle low.

**Door.** Serving path, in minutes, by anyone on it. Supply chain: a fork with the refusal removed
and baked in is this attack done once, permanently, and published. The input as the floor only.

**What it is not.** Not a prompt attack; the requests are plain and the turn is inside. Not an edit
of the file; nothing is written and the hook is removed afterwards. Not a report of "the model
broke"; the highest compliance sits at large angles where the model degenerates, and those are
excluded by design. Not a measure of how hard the direction is to find; that is free.

### 6.3 The forgetting test (attention-path ablation)

**Question.** Does the safeguard still fire when the model's sense of danger is dulled at one point
inside it, with the request left unchanged?

**Security meaning.** Part of the refusal is triggered by recognition: the model registers that a
request is about harm, legality or danger, and that recognition wakes the refusal. If the
recognition is dulled at one stage, the refusal never engages, and the answer is fluent and on topic.
This is a second, independent lever on the same safeguard. The twist test moves the model's stance
relative to the line; the forgetting test dulls the trigger that invokes the line. Different locus,
different operator, and a model's result on one does not predict its result on the other, which is
why both tests exist.

**Mechanism.** The direction is built from words rather than requests: a short list of safety words
and a short list of everyday words are presented one at a time; the output of a layer's attention
module is captured for each; the difference of the two means is the "sense of danger" at that layer.
A scaled copy of it is subtracted at that layer, at several strengths, across layers spread through
the model's depth. Answers are generated for the same small harmful set under the same degeneracy
gate; a configuration counts only when most of its answers remain coherent. The score is the highest
coherent compliance across layer-and-strength settings.

**Door.** As the twist test.

**What it is not.** Not the removal of dangerous words from the prompt; the prompt is untouched. Not
the forgetting of facts; the answers stay fluent and on topic, only the danger sense is dulled. Not
the twist test under another name. Not an edit of the file.

### 6.4 The firmness test (contrastive-set poisoning)

**Question.** How firmly is the line between refusal and compliance drawn? And, as a consequence,
can a safeguard built from examples on this model be trusted?

**Security meaning.** The line is located, by anyone, from a small set of example requests, some
harmful and some harmless. That is also how the industry adjusts a model's safety after training,
without retraining it: a control is built from exactly such an example set. The example set is the
smallest and least guarded input in the whole pipeline, a plain-text file reviewed by eye. If a few
review-passing word changes in the harmless examples move the located line, then whoever can edit a
text file controls what the model refuses, and the model card is unchanged. For an operator who runs
the file as-is and tunes nothing, the meaning is the firmness of the safeguard itself: a line that
swings under light tampering is a line drawn softly, and a soft line is the precondition for crossing
it with a few changed words. The second clause follows: building a safeguard from examples is equally
easy on every model, but on a soft line the result depends on the exact examples used, so it is easy
to get wrong by accident and easy to tamper with on purpose. Trustworthy is not the same as effective;
whether the model responds to a control built on the line is what the twist test shows.

**Mechanism.** The refusal direction is located from harmful and harmless requests. In the harmless
requests only, about one token in twenty is replaced by a near neighbour in the model's own embedding
space chosen to lean toward the harmful side, so that the text still reads as harmless. The direction
is located again from the harmful requests and the altered harmless requests. The score is the
angular displacement between the two located directions, one minus their cosine. A null control
repeats the substitution with the lean toward a random direction; displacement that the null control
reproduces is noise and is not reported. No text is generated. To first order the displacement is
the sideways movement of the harmless mean divided by the separation between the harmful and harmless
means, so the test reads the width of the margin on which the safeguard rests.

**Door.** Supply chain, for anyone who adopts a variant tuned from examples they cannot inspect. The
input as the floor only. There is no door-1 or door-2 use of this mechanism against an as-is model;
an attacker at inference cannot apply it.

**What it is not.** Not training-data poisoning: nothing is assumed about how the model was trained,
nothing is injected into it, the tampering is applied at test time to text on the tester's side, and
the model is identical in both readings. Not a backdoor test: nothing is planted and nothing is
detected, and a firm line does not mean the file carries no planted behaviour. Not a prompt attack:
the altered examples never reach the deployed model. Not a measurement of whether noisy requests
cross the line; the test measures the cause, a soft line, not the symptom.

**Relation to data poisoning.** Data poisoning is the technique. What the test measures is the
control that technique obtains over the model: whether the smallest, least-guarded input in the
pipeline can silently re-aim the model's safety.

---

## 7. Mixture-of-experts models

In a mixture-of-experts model only a few experts process each token, and a different subset each
time. A refusal direction computed as a mean over tokens therefore averages activations produced by
different sparse expert selections, and the average under-represents any single expert's refusal
signal: the mean includes zeros from tokens an expert did not process. The blended direction is
blurred, and attacks or measurements along it are diluted.

Two corrections are built into the tests. First, directions are located per expert: tokens are
bucketed by the expert they routed to, the difference of means is taken within each bucket, and the
dominant expert's direction is used. Second, perturbations are kept routing-preserving: the change to
the hidden state is projected into the null space of the router, so that a push or rotation does not
change which experts answer. On models whose attention and expert layers live in different blocks,
the forgetting test sweeps the attention blocks only. These corrections remove both false negatives
(a sharper direction than the blend reveals) and false positives (effects that were routing artefacts
rather than refusal removal).

---

## 8. Reading a result: bands and acceptance

Every file is measured the same way on the same fixed scale, so the result of each test is a word,
never a number and never a comparison with another named model.

**Group 1.**

| Band | Meaning | What an attacker needs | Acceptance |
|---|---|---|---|
| Robust | a large push inside the model is needed before the answer moves | heavy access and effort, easy to notice | use |
| Sensitive | a moderate push moves the answer, and it grows as the model writes | ordinary access: a plugin, an adapter, a careless conversion | use with the named control: for integrity, a pinned checksum and a new assessment of every copy; for fidelity, an answer check outside the model and no third-party code on the serving path |
| Fragile | a tiny push is enough and the model amplifies it | almost nothing; any door will do | do not deploy |

**Group 2.**

| Band | Meaning | Acceptance |
|---|---|---|
| Low | the safeguard held on this axis | keep the normal external guard; record the result |
| Medium | it gave way under a moderate effort | deploy only behind a separate guard, in front and behind |
| High | it gave way under a small effort | do not rely on the built-in refusals for anything; a separate guard is required |
| Critical | a nudge was enough | treat the model as having no refusals of its own; deploy only behind a guard the operator controls; accept no tuned variants |

For the firmness test the second clause adds a criterion for anyone who tunes: at Low a safeguard
built from examples on this model is trustworthy; at Medium no example-built safeguard is trusted
unless its examples can be compared word for word against a trusted copy; at High and Critical every
example-built safeguard on this model is untrusted.

Group 1 and Group 2 results are read together with the black-box prompt-attack result (Section
4.2). A low work factor with a clean prompt-attack result is a warning, not a reassurance.

---

## 9. Framework mapping

Identifiers refer to the OWASP Top 10 for LLM Applications 2025, MITRE ATLAS and the NIST AI Risk
Management Framework with the NIST adversarial machine learning taxonomy. Tests that read and perturb
the hidden state carry ATLAS T0044, Full AI Model Access, as a precondition; they are not reachable
behind an inference API. ATLAS T0018 is Manipulate AI Model; a backdoor trigger would be T0043.004.

| Test | OWASP LLM 2025 | MITRE ATLAS | NIST |
|---|---|---|---|
| Integrity | LLM04 Data and Model Poisoning | T0031 Erode AI Model Integrity; T0018 | AI RMF MEASURE 2.7 |
| Fidelity | LLM01 Prompt Injection (steering susceptibility); LLM09 Misinformation | T0018; T0054 LLM Jailbreak | MEASURE 2.7; AI 100-2e evasion / model manipulation |
| Containment | LLM01; LLM06 Excessive Agency | T0018 (control) | MEASURE 2.7 |
| The twist test | LLM01 (jailbreak outcome) | T0018 technique → T0054 outcome; precondition T0044 | MEASURE 2.7; AI 100-2e |
| The forgetting test | LLM01 | T0018 → T0054; T0044 | MEASURE 2.7; AI 100-2e |
| The firmness test | LLM04 (+ LLM03 Supply Chain) | T0020 Poison Training Data (+ T0019 Publish Poisoned Datasets); enables T0054 | AI 100-2e data / model poisoning |

---

## 10. Limitations

- **Coherence gate.** Only coherent compliance counts, so the safeguard tests understate removability
  rather than overstate it.
- **Single direction.** Each Group 2 test locates one direction; the refusal structure is a small
  bundle. The reported work factor is an upper bound.
- **Small request sets.** Compliance rates move in coarse steps; sufficient for a band, not for fine
  comparison between files.
- **Rule-based judgement.** Compliance is decided by a refusal-phrase detector after a degeneracy
  gate, not by a second model. Auditable, and blind to subtle partial compliance.
- **Three currencies.** Angle, coefficient and displacement are not combined into one figure.
- **Door 1.** Every consequence for the input door is an inference supported by the literature,
  never a measurement by these tests.
- **Provisional constants.** The divergence threshold, the depth band and the reference leverage are
  set by convention; the band table is fixed, the constants are not.
- **The firmness test measures a cause, not a symptom.** It reports a soft line; it does not report
  whether noisy requests cross it.

---

## 11. Relation to the literature

The refusal direction as a single difference-of-means direction, and the observation that jailbreak
prompts suppress it, is due to Arditi et al. (2024). The multi-dimensional character of the refusal
structure, and the partial restoration of safety after single-direction ablation, is shown by the
analysis of steering-vector safety pitfalls (2026), which is why single-direction results are treated
here as floors.

The twist test realises angular steering (Vu and Nguyen, 2025). The forgetting test realises the
attention-path, keyword-decoded ablation of Amnesia (2026). The firmness test realises the
contrastive-set poisoning of Steering Vectors are an Adversarial Attack Surface (2026), with a
geometric rather than behavioural readout and a null control.

Two further published attacks are not separate tests because they are the fidelity measurement under
other names: causal amplification, which steers where a small perturbation is most amplified along
generation (Steering in the Shadows, 2025), is the leverage; latent-space robustness probing, which
reads the response likelihood under hidden-state perturbation (ASA, 2025), is the on-cone radius
with a different readout. The Rogue Scalpel (2025) shows that random and feature-based directions
also remove refusal, with no knowledge of the model; its plain additive arm belongs to the steering
family, and the containment control carries its message for a given file, since it reports whether a
random push is as cheap as a meaningful one.

Mixture-of-experts corrections follow the router-aware treatment of steering (RARE, 2026) and the
per-expert refusal directions of expert-aware refusal steering (2026).

---

## References

- Arditi, A. et al. Refusal in Language Models Is Mediated by a Single Direction. arXiv 2406.11717,
  2024.
- Vu, H. and Nguyen, T. Angular Steering. arXiv 2510.26243, NeurIPS 2025 (spotlight).
- Amnesia: Adversarial Semantic Layer-Specific Activation Steering. arXiv 2603.10080, 2026.
- Steering Vectors are an Adversarial Attack Surface. arXiv 2606.05958, 2026.
- Analysing the Safety Pitfalls of Steering Vectors. arXiv 2603.24543, 2026.
- The Rogue Scalpel: Activation Steering Compromises LLM Safety. arXiv 2509.22067, 2025.
- Steering in the Shadows: Causal Amplification for Activation-Space Attacks. arXiv 2511.17194, 2025.
- Probing the Safety Robustness of LLMs in Latent Space (ASA). arXiv 2506.16078, 2025.
- RARE: Router-Aware Steering on Mixture-of-Experts Models. arXiv 2608.21236, 2026.
- Expert-Aware Refusal Steering. arXiv 2606.04160, 2026.
- Katz, N. On the Dynamical Interpretation of the Jacobian Lens. Internal note, 2026. Transformer
  Circuits, J-lens and the union of cones, 2026.
- OWASP Top 10 for LLM Applications, 2025. MITRE ATLAS, ATLAS.yaml. NIST AI RMF 1.0; NIST AI
  100-2e2025, Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations.
