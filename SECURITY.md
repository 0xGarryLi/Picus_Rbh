# Security policy

## Status

This is a public-facing concept website and simulated trace tooling. **Not production-grade trading, wallet or agent-execution infrastructure.**

## Reporting

Please contact the project through [@picus_rbh](https://x.com/picus_rbh) and request a private disclosure channel; do not publish live exploits, private keys or secrets in issues.

## Wallet safety

Website wallet connection only requests accounts through an injected provider. Users should not approve transactions, token spending or signatures to test this repository. No official contract has been published.

## Boundaries

Shadow executions must not place live orders, transfer value, expose credentials, or cause irreversible external effects. Use sandbox mocks only.
