# AI Agent Guides

A small collection of guides about choosing and building agents for internal tools and knowledge retrieval.

There are plenty of ways to get a tool call working. These notes spend more time on the next questions: what should the tool be allowed to do, how do you check its result, and when is a framework worth adding?

[Read in English](docs/en/README.md) · [繁體中文](docs/zh-Hant/README.md)

## Where to start

If you want to run something, start with [the tool-loop example](docs/en/02-bounded-lookup.md). It uses two invented documents and scripted proposals, so you can follow the whole execution without a model or API key.

For the design questions, read:

- [Choosing an approach](docs/en/01-selection.md) — which options fit the task, and which add work you may not need.
- [Comparing frameworks](docs/en/03-framework-workshop.md) — how to give a direct implementation, Pydantic AI and LangGraph a fair comparison.
- [A Pi coding exercise](docs/en/04-pi-workshop.md) — how to ask for a small change and check the resulting patch.
- [Choosing a retrieval design](docs/en/05-retrieval-design.md) — when to consider agent routing or graph-based retrieval.

Those four chapters explain the reasoning and give exercises. The framework, Pi and retrieval integrations have not been run here yet; their implementation work is tracked in the [roadmap](ROADMAP.md).

## Run the example

From the repository root:

```sh
python3 examples/bounded_lookup/run.py
python3 -m unittest discover -s tests -v
```

The example uses Python's standard library. It has been tested on CPython 3.14.5; other versions have not been checked. There is nothing to install beyond Python, and the example makes no network calls.

Look at the four results: a normal lookup, a retry after a simulated failure, a lookup filtered by the caller's simulated role, and a loop stopped by its step budget. This is a teaching fixture, not a model-powered agent or a real access-control system. The [validation record](evidence/VALIDATION.md) includes the test output and remaining limits.

## How these notes are maintained

English is the source language; Traditional Chinese is the companion translation. Technical corrections should reach both. Japanese is planned.

The [sources](docs/SOURCES.md) link to the official documentation used in the guides. The [audit notes](evidence/CONTENT_AUDIT.md) record corrections and distinguish what was read from what was actually run. If you add a lesson, use the [tutorial template](docs/TUTORIAL_TEMPLATE.md) and [contribution notes](CONTRIBUTING.md).

## Related work

For larger examples, look at [AgentChaos](https://github.com/jeffery0929/agentchaos) for fault injection, [TraceGraphBench](https://github.com/jeffery0929/TraceGraphBench) for trace analysis, and [Cloud Agent Platform](https://github.com/jeffery0929/cloud-agent-platform) for an agent-execution reference MVP. Each has its own setup and validation records.

[Consulting services](https://jeffery0929.github.io/services/) · [GitHub profile](https://github.com/jeffery0929)
