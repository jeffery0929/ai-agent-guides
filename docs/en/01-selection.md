# 01 — Choose by scenario, not popularity

[Guide index](README.md) · [繁體中文](../zh-Hant/01-selection.md)

## Separate three layers

- **Developer tools and harnesses** help an engineer inspect, modify and test a repository. Pi is discussed here in its coding-agent role.
- **Application frameworks and orchestration** help you build a service. LangGraph and Pydantic AI are candidates at this layer, with different abstractions.
- **Architecture patterns** include fixed workflows, tool-using agents, Agentic RAG, graph-based retrieval and multi-agent coordination. They are not interchangeable package names.

These categories describe the use cases in this guide, not exclusive product boundaries. Pi also exposes programmatic integration modes; a framework can support more than one architecture. A system may combine layers, but each addition needs a reason.

## Map the task to a candidate

These are engineering recommendations to test, not measured rankings.

| Task | Start by evaluating | Why it may fit | Cost or counterexample |
|---|---|---|---|
| Scheduled data reads, fixed rules and reporting | Ordinary code or a fixed workflow | The path is already known | A model need not decide rules you have already specified |
| Extract document fields for a Python backend | Typed model integration; consider Pydantic AI | The data contract is central | Valid structure does not establish factual correctness |
| Pause a multi-step task for review and recover after restart | Consider LangGraph | State transitions and resumption are central | A short linear task may not justify the extra state/persistence layer |
| Inspect code, make a patch and run tests | Consider Pi as a coding harness | The work centers on a repository and developer tools | A coding environment is not automatically an authenticated enterprise service |
| Answer questions over one document collection | A fixed retrieval baseline | Retrieval and source support can be measured first | Agent routing may add no value |
| Choose documents, SQL or APIs based on intermediate evidence | Bounded Agentic RAG | The useful query path depends on results | More decisions add possible failure paths and may add cost/latency |
| Investigate project, system and document relationships | SQL or explicit relationship queries, then graph retrieval | The question depends on links across records | Extracted edges, updates and derived-data access rules need evaluation |
| Independently checkable subtasks with demonstrated coordination value | Consider multiple agents | Division of work may help | Naming more roles does not prove a quality improvement |

## Official facts versus our interpretation

LangGraph documents stateful orchestration, persistence and human intervention. That supports considering it for state-management requirements, not a claim that selecting it makes a system production-ready. [Official overview](https://docs.langchain.com/oss/python/langgraph/overview)

Pydantic AI documents typed outputs, tools and dependencies. Those features support considering it for typed Python integration; they do not establish lower cost or higher accuracy for your task. [Official overview](https://pydantic.dev/docs/ai/overview/)

Pi describes an extensible agent harness with interactive and programmatic modes. Our coding-task recommendation is a use-case choice, not a claim that embedding Pi is impossible. [Official site](https://pi.dev/)

## Complete a requirement sheet before installing candidates

1. Who is the user, and where does trusted identity come from?
2. What are the input, output, permitted data and forbidden actions?
3. Which steps are fixed, and which actually require model decisions?
4. Must the task survive a process restart, or is manual rerun acceptable?
5. Which actions have side effects, and how will uncertain completion be reconciled?
6. Who defines task labels, failure categories, latency limits and spend limits?
7. Can the maintainer understand, test and replace the approach?

Fill gaps before broadening the stack. Keep a direct implementation as the baseline; admit at most two justified candidates per experiment. Keeping the baseline, deferring or rejecting a framework are valid outcomes.
