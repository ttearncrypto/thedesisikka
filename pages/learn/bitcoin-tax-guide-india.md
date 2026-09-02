---
layout: default
permalink: /pages/learn/bitcoin-tax-guide-india/
title: "Bitcoin Tax in India: 30% Rate, 1% TDS and the Rules That Apply"
description: "Bitcoin and other virtual digital assets are taxed at 30% in India with a 1% TDS on every transfer. Here's how the rules work, in plain English."
last_modified_at: 2026-08-28
sources:
  - https://www.incometax.gov.in/iec/foportal/help/tds-on-crypto-currencies-virtual-digital-assets
  - https://www.incometax.gov.in/
---

<div class="meta-strip compact">
  <span>Learn</span>
  <span>India guide</span>
</div>

<section class="section shell">
  <header class="page-intro">
    <span class="mono-label">Money guide</span>
    <h1 class="page-title">Bitcoin tax in India, explained.</h1>
    <p class="page-sub">Crypto income in India is taxed like almost nothing else. One flat rate, one TDS, and no deductions. Here is exactly how the rules work, updated {{ page.last_modified_at | date: '%B %Y' }}.</p>
  </header>

  <div class="prose" style="max-width:46rem;">
    <h2>First, the vocabulary</h2>
    <p>Indian law doesn't say "crypto". It calls digital assets <strong>Virtual Digital Assets (VDAs)</strong> — defined under <strong>Section 2(47A)</strong> of the Income-tax Act. Bitcoin, Ethereum and most tokens qualify. Non-fungible tokens and some specific tokens fall outside in certain conditions, but for everyday trading, treat your coins as VDAs.</p>

    <h2>The 30% flat rate</h2>
    <p>Income from transferring a VDA is taxed at a flat <strong>30%</strong> plus applicable surcharge and cess, under <strong>Section 115BBH</strong>. The three consequences most people miss:</p>
    <ul>
      <li><strong>No deductions.</strong> You cannot subtract brokerage fees, electricity, internet or other expenses. Only the original cost of acquisition reduces your income.</li>
      <li><strong>No set-off of losses.</strong> If you lost money on one coin but gained on another, you cannot net them. Losses from VDAs cannot be set off against VDA gains, and they cannot be carried forward.</li>
      <li><strong>Rate is flat.</strong> It is 30% regardless of your slab. It never drops to 10% or 20%.</li>
    </ul>

    <h2>The 1% TDS</h2>
    <p>Anyone transferring a VDA must deduct <strong>1% TDS</strong> on the consideration under <strong>Section 194S</strong> — even if the tax already covers the buyer and seller. In practice this means:</p>
    <ul>
      <li>An exchange or platform handling your sale deducts the 1% at source and reports it to the Tax Department.</li>
      <li>In <strong>peer-to-peer trades</strong>, the buyer is responsible for deducting and depositing the TDS. If a buyer doesn't bother, you're not automatically off the hook — keep records of every P2P trade.</li>
      <li>Minors buying via a guardian and custodians get special substitution rules; for most readers, the 1% applies on the full consideration.</li>
    </ul>

    <h2>What's taxable</h2>
    <ul>
      <li><strong>Selling crypto for rupees</strong> — profit is income under 115BBH.</li>
      <li><strong>Trading crypto for crypto</strong> — the fair market value of the asset received counts as consideration, and the TDS rules apply to it.</li>
      <li><strong>Receiving crypto as goods/services</strong> — for a business, the VDA can become business income instead of VDA income, which is usually worse. Check how your income is classified.</li>
      <li><strong>Gifts</strong> — a gift of crypto above the exemption limit can be taxable in the recipient's hands; the giver's cost basis rules are stricter than for cash gifts.</li>
    </ul>

    <h2>The filing checklist</h2>
    <ul>
      <li>Summarise every trade (buy/sell/gift) with date, value and counterparty — even the tiny ones.</li>
      <li>Reconcile the 1% TDS your exchange deducted (check Form 26AS / AIS) so you don't pay it twice.</li>
      <li>Report gains under the correct schedule for VDAs; the ITR forms have a dedicated place for 115BBH income.</li>
      <li>Keep records for the full seven-year retention window.</li>
    </ul>

    <div class="legal-box disclaimer-box">
      <p>Tax rules can change with a budget speech. This guide reflects the law as of {{ page.last_modified_at | date: '%B %Y' }} and is information, not professional tax advice. Verify current rates and thresholds with the Income-tax Department or a registered chartered accountant before filing.</p>
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