# Proposed technical architecture

**Status:** design document, not a production deployment.

```text
Agent workflow → Trace collector → Candidate generator → Shadow sandbox
                  │                                      │
                  └────────→ Comparison evaluator ←──────┘
                                      │
                              Recommendation / report
```

## Components

**Trace collector:** normalizes a workflow into immutable events containing node IDs, model and tool identifiers, declared prices, durations, redacted request metadata, version numbers and error codes. Sensitive prompts, API keys and private responses must not be logged by default.

**Candidate generator:** proposes alternative task plans or substitutions under explicit allow-lists. It must not silently alter user goals or agent permissions.

**Shadow sandbox:** performs isolated tests against mocks, snapshots or disposable environments. Real purchases, brokerage orders and wallet transactions must be disabled. A dry run cannot prove equivalence to a live external service.

**Evaluator:** reports total resource cost, end-to-end latency, task-specific quality rubric scores, failure rates and evidence completeness. Compare identical input snapshots and report confidence intervals over repeated trials.

**Recommendation:** selects the cheaper path **only if** it meets user-defined quality thresholds, resource constraints and safety policies.

## Important limitations

- LLM outputs are nondeterministic. Two runs may require repeated evaluation to establish comparable quality.
- Tool outputs can drift between runs; snapshot or version inputs for fair comparisons.
- Side effects must be blocked during shadow execution.
- Costs need explicit rate cards and effective dates; a simulated cost estimate is not a vendor quote.
- Production deployment requires security review, privacy design and structured observability.

## Potential onchain role

Robinhood Chain is a proposed deployment environment for token-related interactions. Evaluation and LLM execution stay offchain. No blockchain transaction is required for the offline prototype.
