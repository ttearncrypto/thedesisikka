---
layout: default
permalink: /legal/ai-usage/
title: "AI Usage Disclaimer"
description: "How The DESI Sikka uses AI tools in research, drafting and editing, and where a human editor stays in charge of every published story."
---

<div class="meta-strip compact">
  <span>Trust &amp; Legal</span>
  <span>How we use AI</span>
</div>

<section class="section shell">
  <header class="page-intro">
    <span class="mono-label">AI Usage Disclaimer</span>
    <h1 class="page-title">Where AI helps, and where it doesn't.</h1>
    <p class="page-sub">We use AI tools in our workflow. We don't let them publish unchecked. Here's the split, in plain terms.</p>
  </header>

  <div class="prose" style="max-width:46rem;">
    <h2>What we use AI for</h2>
    <ul>
      <li>Research and background, like gathering public sources, summarizing filings and press releases, and translating.</li>
      <li>Drafting support, turning a reporter's notes into a first version.</li>
      <li>Editing, including grammar, readability and tightening copy.</li>
      <li>Metadata, such as meta descriptions, keyword lists and image alt text.</li>
      <li>Utility work, such as generating summaries, feeds and structured data from text we already published.</li>
    </ul>

    <h2>What a human always does</h2>
    <ul>
      <li>A named human editor reviews every story before it goes live.</li>
      <li>Numbers, names, dates and quotes are checked against primary sources: exchange data, official filings, on-chain data and named statements.</li>
      <li>The editor takes responsibility for the final piece. Our bylines name people, not models.</li>
    </ul>

    <h2>What we don't do with AI</h2>
    <ul>
      <li>We don't publish AI-generated quotes or invent sources.</li>
      <li>We don't let a model pick a story, a verdict or a price target without human review.</li>
      <li>We don't create fake authors, fake reviews or fake testimonials.</li>
      <li>We don't mass-produce thin articles to chase search traffic.</li>
    </ul>

    <h2>Where you might see AI-assisted text</h2>
    <p>Quick Summary boxes and meta descriptions may start as a machine draft and are edited by a human before publishing.</p>
    <p>Some machine-readable files, like <a href="{{ '/llms.txt' | relative_url }}">llms.txt</a> and feed summaries, are assembled automatically from articles we already published. The reporting behind them still comes from a person reading sources.</p>

    <h2>Accuracy and mistakes</h2>
    <p>AI tools can be confidently wrong. That's why every fact gets checked and every story gets an editor.</p>
    <p>If an AI-assisted error slips through, we fix it and log it in the public <a href="{{ '/corrections/' | relative_url }}">corrections register</a>, the same as any other mistake.</p>

    <h2>Questions</h2>
    <p>Want to challenge how we use these tools? Reach us at <a href="mailto:{{ site.email }}">{{ site.email }}</a> or through the <a href="{{ '/pages/contact/' | relative_url }}">contact page</a>.</p>
  </div>
</section>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "name": "AI Usage Disclaimer",
  "url": {{ '/legal/ai-usage/' | absolute_url | jsonify }},
  "isPartOf": {{ '/' | absolute_url | jsonify }},
  "inLanguage": "en"
}
</script>
