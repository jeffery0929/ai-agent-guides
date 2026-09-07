# Tutorial authoring template

1. Task and intended reader: identify inputs, expected artifact and prior knowledge.
2. When it fits, why it fits, and a counterexample where a simpler approach wins.
3. Evidence status: design-only, local fixture, actual SDK run, model run or deployment.
4. Exact tested environment: source commit, interpreter, dependency lock and provider boundary.
5. Architecture and contracts: state, tools, identity, source ownership and side effects.
6. Reproducible setup: exact commands verified against the checked-in code; explicit optional paid calls.
7. Walkthrough: show intermediate state and expected output, not just final prose.
8. Failure exercises: invalid inputs, no evidence, unavailable tools, cancellation and relevant recovery.
9. Evaluation: fixed data, task labels, denominators, failures, latency and cost where measured.
10. Limitations: what was not run; no inference of production safety from local tests.
11. Maintenance: primary sources, checked date, version changes and upgrade verification.

Never publish API spellings from memory, unrun commands as tested, model prices without dated verification, or confidential input/output. Planned tutorials remain visibly planned until their acceptance criteria pass.
