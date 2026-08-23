---
layout: default
permalink: /archive/
title: "Archive"
description: "Every story The DESI Sikka has published, newest first."
---

<div class="meta-strip compact">
  <span>Archive</span>
  <span>{{ site.posts.size }} stories</span>
</div>

<section class="section shell" style="padding-top:2rem;">
  {% if site.posts.size > 0 %}
    {% assign by_month = site.posts | group_by_exp: "post", "post.date | date: '%Y-%m'" %}
    {% for m in by_month %}
      <div class="archive-group" id="m-{{ m.name }}">
        <h2 class="archive-year">{{ m.items[0].date | date: '%B %Y' }} <span class="archive-count">({{ m.items.size }})</span></h2>
        <ul class="archive-list">
          {% for post in m.items %}
            <li>
              <a href="{{ post.url | relative_url }}">
                <time class="archive-date" datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: '%b %-d' }}</time>
                <span class="archive-title">{{ post.title | escape }}</span>
              </a>
            </li>
          {% endfor %}
        </ul>
      </div>
    {% endfor %}
  {% else %}
  <p class="empty-note">The archive opens with our first stories on September 1. Check back soon.</p>
  {% endif %}
</section>
