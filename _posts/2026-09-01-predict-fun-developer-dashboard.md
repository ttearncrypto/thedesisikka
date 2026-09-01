---
title: "Predict.fun Launches Self-Service Developer Dashboard"
date: 2026-09-01
categories: [defi]
tags: [featured]
description: "Predict.fun's new developer dashboard lets builders create apps, generate API keys, monitor usage, and manage rate limits without manual support requests."
summary:
  - "Predict.fun launched a self-service developer dashboard on September 1, 2026, replacing Discord support tickets for API access."
  - "Builders can create apps, generate API keys, monitor usage, request higher rate-limit tiers, and import existing keys from one portal."
  - "New trade burst limits cap order creation and cancellation calls per second, on by default for every new application."
  - "The BNB Chain platform has processed over $1.8 billion in volume since its December 2025 launch."
keywords: "predict.fun developer dashboard, predict.fun api key, prediction market api, trade burst limits, prediction market developers"
sources:
  - "https://x.com/predictdotfun/status/2094802487706612216"
  - "https://developers.predict.fun/"
  - "https://predict.fun/"
  - "https://news.predict.fun/predict-fun-announces-strategic-funding-round-with-yzi-labs-and-susquehanna-crypto"
---

Predict.fun launched a self-service developer dashboard on September 1, 2026. Builders can now create applications, generate API keys, monitor usage, and manage rate limits without opening a Discord support ticket. The BNB Chain prediction market is betting that third-party apps keep its $1.8 billion book growing.

Until now, getting a key meant joining Discord and filing a support ticket. That loop is gone for new apps. Teams with existing integrations can import their old keys and run everything from one screen, per the [announcement on X](https://x.com/predictdotfun/status/2094802487706612216).

## What the dashboard actually does

It pulls the whole key lifecycle into one interface. From the announcement, that means:

- Create new applications without filing a support request
- Generate API keys instead of waiting for manual issuance
- See current API usage in real time
- Check the rate limits on each application
- Request a higher usage-based tier when an app outgrows its ceiling

Importing existing keys is the feature teams underestimate. Credentials that lived in chat threads and spreadsheets become one source of truth. Predict.fun has not said whether imported keys keep their permissions or pass through manual review, so check that before moving production keys.

## What are trade burst limits?

A rate limit is a cap on how many requests an application can send within a set time window. Trade burst limits are a targeted version: they govern how many order creation and cancellation requests an app can send per second.

Predict.fun turns them on by default for every new application. Existing apps pick them up the next time the owner requests a rate-limit adjustment, which spares live integrations from a surprise mid-flight. The exact calls-per-second figure was not published, nor whether order creation and cancellation share one bucket or two.

These endpoints take the traffic. The REST API supports submitting orders, cancelling a single order, and cancelling orders in batch, plus order book and account reads. Cap the order calls and you protect the matching engine from one noisy bot.

## How the Predict.fun API works

The production API runs at `api.predict.fun` and needs a key for every request. The testnet at `api-testnet.predict.fun` does not, which makes it the place to prototype. Testnet allows up to 240 requests per minute with no key. The default mainnet limit for a standard API key is the same 240.

Beyond REST, Predict.fun offers WebSocket streams for live order book and market data, with subscriptions and heartbeats. An OAuth flow lets apps place and cancel orders on a user's behalf and read their positions. Official SDKs ship in TypeScript on npm as `@predictdotfun/sdk` and in Python on PyPI as `predict-sdk`. The [developer docs](https://developers.predict.fun/) walk through all of it, and the [live markets](https://predict.fun/) run alongside.

## Why this matters for prediction markets

A prediction market is a platform where you trade shares in the outcome of a real-world event, like a match, an election, or a price milestone. Prices reflect what the crowd thinks is going to happen.

Predict.fun launched on BNB Chain in December 2025. Its founder, Ding, previously built PancakeSwap and led research at Binance. As of April 2026, the platform had processed more than $1.8 billion in cumulative volume, matched over 4 million orders, and crossed 130,000 users, figures YZi Labs shared when it announced a follow-on investment with Susquehanna Crypto.

The distribution is stacked. Binance Wallet made Predict.fun the engine for its prediction markets product in April 2026, letting eligible users trade inside the Binance app with sponsored gas. In March 2026, Predict.fun acquired Probable, an on-chain prediction market. And Predict.fun routes the collateral behind open positions into the Venus Protocol money market, so deposited USDT earns yield while a market resolves.

That last part is where prediction markets usually fall short. Polymarket and Kalshi leave collateral idle while positions are open. Predict.fun puts it to work, the quiet reason this story lives in the [DeFi & Web3]({{ '/category/defi/' | relative_url }}) section.

The sector keeps climbing. TRM Labs data shows monthly prediction market volume rising from roughly $1.2 billion in early 2025 to more than $20 billion in January 2026. FalconX research put 2025 volume at about $64 billion, nearly four times the year before.

## What's still unclear

Predict.fun published the dashboard's job list but kept the numbers close:

- Burst limits: the calls-per-second figure is unpublished
- Tiers: criteria for higher usage tiers are not documented
- Key import: whether imported keys keep permissions is unconfirmed
- Beta: the REST API is still labeled beta, so endpoints can change

There's the US question too. An API key is a credential. Holding one does not authorize you to offer event contracts to US customers, and federal and state rules on prediction markets are still being argued in court. Predict.fun's announcement did not address regional access. Binance.US said in July 2026 that it plans to apply for a CFTC designated contract market license, the regulated route into that market.

## Bottom line

Predict.fun replaced a ticket queue with a product. Developers can go from idea to working API key in minutes, and the trade burst controls show the platform is planning for serious automated order flow. Self-service access is what turns a prediction market into infrastructure that other apps build on. Watch the unpublished ceilings and key-import behavior before you move production traffic. Our [newsdesk]({{ '/news/welcome-to-the-desi-sikka/' | relative_url }}) will keep tracking how the dashboard settles in.