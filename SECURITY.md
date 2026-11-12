# Security policy

## Status

This repository includes a public website, documentation and synthetic route-comparison examples. It is **not production-grade trading or custody infrastructure**.

## Official contract

`0x81f3ad4882233fcaff4e4dfbe570ac1c96f2b7b3`

Verify the address through official PICUS channels. Never paste seed phrases or private keys into an issue, website form or support message.

## Reporting

Contact the project through [@picus_rbh](https://x.com/picus_rbh) and request a private disclosure channel. Do not publish active exploits, private keys or credentials in public issues.

## Wallet safety

The static website's wallet connection requests account access only. Testing the website does not require approving token spending, signing arbitrary messages or executing swaps.

## Routing boundaries

Shadow simulations must not silently broadcast live transactions. Production execution should enforce explicit user / agent permissions, quote freshness checks, chain and contract allow-lists, slippage limits and simulation validation.
