<div align="center">
  <img src="brand/picus-mascot-blue.png" alt="PICUS woodpecker mascot" width="170" />

  # PICUS
  ### One agent. Two executions. See the difference.
  **Shadow Run — research-stage execution optimization for autonomous AI agents.**

  [Website](site/index.html) · [Technology](docs/architecture.md) · [Roadmap](docs/roadmap.md) · [Token utility](docs/token-utility.md) · [X / @picus_rbh](https://x.com/picus_rbh)
</div>

![PICUS Shadow Run banner](brand/picus-shadow-run-banner.png)

## Why PICUS?

Autonomous agents spend resources on model inference, APIs, tools and repeated work. **Shadow Run** is a proposed system to compare candidate execution paths against the same task requirements, measuring cost, latency, output quality and reliability before choosing a preferred approach.

The goal is not blindly choosing the cheapest option. It is **lower cost without violating a task's quality and safety constraints**.

## Core concept

1. **Trace** an agent workflow's model calls, tool usage and costs.
2. **Propose** a comparison candidate, e.g. cheaper model for a noncritical step or safe reuse of intermediate data.
3. **Shadow run** alternative paths in an isolated environment, without performing real-world financial operations.
4. **Evaluate** cost, latency, task-specific quality, and failure rate.
5. **Recommend** the path that satisfies defined acceptance criteria.

> **Status:** PICUS is an early-stage concept and design prototype. The website and example traces use **simulated values**, not live agents or validated production savings. There is no deployed token contract in this repository.

## Token — $PICUS (proposed)

The planned utility is **holding-based eligibility for lower prices on selected Shadow Run resources**. Users would hold $PICUS instead of spending tokens for each call. Underlying chain transaction fees and any fixed protocol fees are **not** changed by token holding. Actual discount tiers, eligibility, commercial funding and token deployment are **not yet defined**. Read [the proposed utility model](docs/token-utility.md).

**Contract:** `NOT DEPLOYED` — no contract address has been announced. Never trust an address shared outside verified official channels.

## Repository map

| Path | Contents |
| --- | --- |
| [`site/`](site/) | Five-page static prototype (HTML, CSS, JS), browser-wallet connection UI |
| [`brand/`](brand/) | Woodpecker mascot SVG/PNG and social artwork |
| [`docs/`](docs/) | Architecture, roadmap, proposed token utility and brand guidelines |
| [`examples/`](examples/) | Sample simulated traces + local comparison script |
| [`.github/`](.github/) | Issue templates, contribution workflows |

## Try the website

```bash
cd site
python3 -m http.server 8000
# open http://localhost:8000
```

The wallet connect button requests account access from an injected EVM wallet only. It **does not** sign, transact or swap networks. A connected wallet does not imply access to a functional deployed protocol.

## Run a reproducible offline comparison

```bash
python3 examples/compare_runs.py examples/sample-runs.json
```

The data is illustrative; the script does **not** call an LLM, run a live agent, or calculate real savings.

## Documentation

- [Architecture / trust boundaries](docs/architecture.md)
- [Product and metrics](docs/product-spec.md)
- [Roadmap](docs/roadmap.md)
- [Token utility](docs/token-utility.md)
- [Brand assets](docs/brand.md)
- [How to contribute](CONTRIBUTING.md)
- [Security reporting](SECURITY.md)

## Links

- X: https://x.com/picus_rbh
- GitHub: this repository (replace with your official URL after publishing)
- Robinhood Chain: intended ecosystem, not a claim of official Robinhood affiliation

## License

Code is provided under the [MIT License](LICENSE). Original PICUS visual brand assets are **not included in that license**; see [`brand/ASSET-LICENSE.md`](brand/ASSET-LICENSE.md).
