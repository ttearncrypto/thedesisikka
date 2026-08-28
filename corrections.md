---
layout: default
permalink: /corrections/
title: "Corrections"
description: "The DESI Sikka's public log of corrections, clarifications and factual updates — dated and linked to the corrected stories."
corrections: []
---

<div class="meta-strip compact">
  <span>Corrections</span>
  <span>Last updated {{ site.time | date: '%d.%m.%Y' }}</span>
</div>

<section class="section shell">
  <header class="page-intro">
    <span class="mono-label">Caught an error?</span>
    <h1 class="page-title">Corrections &amp; clarifications</h1>
    <p class="page-sub">We fix mistakes fast and record them here. Every update that changes the facts is dated below, linked to the corrected story, and mirrored on the article with an <span class="updated-label">Updated</span> label.</p>
  </header>

  {% if page.corrections.size > 0 %}
  <div class="prose" style="max-width:46rem;margin-top:2rem;">
    {% for fix in page.corrections %}
    <article class="legal-box" style="margin-bottom:1rem;">
      <p class="mono-label">{{ fix.date | date: '%d.%m.%Y' }}</p>
      <h2 class="section-title" style="font-size:1.1rem;margin:0.25rem 0 0.4rem;">
        <a href="{{ fix.url | relative_url }}">{{ fix.story }}</a>
      </h2>
      <p style="margin:0;">{{ fix.note }}</p>
    </article>
    {% endfor %}
  </div>
  {% else %}
  <div style="margin-top:2rem;">
    <p class="empty-note">No corrections on record. When facts change, we log them here.</p>
  </div>
  {% endif %}

  <div style="margin-top:2rem;max-width:46rem;">
    <p>Spotted an error in one of our stories? Send the story link and the correction to <a href="mailto:{{ site.email }}">{{ site.email }}</a> or use the <a href="{{ '/pages/contact/' | relative_url }}">contact page</a>. We investigate everything readers flag.</p>
  </div>
</section>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "name": "Corrections",
  "url": {{ '/corrections/' | absolute_url | jsonify }},
  "isPartOf": {{ '/' | absolute_url | jsonify }},
  "description": "Public log of corrections and clarifications to The DESI Sikka articles.",
  "inLanguage": "en"
}
</script>