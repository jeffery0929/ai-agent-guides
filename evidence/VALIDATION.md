# Validation — 2026-09-07

Executed locally using CPython 3.14.5 on macOS. No third-party packages installed and no model/API calls made.

From this repository root:

```sh
python3 -m unittest discover -s tests -v
python3 examples/bounded_lookup/run.py
```

Result: **10 tests passed**. The demo produced normal COMPLETE, retry COMPLETE, role_filtered NO_EVIDENCE and loop_stopped BUDGET_EXHAUSTED. See [actual output](demo-output.json) and [tested source hashes](source-hashes.json).

The initial test-discovery attempt was accidentally run from the parent website repository and found zero Python tests; that attempt provides no evidence. The commands above were then run from this repository and passed.

Markdown relative links were checked. Source examples use Python 3.11-compatible syntax, but only the runtime stated above was executed in this revision. No CI or other interpreter version was run.

Not verified: SDK/provider integration, model tool selection, real identity or ACL enforcement, process restart, external side effects, wall-clock timeouts, cross-user isolation or production deployment. Synthetic roles are test configuration, not authentication. Pi and framework workshops are not executed integrations.
