---
layout: default
permalink: /pages/contact/
title: "Contact The DESI Sikka"
description: "Reach The DESI Sikka for story tips, corrections, partnerships or press queries."
---

<div class="meta-strip compact">
  <span>Contact</span>
  <span>We reply</span>
</div>

<section class="section shell">
  <header class="page-intro">
    <span class="mono-label">Say hello</span>
    <h1 class="page-title">Got a tip? Found an error? Talk to us.</h1>
    <p class="page-sub">We read everything. Story tips get priority, especially regulation updates and exchange issues affecting readers.</p>
  </header>

  <div class="prose" style="max-width:46rem;">
    <p><strong>Email:</strong> <a href="mailto:{{ site.email }}">{{ site.email }}</a></p>

    <h2>What to include in a tip</h2>
    <ul>
      <li>What happened and when (dates matter)</li>
      <li>Links or screenshots as proof</li>
      <li>Whether we can quote you by name</li>
    </ul>

    <h2>Social</h2>
    <ul>
      <li><a href="{{ site.telegram_url }}" rel="noopener">Telegram channel</a> for daily updates</li>
      <li><a href="https://twitter.com/{{ site.twitter_username }}" rel="noopener">Twitter / X</a> for quick takes</li>
    </ul>

    <h2>Corrections</h2>
    <p>Spotted something wrong? Email us the story link and what's off. Verified corrections get fixed fast with a note on the story. We don't quietly edit facts.</p>
  </div>
</section>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ContactPage",
  "name": "Contact The DESI Sikka",
  "url": {{ '/pages/contact/' | absolute_url | jsonify }},
  "isPartOf": {{ '/' | absolute_url | jsonify }},
  "inLanguage": "en",
  "mainEntity": {
    "@type": "Organization",
    "name": {{ site.title | jsonify }},
    "email": {{ site.email | jsonify }},
    "url": {{ '/' | absolute_url | jsonify }},
    "sameAs": [
      "https://twitter.com/{{ site.twitter_username }}",
      {{ site.telegram_url | jsonify }},
      "https://github.com/{{ site.github_username }}"
    ]
  }
}
</script>
