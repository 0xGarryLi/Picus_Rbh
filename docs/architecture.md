# PICUS financial routing architecture

**Status:** product architecture / prototype specification. Live routing integrations are not included in this repository.

```text
Agent intent
    │
    ▼
Intent normalizer
    │
    ▼
Route discovery ──► Quote adapters / venues / data providers
    │
    ▼
Shadow Run simulator
    │
    ▼
All-in cost evaluator
    │
    ├─ expected output
    ├─ explicit fees
    ├─ gas / settlement cost
    ├─ slippage / price impact
    ├─ liquidity constraints
    ├─ latency / quote expiry
    └─ route validity
    │
    ▼
Recommendation or NO ROUTE
```

## Components

**Intent normalizer** converts an agent request into a machine-readable action with asset, amount, destination, timing, permissions and maximum-cost constraints.

**Route discovery** queries supported venues or providers and normalizes heterogeneous quotes into a comparable schema. A quote must carry provenance, timestamp and expiry metadata.

**Shadow Run simulator** evaluates candidate routes without broadcasting the user's real transaction. Depending on the integration, this can include call simulation, allowance checks, balance checks, revert detection and expected-output estimation.

**All-in cost evaluator** compares routes using the user's objective. A superficially lower fee is not necessarily cheaper after gas, spread, slippage and price impact.

**Recommendation layer** returns the best eligible route only when it satisfies all hard constraints. If evidence is stale or simulation fails, PICUS should return no recommendation rather than fabricate certainty.

## Trust boundaries

- Private keys never belong in PICUS routing code.
- Quotes require timestamps and source identity.
- Simulations are estimates, not guarantees of final execution price.
- External liquidity can change between simulation and execution.
- Live execution should require explicit permissions defined by the wallet / agent owner.

## Onchain role

The published $PICUS contract is:

`0x81f3ad4882233fcaff4e4dfbe570ac1c96f2b7b3`

PICUS service eligibility may use onchain balance verification. Quote collection, route analysis and simulation remain primarily offchain for latency and cost reasons.
