---
layout: default
permalink: /author/f9xr/
title: "F9XR News Desk"
description: "F9XR News Desk is the editorial team behind The DESI Sikka, reporting crypto news, market analysis and policy updates around the clock."
---

{% assign author_posts = site.posts | where: "author", "newsdesk" %}
{% assign page_author = site.data.authors.newsdesk %}

<div class="meta-strip compact">
  <span>News Desk</span>
  <span>{% if author_posts.size == 1 %}1 story published{% else %}{{ author_posts.size }} stories published{% endif %}</span>
</div>

<section class="section shell">
  <header class="author-hero">
    {% if page_author.avatar %}
      <img class="author-avatar-lg" src="{{ page_author.avatar | relative_url }}" alt="{{ page_author.name }}" width="96" height="96">
    {% else %}
      <span class="author-avatar-lg author-monogram" aria-hidden="true">{{ page_author.monogram }}</span>
    {% endif %}
    <div>
      <span class="mono-label">The team behind every story</span>
      <h1 class="page-title">{{ page_author.name }}</h1>
      <p class="page-sub">{{ page_author.bio }}</p>
      {% if page_author.credentials %}<p class="page-sub" style="color:var(--accent);">{{ page_author.credentials }}</p>{% endif %}
      <div class="icon-row" style="padding-block:0.5rem 0;">
        {% for link in page_author.sameAs %}
          {% assign icon_name = link | split: '/' | slice: 2 | first %}{% assign icon_name = icon_name | remove: 'www.' %}
          {% if icon_name == 'linkedin.com' %}{% assign icon_name = 'linkedin' %}{% endif %}
          {% if icon_name == 'github.com' %}{% assign icon_name = 'github' %}{% endif %}
          {% if icon_name == 'instagram.com' %}{% assign icon_name = 'instagram' %}{% endif %}
          {% if icon_name == 'x.com' %}{% assign icon_name = 'x' %}{% endif %}
          {% if icon_name == 'youtube.com' %}{% assign icon_name = 'youtube' %}{% endif %}
          {% if icon_name == 'pinterest.com' %}{% assign icon_name = 'pinterest' %}{% endif %}
          {% if icon_name == 'f9xr.github.io' %}{% assign icon_name = 'globe' %}{% endif %}
          <a class="icon-btn" href="{{ link }}" rel="noopener" title="{{ icon_name }}" aria-label="{{ icon_name }}">
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
    "name": {{ page_author.name | jsonify }},
    "description": {{ page_author.bio | jsonify }},
    "url": {{ page_author.url | absolute_url | jsonify }},
    "image": {{ page_author.avatar | absolute_url | jsonify }},
    "sameAs": {{ page_author.sameAs | jsonify }}
  }
}
</script>
