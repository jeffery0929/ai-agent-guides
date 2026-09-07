# 05 — Choose a retrieval pipeline, Agentic RAG or graph retrieval

[Guide index](README.md) · [繁體中文](../zh-Hant/05-retrieval-design.md)

This is an architecture workshop. No model, vector database or graph index has been deployed in this repository. The output is a design that can be implemented and evaluated.

## Separate three question types

1. **“What is the approval procedure for system access?”** Start with lexical/vector retrieval, citations and no-evidence behavior.
2. **“Do this project's documents, open tickets and system-owner records agree?”** Evaluate bounded tool routing when intermediate evidence determines which sources to query.
3. **“Which projects depend on shared systems, and what themes span departments?”** Evaluate explicit relationship queries and graph-based methods. Question length alone does not justify GraphRAG.

Microsoft GraphRAG is a specific indexing and retrieval approach. A design that uses some graph data is not automatically an implementation of that project. [Official documentation](https://microsoft.github.io/graphrag/)

The recommendations below are design hypotheses, not benchmark results.

## 1. Define data and questions

Use a small approved collection with source identifiers, versions, locators and access rules. Classify questions into exact fields, single procedures, cross-document relationships, collection-level summaries and unanswerable requests.

Label supporting passages before tuning. Reserve held-out questions. Without credible reference labels, do not publish a retrieval-accuracy number.

## 2. Build an explainable baseline

Parse → preserve chunks and metadata → enforce access rules → retrieve/rerank → answer or refuse → verify citations.

The logical requirement is that unauthorized evidence must not reach a reranker or generator. The implementation of filtering depends on the index and backend and needs its own tests. Retrieval quality and answer support are separate measurements; prompt changes do not guarantee repair of parsing or table-boundary errors.

Uniform outward responses for missing and inaccessible material may reduce existence leaks. They do not eliminate timing, logging or other side channels by themselves.

## 3. Extend only where the baseline has demonstrated gaps

### Agentic RAG

Introduce a bounded decision point among permitted document, SQL and API tools. Begin with read-only tools and provenance-bearing results. Define step, spend and stopping rules. Test wrong tool selection, loops, untrusted tool text and unavailable tools. If the extra decision does not improve the same task set, remove it.

### Graph retrieval

First check whether the needed relationships already exist in a queryable database. If you extract relationships, retain their source support and uncertainty. Incorrect links can produce plausible but unsupported conclusions. Derived summaries and caches also need access controls, revocation handling and refresh rules.

Test direct relationship lookup separately from collection-wide synthesis. Compare indexing cost, update work, retrieval quality and answer support. Do not presume that graph retrieval is better.

## 4. Produce a reviewable design package

- Data-flow and trust-boundary diagrams.
- Question categories and reasons for each selected path.
- Source, version, parsing, citation and permission contracts.
- No-evidence, unavailable-tool, stale-data, revocation, deletion and reindexing tests.
- Fixed evaluation data, human review procedure, spend and latency budgets.
- Counterexamples and conditions for returning to the baseline.

These artifacts justify an implementation experiment. Claims that a system works require code, executed results and acceptance on the approved data.
