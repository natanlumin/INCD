# Open-weight ecosystems

How a publicly downloadable language model moves from the laboratory that trained it to the system
that runs it: producers, repositories, redistributors, the two ways to consume a model, model
classes, artefact formats, derivatives, and what each step does and does not guarantee.

---

## Definition

An **open-weight ecosystem** is the set of actors, channels, formats and derivation relations
through which a language model whose weights are publicly downloadable moves from the organisation
that trained it to the organisation that runs it. "Open weight" means the file of parameters is
public; it does not by itself mean the training data, the training code or the licence terms are
open, and it does not mean the organisation consuming the model possesses the file. The ecosystem
has five kinds of participant: producers, who train and publish; repositories, which host files and
metadata; redistributors, which repackage a published model for a particular way of running it;
consumers, who run the model in possession or by proxy; and the derivative publishers, who form
most of the long tail by producing compressed, retrained, merged or stripped copies of someone
else's model. Two facts organise the whole: a file is either in the consumer's possession or it is
not, and every derivative is a different model from its parent.

---

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
risks are its own. A model by proxy is open in the sense
that its file is public and the provider could be replaced; it is not open in the sense that the
organisation possesses it. From the consumer's side it is indistinguishable from a closed commercial
model: a key, a request, an answer, a bill.

This document describes the ecosystem on its own terms: who produces models, where they are
published, how they are repackaged, the four ways an organisation consumes them, which resolve into
the two sides of the distinction above, the software that executes a model once it has one, the
classes of model in circulation, the formats the files take, and the derivatives that make up most
of what is downloaded.

## 1. Producers

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
information an organisation needs, and a full landscape report carries the sourced version.

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

## 2. Repositories

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

## 3. Redistributors

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

## 4. Four ways to consume an open model

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

## 5. Inference: how we execute a model

Everything above describes a file. A file does nothing. It is a large table of numbers, and
producing an answer from it takes a second piece of software that loads those numbers and performs
the arithmetic, token by token. That software is the **inference server**. The organisation chooses
it, installs it, configures it and patches it separately from the model, and it has its own
releases, its own defects and its own published vulnerabilities. Several are in common use: vLLM,
SGLang, Text Generation Inference, and the llama.cpp family on which Ollama is built. They are not
part of what the organisation received when it obtained the model, which is why they appear nowhere
in the formats of section 7; they are the other half of what it takes to run one.

Three consequences follow.

These names are not alternatives a reader has to choose between. They are the engines already running
underneath the products of sections 2 and 3, usually without being named on the box. The same three
or four appear nearly everywhere.

| Where an organisation meets it | What runs underneath |
|---|---|
| Ollama | llama.cpp, named as its supported backend |
| NVIDIA NIM | vLLM, SGLang or TensorRT-LLM, one per profile, selected when the container starts |
| Google's Model Garden | vLLM, SGLang, Text Generation Inference, TensorRT-LLM and Google's own Hex-LLM, in containers Google optimises |
| Microsoft Foundry managed compute | vLLM or SGLang, pinned together with the quantisation by a deployment template |
| Amazon SageMaker large-model-inference containers | vLLM and TensorRT-LLM |
| Hugging Face Inference Endpoints | vLLM, Text Generation Inference, or a container the customer supplies |
| hosted providers such as Together, Fireworks and Groq | not stated; Groq names only its own hardware |

Two things are worth taking from that table. The first is that an organisation using a cloud garden,
a vendor container and a laptop runtime is not using three unrelated technologies; it is using two or
three engines, in three wrappers, and a defect in one of those engines reaches all three. The second
is the last row. Where a provider holds the file, it need not say what serves it, and in practice
does not.

Whether the organisation chooses the inference server or simply receives it depends on which of the
four modes above it is in, and that answer decides whose problem the server's defects are.

| How the model is consumed | Who chooses the inference server | Whose defects are they |
|---|---|---|
| hosted API, the model by proxy | the provider, which need not say which it uses or when it changes | the provider's; the organisation cannot inspect them and usually cannot tell when they are patched |
| self-hosted on own accelerators | the organisation, explicitly, along with its version and its configuration | the organisation's, in full |
| vendor-packaged, self-run | the vendor, which selects and pins it inside the container; the organisation chooses the bundle, not its contents | shared: the vendor builds and patches the stack, the organisation runs it and owns the host |
| local or edge | implied by the channel: choosing Ollama chooses the llama.cpp family underneath it | the organisation's, often without its realising a choice was made |

The inference server decides what the outside world can reach. It is the component that exposes an
interface, so it, rather than the model, determines whether a caller sees only generated text or can
reach further.

Loading a model is not a passive act. Each of these servers offers an option that runs code supplied
alongside the model, documented by one vendor in these terms: it "will execute on your local machine
arbitrary code present in the model repository". Each will also fall back to the older pickle format
when a safe one is absent, so the risk described under pickle in section 7 reaches every runtime.

On some hardware the file cannot be loaded at all until it has been compiled into a form built for
that specific hardware. The software that performs that step is a **build toolchain**, and its
output is a **compiled engine**. An engine is not interchangeable: by default it runs only on the
device type, the library version and the host operating system it was built for, and relaxing any of
those is possible only at a stated cost in performance. An engine can be received ready-made from a
vendor rather than built locally, and when it is, none of the repository-side controls described in
section 2 apply to it, because it does not travel through those repositories.

## 6. Large and small models

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

## 7. Artefact formats

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
- **Compiled engines** are not a way of storing parameters but the output of building them for a
  particular target, as described in section 5. They are listed here because an organisation can
  receive one in place of a weight file. A compiled engine cannot be read by the tools that inspect
  weight files, and no vendor documents whether the original parameters can be recovered from one.

The first four are ways of storing parameters and are portable. The last two are built artefacts and
are not: a container pins the software around the model, an engine pins the hardware under it.

A safe format guarantees the safety of the container, not of its contents. A safetensors file can
hold a model whose behaviour has been altered in any way its publisher chose.

## 8. Derivatives and the model tree

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

## Terms used in this document

| Term | Meaning here |
|---|---|
| open-weight model, open model | a model whose parameter file is publicly downloadable, whatever its licence |
| in possession | the organisation holds the file and runs it on accelerators it pays for, with serving software it operates |
| by proxy | the organisation holds an API key to a provider's copy; it never handles the file or the serving software |
| producer | the organisation that trained and published the model |
| repository | a service that hosts model files, their metadata and their revision history |
| redistributor | a service that repackages a published model for a particular way of running it: a garden, a packaged microservice, a local runtime library, a deployment platform, a hosted provider |
| model tree | the graph of declared parent relations between entries: fine-tune, adapter, merge, quantisation |
| derivative | any file produced from another model file: compressed copy, retrained copy, merged model, stripped fork |
| stripped fork | a copy from which the publisher's refusal behaviour was deliberately removed, then published; often labelled "uncensored" or "abliterated" |
| large language model, small language model | tens to hundreds of billions of parameters, run on multi-accelerator servers; under one to a few billion, run on a single accelerator, a workstation or a device |
| artefact format | how the parameters are stored on disk: pickle checkpoint, safetensors, GGUF, ONNX, container image |
| inference server | software that loads a published model file and executes it, embedded as a library or run as a service exposing an API; chosen and patched separately from the model, and not part of what was received with it |
| build toolchain | software that compiles a published checkpoint into a target-specific artefact that must exist before the model can run on that target |
| compiled engine | the output of a build toolchain: an executable artefact bound to a hardware target, a library version and a host platform, which the tools that inspect weight files cannot read |

---

## Bibliography

Source class, per the report's citation policy: S4, platform and vendor documentation, unless marked
otherwise. Access date 2026-10-06. The links were recorded from the organisations' published
addresses and must be re-verified, with the page title and date captured in the source log, before
any cell of the tables above is cited in a deliverable.

**Repositories and hosting**

- Hugging Face Hub, model documentation: https://huggingface.co/docs/hub/models
- Hugging Face Hub, model cards: https://huggingface.co/docs/hub/model-cards
- Hugging Face Hub, pickle scanning and safetensors conversion: https://huggingface.co/docs/hub/security-pickle
- Hugging Face Hub, gated models: https://huggingface.co/docs/hub/models-gated
- Hugging Face Inference Endpoints: https://huggingface.co/docs/inference-endpoints
- Kaggle Models: https://www.kaggle.com/models
- ModelScope: https://www.modelscope.cn
- GitHub releases: https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases
- GitHub Models: https://docs.github.com/en/github-models
- NVIDIA NGC catalog: https://catalog.ngc.nvidia.com
- Ollama library: https://ollama.com/library

**Redistributors: gardens, packaged runtimes, local runtimes, platforms, hosted providers**

- Amazon Bedrock: https://aws.amazon.com/bedrock
- Amazon SageMaker JumpStart: https://docs.aws.amazon.com/sagemaker/latest/dg/studio-jumpstart.html
- Google Vertex AI Model Garden: https://cloud.google.com/model-garden
- Azure AI model catalogue: https://learn.microsoft.com/azure/ai-foundry/how-to/model-catalog-overview
- NVIDIA NIM: https://developer.nvidia.com/nim and hosted endpoints at https://build.nvidia.com
- Ollama: https://ollama.com and https://github.com/ollama/ollama
- Rafay: https://rafay.co
- Together AI: https://www.together.ai
- Fireworks AI: https://fireworks.ai
- Groq: https://groq.com
- OpenRouter: https://openrouter.ai

**Producers and licences** (licence pages change; capture the version and date)

- Meta Llama, licence: https://www.llama.com/llama-downloads and https://www.llama.com/license
- Mistral AI, models and licences: https://docs.mistral.ai/getting-started/models
- Cohere, Command R and Aya (CC BY-NC): https://cohere.com/research and https://huggingface.co/CohereLabs
- Alibaba Qwen: https://qwenlm.github.io and https://huggingface.co/Qwen
- DeepSeek: https://www.deepseek.com and https://huggingface.co/deepseek-ai
- Google Gemma, terms of use: https://ai.google.dev/gemma/terms
- Microsoft Phi: https://huggingface.co/microsoft and https://azure.microsoft.com/products/phi
- NVIDIA Nemotron and the NVIDIA open model licence: https://huggingface.co/nvidia and https://developer.nvidia.com/nemotron
- Apache License 2.0: https://www.apache.org/licenses/LICENSE-2.0
- MIT License: https://opensource.org/license/mit
- Creative Commons BY-NC 4.0: https://creativecommons.org/licenses/by-nc/4.0

**Inference servers, build toolchains and compiled engines**

Project documentation, for a reader who wants to know what each of these is:

- vLLM: https://docs.vllm.ai
- SGLang: https://docs.sglang.io (the address https://docs.sglang.ai redirects here)
- Text Generation Inference: https://huggingface.co/docs/text-generation-inference
- llama.cpp: https://github.com/ggml-org/llama.cpp
- TensorRT-LLM: https://nvidia.github.io/TensorRT-LLM

Which engine runs underneath which product:

- Ollama, supported backends (llama.cpp): https://github.com/ollama/ollama
- NVIDIA NIM, model profiles and selection: https://docs.nvidia.com/nim/large-language-models/latest/deployment/model-profiles-and-selection.html
- Google, open models serving options: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/open-models/choose-serving-option
- Microsoft Foundry, managed compute: https://learn.microsoft.com/en-us/azure/foundry/concepts/managed-compute-overview
- Amazon SageMaker, large model inference containers: https://docs.aws.amazon.com/sagemaker/latest/dg/large-model-inference-container-docs.html and https://docs.djl.ai/master/docs/serving/serving/docs/lmi/index.html
- Hugging Face Inference Endpoints: https://huggingface.co/docs/inference-endpoints
- Groq: https://groq.com

The specific statements cited in section 5:

- vLLM, engine arguments and security: https://docs.vllm.ai/en/latest/configuration/engine_args.html and https://docs.vllm.ai/en/latest/usage/security.html
- SGLang, server arguments: https://docs.sglang.io/docs/advanced_features/server_arguments.md
- Text Generation Inference, launcher arguments: https://huggingface.co/docs/text-generation-inference/en/reference/launcher
- Optimum Intel, export (the quoted statement that trusted remote code executes arbitrary code locally): https://huggingface.co/docs/optimum/en/intel/openvino/export
- TensorRT-LLM, trtllm-build and checkpoint loading: https://nvidia.github.io/TensorRT-LLM/commands/trtllm-build.html and https://nvidia.github.io/TensorRT-LLM/features/checkpoint-loading.html
- NVIDIA TensorRT, engine compatibility and support matrix (the three axes of non-portability): https://docs.nvidia.com/deeplearning/tensorrt/latest/inference-library/engine-compatibility.html and https://docs.nvidia.com/deeplearning/tensorrt/latest/getting-started/support-matrix.html
- NVIDIA NIM, model profiles (pre-compiled engines downloaded per profile): https://docs.nvidia.com/nim/large-language-models/latest/deployment/model-profiles-and-selection.html
- ONNX Runtime, custom operators: https://onnxruntime.ai/docs/reference/operators/add-custom-op.html

**Artefact formats**

- Python pickle, security warning (S1-adjacent, language documentation): https://docs.python.org/3/library/pickle.html
- safetensors: https://huggingface.co/docs/safetensors
- GGUF specification: https://github.com/ggml-org/ggml/blob/master/docs/gguf.md
- ONNX: https://onnx.ai
- Open Container Initiative image specification: https://github.com/opencontainers/image-spec

**Model classes and derivation**

- Hugging Face Hub, base-model relations and the model tree (model card metadata): https://huggingface.co/docs/hub/model-cards#specifying-a-base-model
- Hugging Face PEFT (adapters): https://huggingface.co/docs/peft
- Model merging, mergekit: https://github.com/arcee-ai/mergekit
- Arditi et al., Refusal in Language Models Is Mediated by a Single Direction (S3, preprint; basis of the "stripped fork" notion): https://arxiv.org/abs/2406.11717
