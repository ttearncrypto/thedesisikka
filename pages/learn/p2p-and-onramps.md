---
layout: default
permalink: /pages/learn/p2p-and-onramps/
title: "P2P Crypto Trading in India: On-Ramps, DIN Checks and TDS"
description: "Peer-to-peer crypto trading in India works without UPI: how P2P on-ramps work, the DIN check that keeps you safe, and why 1% TDS applies on peer trades."
last_modified_at: 2026-08-28
sources:
  - https://www.rbi.org.in/
  - https://fiuindia.gov.in/
---

<div class="meta-strip compact">
  <span>Learn</span>
  <span>India guide</span>
</div>

<section class="section shell">
  <header class="page-intro">
    <span class="mono-label">Money guide</span>
    <h1 class="page-title">Peer-to-peer trading in India, done safely.</h1>
    <p class="page-sub">P2P is how a lot of Indians still buy crypto after UPI onramps ended. It works — if you understand the counter-party risk and the tax bit most people forget. Updated {{ page.last_modified_at | date: '%B %Y' }}.</p>
  </header>

  <div class="prose" style="max-width:46rem;">
    <h2>How P2P works</h2>
    <p>A P2P platform connects a buyer and a seller directly. The seller advertises "sell USDT for ₹X", the buyer matches the order, and the platform holds the trade and releases funds in steps. You are transacting with a stranger, so the platform's escrow flow and limits matter more than the few-paise price difference.</p>

    <h2>The DIN check</h2>
    <ul>
      <li><strong>DIN</strong> is the "Deposit/Withdrawal Identification Number" some Indian platforms auto-generate for each bank transfer. When an exchange asks you to note the DIN in your IMPS/NEFT transfer, include it exactly — that string is what lets the platform match your money to your account instantly.</li>
      <li>No DIN? Recheck the instruction screen. Entering a wrong or missing DIN is the most common reason deposits get stuck in manual review.</li>
      <li>Some platforms also run a one-time <strong>UPI-verification</strong> step to confirm your bank details match. Don't skip it; it's the same KYC hygiene as a bank check.</li>
    </ul>

    <h2>Safety rules that actually matter</h2>
    <ul>
      <li><strong>Never leave the app.</strong> Deals offered "via Telegram, outside the platform" are scams or money-laundering setups. Keep DMs and payment inside the platform.</li>
      <li><strong>Verify the payment name matches the seller.</strong> If someone pays you and the name on the bank credit doesn't match the platform's seller, stop and report it — it may be a stolen card transaction.</li>
      <li><strong>Release step by step.</strong> Platforms hold your market order until both sides confirm. Don't release to a stranger who "already paid" off-platform.</li>
      <li><strong>Keep records.</strong> Every P2P trade is a taxable and TDS-relevant event. A CSV of trades is worth more than a screenshot.</li>
    </ul>

    <h2>The TDS nobody reminds you about</h2>
    <p>1% TDS under Section 194S applies to P2P crypto trades too, because the TDS rules are drafted on "every person responsible for paying consideration". In a P2P sale, the buyer is the deductor. Some buyers are careless — so hold your own record of the consideration, and report the sale correctly in your return regardless of whether the buyer filed the TDS.</p>

    <div class="legal-box disclaimer-box">
      <p>P2P flows and registration requirements change with RBI and FIU guidance. Re-verify current rules with the platform and the Income-tax Department before trading. Information, not advice.</p>
    </div>
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