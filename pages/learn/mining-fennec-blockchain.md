---
layout: default
permalink: /pages/learn/mining-fennec-blockchain/
title: "Mining Fennec Blockchain (FNNC): CPU Setup, Pools and Payouts"
seo_title: "Fennec Blockchain Mining Guide: CPU, Pools, Payouts"
description: "How to mine Fennec (FNNC) on a CPU: the YescryptR16 setup, pool commands, what a kilohash actually earns, and why this fork's market cap sits under $25,000."
keywords: "fennec blockchain mining, FNNC mining, yescryptR16 miner, fennec cpu pool, how to mine fennec, fennec blockchain guide"
last_modified_at: 2026-10-22
date: 2026-10-22
cover_image: /assets/articles-images/learn-fennec-blockchain.png
image_alt: "Fennec Blockchain CPU mining guide cover"
sources:
  - https://www.mining-dutch.nl/pools/fennec.php
  - https://zpool.ca/
  - https://mine.fennecblockchain.com/
  - https://scan.fennecblockchain.com/
  - https://nonkyc.io/
  - https://www.mining-scan.com/coin/fnnc
---

Fennec is a Bitcoin fork you can mine on a CPU. No ASIC, no graphics card required. That sounds like good news until you run the numbers, because the entire network mines about 3,600 FNNC a day and FNNC trades around $0.0017.

This guide covers how the chain works, how to point a miner at a pool, what the payout looks like, and where the economics land.

## What Fennec actually is

Fennec launched in November 2022 as a Bitcoin fork with a few numbers changed and one algorithm swapped out.

| Spec | Value |
| ---- | ----- |
| Algorithm | YescryptR16 (CPU and GPU only) |
| Block time | 2.5 minutes |
| Block reward | 6.25 FNNC |
| Max supply | 21,000,000 FNNC |
| Circulating supply | ~11.06M FNNC (52.7% of max) |
| Premine | 6,300,000 FNNC (30%) |
| Halving | Every 1,176,055 blocks, roughly 5.6 years |
| Coin maturity | 100 blocks |
| Difficulty retarget | Every block |
| Block size cap | 4 MB, about 26 TPS |
| P2P port | 8338 |
| RPC port | 8339 |

YescryptR16 is memory-hard, which is the whole point. Bitcoin's SHA-256 can be burned on ASICs because the work is pure compute with no memory requirement. YescryptR16 needs a large, fast memory dataset for every hash, so ASICs gain much less. That is why CPUs can still compete.

The 2.5-minute block time cuts Bitcoin's 10 minutes down by a factor of four. Fewer confirmations needed, faster settlement, less waiting.

The halving schedule matters for anyone thinking long term. At 1,176,055 blocks and 2.5-minute spacing, each halving lands about 5.6 years apart, so roughly 2032 and 2038 rather than Bitcoin's four-year cycle.

## The numbers, as of October 2026

Here is where Fennec stands right now.

- Network hashrate is about 115 kH/s.
- Difficulty is around 0.0036.
- Price is between $0.0017 and $0.0018.
- Market cap is roughly $19,000 to $20,000.
- 24-hour volume is somewhere between $28 and $55.
- All-time high was $0.1621.

Read the market cap again. The whole coin is worth less than a used laptop. Total daily issuance works out to 576 blocks times 6.25 FNNC, which is 3,600 FNNC, or about $6.30 at current prices.

For scale, Bitcoin issues about 900 BTC a day and trades in the hundreds of billions. Fennec's daily issuance is a rounding error next to that.

## The pools

Eight pools are tracked across the mining directories. Two of them actually find blocks.

**Zpool** is the largest by hashrate at roughly 105 kH/s and around 233 workers, running PROP with a 1% fee and a 0.05 FNNC minimum payout.

**Mining-Dutch** is the other big one, at about 87.6 kH/s from 25 workers on its own pool, with a much wider set of payout options.

The rest, aikapool, cpu-pool, the project's own pool at mine.fennecblockchain.com, miners-pool, zapto, and nitropool, are tracked but rarely find blocks. Payouts there come from whatever they do find, so expect a long wait.

Mining-Dutch's reward modes and fees:

| Mode | Fee |
| ---- | --- |
| D-PPS | 1.50% |
| PROP | 1.00% |
| PPLNS | 1.00% |
| PARTY | 1.00% |
| SOLO | 0.50% |

D-PPS pays you the full block reward plus fees for every share you submit. SOLO keeps the entire block reward for yourself, minus 0.5%, but you only get paid when your pool finds a block. Payouts run every 15 minutes once you clear your own threshold, and there is no withdrawal fee.

## Connecting a miner

Mining-Dutch uses the standard stratum setup. Create a wallet address first, then point your miner at the pool.

```
stratum+tcp://europe.mining-dutch.nl:3407
```

Your worker string is `Worker.yourname.yourworkername` and the password is `x`. Set your own share difficulty with `d=` in the password field, or let the port adjust it. The pool accepts NiceHash, MiningRigRentals and Braiins hashpower, and you can switch between pooled and solo mining without restarting the miner.

For the software, use cpuminer-multi or cpuminer-opt with the `yescryptr16` algorithm. If you have a GPU, ccminer is the usual choice. The pool runs on donations, which is a polite way of saying the operator keeps what the donations earn, so fees stay low.

Solo mining is worth a look if you have a fast machine. You set your share difficulty, and if you find a block, the 6.25 FNNC reward is yours minus the 0.5% solo fee.

## What you would actually earn

This is the part most guides skip, so here it is.

Mining-Dutch publishes its own multiport earnings table, and at a $0.10 per kWh power cost it puts **1 kH/s at about $0.06 per day**. So:

| Your hashrate | Gross per day |
| -------------- | ------------- |
| 1 kH/s | $0.06 |
| 5 kH/s | $0.30 |
| 10 kH/s | $0.60 |
| 50 kH/s | $3.00 |

Now add power. A CPU pulling 100 watts at $0.10 per kWh burns $0.10 a day. At 10 kH/s you would clear electricity and keep roughly $0.50 a day, about $15 a month, before pool fees. At 1 kH/s on a 100-watt CPU, power eats everything you earn.

The break-even depends almost entirely on your electricity rate. Indian residential tariffs around Rs 8 per kWh sit close to the $0.10 assumption. If your power is cheap or you already have the machine running, it works out positive. If you are paying business rates and buying a rig for this, it does not.

The honest summary: Fennec mining is a hobby that pays a few dollars a month on a machine you already own. It is not a business.

## Selling what you mine

Fennec has thin liquidity. NonKYC lists two spot markets, FNNC/USDT and FNNC/DOGE, with about $57 of combined daily market volume and roughly $1,287 sitting in the three liquidity pools. The BSC contract for the bridged token is `0xC98EeBd2B02322a9C24331c18D7A9a3414993Db0`.

That volume figure is the practical limit on your earnings. You can mine far faster than you can sell.

Getting the coin off the chain also means running a full node or trusting a remote node, since Fennec is not on every wallet and exchange. The explorer at scan.fennecblockchain.com tracks blocks, and the chain itself is the record.

## Fennec's honest scorecard

**What works.** No ASIC required, a real developer and community behind the chain, an explorer, several pools with competitive fees, bridges to Ethereum and BNB Chain, and a listing on NonKYC. It is a functioning CPU-mineable fork, which is a small category now.

**What does not.** The market cap is under $25,000. Daily trading volume is in the tens of dollars. The premine was 30% of the total supply. Block rewards are worth fractions of a cent. Nothing here justifies spending money to start.

**Who it suits.** Someone with a spare CPU, a curiosity about CPU-mineable chains, and no expectation of profit.

**Who it does not suit.** Anyone looking for income, or anyone who would have to buy hardware to try it.

If you want a picture of where this sits, read the [wallet and security guide]({{ '/pages/learn/wallet-and-security/' | relative_url }}) before you move any coin off an exchange, and the [crypto security guide]({{ '/pages/learn/crypto-security-holdings/' | relative_url }}) for the full custody breakdown.

<div class="legal-box disclaimer-box">
  <p>Mining data is a snapshot taken on October 22, 2026 and moves constantly. Pool fees, hashrate, difficulty and prices change daily. Verify current numbers on the pool dashboard and the block explorer before you commit any time or electricity. This is an educational guide, not financial advice.</p>
</div>
</section>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": {{ page.title | jsonify }},
  "description": {{ page.description | jsonify }},
  "datePublished": {{ page.date | default: page.last_modified_at | date_to_xmlschema | jsonify }},
  "dateModified": {{ page.last_modified_at | date_to_xmlschema | jsonify }},
  "author": {
    "@type": "Organization",
    "name": {{ site.data.authors.newsdesk.name | jsonify }},
    "url": {{ site.data.authors.newsdesk.url | absolute_url | jsonify }}
  },
  "publisher": {
    "@type": "NewsMediaOrganization",
    "name": {{ site.title | jsonify }},
    "logo": { "@type": "ImageObject", "url": {{ site.logo | absolute_url | jsonify }} }
  },
  "inLanguage": "en",
  "mainEntityOfPage": {{ page.url | absolute_url | jsonify }}
}
</script>
