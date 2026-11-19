---
layout: default
permalink: /author/anjanikm/
title: "Anjani Kr Mishra (AKM)"
description: "Anjani Kumar Mishra (AKM) is a Hyderabad-based Jr Financial Data Analyst and ACCA Strategic Professional student covering Web3, crypto markets, DeFi and fintech for The DESI Sikka."
---

{% assign author_posts = site.posts | where: "author", "anjanikm" %}
{% assign page_author = site.data.authors.anjanikm %}

<div class="meta-strip compact">
  <span>Author profile</span>
  <span>{{ page_author.location }}</span>
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
      <span class="mono-label">{{ page_author.jobTitle }}</span>
      <h1 class="page-title">{{ page_author.name }}</h1>
      <p class="page-sub">{{ page_author.bio }}</p>
      {% if page_author.credentials %}<p class="page-sub" style="color:var(--accent);">{{ page_author.credentials }}</p>{% endif %}
      <div class="icon-row" style="padding-block:0.5rem 0;">
        {% for link in page_author.links %}
          <a class="icon-btn" href="{{ link.url }}" rel="noopener" title="{{ link.name }}" aria-label="{{ link.name }}">
            {% include social-icon.html name=link.icon size="16" %}
          </a>
        {% endfor %}
      </div>
    </div>
  </header>

  <div class="prose" style="max-width:46rem;margin-top:2.75rem;">
    <h2>Welcome to my corner of the internet</h2>

    <p>I'm Anjani Kumar Mishra (AKM), a Jr Financial Data Analyst, FP&amp;A enthusiast and fintech developer based in Hyderabad, India. At The DESI Sikka, I write about the intersection of traditional finance, blockchain infrastructure, crypto markets and the emerging technologies I explore and use every day.</p>

    <p>A B.Com (Honors) graduate and ACCA Strategic Professional candidate (9/12 papers cleared), I combine formal accounting standards (IFRS, IAS, GAAP) with technical expertise in Power BI, Bloomberg Terminal (BQL), SQL, Python and AI workflow automation (n8n, Claude, Copilot). Whether I'm analyzing tokenomics, evaluating market shifts or building financial models, my goal is to bridge the gap between institutional finance and decentralized ecosystems for everyday readers.</p>

    <h2>Areas of coverage</h2>

    <ul>
      <li><strong>Web3 &amp; blockchain infrastructure:</strong> how chains, L2s and on-chain data actually work, and what the architecture means for users.</li>
      <li><strong>Crypto markets &amp; tokenomics:</strong> supply schedules, unlock pressure and the numbers behind a price move.</li>
      <li><strong>DeFi vs. TradFi:</strong> where decentralized markets genuinely beat the old system, and where they quietly repeat its mistakes.</li>
      <li><strong>Financial modeling, FP&amp;A &amp; AI workflow automation:</strong> the Excel, Power BI and automation stack that turns raw data into readable decisions.</li>
    </ul>

    <h2>Credentials &amp; tools</h2>

    <p>B.Com (Honors), GITAM University. ACCA Strategic Professional candidate with 9 of 12 papers cleared. Certified in Bloomberg Market Concepts, Bloomberg Finance Fundamentals and Bloomberg Spreadsheet Analysis (BQL), with working experience across Power BI, SQL, Python, IFRS/IAS reporting and variance analysis.</p>

    <h2>Connect</h2>

    <p>Portfolio: <a href="https://inakm.github.io" rel="noopener">inakm.github.io</a> · LinkedIn: <a href="https://linkedin.com/in/inakmm" rel="noopener">in/inakmm</a> · GitHub: <a href="https://github.com/inakm" rel="noopener">inakm</a> · Email: <a href="mailto:inakm@proton.me">inakm@proton.me</a></p>
  </div>

  {% if author_posts.size > 0 %}
  <h2 class="section-title" style="margin-top:2.5rem;">Latest from Anjani Kr Mishra</h2>
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
    "name": {{ page_author.name | jsonify }},
    "alternateName": {{ page_author.alternateName | jsonify }},
    "jobTitle": {{ page_author.jobTitle | jsonify }},
    "description": {{ page_author.bio | jsonify }},
    "url": {{ page_author.url | absolute_url | jsonify }},
    {% if page_author.avatar %}"image": {{ page_author.avatar | absolute_url | jsonify }},{% endif %}
    "email": {{ page_author.email | jsonify }},
    "address": {
      "@type": "PostalAddress",
      "addressLocality": "Hyderabad",
      "addressRegion": "Telangana",
      "addressCountry": "IN"
    },
    "sameAs": {{ page_author.sameAs | jsonify }},
    "knowsAbout": {{ page_author.knowsAbout | jsonify }},
    "alumniOf": [
      { "@type": "CollegeOrUniversity", "name": "GITAM University" },
      { "@type": "EducationalOrganization", "name": "ACCA" }
    ],
    "worksFor": {
      "@type": "Organization",
      "name": {{ site.title | jsonify }},
      "url": {{ site.url | append: site.baseurl | jsonify }}
    }
  }
}
</script>
