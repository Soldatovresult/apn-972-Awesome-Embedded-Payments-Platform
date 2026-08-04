# Awesome-Embedded-Payments-Platform

# Similar Projects to Embedded Payments Platforms

**Embedded Payments Platforms** (also called Banking-as-a-Service / BaaS or embedded finance platforms) enable companies to integrate payments, accounts, cards, payouts, and related financial services directly into their products via APIs. Leading platforms include Stripe, Adyen, Rapyd, Unit, Moov, Finix, Checkout.com, Treasury Prime, Synctera, and Weavr.

Below is a **curated list** of notable platforms and their open-source equivalents. Fully regulated embedded banking (FDIC-insured accounts, card issuing, etc.) requires licensed banks or BaaS partners and cannot be purely open-source. Open-source strength lies in ledgers, payment orchestration primitives, and financial infrastructure that teams can use to build or complement embedded finance products.

## 🏢 SaaS / Hosted Platforms

- **[Stripe](https://stripe.com/)** — Dominant payments and embedded finance platform (Payments, Connect, Treasury, Issuing, etc.).
- **[Adyen](https://www.adyen.com/)**, **[Checkout.com](https://www.checkout.com/)**, **[Rapyd](https://www.rapyd.net/)** — Global payments platforms with strong acquiring, payouts, and platform capabilities.
- **[Unit](https://www.unit.co/)**, **[Treasury Prime](https://treasuryprime.com/)**, **[Synctera](https://synctera.com/)**, **[Moov](https://moov.io/)**, **[Finix](https://finix.com/)**, **[Weavr](https://www.weavr.io/)** — Banking-as-a-Service and embedded finance platforms focused on accounts, cards, and money movement for software companies and fintechs.

## 🔓 Open-Source Software

### Open-Source Ledgers & Financial Core
- **[Formance Ledger](https://github.com/formancehq/ledger)** — Programmable open-source core ledger for fintech. Supports atomic multi-posting transactions, account-based modeling, and a domain-specific language (Numscript) for financial logic. Excellent foundation for wallets, marketplaces, and embedded payment systems.
- **[Blnk Core](https://www.blnkfinance.com/)** — Immutable, developer-friendly open-source ledger designed for accuracy and multi-currency support. Useful for building balances, wallets, and money-movement applications.
- **[Apache Fineract](https://fineract.apache.org/)** — Mature open-source core banking platform that provides accounts, portfolios, transactions, and can serve as a backend for digital financial services (often paired with a licensed partner for regulated activities).

### Payments Infrastructure & Messaging
- **[jPOS](https://jpos.org/)** — Long-standing open-source payments infrastructure focused on ISO-8583, ISO-20022, and high-integrity transaction processing. Used in gateways, switches, acquirers, and issuers.
- Open-source payment orchestration and double-entry systems that teams combine with commercial processors for a hybrid embedded finance stack.
- Community projects offering Stripe-inspired APIs or self-hosted payment primitives (ledgers + webhooks + basic payment intents).

### Related Open-Source Building Blocks
- **Mojaloop** — Open-source framework originally aimed at inclusive, interoperable payments (more relevant for national or large-scale payment systems than typical SaaS embedded finance).
- Open-source identity, KYC orchestration, and consent tools that support onboarding flows in embedded finance products.
- Self-hosted wallet and multi-currency balance engines built on the ledgers above.

### Typical Open-Source + Hybrid Approach
1. **System of record** — Formance Ledger, Blnk, or Fineract for balances and transactions
2. **Payment rails** — Commercial processors (Stripe, Adyen, etc.) or bank partners for actual money movement
3. **Card issuing / accounts** — BaaS providers (Unit, Synctera, Treasury Prime…) or direct bank partnerships
4. **Orchestration layer** — Custom services or open-source tools that coordinate the ledger with external rails
5. **Compliance & reporting** — Self-hosted or third-party tools layered on top of the ledger

This combination gives platforms strong ownership of the financial ledger and business logic while relying on regulated partners for the licensed banking and card activities.

---

**How to contribute**  
Fork this repository, add a new project (with link + short description + category), and open a pull request.  
Prefer actively maintained open-source projects related to embedded payments, Banking-as-a-Service infrastructure, financial ledgers, or payment orchestration.

**License**  
This list is public domain / CC0. Feel free to copy into your own awesome list or README.

Star the projects you find useful — open financial infrastructure helps more companies embed payments responsibly! 💳
