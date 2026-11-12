# PICUS — Shadow Run website

A standalone, responsive, five-page concept site for PICUS. Built with HTML, CSS and vanilla JavaScript. No build step or API keys required.

## Start

Open `index.html` in a browser, or run `python -m http.server 8000` in this folder and visit `http://localhost:8000`.

## Pages

- `index.html`: unconventional animated hero, simulated comparison lab, product overview.
- `technology.html`: proposed execution engine, research challenges.
- `token.html`: proposed holding-based token utility and contract placeholder.
- `roadmap.html`: staged development plan with non-fabricated statuses.
- `docs.html`: conceptual API, transparency and FAQ.

## Configure official links

Edit `assets/site.js` at the top:

```js
const CONFIG = {
  twitter: 'https://x.com/picus_rbh',
  github: '', // set verified official repository URL here
  contract: '', // set only after deployment and verification
  chainName: 'Robinhood Chain'
};
```

GitHub controls show a transparent notification until configured, rather than linking to a fictitious repository. Contract address remains "NOT PUBLISHED" until configured.

## Wallet

The Connect Wallet button uses the browser's injected EIP-1193 wallet (`window.ethereum`), supporting wallets such as MetaMask or Rabby. It calls `eth_requestAccounts` only; it does **not** sign, transact, request spending approvals or switch networks. Tested behavior depends on an installed wallet and user approval. For production, add account state persistence/UI, wallet compatibility testing, chain gating, SIWE authentication as necessary, and legal/security review.

## Notes

All benchmark figures on the home demo are **simulated**. No functional optimization engine or token has been implemented in this package. The site makes no claims about current deployment, token availability, achieved savings, or confirmed integration partnerships.

External dependency: Google Fonts for Space Grotesk / DM Mono (system fonts are provided as fallback). No third-party runtime JavaScript dependency.
