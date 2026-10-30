---
title: "Bitcoin Purity (BTC1) Lists on NonKYC.io With BTC1/USDT Market"
date: 2026-10-30
categories: [exchanges, news]
tags: [featured]
description: "Bitcoin Purity (BTC1) started trading on NonKYC.io at 11:30 UTC on October 27, 2026. Deposits and withdrawals are open, with a 0.25 BTC1 minimum deposit."
summary:
  - "Bitcoin Purity (BTC1) opened a single BTC1/USDT market on NonKYC.io at 11:30 UTC on October 27, 2026, with a 0.25 BTC1 minimum deposit and a 0.2% base trading fee."
  - "Bitcoin Purity is a Bitcoin Knots fork that makes BIP110 Reduced Data rules permanent. It keeps SHA-256d mining and 10-minute blocks."
  - "The project describes BTC1 as a label for a chain that keeps Bitcoin's addresses and transaction format. It says no new asset was issued."
  - "It adds no replay protection, and its own safety page warns of reorg and double-spend risk while hash rate is low."
  - "BTC1 traded at $2.57 on October 30, down 13.26% in 24 hours, on about $819 of volume."
keywords: "bitcoin purity btc1, btc1 usdt nonkyc, nonkyc new listing, what is bitcoin purity, bitcoin purity replay protection"
sources:
  - "https://nonkyc.io/post/new_listing_bitcoinpurity_btc1"
  - "https://nonkyc.io/asset/BTC1"
  - "https://nonkyc.io/market/BTC1_USDT"
  - "https://nonkyc.io/fees"
  - "https://bitcoinpurity.org/"
  - "https://bitcoinpurity.org/safety/"
  - "https://api.nonkyc.io/api/v2/market/getbysymbol/BTC1%2FUSDT"
  - "https://bitcointalk.org/index.php?topic=5597609.0"
cover_image: https://images.nonkyc.io/announce/72766079-d1ce-43d8-a2e8-62e87ef23f2d.webp
cover_caption: "Bitcoin Purity (BTC1) started trading on NonKYC.io in a BTC1/USDT market on October 27, 2026."
---

Bitcoin Purity (BTC1) began trading on [NonKYC.io](https://nonkyc.io/?ref=657ee52b7dcff9a0fc0cfa38) at 11:30 UTC on October 27, 2026, in a single BTC1/USDT market. Deposits and withdrawals are active, the minimum deposit is 0.25 BTC1, and the venue runs without identity checks.

The listing gives the Bitcoin fork another venue outside NestEx and NeoxEX. It also attaches a ticker to a project that says it does not have one.

## What are the NonKYC.io listing details?

| Detail | Info |
| --- | --- |
| Exchange | NonKYC.io, a no-KYC venue |
| Pair | BTC1/USDT (the only market) |
| Trading start | October 27, 2026, 11:30 UTC |
| Deposits and withdrawals | Active |
| Minimum deposit | 0.25 BTC1 |
| Base trading fee | 0.2%, lower with NKYC holdings or 30-day volume |
| Withdrawal fee | $1 on most networks, higher on BTC and ERC-20 |
| Liquidity pool | About $621 |
| Proof of reserve | [nonkyc.io/asset/BTC1](https://nonkyc.io/asset/BTC1) |

The 0.25 BTC1 floor means smaller transfers will not credit. At $2.57, that is about 64 cents, so the cutoff is more about network dust than ticket size.

Indian residents still owe the 30% flat tax on crypto gains and 1% TDS on transfers, whichever venue they use.

## What is Bitcoin Purity (BTC1)?

Bitcoin Purity is a Bitcoin full node and chain built from Bitcoin Knots that locks BIP110's Reduced Data rules into consensus.

Mainnet launched at 10:00 UTC on August 19, 2026. Activation is pinned to block 961637 and hash 0000000000000000003ea74f4dafdda7ed4e02c4c1ccb9768e0ca4f9e1a35159. The current release, v1.1.0, is based on Bitcoin Knots 29.4.0.

The chain keeps SHA-256d proof of work, Bitcoin's 10-minute block target, and Bitcoin address and transaction formats. It changes difficulty to aserti3-1d with a 24-hour half-life, so it reacts faster when hash rate swings. It also rejects large arbitrary data payloads at the consensus level, which is the BIP110 idea made permanent.

Here is the part that trips people up. The project does not describe BTC1 as a new asset. Its docs say users get no new token, no claim event, and no conversion step. BTC1 is the label exchanges use for the Purity chain. The ticker is a market convention, not a protocol feature.

## Why does BTC1 have no replay protection?

Replay protection is a rule that stops a transaction signed on one chain from being valid on a forked chain. Bitcoin Purity adds none on purpose.

Because addresses, transaction serialization, and sighash stay compatible, a transaction can be valid on both Purity and the legacy Bitcoin history. That is the project's stated design: keep the path open for economic migration instead of forcing a one-time swap.

It also raises settlement risk. The project's own [safety page](https://bitcoinpurity.org/safety/) warns that reorgs and double-spend attempts can become more likely when Purity hash rate is low or unstable. It tells users not to treat zero-confirmation or lightly confirmed payments from untrusted counterparties as final.

Two limits matter here. Deep-reorg parking, which holds back a block that would rewind more than 3 blocks, is local node policy and not a consensus rule. The double-spend freeze described in the repo is specified, not implemented. Neither one is 51% attack immunity.

## How is BTC1 trading so far?

Thin. On October 30, 2026, BTC1/USDT last traded at $2.570151, down 13.26% over 24 hours, according to NonKYC's market API. The session range ran from $1.810001 to $3.487967.

Volume was 319.17 BTC1, about $819.49. The liquidity pool held roughly $621.39, with a spread of 0.498%. One order can move a book that size.

That pattern is normal for a new listing on a small venue. It is also the main risk for anyone sizing a trade from an aggregator quote.

## What should traders watch next?

Watch depth first. Compare the order book against the last print before sending a market order, and use limit orders while the book fills.

Check prices across venues. BTC1 also trades on NestEx and NeoxEX. Wide gaps between venues can look like arbitrage and turn into a bad fill if one book is thin or withdrawals are slow.

Then watch the chain. Block production and hash rate on the Purity explorer tell you whether the network is stable. A quiet chain makes the replay and reorg warnings more relevant, not less.

The proof of reserve page is labeled beta, so treat it as a signal to verify, not a guarantee. And keep an eye on whether NonKYC adds a second pair. One market means one exit route.

## Bottom line

BTC1 now trades against USDT on NonKYC.io, three days after the market opened. The listing is live and the book is small.

The details that matter sit in the project's own documentation. It is a Bitcoin fork that claims continuity, carries no new token, and skips replay protection. Read the safety page before moving size onto it.
