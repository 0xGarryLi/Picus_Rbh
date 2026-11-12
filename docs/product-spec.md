# Product specification — PICUS Shadow Run

## User story

As an autonomous agent or agent developer, I want to compare eligible financial execution routes before value moves so I can choose a lower-cost valid path under explicit constraints.

## Input

- financial intent
- asset / amount / destination
- permitted venues and networks
- quote timestamps / expiries
- gas and fee estimates
- liquidity / price-impact data
- user-defined hard constraints

## Output

- normalized candidate routes
- expected received amount / all-in execution cost
- explicit fees and estimated gas
- slippage / price-impact estimate
- simulation pass / fail
- quote freshness and provenance
- recommended route, or **no recommendation**

## Minimum usable prototype

1. Import two or more route quotes from JSON.
2. Normalize cost components.
3. Reject stale or failed routes.
4. Rank valid routes by all-in cost.
5. Export a machine-readable Shadow Run report.
6. Clearly mark simulated or estimated values.

## Marketing-native product loop

A developer submits an intent and receives a shareable **Shadow Run Report** showing which path PICUS would choose and why. Public comparisons should include methodology and source timestamps rather than invented savings claims.

## Success metrics

- all-in savings against a disclosed baseline
- simulation failure detection rate
- quote freshness
- recommendation latency
- rate of invalid / stale routes correctly rejected
- difference between simulated and realized execution where live measurement is permitted
