# The DESI Sikka

Crypto news, zero jargon. The DESI Sikka is a Jekyll static site that publishes
crypto news, price predictions, learn guides, press releases and daily combos
for readers worldwide.

- Live site: https://ttearncrypto.f9xr.org/thedesisikka/
- Publisher: TTEarnCrypto — https://ttearncrypto.f9xr.org
- Contact: hello@f9xr.org

## What's in here

| Path | What it holds |
| --- | --- |
| `_posts/` | All published articles. One Markdown file per story. |
| `_drafts/` | Unpublished drafts. Only built with `jekyll build --drafts`. |
| `_layouts/` | Page templates: `post`, `home`, `category`, `section`, `default`. |
| `_includes/` | Header, footer, nav dropdown, cards, newsletter form and other partials. |
| `pages/` | Standalone pages (learn hub, predictions, airdrops, events, combos). |
| `category/` | One file per category landing page (`/category/<slug>/`). |
| `_data/` | Author profiles and the Learn guide index. |
| `assets/` | CSS (`main.css`), site JS (`site.js`) and images. |
| `legal/` | Editorial policy, disclosures, privacy, terms, disclaimer. |
| `scripts/` | Local helpers (WOTD data, audits). Excluded from the build. |
| `skills/` | Agent skills for the publishing workflow. Excluded from the build. |

## Categories and sections

Posts declare `categories:` and `tags:` in their front matter. The layout and
the homepage sections read those values.

- **News categories** (`categories: [<topic>, news]`) roll up under
  `/category/news/` and the homepage **Latest Crypto News** section. Topics:
  `bitcoin`, `ethereum`, `altcoins`, `regulation`, `defi`, `exchanges`.
- **Dedicated sections** are driven by tags and are kept out of Latest Crypto
  News so they don't publish twice: `combo` (Today's Combo),
  `prediction` (Price Predictions), `press` (Press Releases), `airdrop`,
  `video`, `event`. The `featured` tag feeds the editor's picks.

Latest Crypto News filters out any post that carries a section tag or sits in
the `todays-combo` / `press` category. If a story is news, give it a normal
topic category and no section tag.

## Writing a post

Create `_posts/YYYY-MM-DD-slug-here.md` with front matter:

```yaml
---
title: "Headline as it should appear"
seo_title: "Shorter SEO title"
date: 2026-10-09
categories: [ethereum, news]
tags: [prediction]        # only for price predictions
author: newsdesk
description: "One-sentence summary used for cards, SEO and feeds."
summary:
  - "Key point one."
  - "Key point two."
keywords: "comma, separated, target, keywords"
cover_image: /assets/articles-images/example.webp
image_alt: "Describe the image for screen readers"
sources:
  - "https://example.com/source"
faq:
  - q: "A question worth answering?"
    a: "A direct 40-60 word answer."
---
```

Guidelines:

- File names are kebab-case and unique. The URL is `/news/<slug>/`.
- Post dates use the `Asia/Kolkata` calendar day. Never date a post in the
  future.
- Prefer 600-900 words, short paragraphs, named sources and plain English.
- Nothing here is financial advice; keep the disclaimers accurate.

## Local development

Requires Ruby, Bundler and Jekyll.

```bash
bundle install
bundle exec jekyll serve        # http://localhost:4000/thedesisikka/
bundle exec jekyll build        # output in _site/
bundle exec jekyll build --drafts   # include _drafts/
```

On Windows PowerShell, run one command per line (no `&&`):

```powershell
bundle exec jekyll build
```

## Configuration

Site settings live in `_config.yml`: identity, `url`/`baseurl`, social links,
navigation (`header_nav`), categories (`site_categories`), authors, analytics,
newsletter and ad hooks.

`url` must stay pointed at the host that actually serves the site
(`https://ttearncrypto.f9xr.org`) so canonical URLs, the sitemap and JSON-LD
don't resolve through a redirect.

## Deploying

The site builds and deploys through GitHub Actions to GitHub Pages on every
push to `main`. Do not commit `_site/` by hand.

## License and use

Content is published by TTEarnCrypto. Quoting is welcome with attribution
("The DESI Sikka") and a link to the source article. Nothing on the site is
financial advice.
