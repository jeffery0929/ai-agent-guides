import unittest
from examples.bounded_lookup.run import run, DOCUMENTS

S = {"tool": "search", "args": {"query": "access"}}
F = {"tool": "finish", "args": {}}


class LookupContract(unittest.TestCase):
    def test_exact_source(self):
        r = run([S, F])
        self.assertEqual(r["status"], "COMPLETE")
        self.assertEqual(r["citations"], [{"id": "IT-001", "excerpt": DOCUMENTS[0].excerpt}])

    def test_role_filter(self):
        r = run([S, F], role="finance")
        self.assertEqual(r["status"], "NO_EVIDENCE")
        self.assertEqual(r["citations"], [])

    def test_no_unearned_success(self):
        self.assertEqual(run([S])["status"], "INCOMPLETE")
        self.assertEqual(run([F])["status"], "NO_EVIDENCE")

    def test_bad_arguments(self):
        for p in [{"tool": "search", "args": {"query": "access", "role": "finance"}},
                  {"tool": "finish", "args": {"answer": "invented"}},
                  {"tool": "search", "args": {"query": " "}},
                  {"tool": "search", "args": {"query": 4}},
                  {"tool": "search", "args": {"query": "x" * 121}},
                  {"tool": "search", "args": {"query": "access"}, "extra": True},
                  {"tool": "search", "args": []}, None]:
            with self.subTest(proposal=p):
                self.assertEqual(run([p])["status"], "REJECTED")

    def test_unlisted_tool(self):
        self.assertEqual(run([{"tool": "send_email", "args": {}}])["status"], "REJECTED")

    def test_failure_and_retry(self):
        r = run([S, S, F], fail_once=True)
        self.assertEqual(r["status"], "COMPLETE")
        self.assertEqual([e["event"] for e in r["trace"]],
                         ["TOOL_UNAVAILABLE", "SEARCH", "FINISH"])

    def test_failed_tool_cannot_supply_citations(self):
        r = run([S, F], fail_once=True)
        self.assertEqual(r["status"], "NO_EVIDENCE")
        self.assertEqual(r["citations"], [])

    def test_new_query_clears_old_evidence(self):
        r = run([S, {"tool": "search", "args": {"query": "unmatched"}}, F])
        self.assertEqual(r["status"], "NO_EVIDENCE")
        self.assertEqual(r["citations"], [])

    def test_budget_stops_loop(self):
        r = run([S] * 5 + [F], max_steps=4)
        self.assertEqual(r["status"], "BUDGET_EXHAUSTED")
        self.assertEqual(len(r["trace"]), 4)
        self.assertEqual(r["citations"], [])

    def test_invalid_configuration(self):
        for budget in [0, 11, True, 1.5]:
            with self.assertRaises(ValueError):
                run([S, F], max_steps=budget)
        with self.assertRaises(ValueError):
            run([S, F], role="admin")

    def test_configuration_types(self):
        for role in [[], {}, None, 1]:
            with self.subTest(role=role), self.assertRaises(ValueError):
                run([S, F], role=role)
        for fault in ["false", 0, 1, None]:
            with self.subTest(fault=fault), self.assertRaises(ValueError):
                run([S, F], fail_once=fault)

    def test_lazy_proposals_rejected_without_consumption(self):
        consumed = []
        def proposals():
            consumed.append(True)
            yield S
        with self.assertRaises(ValueError):
            run(proposals())
        self.assertEqual(consumed, [])

    def test_budget_boundary_and_terminal_state(self):
        self.assertEqual(run([S, F], max_steps=2)["status"], "COMPLETE")
        self.assertEqual(run([S, F], max_steps=1)["status"], "BUDGET_EXHAUSTED")
        self.assertEqual(run([S], max_steps=1)["status"], "INCOMPLETE")
        r = run([S, F, {"tool": "send_email", "args": {}}])
        self.assertEqual(r["status"], "COMPLETE")
        self.assertEqual(len(r["trace"]), 2)


if __name__ == "__main__":
    unittest.main()
