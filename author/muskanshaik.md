---
layout: default
permalink: /author/muskanshaik/
title: "Muskaan Shaik (مسکان شیخ)"
description: "Muskaan Shaik is a Freelancer News Reporter covering crypto and finance for The DESI Sikka."
---

{% assign author_posts = site.posts | where: "author", "muskanshaik" %}

<div class="meta-strip compact">
  <span>Muskaan Shaik</span>
  <span>{% if author_posts.size == 1 %}1 story published{% else %}{{ author_posts.size }} stories published{% endif %}</span>
</div>

<section class="section shell">
  <header class="author-hero">
    <span class="author-avatar-lg author-monogram" aria-hidden="true">MS</span>
    <div>
      <span class="mono-label">Freelancer News Reporter</span>
      <h1 class="page-title">Muskaan Shaik (مسکان شیخ)</h1>
      <p class="page-sub">Freelancer News Reporter</p>
      <div class="icon-row" style="padding-block:0.5rem 0;">
      </div>
    </div>
  </header>

  {% if author_posts.size > 0 %}
  <h2 class="section-title" style="margin-top:2.5rem;">Latest from Muskaan Shaik</h2>
  <div class="post-grid">
    {% for post in author_posts %}
      {% assign pcat_slug = post.categories | first %}
      {% assign pcat = site.site_categories | where: 'slug', pcat_slug | first %}
      <a class="post-card" href="{{ post.url | relative_url }}">
        <div class="post-card-cover cover-{{ pcat_slug }}">
          <span class="cover-glyph"></span>
        </div>
        <div class="post-card-body">
          <span class="post-card-cat">{% if pcat %}{{ pcat.name }}{% else %}News{% endif %}</span>
          <h3 class="post-card-title">{{ post.title | escape }}</h3>
          <span class="post-card-meta">{{ post.date | date: '%b %-d, %Y' }}</span>
        </div>
      </a>
    {% endfor %}
  </div>
  {% else %}
  <div style="margin-top:2rem;">
    <p class="empty-note">First stories publish soon.</p>
  </div>
  {% endif %}
</section>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ProfilePage",
  "mainEntity": {
    "@type": "Person",
    "name": "Muskaan Shaik",
    "alternateName": "مسکان شیخ",
    "jobTitle": "Freelancer News Reporter",
    "url": {{ site.url | append: site.baseurl | append: '/author/muskanshaik/' | jsonify }}
  }
}
</script>
