# Content and correctness audit — 2026-09-07

## Verdict and scope

Reviewed the five English guides, their Chinese counterparts, repository navigation, example implementation, tests and commands. Official feature descriptions were checked against primary documentation on the date above. No unresolved contradiction was identified within this reviewed scope after the fixes below. This is not a guarantee of zero errors or production readiness.

English is now the canonical language. Both language sets distinguish documented features, recommendations, executed fixture behavior and work not yet run.

## Findings and corrections

| Finding | Evidence | Resolution |
|---|---|---|
| String `"false"` silently enabled fault injection | Reproduced: `fail_once="false"` caused `TOOL_UNAVAILABLE` | Require an actual boolean; regression tests reject strings, integers and None |
| Invalid role types could raise an incidental TypeError | Reproduced with `role=[]` | Validate role type before membership; invalid configuration consistently raises ValueError |
| Lazy proposal input could advance before the step-budget check | Source inspection of enumerate before budget check | Accept only prebuilt list/tuple; a test proves a generator is rejected without consumption |
| “Python 3.11+” could imply a verified compatibility range | Only CPython 3.14.5 had execution evidence | Entry points state the actually tested runtime; other versions remain unverified |
| Product categories could look exclusive | Pi documents programmatic integration as well as interactive use | Explain that categories describe use cases, not impossible product combinations |
| Budget boundary was underspecified | Finite input ending at the limit differs from an additional queued proposal | Document and test INCOMPLETE versus BUDGET_EXHAUSTED, final-step finish and immediate termination |
| Provider budget wording could imply a universal hard cap | No provider-specific enforcement was verified | Require checking enforcement in the selected environment; do not promise an account cap |
| Uniform no-access/no-data responses could imply complete leak prevention | Design inspection; no side-channel tests exist | State that timing/logging and other channels still require review |

## Claim-to-evidence register

| Claim | Evidence class | Basis and limit |
|---|---|---|
| Fixture returns exact synthetic excerpts with caller-selected role filtering | EXECUTED LOCAL FIXTURE | Tests and demo output; role is not authenticated and public source contains every record |
| Fixture rejects unsupported tools and clears stale citations | EXECUTED LOCAL FIXTURE | Named contract tests; this is not a model prompt-injection benchmark |
| A step budget bounds executed scripted proposals | EXECUTED LOCAL FIXTURE | Boundary tests; no wall-clock timeout, hostile-code sandbox or network tool exists |
| LangGraph supports state-oriented orchestration | DOCUMENTATION CHECKED | [Overview](https://docs.langchain.com/oss/python/langgraph/overview); SDK not installed here |
| In-memory checkpoints do not survive restart | DOCUMENTATION CHECKED | [Persistence](https://docs.langchain.com/oss/python/langgraph/persistence); no backend restart test here |
| Interrupted node code can be rerun on resume | DOCUMENTATION CHECKED | [Interrupts](https://docs.langchain.com/oss/python/langgraph/interrupts); no exactly-once external-write claim |
| Pydantic AI provides typed outputs, dependencies and tools | DOCUMENTATION CHECKED | [Overview](https://pydantic.dev/docs/ai/overview/); schema validity is not factual accuracy |
| Pi is extensible and offers interactive/programmatic use | DOCUMENTATION CHECKED | [Official site](https://pi.dev/); no installed configuration or execution verified here |
| Microsoft GraphRAG is a specific graph-based RAG approach | DOCUMENTATION CHECKED | [Official documentation](https://microsoft.github.io/graphrag/); no local graph index exists |
| A candidate may suit a particular task | RECOMMENDATION / HYPOTHESIS | Rationale and counterexample stated; not a measured superiority claim |
| More complex retrieval improves a client's result | UNVERIFIED | Requires approved data, held-out labels, runtime and cost evaluation; not asserted as fact |

## Verification performed

- Reproduced the two configuration defects before changing code.
- Executed the revised baseline and 13 unit tests under CPython 3.14.5.
- Checked exact sample outputs, local Markdown targets and fenced JSON examples.
- Reviewed English instructions against actual identifiers and commands in source.
- Synchronized material contract and evidence corrections in Chinese translations.
- Changed profile lesson links to English; retained Chinese navigation.

Actual command results and source hashes are recorded in [VALIDATION.md](VALIDATION.md), [test-output.txt](test-output.txt), [demo-output.json](demo-output.json) and [source-hashes.json](source-hashes.json).

## Remaining limitations

Framework SDKs, Pi execution, real models/providers, real identity/ACLs, production hosting, external writes, crash recovery, cost/latency benchmarks, cross-version Python and independent security review are NOT RUN in this repository. Design exercises intentionally have no fabricated SDK API examples or measured rankings. Translations have not received independent language-editor review. Live official docs may change; implementation tutorials must pin and test their actual dependencies.
