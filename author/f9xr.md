---
layout: default
permalink: /author/f9xr/
title: "F9XR News Desk"
description: "F9XR News Desk is the editorial team behind The DESI Sikka, reporting crypto news, market analysis and policy updates around the clock."
---

{% assign author_posts = site.posts %}

<div class="meta-strip compact">
  <span>News Desk</span>
  <span>{% if author_posts.size == 1 %}1 story published{% else %}{{ author_posts.size }} stories published{% endif %}</span>
</div>

<section class="section shell">
  <header class="author-hero">
    {% if site.default_author.avatar %}
      <img class="author-avatar-lg" src="{{ site.default_author.avatar | relative_url }}" alt="{{ site.default_author.name }}" width="96" height="96">
    {% else %}
      <span class="author-avatar-lg author-monogram" aria-hidden="true">F9</span>
    {% endif %}
    <div>
      <span class="mono-label">The team behind every story</span>
      <h1 class="page-title">{{ site.default_author.name }}</h1>
      <p class="page-sub">{{ site.default_author.bio }}</p>
      <div class="icon-row" style="padding-block:0.5rem 0;">
        {% for link in site.author_links %}
          {% assign icon_name = link.name | downcase %}
          {% if icon_name == 'website' %}{% assign icon_name = 'globe' %}{% endif %}
          <a class="icon-btn" href="{{ link.url }}" rel="noopener" title="{{ link.name }}" aria-label="{{ link.name }}">
            {% include social-icon.html name=icon_name size="16" %}
          </a>
        {% endfor %}
      </div>
    </div>
  </header>

  {% if author_posts.size > 0 %}
  <h2 class="section-title" style="margin-top:2.5rem;">Latest from F9XR News Desk</h2>
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
    <p class="empty-note">First stories publish September 1.</p>
  </div>
  {% endif %}
</section>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ProfilePage",
  "mainEntity": {
    "@type": "Organization",
    "name": "F9XR News Desk",
    "description": {{ site.default_author.bio | jsonify }},
    "url": {{ site.url | append: site.baseurl | append: '/author/f9xr/' | jsonify }},
    "sameAs": [{% for link in site.author_links %}{{ link.url | jsonify }}{% unless forloop.last %},{% endunless %}{% endfor %}]
  }
}
</script>
