---
layout: default
permalink: /pages/learn/wallet-and-security/
title: "Crypto Wallets & Security: Exchange vs Self-Custody"
description: "Custody, seed phrases, hardware wallets and the scams draining Indian crypto accounts. The plain-English security guide every holder should read."
last_modified_at: 2026-08-28
sources:
  - https://www.rbi.org.in/
---

<div class="meta-strip compact">
  <span>Learn</span>
  <span>Security guide</span>
</div>

<section class="section shell">
  <header class="page-intro">
    <span class="mono-label">Security guide</span>
    <h1 class="page-title">Wallets, custody and the scams to avoid.</h1>
    <p class="page-sub">The single biggest risk in crypto isn't the market — it's where you store the coins and what you click. Here's the framework, as of {{ page.last_modified_at | date: '%B %Y' }}.</p>
  </header>

  <div class="prose" style="max-width:46rem;">
    <h2>"Not your keys, not your coins"</h2>
    <p>Coins kept on an exchange are IOUs from that exchange. If the platform freezes, gets hacked or shuts down, you're a creditor in a queue, not an owner. Coins in your own wallet are actually under your control. Security is the trade: Custody is a risk-transfer; self-custody is risk management.</p>

    <h2>The three storage levels</h2>
    <ul>
      <li><strong>Exchange (custodial):</strong> easy to buy and sell, but you don't control the keys. Fine for small active balances; treat as a current account, not a vault.</li>
      <li><strong>Software wallet (self-custodial):</strong> app on your phone or desktop where you hold the private keys. Good for medium amounts you actively use.</li>
      <li><strong>Hardware wallet (cold):</strong> a dedicated device that keeps keys offline. The right place for anything you're not trading this week. In India, buy only from the official store or an authorised distributor — tampered hardware wallets are a known attack.</li>
    </ul>

    <h2>Seed phrases, invented once</h2>
    <ul>
      <li>Write the 12–24 word recovery phrase on paper (or metal) and store it somewhere only you can access. Never photograph it, never paste it into a chat, never "sync" it to a cloud service.</li>
      <li>One phrase per wallet. Share it with nobody — support agents, "verification" bots and "official recovery" sites never need it.</li>
      <li>Anyone with your phrase owns your coins, instantly and irreversibly.</li>
    </ul>

    <h2>The scams draining accounts in 2026</h2>
    <ul>
      <li><strong>Pig-butchering:</strong> "trading mentor" sends you to a fake exchange app. You can't withdraw until you deposit "tax to unlock". The money and the "tax" both disappear.</li>
      <li><strong>Fake airdrops:</strong> a free token that requires you to "connect wallet" to claim — the connect is a signature-stealer that empties your wallet.</li>
      <li><strong>SIM swap &amp; 2FA reset:</strong> keep 2FA in an authenticator app, not SMS, and disable SMS recovery where your bank allows.</li>
      <li><strong>Seeded recovery sites:</strong> give the phrase to any website and it is gone; there is no legitimate "sync your backup" service.</li>
    </ul>

    <h2>Your minimum security checklist</h2>
    <ul>
      <li>2FA via authenticator app on exchange + email accounts.</li>
      <li>Long unique passwords for every account; a password manager is fine.</li>
      <li>Withdraw idle coins to a hardware wallet or a trusted self-custody wallet.</li>
      <li>Test withdrawals with a tiny amount before moving real balances.</li>
      <li>Assume any message offering "guaranteed returns" or "free coins" is a scam until proven otherwise.</li>
    </ul>

    <div class="legal-box disclaimer-box">
      <p>This is a general security guide, not a guarantee of safety for any specific product. Verify any wallet's legitimacy independently before installing or buying. Information, not advice.</p>
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