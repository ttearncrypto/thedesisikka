---
layout: default
permalink: /pages/learn/
title: "Learn: Crypto Guides in Plain English"
description: "The DESI Sikka's guides: India crypto tax, exchange comparison, P2P on-ramps, wallet security and a plain-English glossary."
---

<div class="meta-strip compact">
  <span>Learn</span>
  <span>Guides &amp; reference</span>
</div>

<section class="section shell">
  <header class="page-intro">
    <span class="mono-label">No jargon walls</span>
    <h1 class="page-title">Learn crypto without the homework.</h1>
    <p class="page-sub">Money questions answered in plain English — updated as the rules change. If a news story confused you, the answer probably lives here.</p>
  </header>

  {% if site.data.guides.size > 0 %}
  <div class="post-grid" style="margin-top:2.5rem;">
    {% for guide in site.data.guides %}
      <a class="post-card" href="{{ '/pages/learn/' | append: guide.slug | append: '/' | relative_url }}">
        <div class="post-card-cover">
          <span class="cover-glyph"></span>
        </div>
        <div class="post-card-body">
          <span class="post-card-cat">{{ guide.label }}</span>
          <h3 class="post-card-title">{{ guide.title | escape }}</h3>
          <p class="post-card-excerpt">{{ guide.desc }}</p>
        </div>
      </a>
    {% endfor %}
  </div>
  {% endif %}

  {% comment %} ---- Newsletter signup (Tier 4) ---- {% endcomment %}
  {% include newsletter-form.html %}

  <div style="margin-top:2rem;max-width:46rem;">
    <p>Can't find a term or a how-to? <a href="{{ '/pages/contact/' | relative_url }}">Ask us</a> — the glossary is updated from real reader questions.</p>
  </div>
</section>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "CollectionPage",
  "name": "Learn Guides",
  "url": {{ page.url | absolute_url | jsonify }},
  "isPartOf": {{ '/' | absolute_url | jsonify }},
  "inLanguage": "en",
  "hasPart": [
    {% for guide in site.data.guides %}
    {
      "@type": "Article",
      "name": {{ guide.title | jsonify }},
      "url": {{ '/pages/learn/' | append: guide.slug | append: '/' | absolute_url | jsonify }}
    }{% unless forloop.last %},{% endunless %}
    {% endfor %}
  ]
}
</script>