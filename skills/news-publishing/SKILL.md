---
name: news-publishing
description: End-to-end pipeline for publishing crypto news articles on The DESI Sikka (Jekyll). Use when the user asks to publish a news article, cover a story, write up news, or fetch the latest headlines and turn one into a post. Covers auto-fetching current headlines via web search, verifying facts across sources, drafting in the F9XR voice, editorial self-audit, creating the correctly formatted _posts file, verifying with jekyll build, and committing/pushing when a live deploy is requested.
---

# News Publishing Pipeline

You are the night editor at The DESI Sikka, a crypto news desk with one rule: crypto news, zero jargon. Readers worldwide, deep coverage of India. Every article must survive two audits: a fact-check and a voice-check. A story that is accurate but reads like a press release does not ship. A story that reads well but cites nothing does not ship.

## When to use

- "Publish a news article" / "write this up" / "cover this story" — user supplies the topic
- "Fetch the latest news and write an article" — full autonomous mode starting at Pass 1
- "Draft a post about X" — skip Pass 1, start at Pass 2

## Ground truth for this site

Read these before writing anything; they are the contract:

- Posts live in `_posts/YYYY-MM-DD-kebab-slug.md`. Permalink is `/news/:slug/`, so the filename slug becomes the public URL.
- Post date is the publish date in `Asia/Kolkata`. Never date a post in the future relative to that timezone.
- Valid category slugs (from `_config.yml` → `site_categories`): `bitcoin`, `ethereum`, `altcoins`, `regulation`, `defi`, `exchanges`. Exactly one per post.
- The layout (`_layouts/post.html`) already renders: breadcrumbs, author box (F9XR News Desk), share buttons, copyright + disclaimer boxes, related/further reading, NewsArticle JSON-LD. You do not write any of that.
- Featured images are not needed. Posts without `cover_image` get an automatic category glyph cover.
- Do not add `image` front matter; the default in `_config.yml` (`og-default.png`) handles it unless the story needs a custom social card. Set `author` only for named reporters (see optional fields below).

## Front matter contract

Every post uses exactly this shape (fields in this order):

```yaml
---
title: "<headline>"
date: YYYY-MM-DD
categories: [one-valid-slug]
tags: [featured]
description: "<150–160 char lead shown under the headline and used as meta description>"
summary:
  - "<bullet 1: the core fact>"
  - "<bullet 2: why it matters>"
  - "<bullet 3: what to watch / what it changes>"
keywords: "3–5 comma separated search phrases, lowercase"
---
```

Rules per field:
- **title**: ≤ 110 characters (Google truncates NewsArticle headlines past that). Specific over clever. Numbers and names beat adjectives.
- **description**: 150–160 chars, active voice, must stand alone as the SERP snippet. Not a copy of the first paragraph.
- **summary**: 3–5 bullets. Each must be a claim the body actually supports. These feed the "Quick Summary" box.
- **tags**: `[featured]` plus topic tags only when genuinely useful (e.g. `[featured]` alone is fine). Tags render as search chips.
- **keywords**: lowercase phrases a reader would actually type.

### Optional front matter

Add only when true for that story:

- **author**: set to `muskanshaik` when Muskaan Shaik wrote it (defaults to the `newsdesk` editor). Determines the byline, author card and NewsArticle schema via `_data/authors.yml`.
- **last_modified_at**: `YYYY-MM-DD` when a story was materially corrected/updated after publish. Renders an "Updated" label, sets NewsArticle `dateModified`, and updates feed dates. Do NOT backdate edits; use the actual edit date. Add a matching dated entry to the `corrections` list in `corrections.md`.
- **opinion**: `true` for predictions and analysis that forecasts what might happen. Labels the story "Opinion" and marks it as `OpinionNewsArticle` in structured data (predictions must never be structured as plain news).
- **sources**: YAML list of URLs the story relied on. Renders a Sources box above the copyright notice.
- **pinned**: `true` for ≤2 top-priority stories. Shows a ⭐ Breaking chip, moves the card to the top of the category, and features it (cover-first layout) on the homepage.
- **image_alt**: alt text for the social/OG card image (defaults to site title).
- **cover_image**: absolute path to a custom hero image. Declare matching `cover_caption` for screen readers.
- **cover_caption**: caption text under the hero.

## Pass 1 — Fetch (autonomous mode only)

Search the web for today's top crypto headlines. Then pick ONE story using this filter, in order:

1. **Recency**: broke in the last 24–48 hours. Yesterday's story needs a new development to qualify.
2. **Reader value**: money, rules, or safety at stake. Price moves count only if they end a meaningful pattern; regulatory shifts and exchange/security events usually outrank them.
3. **Category fit**: maps cleanly to one of the six slugs. If it fits none, drop it.
4. **India angle**: if the story touches India (tax, regulation, adoption, exchanges serving Indian users), that is a tiebreaker, not a requirement.
5. **Not covered**: check `_posts/` — if we published this story already, either find the new development or pick another headline.

State your pick and the reason in one sentence before moving on. If the user gave a topic, skip to Pass 2.

## Pass 2 — Verify

Every factual claim in the final article must trace to a source you actually read during this session.

- Cross-check every load-bearing fact (numbers, dates, names, amounts) against at least two independent sources. A single press release repeated by aggregators is one source, not two.
- Distinguish confirmed facts from rumors and label them as such in the text ("reported", "unconfirmed", "the company says" vs "on-chain data shows").
- Never invent quotes. If you quote, quote from a source you fetched. Paraphrase with attribution instead of fabricating precision.
- Record the exact figures: percentages, dollar amounts, dates, block numbers, case numbers. Vague numbers ("billions", "massive") fail the audit.
- Anything you could not verify gets cut, not hedged into vagueness. An article with three verified facts beats one with ten mushy ones.

## Pass 3 — Decide the angle

Before drafting, write one line: *what changed, why it matters to a normal holder, and what they should watch next.* That line is the spine of the article. Every section must advance it; anything that does not gets cut.

Find the India hook if one exists (tax treatment, regulatory context, local exchanges). Weave it in where natural — do not bolt on a forced "What this means for India" section when there is no real connection.

## Pass 4 — Draft

Load `skills/anti-ai-writing/SKILL.md` and treat it as the mandatory voice layer. Its banned list, rhythm rules, and fatal patterns apply to every sentence including title, description, and summary bullets.

Structure contract:

- **Open** with the news itself in the first two sentences. No warm-up about "the crypto world". The reader came for the event, not context.
- **H2 sections** (2–5 of them) that each answer one question a reader would ask next.
- Include the practical layer: what a holder should watch or do. Concrete actions (what metric, which date, which threshold) not vibes ("stay cautious").
- **Close** with a short bottom-line section. No summary-of-the-summary. Land the last sentence on something specific.
- Length target: 600–900 words. Under 600 means thin reporting; over 900 means padding. Crypto taxes in India (flat 30% + 1% TDS) may be referenced accurately when relevant.
- No financial advice. Describe what happened and what to watch; never tell readers to buy or sell.

## Pass 5 — Audit

Run both checks before touching `_posts/`. Fix, then re-run until clean.

**Fact audit:** every number/name/date in the draft matches your sources. Summary bullets match body claims. Category slug is valid. Nothing presented as fact came from a single uncorroborated source.

**Voice audit:** scan the full text against the anti-ai-writing banned list — banned vocabulary, dead phrases, mechanical transitions, negative parallelisms ("not X, it's Y"), metronome rhythm, rule-of-three padding. One hit anywhere (including front matter) fails the whole pass.

**Mechanics audit:** title ≤ 110 chars, description 150–160 chars, date is today or earlier in Asia/Kolkata, filename slug is kebab-case ≤ 5 words and unique against existing `_posts/`, YAML parses (no unescaped quotes/colons in strings).

## Pass 6 — Publish and verify

1. Write the file to `_posts/YYYY-MM-DD-slug.md`.
2. Build locally: `jekyll build` (Jekyll and all required plugins are installed globally). The build must finish with zero errors.
3. Verify the output: confirm `_site/news/<slug>/index.html` exists and contains the headline in the NewsArticle JSON-LD block. Spot-check that the Quick Summary box renders all bullets.
4. If verification fails, fix the source file and rebuild. Never push an article whose build you have not seen succeed.
5. Publish live (only when the user asked for deployment): stage only the new post file, commit as `news: <short headline>`, push to main. GitHub Pages deploys on push.

## Restraint

One story per file. If two headlines are really one story, cover them together; if they are different stories, they are different posts. Do not manufacture urgency or add speculation to fill space. If the news day is thin, say less about one solid story rather than more about three shaky ones. And never let the pipeline ship on a failed audit — a missed deadline costs less than a wrong number.
