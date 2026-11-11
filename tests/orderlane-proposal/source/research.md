# Opportunity finding → offer → proposal: Orderlane

## The decision in plain English
Research one implementation service for industrial supply distributors: turn emailed customer purchase orders into checked drafts in their existing order system. Their team approves them, instead of retyping everything.

This is a discovery-ready hypothesis, not a validated business or a signed scope. The proposal uses a fictional example buyer because Blake supplied no prospect or call recording. We assumed US buyers, an agency student comfortable with sales/basic automation, and access to a paid NetSuite/Celigo specialist. This is intermediate delivery with specialist support, not a beginner coding exercise.

## Six contrasting options considered
| Service | Buyer | What they get | Investigation result |
|---|---|---|---|
| Email purchase-order intake | Industrial supply distributors | Checked draft orders plus an exception queue | Selected for this demonstration; deepest research, S1–S8 |
| Supplier quote assembly | MSPs / IT resellers | Supplier pricing and line items assembled for rep review | Light scan, S9; existing CPQ software is a strong alternative; unranked |
| Maintenance agreement renewal workflow | Commercial HVAC contractors | Renewal dates, draft offers and assigned follow-up | Light scan, S10; native service software must be checked; unranked |
| Candidate reactivation | Staffing firms | Relevant candidate follow-up and recruiter handoffs | Light scan, S11; a basic sequence is already native; unranked |
| Email-to-freight quote preparation | Expedited freight operators | Request details routed into pricing and driver approval | Concrete vendor case, S12; deeper TMS/rating dependencies, not fully evaluated |
| Supplier catalogue synchronisation | Telecom / industrial distributors | Product data kept aligned across selling systems | Case background scanned, S13; feed rights and data quality unknown; unranked |

Only order intake was deepened enough for a full concept proposal. These are not six proven businesses or a ranking of the entire market.

## Why this one
The business and demonstration are understandable: customers buy parts; staff transfer their order into the system; a missed item, wrong unit or typing backlog gets in the way. A named distributor has adopted this category (S1), current documentation explains a delivery route (S2), and buyer/practitioner discussions describe the workflow (S7–S8). Those threads are anecdotal and potentially promotional, so they carry less weight than the deployment case.

The strongest objection is real: Conexiom, Prokeep and Celigo already address this. Our potential service is configuring the customer's mappings, checks, approval process, testing and staff adoption. It is NOT a proprietary breakthrough or an underserved niche claim. Prokeep provides its own implementation support (S4); if its native setup is sufficient and cheaper, recommend it. A prospective client with an able internal admin may not need us at all.

## Buyer and qualification
Target operations directors, customer-service managers or owners at independent US industrial distributors already running NetSuite, initially with Celigo in use. They need repetitive emailed orders, clean enough item/customer records, accessible test environments, and a responsible staff reviewer. Use roughly 3,000 supported orders/month as an initial economics screen, not an observed industry average. Measure actual touch time before quoting. Exclude firms already using working order automation, mostly portal/EDI ordering, low manual volumes, highly bespoke engineered products, or inaccessible ERP integrations.

There is no defensible count yet of US firms satisfying this entire filter. Broad distributor counts would overstate the market. Start by verifying a named 100-account list; that is a proposed prospecting batch, not a list created in this run or a TAM estimate.

## Acquisition route
Start with targeted owner/operations conversations, not broad Meta ads. Find industrial suppliers via public directories and manufacturer dealer lists; verify their product range, branches and team on their sites. Confirm software rather than inferring it from company size. LinkedIn is for identifying the relevant decision-maker and public signals, not assumed permission to scrape or mass message. Draft personalised emails and phone openers for review. No unsolicited SMS campaign is part of this test, and nothing has been sent.

Opening question: “When a customer emails a purchase order, does someone still retype the lines into NetSuite? We’re exploring a way to prepare checked drafts while your team keeps approval. Is that a bottleneck for you, or already handled?”

First test: research 30 accounts, seek 10 actual discovery conversations, and obtain 3 willing sample-workflow reviews. These are activity targets, not conversion forecasts. Ask about the last delayed order, manual monthly volume, touch time, exception rate, current licences and prior automation attempts. Continue to a scoped pilot only when an actual buyer's economics and integration access work. If most already have it solved, narrow or abandon this offer instead of improving the pitch.

## Proposed system and delivery
One shared mailbox feeds an intake flow. It identifies a supported order, extracts fields, matches to authoritative customer/product records, and checks quantity, unit, address and price. Staff resolve exceptions and approve before any production order is created. Original files and decisions remain traceable; retries must not create duplicate orders.

Preferred route: configure existing platform capabilities and add only the necessary mapping/review work. Do not replace NetSuite or force customers onto a new portal. AI reads variable documents; deterministic rules and staff decide whether data may be posted. No autonomous stock promises, substitution, pricing negotiation, credit approval, fulfilment or payment.

Technical gate before sale: verify mailbox permissions, NetSuite test account and sales-order permissions, Celigo IDP and connector entitlement/limits, approval-state support, duplicate handling, data retention/location, and actual vendor pricing. Existing product documentation does not prove these are enabled for this buyer. Specialist must run a read/write sandbox test and price the exact work. If the review UI needs a custom build, rescope instead of burying it inside the allowance.

First scope: one subsidiary, one mailbox, five high-volume recurring document families, staff approval, exception reporting, training and a runbook. Six weeks is a planning assumption after inputs/access, not a verified delivery promise. No real platform connections were made.

## Student understanding
They make money on the margin between buying and selling supplies. An emailed purchase order is already buying intent; faster processing does not automatically create an extra sale. We sell fewer manual touches and more processing capacity, with potential customer-service improvement. We are not guaranteeing extra revenue from orders the buyer already had.

Teach-back: explain what a purchase order is, which information changes between customers, who approves an uncertain product match, why a platform licence alone may not finish the implementation, and when a native product would make our offer unnecessary.

## What could kill the deal
Too little manual work; software uplift much greater than assumed; poor master data; ERP access restrictions; exceptions eating the savings; vendor implementation doing it better; or no person owning adoption. We have no verified price acceptance, no sampled buyer data and no technical sign-off yet.
