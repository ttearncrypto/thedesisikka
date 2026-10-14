# The DESI Sikka — SEO + YMYL Audit Report (Refresh)

**Date:** October 14, 2026
**Previous audit:** September 16, 2026
**Auditor:** F9XR Code Agent
**Site:** `https://ttearncrypto.f9xr.org/thedesisikka/`
**Platform:** Jekyll 3.10, GitHub Pages
**Content:** 55 published posts (44 daily Binance WOTD answers + 11 news/features), 5 learn guides, ~21 static pages, 79 sitemap URLs
**Target audience:** Global crypto readers with deep India focus; financial news (YMYL-adjacent)

---

## Executive Summary

The September 16 audit raised 18 findings, including two AdSense-readiness blockers (H1: the predict.fun post lacked a body-level "not financial advice" disclaimer; H2: Muskaan Shaik's author page had no photo, credentials, or complete schema). **Both blockers are now closed**, along with 14 other findings. Every HIGH and MEDIUM item from the prior report is resolved.

The site also shipped a layer of AI-agent discovery infrastructure that puts it ahead of most crypto publishers: a `.well-known/ai-catalog.json` agent catalog, a robots.txt `Agentmap` directive, an explicit `Content-Signal` policy, and a WebMCP tool registration so browser agents can drive the site's search. Cover images now preload with `fetchpriority="high"` for LCP, and Google Fonts load non-blocking.

**Two low-severity technical items remain open:**
1. `assets/main.css` (57KB) and `assets/site.js` (21KB) are still unminified
2. No IndexNow ping (Bing/Yandex are not notified on publish)

**One new strategic item to watch:**
3. The daily WOTD series now produces 44 near-template posts in `/news/`. Each covers a distinct puzzle with unique data, but the volume and shared structure need active curation so Google does not read the archive as mass-produced content.

**Overall YMYL Confidence Score: 90/100** (up from 72). AdSense-readiness blockers are cleared; what remains is performance polish and content-scale hygiene.

---

## What changed since the September 16 audit

| # | Finding (Sept 16) | Severity | Status now | Evidence |
|---|-------------------|----------|------------|----------|
| 1 | No favicon anywhere | HIGH | ✅ Fixed | `assets/site-images/favicon-16x16.png`, `favicon-32x32.png`, `apple-touch-icon.png` exist; linked in `head.html:103-105` |
| 2 | About grammar "a exit-liquidity" | HIGH | ✅ Fixed | `about.md:31` now "an exit-liquidity trap" |
| 3 | predict.fun missing disclaimer | HIGH | ✅ Fixed | `_posts/2026-09-01-predict-fun-developer-dashboard.md:28-30` "Not financial advice" box |
| 4 | Muskaan author E-E-A-T weak | HIGH | ✅ Fixed | `_data/authors.yml:21-45` avatar, "Freelance Crypto Reporter", credentials, `sameAs`, `knowsAbout`; full ProfilePage schema in `author/muskanshaik.md:56-77`; `assets/authors/muskaan.png` present |
| 5 | `website_credit_url` old domain | MEDIUM | ✅ Fixed | `_config.yml:23` → `https://f9xr.org` |
| 6 | Privacy/Terms stale dates | MEDIUM | ✅ Fixed | Both now "Last updated: October 2026" |
| 7 | About page lists 5 of 8 categories | MEDIUM | ✅ Fixed | `about.md:29-37` lists all 7 editorial sections |
| 8 | Cover images lack width/height | MEDIUM | ✅ Fixed | `_layouts/post.html:39` `width="1200" height="675"` |
| 9 | Logo 639KB loaded in header | MEDIUM | ✅ Fixed | Header uses `logo-square.png` (12KB) at `_includes/header.html:4` |
| 10 | Learn guides lack cover images | MEDIUM | ✅ Fixed | All 5 guides define `cover_image` in front matter |
| 11 | Unminified CSS/JS | LOW | ⏳ Deferred | `main.css` 57KB, `site.js` 21KB — GitHub Pages serves gzip/brotli; manual minification risks breakage |
| 12 | Google Fonts render-blocking | LOW | ✅ Fixed | `head.html:108` async pattern (`media="print" onload="this.media='all'"`) + `<noscript>` fallback |
| 13 | No IndexNow | LOW | ⏳ Deferred | Subpath deployment blocks domain-root key placement; `ai-catalog.json` + `Agentmap` now cover agent discovery instead |
| 14 | llms-full.txt misleading header | LOW | ✅ Fixed | `llms-full.txt:5` now "site overview and content summaries for LLM consumption" |
| 15 | No skip-to-content link | LOW | ✅ Fixed | `_layouts/default.html:5` skip link to `#main` |
| 16 | No related posts section | LOW | ✅ Fixed | `_layouts/post.html:210-221` "Related News" + sidebar "More in" |
| 17 | About page schema incomplete | LOW | ✅ Fixed | `about.md:59-60` adds `datePublished` + `dateModified` |
| 18 | Learn guides missing datePublished | LOW | ✅ Fixed | All 5 guides carry `date: 2026-08-28` |

**Scorecard: 16 of 18 resolved, 2 deferred with documented rationale.**

---

## Pillar-by-Pillar Findings (current)

| # | Pillar | Status | Score | Key Finding |
|---|--------|--------|-------|-------------|
| 1 | Technical Foundation | ✅ Pass | 9/10 | HTTPS, canonical, robots.txt + sitemap clean |
| 2 | Crawlability & Indexability | ✅ Pass | 9/10 | Empty pages noindexed, feeds disallowed, `.well-known` included in build |
| 3 | Core Web Vitals | ⚠️ Improve | 8/10 | Cover preload + async fonts shipped; CSS/JS still unminified |
| 4 | Mobile SEO | ✅ Pass | 8/10 | Responsive, flex nav, 48px touch targets |
| 5 | Site Architecture | ✅ Pass | 8/10 | Flat hierarchy, category nav, breadcrumbs |
| 6 | On-Page SEO | ✅ Pass | 9/10 | Unique titles (now with `seo_title` overrides), descriptions, H1s, OG tags |
| 7 | Content Quality & E-E-A-T | ✅ Pass | 9/10 | Author credibility fixed; grammar clean; disclaimer present |
| 8 | Structured Data | ✅ Pass | 9/10 | NewsArticle/OpinionNewsArticle, FAQPage, BreadcrumbList, Organization, WebSite, ProfilePage, AboutPage, Speakable |
| 9 | IndexNow & Fresh Indexing | ⚠️ Partial | 6/10 | No IndexNow; `ai-catalog.json` + `Agentmap` + WebMCP added for agent discovery |
| 10 | Images & Media | ✅ Pass | 9/10 | Favicon set, learn-guide covers, PNG/WebP with dimensions |
| 11 | Internal Linking | ✅ Pass | 8/10 | Category nav, footer, Related News, WOTD hub strip |
| 12 | External Linking | ✅ Pass | 8/10 | `rel="noopener"` handled, authoritative sources cited |
| 13 | Social SEO | ✅ Pass | 8/10 | OG + Twitter on all pages, per-page OG image dimensions |
| 14 | News SEO & Google News | ⚠️ Improve | 7/10 | NewsArticle present, 55 posts, fresh daily cadence; no news sitemap |
| 15 | Local/Geo SEO | ⚠️ Improve | 6/10 | India content strong; no `geoCoordinates` in Organization schema |
| 16 | YMYL & E-E-A-T | ✅ Pass | 9/10 | Legal stack complete, disclaimers everywhere, author E-E-A-T fixed |
| 17 | Schema Markup | ✅ Pass | 9/10 | Coverage broad and valid post-fixes |
| 18 | AI/SGE Readiness | ✅ Pass | 9/10 | `llms.txt`, `llms-full.txt`, `ai-catalog.json`, `Content-Signal`, WebMCP |
| 19 | Security | ⚠️ Partial | 6/10 | HTTPS + security.txt; no CSP headers (GitHub Pages limitation) |
| 20 | Accessibility | ✅ Pass | 8/10 | Semantic HTML, alt text, skip link present |
| 21 | Competitive Analysis | N/A | — | Standalone audit |
| 22 | Video/YouTube SEO | N/A | — | Videos page noindexed until real video is published |
| 23 | Voice Search | ✅ Pass | 8/10 | FAQPage + Speakable selectors on posts |
| 24 | Feed & Syndication | ✅ Pass | 9/10 | RSS, Atom, JSON Feed full-text and current |

---

## New / Remaining Findings

### FINDING A — Unminified CSS and JS (carried over)
**Pillar:** 3 (CWV)
**Severity:** LOW
**File:** `assets/main.css` (57KB), `assets/site.js` (21KB)
**Evidence:** Both files ship with comments and whitespace. Combined ~78KB uncompressed.
**Impact:** Marginal. GitHub Pages compresses responses (gzip/brotli), so wire size is roughly a third of that. Parse time on low-end mobile is the only real cost, and the JS is `defer`red.
**Recommendation:** Add a build-time minifier (e.g., `jekyll-minifier`) in CI rather than hand-minifying. Keep this deferred until total payload crosses ~150KB or Lighthouse flags a parse-time cost.
**Effort:** 30 min | **Traffic impact:** Minimal | **Revenue impact:** Low

### FINDING B — No IndexNow implementation (carried over)
**Pillar:** 9 (Indexing)
**Severity:** LOW
**File:** N/A (missing infrastructure)
**Evidence:** No IndexNow key file and no ping step. Bing and Yandex learn about new posts only via their crawl schedule.
**Impact:** Small for a crypto news audience dominated by Google. The site mitigates this with `ai-catalog.json`, a robots.txt `Agentmap`, and explicit `Content-Signal` policy for AI agents.
**Recommendation:** Because the site is served from a `/thedesisikka` subpath, the IndexNow key must live at the domain root (`https://ttearncrypto.f9xr.org/<key>.txt`), which this repo does not control. If root access becomes available, ship a post-deploy ping. Otherwise leave as-is.
**Effort:** 1–2 hrs (blocked on root) | **Traffic impact:** Low | **Revenue impact:** Low

### FINDING C — WOTD daily series now dominates the archive (new)
**Pillar:** 7 (Content), 14 (News SEO)
**Severity:** MEDIUM (watch)
**File:** `_posts/*binance-wotd-*.md` (44 posts)
**Evidence:** 44 of 56 `/news/` URLs are the same daily template ("Binance WOTD Answers <Date>"), roughly 800 words each with unique word lists per day. They are published under `[todays-combo, news]`, so they surface under the indexable News category and in the main feed.
**Impact:** Each post targets a real, dated query ("Binance WOTD answers October 14"), so individual pages can rank. The risk is a site-level quality signal: a feed where 79% of items share one structure can read as scaled/templated content, which Google's spam policies name specifically. The hub page (`/pages/binance-wotd-answers/`) already consolidates them, which helps.
**Recommendation:**
1. Keep the WOTD hub as the single canonical entry point and cross-link every WOTD post to it (already partially done via `post.html:200-208`).
2. Consider `categories: [todays-combo]` only for older posts after a cycle closes, so the News category stays editorial-led. (Currently they are dual-categorized into News.)
3. Keep per-post data unique (word lists already are) and avoid auto-generating posts for dates with no real puzzle data.
4. Watch Search Console for "Crawled – currently not indexed" clustering on WOTD URLs; if it appears, prune or consolidate older cycles.
**Effort:** 1–2 hrs (categorization) | **Traffic impact:** Medium | **Revenue impact:** Medium

### FINDING D — Google Fonts still external (optional)
**Pillar:** 3 (CWV), 19 (Security)
**Severity:** LOW
**File:** `_includes/head.html:106-109`
**Evidence:** Fonts now load non-blocking (`media="print" onload`), so the render-blocking issue from the prior audit is resolved. The stylesheet is still fetched from `fonts.googleapis.com`, which adds a third-party request and a privacy consideration.
**Recommendation:** Self-host the two families as WOFF2 with `font-display: swap` if privacy or a stricter CSP becomes a goal. No urgency — current behavior is acceptable.
**Effort:** 30 min | **Traffic impact:** Minimal | **Revenue impact:** Low

---

## Strengths added since the last audit

These are worth preserving, not just noting:

- **AI-agent discovery stack.** `.well-known/ai-catalog.json` (a DID-based agent catalog), robots.txt `Agentmap`, a `Content-Signal: search=yes, ai-input=yes, ai-train=yes` policy, and a WebMCP `registerTool` handler in `site.js` that lets browser agents call site search. Few crypto publishers have shipped any of this.
- **Per-page `seo_title` overrides.** Long headlines now carry a tighter SERP variant (e.g., the Ethereum prediction post), reducing truncation risk.
- **LCP preload.** `head.html:101` preloads the cover image with `fetchpriority="high"` on any post that has one.
- **Non-blocking fonts.** See Finding D.
- **Disclaimer coverage.** The predict.fun post now adds an in-body "Not financial advice" box on top of the layout-level site disclaimer applied to every post.
- **Opinion separation enforced.** `post.html:9-10` renders `OpinionNewsArticle` whenever a post is tagged `prediction` or sets `opinion: true`, so speculative content is schema-flagged automatically.

---

## Quick Wins (do now)

| # | Fix | File | Effort |
|---|-----|------|--------|
| 1 | Add `geoCoordinates` to the Organization schema | `_layouts/default.html` | 5 min |
| 2 | Re-categorize closed WOTD cycles to `todays-combo` only | `_posts/*binance-wotd-*` | 15 min |
| 3 | Add a `dateModified` refresh pass on the 11 evergreen news posts | `_posts/*` | 15 min |

## Medium-Term Fixes

| # | Fix | Effort | Impact |
|---|-----|--------|--------|
| 1 | Build-time CSS/JS minification | 30 min | CWV polish |
| 2 | News sitemap (last 48h) for Google News ingestion | 1 hr | News/Discover |
| 3 | WOTD archive curation policy (see Finding C) | 1–2 hrs | Content quality signal |
| 4 | Self-host fonts | 30 min | Privacy + CSP readiness |

## Long-Term (as content scales)

| Fix | When | Impact |
|-----|------|--------|
| IndexNow ping | When domain-root access exists | Bing/Yandex speed |
| Related-news tuning / topic clusters | 100+ posts | Internal linking |
| Full content in `llms-full.txt` | AI citation strategy | GEO depth |

---

## YMYL Confidence Score

| Factor | Score | Notes |
|--------|-------|-------|
| Financial disclaimer | 9/10 | Layout-level box on every post + a dedicated box in the predict.fun post |
| Author credibility | 9/10 | F9XR desk strong; Muskaan page now has photo, jobTitle, credentials, `sameAs`, `knowsAbout`, full schema |
| Editorial standards | 9/10 | Editorial policy, corrections, disclosures, AI-usage policy all present |
| Trust pages (About, Contact, Legal) | 10/10 | All present, current (Oct 2026), and schema-marked |
| Content freshness | 9/10 | Daily WOTD cadence + 11 news posts; legal pages refreshed |
| Source citation | 8/10 | Learn guides cite incometax.gov.in/RBI; posts cite primary sources |
| Opinion vs fact separation | 9/10 | Enforced in schema via `is_opinion` derivation |
| India-specific accuracy | 8/10 | 115BBH, 194S, 30% + 1% TDS correctly cited |
| AI/SGE readiness | 10/10 | llms.txt, llms-full.txt, ai-catalog.json, Agentmap, WebMCP |

**Overall YMYL Confidence: 90/100** (up from 72/100 on September 16).

The remaining 10 points are structural, not editorial: no CSP (GitHub Pages constraint), no IndexNow (root-access constraint), and the WOTD archive-scale question, which resolves through curation over time rather than a one-time fix.

---

## Verdict

The two AdSense-readiness blockers from September are gone. The predict.fun post now disclaims in the body, and Muskaan Shaik's author page carries the photo, credentials, and complete `ProfilePage` schema a YMYL reviewer looks for. Sixteen of eighteen findings are closed; the two that remain are low-severity and documented as deferred for good reasons.

The site is **ready to apply for AdSense** and has the E-E-A-T and structured-data depth to compete with established crypto publishers. The next frontier is not fixing defects but managing scale: keep the daily WOTD series curated, keep external notifications (IndexNow) on the roadmap, and treat Core Web Vitals as an ongoing budget. None of that blocks a launch — it is the work of a site that has outgrown its first audit.
