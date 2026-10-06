# Serving software and compiled artefacts

Evidence and proposals for the layer between the model file and the answer: the software that
executes a model, and the artefacts that software consumes or produces. Research cut-off and access
date 2026-10-06. Source identifiers resolve in §5. Companion to `landscape-platform-comparison.md`.

Written because the taxonomy's four storage formats do not describe everything an organisation can
receive, and because a reader who meets vLLM or TensorRT-LLM in a later chapter needs to have been
told what they are.

---

## 1. The three things that get confused

| Canonical term | Definition | Technical anchor | Avoid |
|---|---|---|---|
| inference server | software that loads a published model file and executes it, either embedded in an application as a library or run as a standalone service exposing an API. It determines throughput, memory behaviour and the shape of the interface. It does not alter the model's parameters and is not part of what the organisation received with the model | vLLM, SGLang, Text Generation Inference, the llama.cpp server, Ollama's server | *framework*, reserved here for ATLAS, OWASP, NIST and ISO; *runtime* alone, since §4.4 uses it for inference time; listing it among artefact formats |
| build toolchain | software that compiles a published checkpoint into a target-specific artefact that must exist before the model can run on that target | the TensorRT-LLM builder (`trtllm-build`), the ExecuTorch exporter, the MLC compiler | treating the build as packaging rather than transformation |
| compiled engine | the output of a build toolchain: an executable artefact bound to a hardware target, a library version and a host platform, which cannot be scanned by the tools that read weight files | a serialized TensorRT engine or "plan"; an ExecuTorch `.pte`; an MLC model library | calling it a storage format; assuming it is portable; asserting that the weights inside it are either protected or extractable |

**vLLM and SGLang are the same kind of thing**, and neither produces anything distributable. Both load
a checkpoint and serve it. **TensorRT-LLM is not parallel to them**: it is a compiler as well as a
runtime, and it emits an artefact that did not previously exist.

## 2. Two corrections to earlier drafts

**An engine's opacity is *not established*, not proven.** An earlier version of the glossary row above
said the original checkpoint "is not recoverable by inspection" from an engine. The evidence does not
support that. NVIDIA documents writing weights *into* a plan through the refit interface, and
enumerating refittable weights through `getAllWeights()` [SV-05]; it documents *omitting* them, in
weight-stripped plans [SV-05]; it states nothing about whether the full original weights can be
recovered from an ordinary engine [SV-06]. The report should say that no confidentiality claim and no
extraction guarantee is documented, and leave it there. What *is* established is that an engine is a
binary that existing weight-level inspection tooling cannot read.

**Compiled engines are distributed, so they belong in Chapter 3 after all.** I had treated this as
open, on the view that an artefact only matters to the landscape chapter if an organisation receives
it. It does receive it. NVIDIA NIM "downloads pre-compiled TensorRT-LLM engines for optimized
profiles", falling back to downloading raw weights and compiling locally only for generic profiles
[SV-10]; and a Hugging Face organisation publishes "prebuilt TensorRT-LLM compatible engines" with
branches per GPU [SV-07].

## 3. Findings

**Non-portability is the defining property, and it is documented on three independent axes.** By
default a TensorRT engine is compatible only with the version of TensorRT that built it, only with the
type of device it was built on, and only with the operating system and CPU architecture of the build
host [SV-01, SV-02, SV-03]. Each restriction can be relaxed at a stated performance cost, and the
support matrix repeats the point: "Serialized engines are not portable across platforms" [SV-04].

The consequence for assessment is the one that matters. A defender's cheapest integrity check on a
compiled artefact is to rebuild it and compare. Hardware and version pinning removes that check unless
the defender holds the identical stack. It also means a received engine is useless to anyone whose
hardware differs, which narrows the blast radius of a tampered one.

**Engine distribution is concentrated in vendor channels, where the community scanning does not
reach.** Hugging Face has no library filter for TensorRT-LLM at all, zero results [SV-08], and the 230
repositories tagged `tensorrt` are mostly diffusion models [SV-09]. The real channel is NGC and NIM.
Everything the platform comparison establishes about repository-side scanning therefore does not apply
to engines: there is no pickle scanner equivalent for a plan file.

**Loading a model can execute code in every serving path examined.** The clearest vendor statement is
Intel and Hugging Face's: the trust-remote-code option "will execute on your local machine arbitrary
code present in the model repository" [SV-14]. vLLM and SGLang both carry the same flag [SV-11,
SV-13], Text Generation Inference adds the mutable-revision warning and advises pinning a revision
[SV-15], and ONNX Runtime loads arbitrary native libraries into the session to provide custom
operators [SV-16]. All three engines also fall back to the pickle-based PyTorch format when
safetensors is absent [SV-11, SV-13, SV-17], so the pickle surface in the platform table reaches every
runtime.

**vLLM's plugin system is executed code by design.** Plugins are discovered through Python entry
points and vLLM states that an endpoint plugin "must be treated as part of the server's trusted code
base and not as sandboxed or reviewed input", and can shadow a core route [SV-12]. Dynamic adapter
loading is documented as "not a secure operation" for deployments exposed to untrusted clients
[SV-12].

**The overlooked artefact is the one the defender builds themselves.** vLLM compiles by default and
persists compiled graphs and kernels to a cache directory [SV-18]. Its own security page states that
cache contents are "loaded without cryptographic integrity verification, including formats that
support arbitrary code execution", and that an attacker able to write to the cache "may be able to
crash vLLM or cause it to execute arbitrary code" [SV-12]. This is a compiled artefact created on the
defender's own machine and trusted implicitly. It is a candidate finding in its own right, and it
belongs in §4.4 and §5.4 rather than in the landscape.

## 4. Where each piece lands in the skeleton

| Piece | Section | Why |
|---|---|---|
| the explanatory passage below | Chapter 3, with the consumption material | the reader must know what executes a model before §4.4 names one |
| compiled engine as an artefact received | 3.1, as a distribution channel; a row in the platform comparison for NGC/NIM | it is received, from a vendor channel, with no repository-side scanning |
| the three storage-format rows stay as they are | 3.2 | an engine is not how parameters are stored, so Axis B keeps its four values |
| trust-remote-code, plugins, custom operators, pickle fallback | 4.4 | the skeleton asks that section for the model-level versus system-level boundary, and this is the system level |
| the locally built compile cache | 4.4 and 5.4 | a control that survives contact with production has to cover the artefacts production creates |
| non-portability removes rebuild-and-compare | 6.3 and 7.4 | what is attestable, and what access a test needs |
| ExecuTorch `.pte` | 3.2, if the edge is in scope | "a `.pte` file specialized for that hardware" [SV-19]; 746 repositories on the Hub |
| OpenVINO IR, MLX, Core ML | 3.2 storage formats, not compiled | converted or containerised storage, device chosen at load [SV-20, SV-21, SV-22] |
| MLC model library | 4.2 | a per-platform native library shipped beside portable weights: executable code distributed as part of "a model" [SV-23] |

## 5. Proposed passage for the reader

> So far this chapter has described a file. A file does nothing. It is a large table of numbers, and
> producing an answer from it takes a second piece of software that loads those numbers and performs
> the arithmetic, token by token. That software is the **inference server**. The organisation chooses
> it, installs it, configures it and patches it, separately from the model, and it has its own
> releases, its own defects and its own published vulnerabilities. Several are in common use: vLLM,
> SGLang, Text Generation Inference, and the llama.cpp family that Ollama is built on.
>
> Three things follow, and the later chapters depend on all of them.
>
> The inference server decides what the outside world can reach. It is the component that exposes an
> interface, so it, rather than the model, determines whether a caller sees only generated text or can
> reach further.
>
> Loading a model is not a passive act. Each of these servers offers an option that runs code supplied
> alongside the model, documented by one vendor in these terms: it "will execute on your local machine
> arbitrary code present in the model repository". Each will also load the older pickle format when a
> safe one is absent.
>
> On some hardware the file cannot be loaded at all until it has been compiled into a form built for
> that specific hardware. The result is an **engine**, and it is not interchangeable: by default it
> runs only on the device type, the library version and the operating system it was built for. An
> engine can be received ready-made from a vendor rather than built locally, and when it is, none of
> the repository scanning described earlier in this chapter applies to it.

## 6. Source log

| ID | Class | Title | Publisher | URL | Date / version | Tag | Verified |
|---|---|---|---|---|---|---|---|
| SV-01 | S4 | Engine Compatibility, NVIDIA TensorRT | NVIDIA | https://docs.nvidia.com/deeplearning/tensorrt/latest/inference-library/engine-compatibility.html | docs 11.3.0 | [CHECKED] | "By default, TensorRT engines are compatible only with the version of TensorRT used to build them"; forward-only within a major version; version-compatible engines can be slower |
| SV-02 | S4 | Engine Compatibility | NVIDIA | as SV-01 | 11.3.0 | [CHECKED] | "By default, TensorRT engines are only compatible with the type of device where they were built"; `kAMPERE_PLUS` and `kSAME_COMPUTE_CAPABILITY` relax it at a throughput or latency cost |
| SV-03 | S4 | Engine Compatibility | NVIDIA | as SV-01 | 11.3.0 | [CHECKED] | "engines can only be executed on the same platform (operating system and CPU architecture) where they were built"; a cross-platform engine "cannot run on the host platform it was built on" |
| SV-04 | S4 | Support Matrix, NVIDIA TensorRT | NVIDIA | https://docs.nvidia.com/deeplearning/tensorrt/latest/getting-started/support-matrix.html | 11.3.0 | [CHECKED] | "Serialized engines are not portable across platforms"; without hardware-compatibility mode "engines are not portable across different GPU architectures" |
| SV-05 | S4 | Refitting an Engine | NVIDIA | https://docs.nvidia.com/deeplearning/tensorrt/latest/inference-library/refitting-engines.html | 11.x | [PARTIAL] | refit writes new weights without rebuilding; `getAllWeights()` returns refittable weights; weight-stripped plans omit weights for later refit. Does not state that full original weights can be dumped from an ordinary engine |
| SV-06 | — | searched: Engine Compatibility, Support Matrix, Advanced Topics, Refitting an Engine, web | NVIDIA | — | 2026-10-06 | [NOT ESTABLISHED] | no documented claim that original weights are recoverable from a standard serialized engine, and none that they are protected |
| SV-07 | S4 | optimum-nvidia organisation page | Hugging Face / NVIDIA | https://huggingface.co/optimum-nvidia | repos 2024 | [CHECKED] | "prebuilt TensorRT-LLM compatible engines for various fondational models" [sic], with hardware-specific branches |
| SV-08 | S4 | Models, library=tensorrtllm | Hugging Face | https://huggingface.co/models?library=tensorrtllm | 2026-10-06 | [CHECKED] | count shown 0, "No results found" |
| SV-09 | S4 | Models, other=tensorrt | Hugging Face | https://huggingface.co/models?other=tensorrt | 2026-10-06 | [CHECKED] | count shown 230; visible examples mostly diffusion models |
| SV-10 | S4 | Model Profiles, NIM for LLMs 1.8.0; Model Profiles and Selection, latest | NVIDIA | https://docs.nvidia.com/nim/large-language-models/1.8.0/profiles.html ; https://docs.nvidia.com/nim/large-language-models/latest/deployment/model-profiles-and-selection.html | 1.8.0 updated 2026-01-14; latest updated 2026-10-06 | [CHECKED] | "NIM for LLMs downloads pre-compiled TensorRT-LLM engines for optimized profiles"; local-build profiles "download the raw model weights and perform compilation on the local system"; backend per profile is vllm, sglang or trtllm |
| SV-11 | S4 | Engine Arguments; Supported Models | vLLM | https://docs.vllm.ai/en/latest/configuration/engine_args.html ; https://docs.vllm.ai/en/latest/models/supported_models/ | supported-models page 2026-10-05 | [CHECKED] | `--load-format auto` "tries safetensors first, falls back to pytorch bin"; `--trust-remote-code` "Trust remote code (e.g., from HuggingFace) when downloading the model and tokenizer", default False; remote code recommended for models not natively supported |
| SV-12 | S4 | Security | vLLM | https://docs.vllm.ai/en/latest/usage/security.html | 2026-10-03 | [CHECKED] | an endpoint plugin "must be treated as part of the server's trusted code base and not as sandboxed or reviewed input" and can shadow a core route; "Cache contents are loaded without cryptographic integrity verification, including formats that support arbitrary code execution"; a writable cache directory may let an attacker "cause it to execute arbitrary code"; "Dynamic LoRA loading is not a secure operation"; a Ray cluster is one trust domain |
| SV-13 | S4 | Server Arguments; Model Loading | SGLang | https://docs.sglang.io/docs/advanced_features/server_arguments.md ; https://docs.sglang.io/docs/advanced_features/model_loading.md | no date shown | [CHECKED] | `--trust-remote-code` "allow for custom models defined on the Hub in their own modeling files", default False; load formats include `pt` and `gguf`, with the same safetensors-then-pickle fallback |
| SV-14 | S4 | Export your model, Optimum Intel / OpenVINO | Hugging Face and Intel | https://huggingface.co/docs/optimum/en/intel/openvino/export | no date shown | [CHECKED] | trust-remote-code "should only be set for repositories you trust and in which you have read the code, as it will execute on your local machine arbitrary code present in the model repository" |
| SV-15 | S4 | Text-generation-launcher arguments; Text Generation Inference | Hugging Face | https://huggingface.co/docs/text-generation-inference/en/reference/launcher ; https://huggingface.co/docs/text-generation-inference/en/index | no date shown | [CHECKED] | `--trust-remote-code` executes hub modelling code, with explicit revision pinning "encouraged ... to ensure no malicious code has been contributed in a newer revision"; custom CUDA kernels tested only on one GPU; the project is in maintenance mode |
| SV-16 | S4 | Custom operators | ONNX Runtime (Microsoft) | https://onnxruntime.ai/docs/reference/operators/add-custom-op.html | no date shown | [CHECKED] | a session registers a custom-ops library by path; the shared library exports `RegisterCustomOps` and is loaded into the inference process |
| SV-17 | S4 | Checkpoint Loading; trtllm-build | NVIDIA | https://nvidia.github.io/TensorRT-LLM/features/checkpoint-loading.html ; https://nvidia.github.io/TensorRT-LLM/commands/trtllm-build.html | build page updated 2026-06-27 | [CHECKED] | loads `.safetensors/.bin/.pth`, so the pickle path reaches it; `trtllm-build` takes a checkpoint directory and writes "the serialized engine files and engine config file" |
| SV-18 | S4 | torch.compile integration | vLLM | https://docs.vllm.ai/en/latest/design/torch_compile.html | 2026-09-24 | [CHECKED] | compilation is on by default in V1 and "a critical part of the framework"; artefacts persist under a hashed cache directory containing the transformed graph and compiled kernels |
| SV-19 | S4 | ExecuTorch documentation, Getting Started, Backends | PyTorch | https://docs.pytorch.org/executorch/stable/index.html ; .../getting-started.html ; .../backends-overview.html | stable, no date shown | [CHECKED] | export produces "a `.pte` file specialized for that hardware"; a separate file per backend is typical. Hub: 746 repositories under library=executorch |
| SV-20 | S4 | Export your model, Optimum Intel | Hugging Face and Intel | https://huggingface.co/docs/optimum/en/intel/openvino/export | no date shown | [PARTIAL] | OpenVINO IR is an `.xml` topology plus a `.bin` of weights, converted ahead of time or on load. First-party docs.openvino.ai pages returned navigation only on five attempts, so Intel is not the citation. Hub: 3,080 repositories under library=openvino |
| SV-21 | S4 | MLX documentation, saving and loading | Apple | https://ml-explore.github.io/mlx/build/html/index.html | 0.32.3 | [CHECKED] | stores and loads `.npy`, `.npz`, `.safetensors` and `.gguf`; no compiled artefact. Hub: 25,402 repositories under library=mlx |
| SV-22 | S4 | Convert Models to ML Programs, Core ML Tools | Apple | https://apple.github.io/coremltools/docs-guides/source/convert-to-ml-program.html | coremltools 8 | [PARTIAL] | an ML program saves as an `.mlpackage` container that separates weights from architecture; the on-device compiled form is not described on the pages fetched. Hub: 2,442 repositories under library=coreml |
| SV-23 | S4 | Compile Model Libraries; Convert Model Weights | MLC AI | https://llm.mlc.ai/docs/compilation/compile_models.html ; https://llm.mlc.ai/docs/compilation/convert_weights.html | 0.1.0 | [CHECKED] | a model library is compiled per platform to `.so`, `.dll`, `.tar` or `.wasm` and carries the inference logic, while "all platforms can share the same compiled/quantized weights" |

Unreachable or redirected, recorded for the log: `nvidia.github.io/TensorRT-LLM/latest/commands/trtllm-build.html` and `.../inference-library/refitting-engine.html` return 404, the working URLs being those above; all five `docs.openvino.ai` pages tried returned navigation only; the SGLang landing page carries no topic links, its index being `docs.sglang.io/llms.txt`.
