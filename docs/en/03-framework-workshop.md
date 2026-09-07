# 03 — Compare frameworks on the same task

[Guide index](README.md) · [繁體中文](../zh-Hant/03-framework-workshop.md)

This is an experiment-design workshop. No LangGraph or Pydantic AI SDK run has been performed in this repository. Exact installation/API instructions will follow a pinned, executed implementation. The current runnable control-boundary fixture is [lesson 02](02-bounded-lookup.md).

## Task: classify an internal request and prepare a draft

The proposed system receives a synthetic request, permitted documents and identity from a trusted host. It returns a classification, sources, missing information and an action draft. Initially it does not write to a real ticketing system.

Start with four steps: validate → retrieve permitted sources → prepare draft → validate fields and source support. Decide whether this fixed path is sufficient before assigning an agent to each step.

## 1. Freeze a fair comparison contract

Use the same document snapshot, question set, tools and rubric. Model experiments must record model identity, prompts, parameters, retries and spend limits. If a framework injects different instructions or changes the tool schema, record that difference as a potential confounder.

| Dimension | Check | Failure example |
|---|---|---|
| Useful result | Human-reviewed classification and required fields | Valid JSON with incorrect facts |
| Evidence | Version-resolvable citations supporting each material claim | A real citation unrelated to the answer |
| Access | Same question under two trusted identities | Restricted text reaches a model before being hidden |
| Failure | Unavailable tools, no results, invalid output, cancellation | Error converted into an empty string and reported as success |
| Resources | All runs, retries, requests, latency and billed usage | Reporting only successful runs |

Set thresholds from the task's risk and user needs before comparing results. There is no universal accuracy percentage that establishes deployment readiness.

## 2. State falsifiable candidate hypotheses

### Direct implementation

**Hypothesis:** explicit functions and state satisfy the fixed workflow with manageable maintenance cost.

Exercise: add a model adapter around the fixture's tool gateway rather than trusting raw model output. Define labeled classification and source-support checks. Do not add persistence solely to make an experiment look complex.

### Pydantic AI

Its documentation covers typed outputs, dependencies and tools. **Hypothesis:** typed integration reduces manual contract code for this Python drafting task without weakening rejection or source rules. [Official documentation](https://pydantic.dev/docs/ai/overview/)

Exercise: specify classification, sources and missing-information contracts; encapsulate data access in tools. Test structurally valid but factually wrong output separately from tool denial. Schema validation cannot establish factual correctness.

Adopt only if observed maintainability benefits justify dependency and upgrade costs while task and failure criteria remain satisfied. Merely expressing the same code differently is not sufficient evidence.

### LangGraph

**Hypothesis:** state orchestration is useful if the task genuinely requires pausing for review and resuming after a process restart. This is a conditional recommendation. [Overview](https://docs.langchain.com/oss/python/langgraph/overview)

Exercise: define retrieval, draft, waiting and completion transitions. Select the persistence backend before a kill/restart test. In-memory checkpoints do not survive process restart. [Persistence](https://docs.langchain.com/oss/python/langgraph/persistence)

Review must be tied to a specific draft and action version. Resuming an interrupted node can rerun earlier node code; side effects require idempotency or reconciliation. Checkpointing alone does not prove exactly-once external actions. [Interrupts](https://docs.langchain.com/oss/python/langgraph/interrupts)

## 3. Bound the experiment

For a fixed classification draft, compare the direct implementation with one justified candidate first. Add a state-oriented candidate only when state requirements exist. Keep the baseline and admit at most two framework candidates per experiment.

## 4. Record reproducible evidence

Record source commit, interpreter, exact packages and lockfile, tool/data snapshots, test IDs, model settings, all failures, latency and cost. Use `PASS`, `FAIL`, `NOT_RUN` or `NOT_APPLICABLE` with reasons. A documentation review cannot turn `NOT_RUN` into `PASS`.

Conclude with adopt / retain baseline / defer / reject, supporting evidence, maintenance costs and an exit path. This is a task-specific decision, not a general framework ranking.
