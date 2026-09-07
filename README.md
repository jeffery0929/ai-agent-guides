# AI Agent Guides

**Choose an approach for the task. Understand why it fits. Test how it fails.**

Practical notes and small examples for enterprise AI automation, tool-using agents and knowledge retrieval. Start with the workflow, data and acceptance criteria before choosing a framework.

[繁體中文教學入口](docs/zh-Hant/README.md) · [Consulting services](https://jeffery0929.github.io/services/) · [Engineering projects](https://github.com/jeffery0929)

## What you can read and run today

| Resource | What you will learn | Evidence |
|---|---|---|
| [Scenario-based selection](docs/zh-Hant/01-selection.md) | Separate coding tools, orchestration frameworks and retrieval architectures; compare when each helps | Source-backed design guidance; no performance ranking |
| [Bounded tool-loop tutorial](docs/zh-Hant/02-bounded-lookup.md) | Validate proposals, filter synthetic records, trace failures and stop a loop | Runnable Python standard-library fixture and tests |
| [Framework comparison workshop](docs/zh-Hant/03-framework-workshop.md) | Design the same internal-service task for LangGraph, Pydantic AI and a direct implementation | Step-by-step experiment design; SDK implementations pending |
| [Pi coding-agent exercise](docs/zh-Hant/04-pi-workshop.md) | Plan a reviewable coding task and evaluate its patch and tool use | Manual exercise protocol; Pi execution not yet verified here |
| [RAG architecture workshop](docs/zh-Hant/05-retrieval-design.md) | Decide among retrieval pipelines, Agentic RAG and graph-based retrieval | Design exercise; no connected model or graph index |

## Run the first example

From the repository root, using Python 3.11+:

```sh
python3 examples/bounded_lookup/run.py
python3 -m unittest discover -s tests -v
```

No installation, model credentials or network calls. The script uses **synthetic data and scripted proposals**, not an LLM. It teaches the execution boundary that an actual agent would need. See [validation](evidence/VALIDATION.md) for the runtime actually tested.

The cases demonstrate normal completion, one injected tool failure followed by retry, role filtering and a step-budget stop. A passing fixture proves those local contracts only.

## Curriculum and maintenance

- [Roadmap](ROADMAP.md): a complete baseline first; bounded framework experiments next.
- [Tutorial template](docs/TUTORIAL_TEMPLATE.md): prerequisites, decisions, execution, failure cases and verification.
- [Sources](docs/SOURCES.md): official documentation checked on 2026-09-07.
- [Contribution rules](CONTRIBUTING.md): cite exact versions and preserve unverified boundaries.

Detailed teaching currently starts in Traditional Chinese; this English landing page supports discovery. English and Japanese full tutorials are planned after the runnable examples and Chinese explanations stabilize.

## Related engineering work

[AgentChaos](https://github.com/jeffery0929/agentchaos) explores fault injection and agent diagnostics. [TraceGraphBench](https://github.com/jeffery0929/TraceGraphBench) explores trace graphs and deterministic evaluation. [Cloud Agent Platform](https://github.com/jeffery0929/cloud-agent-platform) documents an agent-execution reference MVP. These are separate projects; this guide does not rerun or certify them.
