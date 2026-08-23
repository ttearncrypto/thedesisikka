---
layout: default
permalink: /author/f9xr/
title: "f9xr"
description: "Author profile of f9xr, crypto writer and analyst at The DESI Sikka."
---

{% assign author_posts = site.posts %}

<div class="meta-strip compact">
  <span>Author</span>
  <span>{% if author_posts.size == 1 %}1 story published{% else %}{{ author_posts.size }} stories published{% endif %}</span>
</div>

<section class="section shell">
  <header class="author-hero">
    <img class="author-avatar-lg" src="{{ site.default_author.avatar | relative_url }}" alt="{{ site.default_author.name }} avatar" width="96" height="96">
    <div>
      <span class="mono-label">Written by</span>
      <h1 class="page-title">{{ site.default_author.name }}</h1>
      <p class="page-sub">{{ site.default_author.bio }}</p>
      <div class="chip-row" style="border-bottom:none;padding-block:1rem 0;">
        <a class="chip" href="https://twitter.com/{{ site.twitter_username }}" rel="noopener">Twitter / X</a>
        <a class="chip" href="https://github.com/{{ site.github_username }}" rel="noopener">GitHub</a>
        <a class="chip" href="{{ site.telegram_url }}" rel="noopener">Telegram</a>
        <a class="chip" href="{{ site.website_credit_url }}" rel="noopener">Website</a>
      </div>
    </div>
  </header>

  {% if author_posts.size > 0 %}
  <div class="post-grid" style="margin-top:2.5rem;">
    {% for post in author_posts %}
      {% assign pcat_slug = post.categories | first %}
      {% assign pcat = site.site_categories | where: 'slug', pcat_slug | first %}
      <a class="post-card" href="{{ post.url | relative_url }}">
        <div class="post-card-cover cover-{{ pcat_slug }}">
          <span class="cover-glyph"></span>
        </div>
        <div class="post-card-body">
          <span class="post-card-cat">{% if pcat %}{{ pcat.name }}{% else %}News{% endif %}</span>
          <h2 class="post-card-title">{{ post.title | escape }}</h2>
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
