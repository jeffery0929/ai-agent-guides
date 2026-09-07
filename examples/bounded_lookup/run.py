"""Offline teaching fixture. No model, network, business writes, or real identity."""
from dataclasses import dataclass
import json


@dataclass(frozen=True)
class Document:
    id: str
    keyword: str
    roles: frozenset[str]
    excerpt: str


DOCUMENTS = (
    Document("IT-001", "access", frozenset({"it"}),
             "Request access through the service desk; the system owner reviews it."),
    Document("FIN-001", "invoice", frozenset({"finance"}),
             "Match the invoice to its purchase order before preparing a payment request."),
)


def run(proposals, *, role="it", max_steps=4, fail_once=False):
    """Execute scripted tool proposals under a bounded, read-only contract."""
    if type(proposals) not in (list, tuple):
        raise ValueError("proposals must be a prebuilt list or tuple")
    if type(fail_once) is not bool:
        raise ValueError("fail_once must be a boolean")
    if not isinstance(role, str) or role not in {"it", "finance"}:
        raise ValueError("Unknown simulated role")
    if type(max_steps) is not int or not 1 <= max_steps <= 10:
        raise ValueError("max_steps must be an integer from 1 to 10")
    trace = []
    citations = []
    fault_pending = fail_once

    def result(status, approved_citations=None):
        return {"status": status, "citations": approved_citations or [], "trace": trace}

    for step, proposal in enumerate(proposals, start=1):
        if step > max_steps:
            return result("BUDGET_EXHAUSTED")
        if not isinstance(proposal, dict) or set(proposal) != {"tool", "args"}:
            trace.append({"step": step, "event": "INVALID_PROPOSAL"})
            return result("REJECTED")
        tool, args = proposal["tool"], proposal["args"]
        if tool not in ("search", "finish") or not isinstance(args, dict):
            trace.append({"step": step, "event": "DISALLOWED_TOOL_OR_ARGS"})
            return result("REJECTED")
        if tool == "finish":
            if args:
                trace.append({"step": step, "event": "INVALID_FINISH_ARGS"})
                return result("REJECTED")
            trace.append({"step": step, "event": "FINISH"})
            return result("COMPLETE" if citations else "NO_EVIDENCE", citations)
        if set(args) != {"query"} or not isinstance(args["query"], str):
            trace.append({"step": step, "event": "INVALID_SEARCH_ARGS"})
            return result("REJECTED")
        query = args["query"].strip().lower()
        if not query or len(query) > 120:
            trace.append({"step": step, "event": "INVALID_QUERY"})
            return result("REJECTED")
        citations = []  # Never retain evidence from an earlier search after failure/no match.
        if fault_pending:
            fault_pending = False
            trace.append({"step": step, "event": "TOOL_UNAVAILABLE"})
            continue
        citations = [{"id": d.id, "excerpt": d.excerpt} for d in DOCUMENTS
                     if role in d.roles and query == d.keyword]
        trace.append({"step": step, "event": "SEARCH", "matches": len(citations)})
    return result("INCOMPLETE")


def demo():
    search = {"tool": "search", "args": {"query": "access"}}
    finish = {"tool": "finish", "args": {}}
    return {
        "normal": run([search, finish]),
        "retry": run([search, search, finish], fail_once=True),
        "role_filtered": run([search, finish], role="finance"),
        "loop_stopped": run([search] * 5),
    }


if __name__ == "__main__":
    print(json.dumps(demo(), indent=2, ensure_ascii=False))
