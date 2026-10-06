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
| Ollama library | files, repackaged into the platform's own layers | Narrow rather than absent. Two formats are accepted on the way in, and what leaves is Ollama's own packaging, so the publisher's choice of format does not survive the trip | Partly, and the vocabulary is the runtime's capabilities rather than a task taxonomy |
| GitHub releases | files, any content | No. There is no model convention at all, so the format is whatever the publisher attached | No |
| Cloud model gardens | a deployment into the customer's account, or a provider-hosted endpoint | Partly. The provider selects and often converts, so the format reflects the provider's choice rather than the publisher's | Yes, but the catalogue is curated, so coverage describes the provider's selection |
| Hosted inference providers | an API key | No. No file is received | Partly. Only what the provider has chosen to offer, and only as a menu |

Two rows deserve the emphasis. **Ollama is the clearest case of a dimension changing shape rather than
disappearing.** Its documentation accepts two formats on the way in, a safetensors directory or a GGUF
file, and what the library then distributes is Ollama's own layered packaging [LD-14]. So the question
worth asking is not which formats it carries but what the runtime can execute, and the platform answers
that in capability labels rather than tasks. **The hosted providers are the clearest case of a dimension
disappearing**: with no file, format is not merely uninformative but meaningless, and the organisation's
exposure shifts entirely to what the provider discloses, which section 5 of the ecosystems document
shows is usually nothing.

## 2. What each platform carries

Governance, platform-side controls, guaranteed metadata and distribution mechanism are tabulated in
`../landscape/landscape-platform-comparison.md` and are not repeated here. This section answers the
question that table does not: what is actually inside each platform, and in whose vocabulary.

### 2.1 Hugging Face Hub

The only platform here that publishes a closed, machine-readable vocabulary for all three dimensions,
and by a wide margin the largest: **3,127,450 model repositories** as at 2026-10-06 [LD-08].

**Tasks and modalities.** Sixty-three task names, which the Hub calls pipeline tags, grouped into six
published modality headings: multimodal (9 tasks), natural language processing (12), computer vision
(19), audio (4), tabular (2) and reinforcement learning (1) [LD-01]. The task is declared per
repository in the model card, drives the filters, and selects which inference widget and API the Hub
uses [LD-02]. Counts for the tasks this report cares about, as at 2026-10-06 [LD-08]:

| Task | Repositories |
|---|---|
| text generation | 420,432 |
| text classification | 123,517 |
| text to image | 111,121 |
| image-text to text | 41,388 |
| automatic speech recognition | 37,185 |
| feature extraction | 21,283 |
| object detection | 6,931 |

Two readings matter. Text generation, the class the six tests address, is about one repository in
seven. And those seven tasks together account for roughly 762,000 of 3.13 million repositories, so
**about three quarters of the Hub carries no pipeline tag at all** [LD-08]. The untagged remainder is
largely adapters, quantisations and other derivatives, which means any statement about what the
ecosystem contains, built on task counts alone, undercounts derivative artefacts severely.

**Formats.** The Hub's own libraries facet enumerates fifty-four values [LD-04], and a parallel
documented table lists the integrated libraries with what each supports [LD-05]. The format is
declared per repository, and where it is absent the Hub infers it from the files present, for example
recognising a NeMo or Core ML model by extension [LD-03].

That facet is the single most important thing in this section, and not for the reason it looks like.
**It mixes three different kinds of thing under one name.** Serialisation formats are there, such as
safetensors, GGUF, ONNX, Core ML, LiteRT and DDUF. So are training libraries, such as Transformers,
Diffusers and timm. So, in a second facet of seventeen values, are the local runners and applications
that can consume the artefact, among them llama.cpp, vLLM, SGLang, Ollama, LM Studio and Docker Model
Runner [LD-06]. Only the first kind carries load-time execution risk. A security taxonomy that adopts
the Hub's facet wholesale inherits a category error, which is the argument for section 4 keeping its
format axis to serialisation formats alone.

The Hub also publishes twelve parameter-size bands, from under one billion to over five hundred
billion [LD-07], which is the closest thing in the ecosystem to a published scale axis.

### 2.2 Kaggle Models

**Formats.** Kaggle treats framework structurally rather than as a tag: it is a mandatory segment of
every model's address, so one logical model fans out into one artefact per framework [LD-10]. The
documented enumeration is nonetheless open-ended, published as a list of examples ending in an
ellipsis rather than a closed set [LD-09]. Values observed in the catalogue go beyond the seven
documented ones, GGUF among them [LD-12].

**Tasks and modalities.** The index offers nine filter groups, including a task facet and a data-type
facet, which is Kaggle's modality axis [LD-11]. The values inside them are loaded on expansion and
appear in no published document. The documentation treats task as free-text guidance for naming a
variation rather than a controlled vocabulary [LD-12]. So Kaggle has the axes without publishing the
vocabulary, and a report cannot key a matrix off it.

**A composition point.** Part of the Kaggle catalogue is not Kaggle's. Entries appear under a Hugging
Face surface and resolve to links out rather than to files Kaggle holds [LD-13]. An organisation that
believes it is sourcing from Kaggle may be sourcing from the Hub.

### 2.3 ModelScope

**Modalities.** Six top-level groups, from the platform's own tag service: text, image, audio, video,
multimodal and scientific computing [LD-15]. The last of these has no counterpart among the Hub's six
headings, and the catalogue backs it with a science facet covering life sciences, earth science,
physics and the social sciences [LD-18].

**Tasks.** Two hundred and nineteen task strings across five fields, published in ModelScope's own
open-source toolkit: 130 in computer vision, 47 in natural language processing, 21 in audio, 20
multimodal and one in science [LD-16]. This is more than three times the granularity of the Hub's
taxonomy, and it is weighted differently, with heavy coverage of document and character recognition,
face and person analysis, and Chinese-language processing. It is also the taxonomy of record only
because the website's own task filter does not publish its values [LD-17].

**Formats.** Sixty-nine library values across a catalogue of 264,794 models, with counts [LD-18]. The
top of the distribution tells the story:

| Value | Models |
|---|---|
| PyTorch | 230,091 |
| safetensors | 194,143 |
| LoRA | 114,361 |
| GGUF | 20,918 |
| MLX | 9,823 |
| ONNX | 7,353 |

**Adapters are 43 per cent of that catalogue.** They are not an edge case in the ecosystem; on this
platform they are the third-largest population and larger than every format except the two dominant
ones. Any matrix that treats an adapter as a minor row misdescribes what is actually in circulation.

### 2.4 Ollama library

**Formats.** Two accepted inputs, documented: a directory of safetensors weights, or a GGUF file,
single or sharded. Ollama states it does not quantise GGUF models on import, so the compression is
done before the file arrives [LD-14]. What the library then distributes is Ollama's own layered
packaging, so neither input format survives to the consumer as such.

**What it can run, in place of a task taxonomy.** The documentation enumerates eight capabilities:
streaming, thinking, structured outputs, decision, vision, embeddings, tool calling and web search
[LD-19]. Vision models taking images alongside text are served [LD-20], and dedicated embedding models
are distributed with their own API endpoint [LD-21]. The library labels every entry with capability
chips, and across the index those labels occur as tools 94 times, thinking 44, vision 41, cloud 16,
embedding 12, decision 4 and audio once [LD-22].

That is the answer to what Ollama carries, and it is a different shape of answer from the Hub's. It
is a few hundred curated entries described by what the runtime can do with them, not a taxonomy of
what the models are.

### 2.5 GitHub releases

No taxonomy of any kind: not formats, not modalities, not tasks. The only constraints that shape the
artefact are mechanical, up to a thousand assets per release and under two gibibytes per file, with no
limit on total size or bandwidth [LD-23]. That per-file ceiling is why large models arrive here as
multi-part shards.

This is the uncontrolled channel, and it is uncontrolled in a specific sense: not that it is permissive
about content, but that it holds no description of what a file is. Everything a reader could key a
matrix off has to come from outside the platform.

### 2.6 Cloud model gardens

The gardens enumerate deployment and commerce, not artefacts. None of the four publishes an artefact
format vocabulary, because in a garden the weights are not the unit of distribution.

**Amazon Bedrock** publishes the cleanest modality enumeration of any platform here, and it is also the
narrowest: text, image and embedding [LD-24]. The catalogue itself is wider than its own filter,
carrying video, speech, reranking and more across eighteen provider rows [LD-25]. The page that used to
hold the modality table now redirects to a provider-organised catalogue [LD-25].

**Microsoft Foundry** states a catalogue of over ten thousand models growing by about fifty a month,
split commercially into models sold by Azure and models from partners and community, with eight filter
axes including an explicit inference-task axis whose values are given only as examples [LD-26]. Its
catalogue includes a Hugging Face collection served on managed compute [LD-27].

**Google's Model Garden** documents three catalogue categories, foundation models, fine-tunable models
and task-specific solutions, and a four-axis filter pane covering tasks, collections, providers and
features. The values inside tasks and features are not published [LD-28].

**NVIDIA NIM** is the outlier and publishes the richest category list, seventeen families spanning
large language and vision-language models, embedding and reranking, optical character recognition and
object detection, speech recognition, translation and synthesis, safety guardrails, digital humans,
medical imaging, protein and molecular biology, weather and physics simulation [LD-29]. It is also the
one whose unit of distribution is explicitly a container rather than a weight file [LD-30].

### 2.7 What the comparison shows

**Only two platforms publish a closed task vocabulary**, the Hugging Face Hub with 63 and ModelScope
with 219. Kaggle, Google, Microsoft and AWS all document that a task filter exists without publishing
what is in it. A report that needs a stable task axis has two sources and must pick one or reconcile
them.

**The supply chains are nested, and a finding propagates.** Kaggle surfaces Hugging Face repositories
as links [LD-13], Microsoft Foundry hosts a Hugging Face collection [LD-27], and Google's Model Garden
relies on Hugging Face's own scanners for the Hugging Face models it serves, blocking what they call
unsafe and merely flagging what they call suspicious [LD-28]. A weakness in one platform's hygiene is
therefore not contained to that platform.

**Derivatives dominate and are invisible in task counts.** Adapters are 43 per cent of ModelScope's
catalogue [LD-18], and roughly three quarters of Hugging Face repositories carry no task tag at all
[LD-08]. The ecosystem is mostly derivative artefacts, and the published taxonomies describe the
minority.

## 3. Artefact formats

<!-- FORMATS -->

## 4. The segmentation

<!-- TAXONOMY -->

## 5. Source log

<!-- LOG -->
