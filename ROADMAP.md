# Learning roadmap

| Phase / priority | Status | Goal and reason | Dependency | Acceptance criteria |
|---|---|---|---|---|
| G0 / P0 | DONE | Establish categories and scenario selection so readers compare like with like | Primary documentation | Separate coding harnesses, frameworks and architecture patterns; cite sources and counterexamples |
| G1 / P0 | DONE | Teach a bounded execution boundary with inspectable code | Synthetic data, Python | Normal/no-evidence/retry/budget cases and all contract tests pass; tutorial commands verified |
| G2 / P1 | TODO | Implement the first real model adapter without a framework | Fixed task, approved provider/model and spend budget | Lock dependencies; separately record offline and opt-in model tests; no implicit paid calls |
| G3 / P1 | TODO | Compare at most two admitted framework candidates against the baseline | G2, frozen task and evaluation contract | Same tools/data/model; exact versions; failure cases, quality, cost and decision recorded |
| G4 / P1 | TODO | Execute the Pi coding exercise and document a complete walkthrough | Isolated fixture checkout, pinned Pi, provider budget | Actual diff, independent tests, trace/commands and limitations; no simulated run claims |
| G5 / P1 | TODO | Build the retrieval baseline before agentic or graph extensions | Approved corpus and answer/source labels | Parsing, permissions, citations, refusal and held-out evaluation |
| G6 / P2 | TODO | Evaluate Agentic RAG and graph retrieval where baseline gaps justify them | G5 failure analysis | Same questions, incremental benefits and costs, source-update/revocation behavior |
| G7a / P0 | DONE | Make English the primary full tutorial language | Owner request; source and code audit | Five complete English guides, primary links updated, Chinese technical corrections synchronized |
| G7b / P2 | TODO | Add Japanese translations | Stable English source | Equivalent instructions and technical editorial review |

The design workshops for G3–G6 are readable now. Their runtime milestones remain TODO. New articles are published as runnable tutorials only after their commands and expected outputs have been executed. Complete one vertical slice before opening another framework implementation.

## Editorial revision

DONE: revised the English entry pages and five lessons for clearer, less repetitive prose. Technical commands, source links and runtime status are preserved; source/test hashes and lesson code blocks were checked unchanged. Chinese remains technically aligned; this revision changes the English voice. See docs/VOICE.md.
