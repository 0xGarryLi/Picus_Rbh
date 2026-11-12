# Product specification — PICUS Shadow Run

## User story

As an AI-agent developer, I want to compare two permitted execution plans for the same task so I can choose a lower-cost plan without reducing required quality.

## Input

A named workflow, two or more candidate plans, normalized traces, estimated or measured costs, end-to-end latency and output-quality measurements.

## Output

- Total cost and latency per candidate, with provenance of measurements
- Quality gate pass/fail per candidate
- Recommended plan, or **no recommendation** if evidence is insufficient
- Trade-offs, sample size, known risks, and a shareable comparison card

## Minimum usable prototype

1. Import traces from JSON.
2. Show a side-by-side comparison.
3. Enforce a configurable quality threshold.
4. Export a comparison JSON or shareable graphic.
5. Mark synthetic or estimated measurements visibly.

## Marketing-native product loop

A developer compares two paths, downloads a **Shadow Run Report** with reproducible methodology and shares it on X. Avoid invented percent-savings claims; only publish comparisons derived from measured workloads and disclosed baselines.

## Proposed success metrics

Compare p50/p95 latency, cost per passing task, output-quality gate adherence, percentage of eligible steps successfully shadowed, false-positive optimization recommendations, and sandbox isolation failures.
