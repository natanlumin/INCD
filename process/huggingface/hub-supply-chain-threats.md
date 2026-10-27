# Supply-chain and artefact-level threats on the Hugging Face Hub

**Scope.** This document covers the supply-chain and artefact-level threats to an open-source model, read
through the primary model repository (SCRUM-281), the Hugging Face Hub. The Hub is the primary repository by
the ecosystem quantification (SCRUM-286), the other repositories examined are largely mirrors of it, and every
research study cited here measured the Hub. Whether the same threats exist on the other repositories is
treated in its own part rather than assumed, because the repositories differ in what they guarantee and in
what they scan.

**Structure.** Part 1 describes the Hub as an object, element by element, with what each element guarantees
and what it merely declares. Part 2 gives the threats by the layer at which they enter the path: publishing,
artefact, loading. Part 3 inventories the Hub's own controls. Part 4 asks which threats transfer to the other
repositories. Part 5 rates the threats. Part 6 hands on to the control inventory, the lifecycle framework and
the assessment gaps.

**Symbols.** Terms, questions, citation prefixes and section numbers that come from outside this document are
listed, with where each is defined, in "Symbols from outside this document" after the source log.

## Introduction: how a file becomes a threat

The threats in this family are easiest to see by following a model from the account that publishes it to the
process that runs it. Eight observations about that path set the scene; the parts that follow give each its
threats, its evidence and its controls.

**Anyone can publish, and reputation is declared (SCRUM-281), not guaranteed (SCRUM-281).** A Hub account is open to any natural
person aged 13 or over, or any legal entity, and the publisher is solely responsible for what it uploads [HF-01]. The
platform guarantees who uploaded and when; it does not guarantee that the account is the producer (SCRUM-281) whose name
appears in the repository's title, that the parent model named on the card is the real parent, or that the
download and like counts measure anything but attention [HF-14, HF-15]. A name is a string chosen by the
uploader, and a study of the Hub found 1,574 repositories whose names sat one edit away from the 100 most
downloaded models [SC-19]. The organisation that selects a model by its name and its popularity is trusting a
signal the repository does not stand behind.

**The model is a binary file, and some formats are programs.** What is downloaded is a serialised object, not
a document. The pickle format, still the container of 44.9 per cent of the models in one Hub-wide census
[SC-18], is a program for a small virtual machine, and loading it executes whatever that program says
[TX-02, TX-03]. Formats that cannot carry a program, safetensors, GGUF and ONNX among them, are still read by
parsers written in C and C++, and a parser with an integer overflow turns a well-formed-looking file into a
memory-corruption attack on the loader [SC-14]. The file is therefore not inert: it is an input to code, and
in the worst case it is the code.

**Loading is execution, and it can install or call third parties.** Loading a model does more than read its
weights. With the relevant option set, the loader imports Python files that travelled with the model and runs
them [SC-08, LC-01]. It renders the chat template, which is a Jinja program [SC-06, SC-13]. Depending on the
inference server (SCRUM-281), it may install plugins, load native libraries named by the file, write and later execute a
compile cache, or fetch a dependency from a package index at load time [SV-12, SV-16, SV-18]. Each of these is
a point at which software the organisation did not select enters the process, and some of them reach out to a
third party over the network to do so. None of them is visible in the weights.

**The artefact is more than the weights.** A model repository (SCRUM-281) carries, beside the weights, a configuration,
a tokenizer, a chat template, processor code, and often adapters (SCRUM-281) that change what the model does when they
are loaded with it [SC-08, TX-14]. Each is a separate file with its own format and its own loader, and a
review that inspects the weights alone has inspected the part of the artefact least able to carry a payload.

**The file reviewed is not necessarily the file deployed.** An identifier without a pinned revision resolves
to the newest commit, so the same name can return a different file tomorrow [HF-17, SV-15]. The account that
owns the repository can be taken over, since two-factor authentication is optional [SC-02]. A repository can
be renamed or transferred, and the old name redirects to the new owner's content [SC-05]. The gap between
review and deployment is where tampering after publication lives.

**The repository is a dependency, and its controls are advisory.** The Hub runs a malware scan, a pickle
import scan and two third-party scans on every public file, and shows the result; it withholds nothing, and a
flagged file remains downloadable [HF-05, HF-06, HF-07, HF-08]. The pickle scanner it relies on has been
bypassed at least twice, once by a flaw the maintainer states affected the online scanners [SC-15, SC-16].
Where a file is actually withheld or signed, it is at a redistributor (SCRUM-281), not at the repository the producer
published to [CG-12, GH-06].

**The organisation may never hold the file.** By proxy, a serving provider (SCRUM-281) does the downloading and the loading,
and the organisation inherits every choice above without seeing it. The Hub itself is now also a serving
provider: a request to a model on the Hub can be routed to one of eighteen partner providers, with the fastest
selected by default, and Inference Endpoints pull the weights into a container the organisation never sees
[SC-27, HF-18]. "Download" and "call" are no longer different acts with different threats; they are the same
supply chain with the loading step moved out of sight.

**Detection is thin where the artefact is largest.** Scanners exist for pickle and for a few other formats
[SC-26]; none exists for a compiled engine or a container image, the forms in which a growing share of models
is received instead of as a file [SV-01, SV-02, SV-03, SV-04]. Signing schemes that would make the producer's
identity a guaranteed property are available but not adopted by the Hub beyond optional commit signing
[SC-24, HF-11].

## Part 1. The Hub as an object

### 1.1 Guaranteed and declared

A property of a model on the Hub is **guaranteed** (SCRUM-281) when the platform enforces or computes it and
the organisation can rely on it without further checking; it is **declared** (SCRUM-281) when the uploader
supplied it and the platform displays it unverified. Table 1 sorts every property of every element by this
test. Where the platform's documentation is silent, the property is recorded as not established rather than
assumed either way.

### 1.2 The elements, and what each guarantees

**Table 1. Elements of a model on the Hugging Face Hub**

| Element | What it is | Who controls it | Guaranteed by the platform | Declared, or not guaranteed | Sources |
|---|---|---|---|---|---|
| Account and organisation | the identity that owns repositories; a user account or an organisation with members | the uploader; the terms open an account to any natural person aged 13 or over, or any registered legal entity | that the account exists, when it acted, and which account made each commit | that the account is the producer (SCRUM-281) its name suggests; two-factor authentication is optional; access tokens are the uploader's to protect | HF-01, SC-01, SC-02, SC-03 |
| Repository and its name | a git repository under a namespace, selected by the string namespace/name | the owning account; renamable and transferable by the owner | that the name resolves to exactly one repository at a time; that a renamed repository redirects from its old name | that the name means what it suggests; that the name will resolve to the same owner tomorrow, since the redirect follows the owner's choice | SC-05, HF-15 |
| Revision | a commit in the repository's history; an identifier without a revision resolves to the newest commit on the default branch | the owning account | the full commit history with diffs; a SHA-256 and a storage hash recorded for every file in a commit | that the newest commit is the one the organisation reviewed; a commit's author identity is guaranteed only when GPG-signed and the key is on the account, and unsigned commits carry no status | HF-15, HF-13, HF-11, HF-17 |
| Files | the weights and everything beside them: configuration, tokenizer, chat template, custom modelling and processing code, adapters (SCRUM-281), in whatever formats the uploader chose | the repository owner and any account it grants write access. Anyone else can only propose a change as a pull request, which the Hub stores on a separate ref that is not fetched by default, so the served files do not change until the owner merges it; the owner can also disable pull requests for the repository | that each downloaded file matches the hash the platform recorded for it, checked by the storage layer | what the file does when loaded: a pickle checkpoint (SCRUM-281) is a program, a chat template is a program, custom code is a program; the platform records the format and scans some of them, and guarantees nothing about their behaviour | HF-13, HF-16, HF-06, TX-03, SC-06, SC-08, SC-28 |
| Model card and metadata | the README and its machine-read front matter: licence, base model, pipeline tag, library, datasets | the uploader; the card itself is best practice, not required | that the fields shown are the fields the uploader wrote | every field: licence, parent model, training data, intended use; the model tree and the licence filter are built from these declared fields | HF-14, HF-15 |
| Scans | a malware scan at each commit, a pickle import scan on every pickled upload, and two third-party scans of public repositories; results shown on the file listing and through the API | the platform, with two partners | that the scans ran and that their results are displayed | that a flagged file is withheld: every scan is advisory and the file stays downloadable; that a clean result means a safe file, which the platform's own documentation disclaims | HF-05, HF-06, HF-07, HF-08, HF-13 |
| Gating and visibility | the owner may require login and a request before download, approve manually or automatically, restrict by geography, and revoke without notice; the owner may make the repository private | the owning account | that an ungated download of a gated repository is refused; that a private repository is not served to others | who the approved requesters are beyond the username and e-mail they share; that access, once granted, persists | HF-12 |
| Access tokens and secrets scanning | tokens with read, write or fine-grained roles that authenticate the client; a scan on each push for leaked secrets in uploaded content | the uploader; the platform for the scan | that a token's role bounds what the client may do; that a verified leaked secret triggers an e-mail to the owner | that a leaked token is noticed before it is used; the secrets scan notifies and does not block | SC-03, SC-04 |
| Distribution mechanism | the hub client library, the hf command line, or git with the storage extensions; also the libraries that download implicitly when given a model name | the organisation, through software the Hub publishes | that the bytes received match the recorded hash; that a pinned revision returns that revision | that an unpinned name returns the reviewed file; the libraries advise pinning a full commit hash and most callers do not | HF-17, SV-15 |
| Inference Providers and Inference Endpoints | the Hub's own serving: a request to a model page or API routed to one of eighteen partner providers, the fastest selected by default; or a managed endpoint that pulls the weights into a container | the platform and its partners | that the request was served under the Hub's account and billing | which partner served it unless the caller pins one; what the partner loaded and how; the organisation receives an API, not a file, and holds the model by proxy (SCRUM-281) | SC-27, HF-18 |
| Moderation and takedown | the content policy with five prohibited categories including malware, a report channel, graduated actions from an edit request to removal, and a public log of takedown notices | the platform, at its sole discretion | that the takedown log is public | that a reported repository is removed, or when; that a repository the organisation depends on will remain available | HF-01, HF-02, HF-04 |

### 1.3 Reading the table

The guaranteed column is short. Across all eleven elements the Hub guarantees four properties: the identity
of the account that acted, the integrity of every file against the hash the platform recorded, the
completeness of the commit history, and the fact that its scans ran and what they reported. Every other
property on a model page is declared by the uploader and displayed unverified. The page does not make this
split visible: the download count, the licence badge, the base-model link and the scan status appear beside
the commit hash in the same style, although only the last is a property the platform stands behind.

This split is the premise of Part 2. Each of its three layers corresponds to one consequence of the split.

- **Integrity is guaranteed, authenticity is not.** The hash proves the organisation received the file the
  uploader committed. It says nothing about whether the uploader is the producer, and nothing about whether the
  file is safe. Every threat at the publishing layer lives in that gap.
- **The guarantees attach to a revision, and most organisations do not hold one.** An unpinned name is a
  pointer the owner can move. Every guarantee in the table is a guarantee about a specific commit, so an
  organisation that recorded only the name has recorded nothing it can later verify. Every threat in the
  artefact layer that involves change after review lives here.
- **The platform scans but never withholds.** The scan status is the one platform-side control (SCRUM-281) that looks at
  content, and it is advisory by design and disclaimed by its author. The loading software therefore meets the
  file with no platform guarantee about its behaviour, which is where the loading layer begins.

### 1.4 The path through the elements

The elements fall on a path, and Part 2 follows it. Publication puts an account, a name and a first revision
in place. The artefact is the set of files at a revision, with the card and the scan results beside it.
Distribution is the step at which the organisation's client resolves a name to a revision and pulls the
files, or at which the Hub's own serving does so on the organisation's behalf. Loading is the step at which
the organisation's software, or the partner's, turns the files into a running model. The three layers of
Part 2 are these steps: the publishing layer covers the account, the name and the card; the artefact layer
covers the files, the revision and the scans; the loading layer covers the distribution mechanism (SCRUM-281), the
loading software and the Hub's own serving. Gating, tokens and moderation are controls rather than steps, and
belong to Part 3.

## Part 2. The threats, by the layer at which they enter

Eight threats act on a model between its publication on the Hub and its loading by the organisation. None
of them touches what the model was trained to do; each makes the organisation run something other than what
it believes it selected.

- **T1, name confusion and typosquatting.** A repository published under a name, namespace or card that
  makes it look like a producer's own.
- **T2, account and name takeover.** A producer's account, token or repository name passing to an actor who
  then commits as the owner.
- **T3, malicious serialisation.** A pickle checkpoint whose instruction stream executes code when loaded.
- **T4, format and parser exploits.** A malformed GGUF, ONNX or other file that breaks the parser reading
  it.
- **T5, code and templates that ship with the model.** Custom modelling code and chat templates, stored as
  ordinary files, executed by the loader.
- **T6, malicious adapters (SCRUM-281).** An adapter carrying T3 or T5 into a trusted base model, declared
  against that base by a field no one checks.
- **T7, revision drift.** A repository whose newest commit is no longer the one the organisation reviewed,
  served to every deployment that did not pin a revision.
- **T8, software installed or executed during loading.** Packages, plugins, native libraries, compile
  caches or a partner's loader entering the process because the model was loaded.

They are grouped by the layer at which they enter, because the layer decides who the actor is and what the
organisation can see at the time: the publishing layer, 2.1, T1 and T2, needing an account and a name and no
malicious file; the artefact layer, 2.2, T3 to T7, needing a file the organisation holds without knowing
what it is or whether it is still the one reviewed; the loading layer, 2.3, T8, needing only that the
organisation's software, or the Hub's own serving, behaves as documented. Table 2, in 2.4, sets the eight
against the elements of the Hub they act on.

Every entry has the same shape so that the threats can be compared: the elements it acts on, the mechanism,
the evidence on the Hub, then its access state (SCRUM-281), level and confidence label (SCRUM-281), and one
line on what the platform does about it today.

### 2.1 Publishing layer

**T1. Name confusion and typosquatting.** *Element: repository and its name; model card and metadata.*

A model is selected by a string, namespace/name, in a namespace any account can write to, and the Hub checks
the string against nothing. Every signal shown beside it is declared (SCRUM-281): the base-model link that
places a repository in a producer's (SCRUM-281) model tree is a card field the uploader typed [HF-14], the
download and like counts measure attention, and the organisation documentation describes no step that
verifies an organisation is the company its name suggests [SC-29]. A repository that borrows a producer's
name and fills the card accordingly therefore looks, on the page, like the producer's own.

A study of 1,020,755 models on the Hub against the 100 most downloaded found 1,574 squatting candidates, 10.4
per cent with suspicious or harmful characteristics, and 302 of 127,011 organisation namespaces with squatting
patterns; the techniques are those of package registries, character substitution, homoglyphs, inserted
hyphens and version-like suffixes [SC-19]. A second study finds model names often inconsistent with the
architecture they denote [SC-20]. Renaming or transferring a repository redirects the old address to the new
one [SC-05], so a recorded name keeps resolving after the repository behind it has changed hands; whether a
name freed by deletion can be re-registered is not established.

Access state (SCRUM-281): both; by proxy (SCRUM-281) the catalogue entry is mis-selected in the same way.
Level (SCRUM-281): system, since the wrong file is loaded. Label: established. Platform response: none that is
guaranteed (SCRUM-281); the content policy allows reporting an impersonating repository and acting at the
platform's discretion [HF-02].

**T2. Account and name takeover.** *Element: account and organisation; repository and its name; access
tokens.*

The account is the one element whose identity the Hub guarantees, so an actor who holds the account holds
the guarantee. Three routes to the account are documented. Two-factor authentication is offered and not
required [SC-02]. A write token grants push access to every repository its holder can write; the platform
warns against leaking one and offers an endpoint anyone may call to revoke a token they have found [SC-03].
The secrets scan runs on every push and notifies the owner by e-mail when it verifies a leaked secret; it
does not block the push, so a token committed into a repository is live until the owner reads the e-mail
[SC-04]. Organisation membership multiplies the surface: every member with write access is an account whose
compromise reaches the organisation's repositories [SC-01].

Once inside, the actor commits as the owner. The commit history records the act [HF-15], but a commit's
author is guaranteed only when it is GPG-signed with a key on the account, and unsigned commits carry no
status [HF-11], so a reader of the history cannot tell an owner's commit from an intruder's unless the owner
signed every one before. The actor may also rename or transfer the repository, and the redirect carries the
old name's traffic to the new location [SC-05]. No measurement of how often Hub accounts are taken over was
found; the routes are documented, their use is not established.

Access state: in possession (SCRUM-281) for the file; by proxy the serving provider (SCRUM-281)'s copy of the repository changes
under it without the organisation seeing it (Q4.1 (SCRUM-284)). Level: system. Label: established for the routes;
frequency not established. Platform response: two-factor, token roles, token revocation, secrets scanning,
commit signing, all optional or advisory.

### 2.2 Artefact layer

**T3. Malicious serialisation: a pickle checkpoint (SCRUM-281) executes on load.** *Element: files; scans.*

The pickle format is a program for a small virtual machine, and the Python documentation states that
unpickling can execute arbitrary code [TX-02]. PyTorch's default save path uses it, which is why the `.bin`,
`.pt`, `.pth` and `.ckpt` files in circulation are pickle checkpoints [TX-03]. The Hub's own documentation
explains the mechanism in the same terms: the instructions that pose the threat are the global imports and
the reduce that calls what was imported, and "when instantiating an object, the constructor may be called"
[HF-06]. The threat is a file whose instruction stream does something beside restoring tensors, and what it
does is whatever the loading process may do. The published cases include reverse shells, browser credential
theft and system reconnaissance [SC-17].

Three facts bound the threat on the Hub. First, pickle is still common. Of the text-generation repositories counted by the landscape item, 56,780 carry pickle weights, 17 per cent of the safetensors count, and the share is higher in the
older classification and embedding populations [TX-01]; a research sample of popular models found 44.9 per
cent still in pickle [SC-18]. Second, it is exploited on the Hub specifically. A three-month monitoring study
of more than 705,000 models found 91 malicious models and 9 malicious dataset-loading scripts [SC-17]. Third,
the Hub's control over it is a scan that reads the import list without executing the file, highlights
suspicious imports on the file listing, and is disclaimed by its author as "not 100% foolproof", with the
safe and unsafe import lists "maintained in a best-effort manner" [HF-06]. The scanner the Hub relies on has
been bypassed at least twice: once because the package installer was not on the unsafe list, so a file that
called it was reported safe [SC-15], and once through a parsing flaw the maintainer states affected the
online scanners [SC-16]. A flagged file remains downloadable [HF-06]. Whether the scan descends into archives
that contain pickles is not stated in the documentation and is not established.

The safe loading path is itself part of the threat. PyTorch's weights-only mode, the default since version
2.6 [TX-03], could still be made to execute code in every version up to 2.5.1 [SC-09], and the loaders built
on it had pickle paths of their own: two published defects in the transformers library [SC-10, SC-11] and
one in vLLM's weight iterator [SC-12]. These are defects in the loader, not in any file, and an organisation
that pinned the model but not the loader was exposed to them with a clean file.

Access state: in possession only; by proxy the serving provider loads the file and the threat is its. Level:
system, since the payload runs in the loading process. Label: established. Platform response: the pickle
import scan and the two third-party scans, all advisory; safetensors conversion offered to the uploader
[HF-10].

**T4. Format and parser exploits.** *Element: files.*

A format that cannot carry a program can still carry a malformed structure that the parser mishandles, and
the Hub stores every format the uploader chooses without constraint. The GGUF parser in llama.cpp had an
integer overflow that a crafted file turns into out-of-bounds heap reads and writes [SC-14]. ONNX adds a path
by design: a graph may name a custom operator whose implementation is a native library the runtime loads
into the inference process [SV-16]. Safetensors holds tensors only and loading it cannot run code [TX-05];
its parsers were not surveyed for this subsection, and the format guarantees the container, not what the
numbers do. None of the Hub's scans is documented as checking the structural validity of a GGUF, ONNX or
safetensors file; the malware scan is an antivirus pass and the pickle scan reads pickles [HF-05, HF-06].

Access state: in possession. Level: system. Label: established for GGUF and ONNX; safetensors parser defects
not established. Platform response: none documented for these formats.

**T5. Code and templates that ship with the model.** *Element: files; model card and metadata.*

Two kinds of executable content travel in a repository beside the numbers as ordinary files, and both are
run on the organisation's machine.

The first is custom modelling code. A model whose architecture is not in the transformers library ships its
own modelling and configuration modules in the repository, and loading it requires the caller to set
trust_remote_code [SC-08, LC-01]. The vendors describe the option in plain terms: it "will execute on your
local machine arbitrary code present in the model repository (SCRUM-281)" [SV-14]. The Hub displays these files like any
other and scans them with the antivirus pass only; nothing marks a repository as one that requires the option
except the card, if the uploader wrote it there. A preprint study of custom model loading across platforms
reports widespread reliance on the option and uneven enforcement [SC-21].

The second is the chat template. For an instruct or chat model the template is a Jinja program stored with
the tokenizer and run on every call to format a conversation [SC-06]. Whether that program can reach the
host depends on the loader, not the file: the transformers library compiles templates in Jinja's immutable
sandbox [SC-07], while the Python binding of llama.cpp did not, and a template carried in a GGUF file's
metadata gave remote code execution in every version from 0.2.30 to 0.2.71 [SC-13]. The same file on the
same Hub page is safe in one loader and a payload in another.

Access state: in possession. Level: system. Label: established. Platform response: none specific; the custom
code is an ordinary file to the Hub.

**T6. Malicious adapters.** *Element: files; model card and metadata.*

An adapter is a small file loaded together with a model that changes what it does; the glossary assesses the
model-plus-adapter pair, never the adapter alone. As an artefact on the Hub it carries T3 and T5 in
miniature: the PEFT library saves it as safetensors by default or as a pickle `.bin` interchangeably [TX-14],
so an adapter repository is scanned and displayed exactly as a model repository is, with the same advisory
result. What distinguishes it is its position. It is usually smaller, usually published by a different
account than the base, and always declared against a base model through a card field no repository verifies
[HF-14]; the model tree that shows it hanging from a trusted producer's model is built from that declared
field. What the adapter does to the model's behaviour once loaded is 4.3's subject.

Access state: in possession. Level: system for the artefact, model for what it changes. Label: established.
Platform response: the same scans as for a model.

**T7. Revision drift.** *Element: revision; distribution mechanism (SCRUM-281).*

Every guarantee in Table 1 attaches to a commit, and most organisations do not hold one. A model identifier
without a revision resolves to the newest commit on the default branch, and the hub client documentation
advises pinning a full commit hash for that reason [HF-17]; Text Generation Inference adds that a newer
revision may contribute malicious code and gives the same advice [SV-15]. A review of a file is therefore a
review of a revision, and an organisation whose deployment names only the repository has reviewed a file it
is no longer guaranteed to be loading. The actor here need not be an intruder: the owner's own next commit,
a format conversion, a re-upload with a changed template or a newly added custom-code module, arrives
unannounced at every unpinned deployment. The commit history makes the change visible after the fact
[HF-15]; nothing makes it visible before.

Access state: in possession; by proxy the serving provider decides whether to pin, and the organisation
inherits its choice (Q3.4). Level: system. Label: established for the mechanism; frequency of unpinned
deployments not measured. Platform response: revision pinning is available in every client; nothing
requires it.

### 2.3 Loading layer

**T8. Software installed or executed during loading beyond the model.** *Element: distribution mechanism;
loading software; Inference Providers and Endpoints.*

Loading a model from the Hub can bring software onto the machine that is not the model and was not chosen
by the organisation. The Hub's part in this is that it stores and serves whatever the loader will act on;
the acting is the loader's. Six routes are documented.

- A pickle payload can install packages: the pickle scanner did not flag the package installer as unsafe
  before version 0.0.21, so a model could call it and still be reported safe on the Hub [SC-15].
- Custom modelling code imports what it likes, from the repository or from the package index, and runs with
  the loader's privileges [LC-01, SV-14].
- An inference server (SCRUM-281)'s plugins are executed code by design: vLLM states that an endpoint plugin "must be
  treated as part of the server's trusted code base and not as sandboxed or reviewed input" [SV-12].
- An ONNX session loads the native library a graph names for its custom operators [SV-16].
- A compiled model library is executable code distributed as part of "a model": the MLC toolchain ships a
  per-platform shared library carrying the inference logic beside portable weights [SV-23].
- The organisation's own compile cache: vLLM compiles by default and persists graphs and kernels to a cache
  directory whose contents are "loaded without cryptographic integrity verification, including formats that
  support arbitrary code execution" [SV-18, SV-12].

The loading software is itself a dependency with a release history, and the loading threats in T3 were
defects in that software rather than in any file [SC-09, SC-10, SC-11, SC-12]. Every inference server examined
pulls from the Hub by name when given one, and every one falls back to the pickle format when a safetensors
file is absent [SV-11, SV-13, SV-17]. The organisation that pins the model and not the loader has pinned half
the artefact, and the half it left loose is the half that executes.

**By proxy, the Hub does the loading.** Two services move every route above out of the organisation's sight.
Inference Endpoints pull the weights from the Hub into a container and hand the organisation an API [HF-18].
Inference Providers route a request to one of eighteen partner serving providers, the fastest selected by
default unless the caller pins one [SC-27]. In both, the loader, its version, its options and its fall-backs
are the provider's, the revision loaded is the provider's choice, and the organisation holds the model by
proxy with none of the evidence items e1.1 to e1.10 in hand. This is not a ninth threat. It is the same eight
with the loading step performed by a party the organisation did not select and cannot inspect, which is why
the lifecycle framework passes every question to the serving provider in that state.

Access state: in possession for the six routes; by proxy for the two services. Level: system. Label: established. Platform response: none for the loader's
behaviour, which is outside the Hub; for its own serving the Hub documents the routing and the container
and does not document the loader options.

### 2.4 The eight threats against the eleven elements

**Table 2. Which element each threat acts on**

| Threat | Layer | Account, organisation | Repository, name | Revision | Files | Card, metadata | Scans | Gating, visibility | Tokens, secrets | Distribution mechanism | Hub serving | Moderation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| T1 name confusion | publishing | | acts | | | acts | | | | | by proxy | response |
| T2 account takeover | publishing | acts | acts | | | | | | acts | | | |
| T3 malicious serialisation | artefact | | | | acts | | evaded | | | | | |
| T4 parser exploits | artefact | | | | acts | | not covered | | | | | |
| T5 code and templates | artefact | | | | acts | declared only | not covered | | | | | |
| T6 malicious adapters | artefact | | | | acts | acts | evaded | | | | | |
| T7 revision drift | artefact | | | acts | | | | | | acts | by proxy | |
| T8 software during loading | loading | | | | acts | | | | | acts | acts | |

Read across, every threat acts on the files or on the name; a control that sits on neither element meets no
threat in this family. Read down, three columns are empty: gating, visibility and moderation are acted on by
no threat, because they are controls rather than targets, and what each of them actually guards is a
separate question from the one this part answers.

## Part 3. What the Hub does about it

The Hub applies or offers eighteen things that bear on the eight threats. Part 3 lists them as controls (SCRUM-281), one
row each, with the element each sits on, whether it is enforced, advisory or optional, what it guards and
what it does not, and which of T1 to T8 it meets. Four findings follow the table, and Table 4 closes the
part by setting the eight threats against the controls that meet them. Only what the Hub itself applies or
offers is listed; what the organisation must do on its own side is a different inventory.

### 3.1 What counts as a control here

A control is a protection a defender applies against a threat, and a platform-side control (SCRUM-281) is one the
platform applies to hosted files before or at download. Part 3 uses three words for how a control acts,
because the difference decides whether an organisation may rely on it.

- **Enforced.** The platform applies it to every repository and the organisation cannot opt out of it:
  the file hash, the commit history, the refusal of an ungated download.
- **Advisory.** The platform applies it and shows a result, and nothing follows from the result: every
  scan.
- **Optional.** The platform offers it and the publisher or the organisation must switch it on: two-factor
  authentication, commit signing, revision pinning, provider pinning.

An enforced control guarantees something. An advisory control produces evidence. An optional control
guarantees something only for the repositories whose owners adopted it, and the Hub publishes no figure for
how many did.

### 3.2 The controls

**Table 3. Controls the Hub applies or offers**

| # | Control | Element it sits on | Acts as | What it guards | What it does not | Threats met | Sources |
|---|---|---|---|---|---|---|---|
| C1 | SHA-256 per file, recorded at commit, checked by the storage layer on download | files; distribution mechanism (SCRUM-281) | enforced | that the bytes received are the bytes committed at that revision | anything about what the bytes do; anything about who committed them | T7 in part: a changed file is detectable against a recorded hash, if one was recorded | HF-13, HF-16 |
| C2 | Full commit history with diffs | revision | enforced | that every change to the repository is visible after the fact, with its author account and time | that the change was noticed before it was loaded; the author identity beyond the account | T2, T7 after the fact | HF-15 |
| C3 | GPG commit signing | revision; account | optional | that a verified commit was made with a key on the signing account; the Hub's own page notes this "does not guarantee that your file is safe, but it does guarantee the origin" | anything for unsigned commits, which carry no status; the key's holder is the account, not necessarily the producer (SCRUM-281) | T2, where adopted for every commit | HF-11, HF-06 |
| C4 | Malware scan (ClamAV) at every commit | files; scans | advisory | that files matching antivirus signatures are flagged on the file listing | pickle payloads, which the Hub states it "doesn't cover"; novel payloads; the file stays downloadable | none fully; T5 in part for known malware in shipped code | HF-05 |
| C5 | Pickle import scan on every pickled upload | files; scans | advisory | that the imports a pickle references are listed and suspicious ones highlighted, without executing the file | a payload the import lists miss: bypassed by an unlisted installer call and by a parsing flaw the maintainer states affected the online scanners; disclaimed as "not 100% foolproof"; archive handling not stated; the file stays downloadable | T3, T6 in part | HF-06, SC-15, SC-16 |
| C6 | Protect AI Guardian scan | files; scans | advisory | a second opinion on public repositories' files, shown on the Hub | private repositories, not stated; what it detects beyond pickle is not documented on the Hub's page; no withholding | T3, T6 in part | HF-07 |
| C7 | JFrog scan on push | files; scans | advisory | a third opinion on public repositories, exposed in the interface | private repositories, not stated; no withholding | T3, T6 in part | HF-08 |
| C8 | Safetensors conversion offered to the uploader | files | optional | that a pickle checkpoint (SCRUM-281) can be converted to a format that cannot carry a program, by a Hub-run space that opens a pull request against the repository | adoption: the publisher must accept; nothing for repositories that keep pickle; nothing for GGUF or ONNX | T3, where adopted; T6 for adapters (SCRUM-281) saved as pickle, where adopted | HF-10 |
| C9 | Two-factor authentication | account | optional | that a password alone does not open the account | the accounts that did not enable it; the share that did is not published | T2, where adopted | SC-02 |
| C10 | Access tokens with read, write and fine-grained roles, and a public revocation endpoint | account; tokens | enforced for the role bound, optional for the choice of role | that a token can do no more than its role allows; that a found token can be revoked by anyone | a write token in the wrong hands until it is revoked | T2 in part | SC-03 |
| C11 | Secrets scanning on push | tokens; files | advisory | that a verified secret committed into a repository produces an e-mail to the owner | the push itself, which is not blocked; the interval before the owner reads the e-mail | T2 in part | SC-04 |
| C12 | Organisation roles and access control | account and organisation | enforced for the roles set | that write access to an organisation's repositories is limited to the members given it | the members' own accounts, each a T2 surface | T2 in part | SC-01 |
| C13 | Pull requests stored on separate refs | repository; revision | enforced | that a non-owner's proposed change does not reach the served files until the owner merges it; refs are not fetched by default | a change the owner merges without reading; nothing once the actor holds the owner's account | T2 in part, T7 in part | SC-28 |
| C14 | Gated access | gating and visibility | enforced where the owner set it | that a download requires login, a request, and the owner's approval, and that the owner may revoke it; licence and terms acceptance ride on it | what the requester does with the file; nothing about the file's content; nothing for ungated repositories | none of the eight | HF-12 |
| C15 | Private visibility | gating and visibility | enforced where the owner set it | that the repository is served only to accounts the owner allows | the content; coverage of the third-party scans for private repositories is not stated | none of the eight | SC-05, HF-07, HF-08 |
| C16 | Revision pinning in every client | distribution mechanism; revision | optional | that a download names a commit and returns that commit; the client documentation advises it | the deployments that name only the repository, which is the default behaviour | T7, where adopted | HF-17 |
| C17 | Content policy, report channel, graduated moderation, public takedown log | moderation | advisory until the platform acts, then enforced | that an impersonating or malicious repository can be reported and, at the platform's discretion, unranked, tagged, restricted or removed; that takedown notices are public | timing, which is undocumented; anything before the report; the dependents of a removed repository, for whom the terms describe nothing | T1 after the fact; T3 after the fact | HF-02, HF-04, HF-01 |
| C18 | Provider pinning in Inference Providers | Hub serving | optional | that a request is routed to the partner the caller named rather than the fastest | the partner's loader, options, revision and fall-backs, none of which the Hub documents; nothing in Inference Endpoints about loader options | T8 by proxy (SCRUM-281) in part | SC-27, HF-18 |

### 3.3 Four findings

**The Hub scans and never withholds.** Four of the eighteen controls look at the content of a file, C4 to
C7, and all four are advisory: a flagged file stays downloadable, and the Hub's own pages say so for the
malware and pickle scans and disclaim the pickle scan's completeness [HF-05, HF-06]. The result of a scan is
therefore evidence the organisation may read, not a decision the platform took. A flagged badge is
evidence of a problem; an unflagged one is not evidence of its absence.

**The scan can be evaded, and has been.** The scanner the Hub builds on, picklescan, has had a series of
published bypasses: an installer call that was not on the unsafe list, so a model that called it was
reported safe [SC-15], and a parsing flaw in the handling of one opcode that the maintainer states "also
affects the online hugging face pickle scanners" [SC-16]. A research evaluation found the scanners it tested
missed known malicious models [SC-18]. The Hub's verdict also travels: Kaggle links to the Hub's pages, and
two cloud catalogues lean on the Hub's marking of a file as unsafe [LD-13, LD-27, CG-01], so a miss in the
Hub's scan is a miss in theirs.

**The controls that would stop takeover and drift are optional, and adoption is unmeasured.** Two-factor
authentication, commit signing, safetensors (SCRUM-281) conversion and revision pinning, C3, C8, C9 and C16, are the
controls that meet T2, T3 and T7 at their root rather than after the fact, and each is offered rather than
required. The Hub publishes no figure for how many accounts enabled two-factor, how many repositories sign
every commit, or how many deployments pin a revision, and no measurement was found elsewhere; the
organisation cannot tell from a model page whether its producer adopted any of them, except by inspecting
the commit history for verified status and the file listing for formats.

**Three controls guard something other than these threats.** Gating, private visibility and moderation, C14,
C15 and C17, are the controls a reader would expect to meet impersonation and malicious files, and none of
them does. Gating guards the owner's terms and tells the owner who asked; it says nothing about the file.
Private visibility guards the owner's content from others, and may lower the scanning coverage of that
content. Moderation acts after a report, at the platform's discretion, on an undocumented timescale, and the
terms describe nothing for a dependent of a removed repository [HF-01]. For a model held by proxy the
position is narrower still: provider pinning, C18, is the only control the Hub offers, and none of C1 to
C17 follows the key to the partner's copy.

### 3.4 The threats against the controls

**Table 4. Which controls meet each threat, and what remains**

| Threat | Controls that meet it | How | What remains with the organisation |
|---|---|---|---|
| T1 name confusion | C17 | after a report, at the platform's discretion | selecting by a verified producer namespace and a pinned revision rather than by name and popularity; checking the architecture against the name [SC-20] |
| T2 account takeover | C3, C9, C10, C11, C12, C13 | optional at the root (C3, C9); partial around it (C10 to C13); C2 shows the result afterwards | requiring verified commits from the producers it relies on; pinning, so that a takeover changes nothing already deployed |
| T3 malicious serialisation | C5, C6, C7; C8 | advisory, evadable; conversion where the publisher accepted it | refusing pickle; its own scan of what it downloads; a loader with no pickle fall-back |
| T4 parser exploits | none | no scan checks structural validity of GGUF, ONNX or safetensors | a patched loader; its own parser-level checks |
| T5 code and templates | C4 in part | antivirus signatures only; custom code is an ordinary file to the Hub | keeping trust_remote_code off; reading the shipped code and the template; a loader that sandboxes templates |
| T6 malicious adapters | C5 to C8, as for T3 | the same advisory scans; the declared (SCRUM-281) base link is not checked | assessing the model-plus-adapter pair; refusing pickle adapters |
| T7 revision drift | C16; C1, C2, C13 | pinning where adopted; hash, history and refs make a change detectable | pinning a full commit hash in every deployment; recording the hashes it reviewed |
| T8 software during loading | C18 by proxy, in part | provider choice only | everything on the loader's side, which is outside the Hub |

Read down the second column, two threats have no Hub-side control at all, T4 and the in-possession case of
T8, and three more are met only by controls the producer must have adopted. Read down the fourth column, the
organisation's part is the same in every row: hold a revision, hold a hash, refuse the executable formats,
and read what the platform only displays.

## Part 4. Which of these threats transfer to the other repositories

The eight threats were stated against the Hub because the evidence was measured there. Whether each exists
on another platform is a question about that platform's namespace, formats and controls (SCRUM-281), not something to
assume. Part 4 answers it for the two other model repositories, Kaggle and ModelScope, and for four
redistributors (SCRUM-281) through which Hub models reach organisations: the Ollama library, GitHub releases, the
NVIDIA catalogue and Docker Hub. Table 5 gives the answer threat by threat with three marks. *Present*: the
mechanism the threat needs exists on the platform, by the platform's own documentation. *Absent*: the
platform's documentation removes the mechanism. *Not established*: the documentation is silent. A fourth
note, *measured*, marks the one case in which the threat was measured on that platform; everywhere else
"present" means the door is documented open, not that anyone was seen walking through it.

### 4.1 The transfer table

**Table 5. The eight threats on the other platforms**

| Threat | Kaggle Models | ModelScope | Ollama library | GitHub releases | NVIDIA NGC and NIM | Docker Hub, ai namespace |
|---|---|---|---|---|---|---|
| T1 name confusion | present: open account, and a page is created automatically for any Hub model a notebook uses, so a squatted Hub name propagates without an upload [KG-02, KG-01, LD-13] | present: open account; the international site states content is "not verified or approved" [MS-01, MS-02] | present: own namespace per account; curation of the official namespace is not documented [OL-01] | present: repository namespace, open [GH-01] | absent: no community publishing; the catalogue is NVIDIA-curated [CG-11] | absent in the ai namespace, which is Docker's verified publisher; present in every other namespace [DK-02, DK-03] |
| T2 account takeover | not established: one account per user; no statement on a second factor found [KG-02] | not established: one account; no statement found [MS-01] | present: a registered public key is required to push, so the key is the account [OL-03] | present: write permission on the repository [GH-01] | absent for outsiders: no community publishing [CG-11] | present: any account may push to its own namespace [DK-03] |
| T3 malicious serialisation | present: pickle files are hosted and no scanning is documented [KG-04] | present: no scanning documented [MS-05] | absent for the served model, which is GGUF [TX-07] | present: any asset may be attached; no scanning of release assets [GH-10] | present in part: the inference microservice mounts adapters (SCRUM-281) saved as pickle [TX-12, TX-14] | absent for the packaged model, which the runner serves as GGUF [TX-11]; not established for other artefacts |
| T4 parser exploits | present wherever GGUF or ONNX is hosted; follows the format, not the platform | as Kaggle | present: the engine is llama.cpp, the parser with the published overflow [TX-07, SC-14] | present wherever GGUF or ONNX is attached | not established: the engine is NVIDIA's own and was not surveyed | present: the runner's engine is llama.cpp [TX-11, SC-14] |
| T5 code and templates | present: Hub-format repositories carry custom code and templates [KG-01] | present: transformers-format repositories | present in part: the chat template travels inside the GGUF metadata, the route of the llama.cpp binding defect [SC-13] | present: any file may be attached | not established: what runs inside the container is the vendor's, under its signing and bill of materials [CG-12, CG-11] | present in part: as Ollama, through the GGUF template |
| T6 malicious adapters | present: adapter repositories as on the Hub | present | not established: adapter support exists in the runtime, its artefact path was not surveyed | present | present: the microservice mounts adapters of either format into its container [TX-12] | not established |
| T7 revision drift | present: numbered versions exist and a version may be pinned; per-file digest not established [KG-05] | present: git history and revision pinning; per-file hash only through the API; re-uploads carry ModelScope's own hashes, not the producer (SCRUM-281)'s [MS-06, MS-07] | present for tags; a content-addressed manifest with layer digests verified on pull lets a digest be pinned [OL-04, OL-03] | present unless adopted: SHA-256 per asset; immutable releases with a Sigstore attestation are opt-in [GH-05, GH-06, GH-07] | reduced: images signed since 2023 and models since 2025, checksums verified at start; a branch lifecycle moves what a branch serves [CG-12, CG-13, CG-14] | present: nothing documented on signing or digests for model artefacts [DK-01] |
| T8 software during loading | present: in possession (SCRUM-281), the organisation's loader | present | present, with the vendor's loader: the model arrives packaged with llama.cpp [TX-07] | present: in possession | present, with the vendor's loader and container, signed, scanned on a schedule, with a bill of materials by digest [CG-11, CG-12] | present, with the vendor's loader; no scanning or signing documented [DK-01, DK-03] |

### 4.2 What transfers and what does not

**The artefact threats travel with the format.** T3 to T6 need a pickle checkpoint (SCRUM-281), a parser, a shipped
file or an adapter, and nothing else. They exist on any platform that hosts the format, and they are absent
only where the platform fixes the format: the Ollama library and Docker's model runner serve GGUF, which
removes pickle and brings the llama.cpp parser [TX-07, TX-11]. No platform other than the Hub documents a
scan of any of these formats [KG-04, MS-05, OL-09, GH-10, DK-01]; the only scanning outside the Hub is
NVIDIA's partner programme, applied to its own curated catalogue [CG-11].

**The publishing threats depend on the namespace.** T1 and T2 need an open account. They are absent only
at NVIDIA, which has no community publishing, and in Docker's verified ai namespace [CG-11, DK-02]. They are
present on both other model repositories, where they were not measured, and Kaggle adds a route the Hub
lacks: a page created automatically from a Hub name, so that a squatted Hub repository gains a second
address with no act by the squatter [KG-01, LD-13].

**The integrity controls that the Hub leaves optional are standard at three redistributors.** The Ollama
library verifies layer digests on every pull [OL-03], NVIDIA signs images and models and verifies checksums
at start [CG-12, CG-13], and GitHub offers immutable releases with a signed attestation [GH-06]. Each
protects the redistributor's copy, which is a different file from the one the producer published, with the
redistributor's hashes [MS-07, OL-04]. Digests and signatures establish that a file has not changed since
the redistributor took it, not that it is what the card at the source claims.

**The blocking controls exist only at redistributors, on their copies.** Google's model garden blocks
deployment of models the Hub marked unsafe [CG-01]; the newer Microsoft path runs a mandatory malware scan,
refuses models that require custom code and enforces safetensors (SCRUM-281) [CG-09]; AWS custom import and Together AI
custom upload accept safetensors only [CG-07, TA-04]. Three of these lean on the Hub's verdict, so a miss in
the Hub's scan is a miss in theirs [LD-13, LD-27, CG-01].

**Availability is a dependency on every platform.** Kaggle removes without notice [KG-02, KG-03], ModelScope
and the Ollama library act on written notice without a public log [MS-01, OL-02], NVIDIA runs a branch
lifecycle with no stated takedown policy [CG-14], and Docker removes at its discretion [DK-04]. For a model
held by proxy (SCRUM-281), retirement is the same dependency: Together AI gives two to three weeks' notice [TA-01],
Google and AWS run deprecation schedules [CG-02, CG-05], and a model assessed under a key can be withdrawn or
replaced beneath it.

## Part 5. Ratings

Table 6 gives the eight threats with their attributes: layer, level, the access state under which the
organisation is exposed, the model types and formats each applies to, and the confidence label. Table 7
rates orchestration complexity on four axes, access, skill, cost and detectability; the ratings carry the
forecast (SCRUM-281) label.

**Table 6. The eight threats and their attributes** (family: supply-chain and artefact-level throughout)

| Threat | Layer | Level | Organisation exposed | Applies to | Label | Sources |
|---|---|---|---|---|---|---|
| T1 name confusion and typosquatting | publishing | system | both | every model type and format | established on the Hub | SC-19, SC-20, SC-05, SC-29, KG-01 |
| T2 account and name takeover | publishing | system | both; by proxy (SCRUM-281) unseen | every model type and format | established for the routes; frequency not established | SC-02, SC-03, SC-04, SC-01, HF-11, HF-15, SC-05 |
| T3 malicious serialisation | artefact | system | in possession (SCRUM-281) | pickle files of every model type; adapters (SCRUM-281) saved as pickle; every loader that falls back to pickle | established | TX-02, TX-03, HF-06, SC-09 to SC-12, SC-15 to SC-18 |
| T4 format and parser exploits | artefact | system | in possession | GGUF files, chiefly generative and image-and-text models; ONNX files | established for GGUF and ONNX; safetensors (SCRUM-281) parsers not established | SC-14, SV-16, TX-05, TX-07, TX-11 |
| T5 code and templates shipped with the model | artefact | system | in possession | every format when the loader honours custom code; chat templates on instruct and chat models | established | SC-08, LC-01, SV-14, SC-06, SC-07, SC-13, SC-21 |
| T6 malicious adapters | artefact | system; model for the change | in possession | adapter files of every model type | established | TX-14, TX-12, SV-12, HF-14 |
| T7 revision drift | artefact | system | in possession; by proxy the provider's choice | every model type and format | established for the mechanism; frequency of unpinned deployments not measured | HF-17, SV-15, HF-15 |
| T8 software installed or executed during loading | loading | system | in possession, including vendor-packaged; by proxy through the Hub's own serving | every model type and format; engines and containers received instead of a file (SCRUM-281) | established | SC-15, LC-01, SV-12, SV-16, SV-18, SV-23, SC-09 to SC-12, SV-11, SV-13, SV-17, SC-27, HF-18 |

**Table 7. Orchestration complexity** (forecast; higher is harder for the attacker)

| Threat | Access the attacker needs | Skill | Cost | Detectability by the defender |
|---|---|---|---|---|
| T1 name confusion and typosquatting | an account and a similar name | low | low | low: the name is the only signal and it is designed to pass; no organisation verification exists |
| T2 account and name takeover | a producer (SCRUM-281)'s credentials or write token | medium | medium | high where every commit is signed and deployments are pinned; low where they are not, since an intruder's commit looks like the owner's |
| T3 malicious serialisation | an account on the Hub | low: tooling for pickle payloads is public | low | medium: the Hub's scan flags known patterns and has missed new ones |
| T4 format and parser exploits | an account; knowledge of a parser defect | high: a memory-safety exploit per engine version | medium | low: a crafted file looks well formed and no scan reads for it |
| T5 code and templates shipped with the model | an account; the victim must enable custom code, or use an unsandboxed loader | low to medium | low | medium: the code is readable before it is run, if anyone reads it |
| T6 malicious adapters | an account; or the ability to name an adapter path on a dynamic-loading server | low | low | medium: the same scan as T3; the pair, not the file, must be tested; the declared (SCRUM-281) base is unchecked |
| T7 revision drift | the owner's own push, or any write access | low | low | high where a commit hash is pinned and recorded; low where the deployment names only the repository |
| T8 software installed or executed during loading | as T3 or T5; write access to a cache or plugin path for the server-side routes; nothing beyond a request for the by-proxy case | medium | low to medium | low: the installed software is not where model scanners look; by proxy, nothing is visible |

## Part 6. What remains with the organisation

Part 3 showed what the Hub applies and offers, and Table 4 showed, threat by threat, what that leaves undone.
Part 6 names the controls the organisation has to apply on its own side, what each establishes and what it
does not.

**Table 8. Organisation-side controls this family calls for, and their limits**

| Control | Against | What it establishes | What it does not |
|---|---|---|---|
| namespace allow-list and architecture check | T1 | that the account is one the organisation chose; that the architecture matches the name [SC-20] | a squatted name inside an allowed namespace; the first selection, before an allow-list exists |
| require verified commits from relied-on producers (SCRUM-281); token hygiene on the organisation's own accounts | T2 | that a commit was made with the producer's key [HF-11]; reduced blast radius of a leak [SC-03] | the producer's account and its second factor, which the organisation does not control |
| safetensors (SCRUM-281) only, at load and at import | T3, T6 | no code in the container; enforced by Microsoft Foundry, AWS custom import and Together AI upload [CG-09, CG-07, TA-04] | anything about the numbers; the loader's own fall-back to pickle must be off [SV-11, SV-13] |
| restricted loading, weights-only or a policy-based loader | T3 | no arbitrary call during unpickling, on a fixed PyTorch version [TX-03]; a policy loader rejected every malicious sample in one study [SC-18] | the bypass in versions to 2.5.1 [SC-09]; models the policy cannot load, 15 per cent in that sample [SC-18] |
| own scan of the file before load | T3, T6 | the imports a pickle would make; known patterns [HF-06, SC-26] | new patterns and parser bypasses [SC-15, SC-16, SC-18]; engines and containers, which no scanner reads |
| patched loader; parser-level checks | T4 | that the published parser defects are closed [SC-14] | the next defect; no scan exists for structure |
| custom code off by default; read before enabling; pin the code revision; a loader that sandboxes templates | T5, T8 | that the code run is the code reviewed [SV-15, LC-01]; templates in an immutable sandbox [SC-07] | the loader's choice of sandbox, which the file cannot impose [SC-13] |
| assess the model-plus-adapter pair; refuse pickle adapters | T6 | that what is tested is what runs | the declared (SCRUM-281) base, which no repository verifies [HF-14] |
| pin the full commit hash and verify the hash on download; record the hashes reviewed | T7, T2 | that the file is the revision reviewed and arrived intact [HF-17, HF-16] | that the revision is what the card claims; a redistributor (SCRUM-281)'s copy, which has its own hash [MS-07] |
| signatures and attestations where offered | T2, T7 | who published and that it has not changed: GPG commits, Sigstore attestations on GitHub, NVIDIA signing, model-signing manifests of file hashes [HF-11, GH-06, CG-12, CG-13, SC-24] | adoption: optional on the Hub and GitHub, standard only at NVIDIA |
| bill of materials for the model | T7, T8 | a record of what was received: CycloneDX records machine-learning models as components since version 1.5 [SC-25]; NVIDIA ships one per image [CG-11] | its truth, which is declared by whoever wrote it |
| sealed loading environment: no network, no installer, no writable cache or plugin path | T8 | that loading installs nothing and the cache is not writable by others [SV-12] | the native library a graph or a model library legitimately needs [SV-16, SV-23] |
| provider pinning, and the provider's declaration of loader, options and revision | T8 by proxy (SCRUM-281), T7 by proxy | which partner answers [SC-27] | anything the provider does not declare; none of the file-side controls follow the key |

## Source log

The sources this document adds. Each row gives:

- **ID**: the citation key used in the text.
- **Class** (SCRUM-281): *Official*, the platform, maintainer or specification owner writing about its own
  artefact or service, a security advisory included; or *Research*, a paper at an accepted venue, or a
  preprint labelled as such.
- **Source** and **URL**: what was read and where.
- **Verified**: what was checked in it, and the statement the citation rests on.

| ID | Class (SCRUM-281) | Source | URL | Verified |
|---|---|---|---|---|
| SC-01 | Official | Security (overview); Hugging Face Hub documentation | https://huggingface.co/docs/hub/security | [CHECKED] lists access tokens, 2FA, passkeys, SSH, GPG signing, SSO, resource groups, malware scanning, pickle scanning, secrets scanning, Protect AI and JFrog scanners; SOC 2 Type 2 stated |
| SC-02 | Official | Two-Factor Authentication (2FA); Hugging Face | https://huggingface.co/docs/hub/security-2fa | [CHECKED] "If you choose to enable two-factor authentication": optional; passkey or authenticator app; recovery codes |
| SC-03 | Official | User access tokens; Hugging Face | https://huggingface.co/docs/hub/security-tokens | [CHECKED] fine-grained, read and write roles; "Try not to leak your token"; one token per use and fine-grained tokens recommended for production; POST /api/credentials/revoke invalidates any found token without rights over the owning account |
| SC-04 | Official | Secrets Scanning; Hugging Face | https://huggingface.co/docs/hub/security-secrets | [CHECKED] TruffleHog on each push; e-mail on verified secrets only; no blocking statement |
| SC-05 | Official | Repository Settings; Hugging Face | https://huggingface.co/docs/hub/repositories-settings | [CHECKED] "Transferring or renaming a repo will automatically redirect the old URL to the new location"; reuse of a deleted name: not stated → [NOT ESTABLISHED] |
| SC-06 | Official | Writing a chat template; transformers documentation | https://huggingface.co/docs/transformers/chat_templating_writing | [CHECKED] a chat template is a Jinja template stored in the tokenizer, saved as chat_template.jinja and pushed with the model; callables raise_exception and strftime_now; legacy embedding in tokenizer_config.json still loaded Read from documentation later than the research cut-off; admitted because the template file and its sandbox predate it. |
| SC-07 | Official | chat_template_utils.py, transformers source, main branch | https://raw.githubusercontent.com/huggingface/transformers/main/src/transformers/utils/chat_template_utils.py | [CHECKED] `from jinja2.sandbox import ImmutableSandboxedEnvironment`; `jinja_env = ImmutableSandboxedEnvironment(`; the documentation page does not state the sandbox Read from the library's main branch, later than the research cut-off; admitted because the sandbox predates it. |
| SC-08 | Official | Customizing models; transformers documentation | https://huggingface.co/docs/transformers/custom_models | [CHECKED] modeling.py and configuration.py are uploaded with the weights; loading requires trust_remote_code=True; confirms LC-01 on the later version Read from documentation later than the research cut-off; admitted because the custom-code flag predates it, and LC-01 supports it independently. |
| SC-09 | Official | GHSA-53q9-r3pm-6pq6, "torch.load with weights_only=True RCE", CVE-2025-32434; PyTorch | https://github.com/pytorch/pytorch/security/advisories/GHSA-53q9-r3pm-6pq6 | [CHECKED] affected ≤ 2.5.1, patched 2.6.0, severity critical; "When loading model using torch.load with weights_only=True, it can still achieve RCE" |
| SC-10 | Official | GHSA-37q5-v5qm-c9v8, CVE-2024-3568; transformers | https://api.osv.dev/v1/vulns/CVE-2024-3568 (advisory record) | [CHECKED] pickle.load in load_repo_checkpoint of TFPreTrainedModel; fixed 4.38.0 |
| SC-11 | Official | GHSA-wrfc-pvp9-mr9g, CVE-2024-11393, MaskFormer deserialisation; transformers | https://api.osv.dev/v1/vulns/CVE-2024-11393 (advisory record) | [CHECKED] deserialisation of untrusted data in model file parsing; fixed 4.48.0; CVSS 3.0 vector AV:N/AC:L/PR:N/UI:R, high |
| SC-12 | Official | GHSA-rh4j-5rhw-hr54, CVE-2025-24357, "Malicious model to RCE by torch.load in hf_model_weights_iterator"; vLLM | https://github.com/vllm-project/vllm/security/advisories/GHSA-rh4j-5rhw-hr54 | [CHECKED] torch.load with weights_only at its default of False on downloaded checkpoints; fixed 0.7.0; high, CVSS 7.5; "most models now use the safetensors format, which is not vulnerable to this issue" |
| SC-13 | Official | GHSA-56xg-wfcc-g829, CVE-2024-34359, "Remote Code Execution by Server-Side Template Injection in Model Metadata"; llama-cpp-python | https://github.com/abetlen/llama-cpp-python/security/advisories/GHSA-56xg-wfcc-g829 | [CHECKED] tokenizer.chat_template read from GGUF metadata and rendered in a "sandbox-less jinja2.Environment"; affected 0.2.30 to 0.2.71, patched 0.2.72; critical, CVSS 9.6 |
| SC-14 | Official | GHSA-vgg9-87g3-85w8, CVE-2025-53630, "Integer Overflow in GGUF Parser can lead to Heap Out-of-Bounds Read/Write"; llama.cpp (ggml-org) | https://api.osv.dev/v1/vulns/CVE-2025-53630 (advisory record) | [CHECKED] gguf_init_from_file_impl in ggml/src/gguf.cpp; all builds before fix commit 26a48ad6; CVSS 4.0 vector AV:N/AC:L/PR:N/UI:N, high impact |
| SC-15 | Official | CVE-2025-1716 (with CVE-2025-1889), picklescan bypass via pip.main; picklescan | https://api.osv.dev/v1/vulns/CVE-2025-1716 (advisory record) | [CHECKED] before 0.0.21 pip was not an unsafe global, so a pickle could install a package and be reported safe |
| SC-16 | Official | GHSA-9gvj-pp9x-gcfr, CVE-2025-71325, "Picklescan has pickle parsing logic flaw that leads to malicious pickle file bypass"; picklescan | https://github.com/advisories/GHSA-9gvj-pp9x-gcfr | [CHECKED] STACK_GLOBAL handling in _list_globals; below 0.0.27; high, CVSS 4.0 8.9; "it also affects the online hugging face pickle scanners" and modelscan. The statement about the Hub's scanner is the maintainer's about another party's service: emerging |
| SC-17 | Research | Zhao, Wang, Zhao, Hou, Wang, Gao, Zhang, Wei, Wang. "Models Are Codes: Towards Measuring Malicious Code Poisoning Attacks on Pre-trained Model Hubs". ASE 2024 | https://arxiv.org/abs/2409.09368 | [CHECKED] MalHug on a mirrored Hugging Face instance for over three months; more than 705K models and 176K datasets monitored; 91 malicious models and 9 malicious dataset-loading scripts; reverse shells, browser credential theft, reconnaissance |
| SC-18 | Research | Kellas, Christou, Jiang, Li, Simon, David, Kemerlis, Davis, Yang. "PickleBall: Secure Deserialization of Pickle-based Machine Learning Models". ACM CCS 2025; extended report arXiv:2508.15987 | https://arxiv.org/abs/2508.15987 | [CHECKED] 44.9 per cent of popular Hugging Face models still use pickle; 15 per cent of those cannot load under restrictive policies; scanners evaluated missed known malicious models; PickleBall loads 79.8 per cent of benign models and rejects all malicious samples |
| SC-19 | Research | Li, Zhao, Wang, Wu, Wang. "Exploring Typo Squatting Threats in the Hugging Face Ecosystem". Internetware 2025, research track | https://conf.researchr.org/details/internetware-2025/internetware-2025-research-track/42/Exploring-Typo-Squatting-Threats-in-the-Hugging-Face-Ecosystem | [CHECKED] 1,020,755 models against the top 100 by downloads: 1,574 squatting candidates, 10.4 per cent with suspicious or harmful characteristics; 219,812 datasets: 625 cases; 127,011 organisations: 302 with squatting patterns; findings reported to Hugging Face. No preprint or DOI on the page |
| SC-20 | Research | Jiang, Kim, Cheung, Kim, Thiruvathukal, Davis. "An empirical study of pre-trained model naming conventions, plus a tool for improving naming consistency". Empirical Software Engineering 30, 155 (2025); arXiv:2310.01642 | https://arxiv.org/abs/2310.01642 | [CHECKED] survey of 108 Hub users; names often inconsistent with architecture; DARA identifies model type from architecture at 94 per cent; typosquatting raised as future work, no incident cited |
| SC-21 | Research, preprint | Siddiq, Romel, Sekerak, Casey, Santos. "An Empirical Study on Remote Code Execution in Machine Learning Model Hosting Ecosystems". arXiv:2601.14163 | https://arxiv.org/abs/2601.14163 | [PARTIAL] abstract: custom model loading across five platforms, static analysis and YARA, over 600 developer discussions; "unsafe defaults", uneven enforcement, developer confusion. Prevalence figures are in the body, not read: emerging |
| SC-22 | Research, preprint | Casey, Santos, Mirakhorli. "A Large-Scale Exploit Instrumentation Study of AI/ML Supply Chain Attacks in Hugging Face Models". arXiv:2410.04490 | https://arxiv.org/abs/2410.04490 | [PARTIAL] abstract: measures unsafe serialisation on the Hub and whether the platform flags it; counts in the body, not read: emerging; cited for framing only |
| SC-23 | Research | Wang, Zhao, Hou, Wang. "Large Language Model Supply Chain: A Research Agenda". ACM TOSEM; arXiv:2404.12736 | https://arxiv.org/abs/2404.12736 | [CHECKED] defines the supply chain across infrastructure, foundation models and downstream applications; cited for the framing of 1.1 only |
| SC-24 | Official | model-transparency (Model Signing); sigstore | https://github.com/sigstore/model-transparency | [CHECKED] signs "a list of (file path, digest) pairs" as an in-toto statement in a Sigstore bundle; Sigstore, keys, certificates or PKCS #11; no adoption statement on the page |
| SC-25 | Official | "Introducing OWASP CycloneDX v1.5"; OWASP CycloneDX | https://cyclonedx.org/news/cyclonedx-v1.5-released | [CHECKED] machine-learning model becomes a component type; "understand and verify the training and deployment methods employed"; training-data fields not detailed on the page |
| SC-26 | Official | modelscan; Protect AI | https://github.com/protectai/modelscan | [CHECKED] scans H5, pickle and pickle-derived, SavedModel; byte-pattern search for unsafe operators; Apache-2.0; GGUF not listed |
| SC-27 | Official | Inference Providers (overview); Hugging Face | https://huggingface.co/docs/inference-providers/index | [CHECKED] eighteen partner providers listed; "your requests go through Hugging Face's proxy infrastructure"; fastest serving provider selected by default with automatic failover; one Hub token for all |
| SC-28 | Official | Pull requests and Discussions; Hugging Face Hub documentation | https://huggingface.co/docs/hub/repositories-pull-requests-discussions | [CHECKED] "contributors push to a special ref branch directly on the source repo"; refs such as refs/pr/42 "are not fetched (by default) by people (including the repo owner) cloning the repo"; editing, pinning and locking require being the author of the repository or having write access; pull requests and discussions "can be enabled or disabled from the repository settings" |
| SC-29 | Official | Organizations; Hugging Face Hub documentation | https://huggingface.co/docs/hub/organizations | [CHECKED] organisations "group accounts and manage datasets, models, and Spaces", admins set user roles, billing; no verification or identity-proof step described on the page or in its contents list |

Searched and not found, recorded for the log: a maintainer advisory for a 2024 GGUF parser defect in
llama.cpp (the search returned 2025 and 2026 advisories only; SC-14 is cited); a documented statement on
whether a deleted Hugging Face repository name can be re-registered by another account; any published
measurement of post-publication tampering frequency on a model repository. Press and blog coverage of
malicious models, scanner bypasses and typosquatting exists in quantity and is excluded under the citation
policy; it motivated the searches above and nothing more.

## Symbols from outside this document

| Symbol | Meaning | Defined in | File |
|---|---|---|---|
| (SCRUM-281) after a term | the term is a glossary term; shown at its first use in each part | SCRUM-281, report style guide and glossary, version 1.3, section 1 | governing/report-style-guide-and-glossary.md |
| established, emerging, forecast | confidence labels | SCRUM-281, section 2.3 | governing/report-style-guide-and-glossary.md |
| Official, Research | citation classes | SCRUM-281, section 2.2, Table 2.1 | governing/report-style-guide-and-glossary.md |
| (SCRUM-284) after a question or evidence item | defined in the lifecycle assessment framework | SCRUM-284 | process/scrum-284/scrum284.md |
| Q1.1 to Q4.4 | lifecycle assessment questions | SCRUM-284 | process/scrum-284/scrum284.md |
| e1.1 to e1.10 | evidence items for stage 1 | SCRUM-284 | process/scrum-284/scrum284.md and stage-tables.md |
| [LC-nn] | lifecycle framework sources | SCRUM-284 | process/scrum-284/scrum284.md |
| [HF-nn] | Hugging Face Hub sources | SCRUM-280 | process/scrum-280/scrum280.md |
| [KG-nn] | Kaggle sources | SCRUM-280 | process/scrum-280/scrum280.md |
| [MS-nn] | ModelScope sources | SCRUM-280 | process/scrum-280/scrum280.md |
| [OL-nn] | Ollama sources | SCRUM-280 | process/scrum-280/scrum280.md |
| [GH-nn] | GitHub sources | SCRUM-280 | process/scrum-280/scrum280.md |
| [DK-nn] | Docker Hub sources | SCRUM-280 | process/scrum-280/scrum280.md |
| [TA-nn] | TensorFlow Hub sources | SCRUM-280 | process/scrum-280/scrum280.md |
| [CG-nn] | NVIDIA catalogue and cloud garden sources | SCRUM-280 | process/scrum-280/scrum280.md |
| [TX-nn] | format and loader sources | SCRUM-280 | process/scrum-280/scrum280.md |
| [LD-nn] | landscape comparison sources | SCRUM-280, landscape | landscape/landscape-platform-comparison.md |
| [SV-nn] | inference server and compiled artefact sources | landscape | landscape/serving-and-compiled-artefacts.md |
| [EC-nn] | ecosystem quantification sources | SCRUM-286 | process/scrum-286/scrum286.md |
| 4.2, 4.3, 4.4, 4.5, 5.1, 5.2, 6.1, 6.2, 7.x, 9.2 | section numbers of the report skeleton, version 0.2 | skeleton | skeleton/nk_dans_incd_report.docx |
