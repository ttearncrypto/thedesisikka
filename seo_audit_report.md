# The DESI Sikka — SEO + YMYL Audit Report

**Date:** September 16, 2026
**Auditor:** F9XR Code Agent
**Site:** `https://ttearncrypto.github.io/thedesisikka/`
**Platform:** Jekyll 3.10, GitHub Pages
**Content:** 3 published posts, 5 learn guides, 8 category/section pages, 5 legal pages
**Target audience:** Global crypto readers with deep India focus; financial news (YMYL-adjacent)

---

## Executive Summary

The DESI Sikka is structurally sound for a new crypto news publication. Previous fixes (og:image mapping, schema deduplication, empty page noindex, newsletter placement) resolved the two critical Discover/AdSense blockers. The site now has 27 clean sitemap URLs, 9+ schema types, a full legal trust stack, and editorial disclaimers.

**Two high-priority YMYL gaps remain:**
1. The predict.fun post — a financial product explainer — lacks a "not financial advice" body disclaimer, which Google's YMYL quality rater guidelines specifically flag for crypto content
2. Muskaan Shaik's author page has no professional photo, no verifiable credentials, and an incomplete ProfilePage schema — weakening E-E-A-T for every post she bylines

**Three medium-high SEO gaps:**
3. No favicon exists (browser 404s on every page)
4. Cover images lack explicit `width`/`height` attributes (CLS risk)
5. The about page contains a grammar error ("a exit-liquidity") on a high-traffic trust page

**Overall YMYL Confidence Score: 72/100** — strong foundation, two gaps to close before AdSense review.

---

## Pillar-by-Pillar Findings

| # | Pillar | Status | Score | Key Finding |
|---|--------|--------|-------|-------------|
| 1 | Technical Foundation | ✅ Pass | 9/10 | HTTPS, canonical, robots.txt, sitemap clean |
| 2 | Crawlability & Indexability | ✅ Pass | 9/10 | 9 empty pages noindexed, feed.json disallowed |
| 3 | Core Web Vitals | ⚠️ Fix | 6/10 | Unminified CSS/JS, oversized logo, CLS from missing img dimensions |
| 4 | Mobile SEO | ✅ Pass | 8/10 | Responsive, flex nav, 48px touch targets |
| 5 | Site Architecture | ✅ Pass | 8/10 | Clean flat hierarchy, category nav, breadcrumbs |
| 6 | On-Page SEO | ✅ Pass | 8/10 | Unique titles, descriptions, H1s, OG tags on all pages |
| 7 | Content Quality & E-E-A-T | ⚠️ Fix | 6/10 | Grammar error on about.md, weak author E-E-A-T, no "not financial advice" in predict.fun post |
| 8 | Structured Data | ⚠️ Fix | 7/10 | 9 schema types present; learn guides missing datePublished, no Article schema on about.md |
| 9 | IndexNow & Fresh Indexing | ❌ Missing | 3/10 | No IndexNow, no Google Indexing API |
| 10 | Images & Media | ⚠️ Fix | 6/10 | No favicon, no apple-touch-icon, logo 639KB, learn guides lack cover images |
| 11 | Internal Linking | ✅ Pass | 7/10 | Category nav, footer, in-content links; no related posts |
| 12 | External Linking | ✅ Pass | 8/10 | rel="noopener" handled, authoritative sources cited |
| 13 | Social SEO | ✅ Pass | 8/10 | OG + Twitter on all pages, social profiles in footer |
| 14 | News SEO & Google News | ⚠️ Fix | 6/10 | NewsArticle present; no news-specific sitemap, opinion:true unused, only 3 posts |
| 15 | Local/Geo SEO | ⚠️ Fix | 5/10 | India content strong; no geoCoordinates in Organization schema |
| 16 | YMYL & E-E-A-T | ⚠️ Fix | 7/10 | Legal stack excellent; predict.fun post missing disclaimer, Muskaan weak E-E-A-T |
| 17 | Schema Markup | ⚠️ Fix | 7/10 | Good coverage; learn guides Article schema missing datePublished |
| 18 | AI/SGE Readiness | ⚠️ Fix | 7/10 | llms.txt present; llms-full.txt misleading (promises full content, has summaries) |
| 19 | Security | ⚠️ Partial | 6/10 | HTTPS + security.txt; no CSP headers (GitHub Pages limitation) |
| 20 | Accessibility | ⚠️ Fix | 6/10 | Semantic HTML + alt text; no skip-to-content link |
| 21 | Competitive Analysis | N/A | — | Standalone audit |
| 22 | Video/YouTube SEO | N/A | — | No video content on site yet |
| 23 | Voice Search | ✅ Pass | 7/10 | FAQ schema on Binance post, clear headings |
| 24 | Feed & Syndication | ✅ Pass | 9/10 | RSS, Atom, JSON Feed all present with full HTML content |

---

## Detailed Findings

### FINDING 1 — No favicon anywhere in the repository
**Pillar:** 3 (CWV), 10 (Images)
**Severity:** HIGH
**File:** Repository root + `/assets/`
**Evidence:** `glob favicon*` and `glob assets/*icon*` return zero results. Browsers request `/favicon.ico` on every page load — every request 404s. No `<link rel="icon">` in `head.html`.
**Impact:** Unprofessional appearance in browser tabs, bookmark bars, and search results. Minor crawl waste (404 per page load). AdSense reviewers notice missing basics.
**Fix:** Generate `favicon.ico` (16×16, 32×32), `apple-touch-icon.png` (180×180), and `favicon-32x32.png`. Add `<link rel="icon" ...>` and `<link rel="apple-touch-icon" ...>` to `head.html`. Optionally add `site.webmanifest`.
**Effort:** 30 min
**Traffic impact:** Low (indirect credibility signal)
**Revenue impact:** Medium (AdSense reviewer perception)

### FINDING 2 — About page grammar error: "a exit-liquidity"
**Pillar:** 7 (Content/E-E-A-T), 16 (YMYL)
**Severity:** HIGH
**File:** `about.md:31`
**Evidence:** `<li><strong>Altcoins:</strong> what's building and what's a exit-liquidity trap</li>`
**Impact:** The about page is the #1 trust signal for YMYL. Grammar errors on trust pages directly undermine credibility with quality raters. Google's E-E-A-T guidelines emphasize "high quality" as including "well-written, factually accurate."
**Fix:** Change `a exit-liquidity` → `an exit-liquidity`
**Effort:** 1 min
**Traffic impact:** Low (indirect)
**Revenue impact:** Medium (AdSense review perception)

### FINDING 3 — predict.fun post lacks "not financial advice" body disclaimer
**Pillar:** 16 (YMYL)
**Severity:** HIGH
**File:** `_posts/2026-09-01-predict-fun-developer-dashboard.md`
**Evidence:** This post discusses a financial product (prediction markets with USDC contracts on BNB Chain). It has no "not financial advice" disclaimer in the body. The site-wide disclaimer page exists, but Google's YMYL quality rater guidelines specifically require financial content to have "prominent" disclaimers — not just a buried link to a separate page.
**Impact:** Direct YMYL quality rater flag. The post reads as instructional ("Builders can now create applications, generate API keys") without clarifying this is news, not investment advice. A reviewer could flag this as YMYL content lacking appropriate warnings.
**Fix:** Add a visible disclaimer box (matching the legal-box styling used in the tax guide) near the top or bottom of the post body: "This article reports on platform features. Predict.fun is a financial product. Nothing here is investment advice."
**Effort:** 5 min
**Traffic impact:** Low (indirect)
**Revenue impact:** HIGH (AdSense eligibility gate)

### FINDING 4 — Muskaan Shaik author page weak E-E-A-T
**Pillar:** 7 (E-E-A-T), 16 (YMYL)
**Severity:** HIGH
**File:** `_data/authors.yml`, `author/muskanshaik.md`
**Evidence:**
- No professional headshot (shows monogram "MS" via placeholder)
- JobTitle "Freelancer News Reporter" — "Freelancer" not "Freelance" (capitalization error)
- No verifiable credentials, work history, or publication links in bio
- ProfilePage schema missing: `sameAs`, `knowsAbout`, `jobTitle` fields
- The author page bio mentions "independent crypto and education reporter" but provides zero evidence (no links to prior work, no beat description)
**Impact:** For a YMYL reporter covering financial topics, Google requires "expertise" evidence. A bare author page with no photo, no credentials, and incomplete schema weakens E-E-A-T for every post Muskaan bylines (currently 1 of 3). AdSense reviewers specifically check author credibility signals.
**Fix:**
1. Add a professional headshot (or at minimum a branded avatar, not a monogram)
2. Expand bio: add `sameAs` links (X, LinkedIn if available), `knowsAbout` array, fix JobTitle to "Freelance Crypto Reporter"
3. Complete ProfilePage schema: add `sameAs`, `knowsAbout`, `jobTitle`
**Effort:** 1–2 hours (requires headshot from Muskaan)
**Traffic impact:** Low (indirect)
**Revenue impact:** HIGH (AdSense review gate)

### FINDING 5 — `website_credit_url` still points to old domain
**Pillar:** 6 (On-Page)
**Severity:** MEDIUM
**File:** `_config.yml:18`
**Evidence:** `website_credit_url: "https://ttearncrypto.github.io"` — used in footer.html as the "Built for crypto readers" link
**Impact:** Footer link goes to `ttearncrypto.github.io` (no redirect) instead of `f9xr.org`. Inconsistent with the domain migration completed earlier.
**Fix:** Update to `"https://f9xr.org"`
**Effort:** 1 min
**Traffic impact:** None
**Revenue impact:** Low (brand consistency)

### FINDING 6 — Privacy Policy and Terms stale dates
**Pillar:** 7 (E-E-A-T)
**Severity:** MEDIUM
**File:** `legal/privacy-policy.md:11`, `legal/terms.md:11`
**Evidence:** Both pages say "Last updated: August 2026". It is September 2026. The site was significantly modified in the prior session (email change to hello@f9xr.org, newsletter addition, content restructuring).
**Impact:** Stale legal dates undermine trust. Google's YMYL quality rater guidelines explicitly flag outdated information on financial/legal pages.
**Fix:** Update both to "Last updated: September 2026"
**Effort:** 2 min
**Traffic impact:** None
**Revenue impact:** Medium (AdSense review perception)

### FINDING 7 — About page lists 5 coverage sections, site has 7 categories
**Pillar:** 7 (Content), 16 (YMYL)
**Severity:** MEDIUM
**File:** `about.md:29-35`
**Evidence:** The "What we cover" list has 5 items: Bitcoin & Ethereum, Altcoins, Regulation, DeFi & Web3, Exchanges & How-to. Missing: Today's Combo and Press. The welcome post correctly lists 6 categories. The about page is stale.
**Impact:** About page should be the authoritative description of what the site covers. Incompleteness is a minor trust signal.
**Fix:** Add Today's Combo and Press to the list, or note them as supplementary sections
**Effort:** 5 min
**Traffic impact:** None
**Revenue impact:** Low

### FINDING 8 — Cover images lack explicit width/height (CLS)
**Pillar:** 3 (CWV)
**Severity:** MEDIUM
**File:** `_layouts/post.html:35`
**Evidence:** `<img src="{{ page.cover_image }}" ...>` has no `width` or `height` attributes. CSS uses `aspect-ratio: 16/9` on `.article-cover` which mitigates layout shift, but Google's Lighthouse and Chrome's CLS algorithm still flag images without intrinsic dimensions.
**Impact:** CLS score inflated. Core Web Vitals failing CLS threshold degrades search ranking signal.
**Fix:** Add `width="1200" height="675"` to the cover img tag (matching the 16:9 aspect ratio)
**Effort:** 2 min
**Traffic impact:** Low (CWV is a ranking signal)
**Revenue impact:** Low

### FINDING 9 — Logo.png is 639KB (1408×768)
**Pillar:** 3 (CWV)
**Severity:** MEDIUM
**File:** `assets/images/logo.png`
**Evidence:** Logo is 1408×768 at 639KB, displayed at 28×28 in header and 44×44 in footer. The OG default image is separate at 94KB. The logo is loaded on every page via header.html.
**Impact:** Unnecessary bytes on every page load. First-byte delay on mobile. Not a huge CWV impact (logo is small DOM element) but poor practice.
**Fix:** Create a 120×120 or 200×200 version of the logo for header/footer use. Keep the full-size for OG if needed (but og-default.png already exists).
**Effort:** 10 min (image resize + update header/footer references)
**Traffic impact:** Minimal
**Revenue impact:** Low

### FINDING 10 — Learn guides lack cover images
**Pillar:** 10 (Images), 14 (News SEO)
**Severity:** MEDIUM
**File:** `pages/learn/*.md`
**Evidence:** None of the 5 learn guides define `cover_image` or `image` in front matter. They all fall back to `og-default.png`. These are the site's most important YMYL pages (tax guide, exchange comparison, P2P guide) and they get the generic OG image.
**Impact:** Poor social sharing appearance. Google Discover cannot feature them with distinctive imagery. Weakens visual E-E-A-T signals for the most important trust-building content.
**Fix:** Create cover images for each learn guide (or use a branded template). Add `cover_image` to each guide's front matter.
**Effort:** 1–2 hours (design + implementation)
**Traffic impact:** Medium (Discover eligibility for learn guides)
**Revenue impact:** Medium

### FINDING 11 — Unminified CSS and JS
**Pillar:** 3 (CWV)
**Severity:** LOW
**File:** `assets/main.css` (49KB), `assets/main.js` (15KB)
**Evidence:** Both files are unminified with comments and whitespace. Total payload: ~64KB uncompressed.
**Impact:** Marginal performance impact. GitHub Pages serves with gzip/brotli compression, so actual transfer size is smaller. But parse time on low-end mobile devices is affected.
**Fix:** Add a build step to minify CSS/JS, or use a Jekyll plugin. Alternatively, precompress during `jekyll build`.
**Effort:** 30 min
**Traffic impact:** Minimal (CWV marginal)
**Revenue impact:** Low

### FINDING 12 — Google Fonts render-blocking
**Pillar:** 3 (CWV)
**Severity:** LOW
**File:** `_includes/head.html:58-60`
**Evidence:** `<link rel="preconnect" ...>` exists but the actual `fonts.googleapis.com/css2` stylesheet still blocks rendering. `font-display=swap` is the default in Google Fonts v2, so FOUT is handled, but the initial render is delayed.
**Impact:** LCP element (hero heading) uses Playfair Display. Font swap means text appears quickly in fallback font then reflows — minor CLS.
**Fix:** Self-host the font files and use `font-display: swap` explicitly. Or accept the current behavior (already reasonable).
**Effort:** 30 min (self-hosting) or 0 (accept current)
**Traffic impact:** Minimal
**Revenue impact:** Low

### FINDING 13 — No IndexNow implementation
**Pillar:** 9 (Indexing)
**Severity:** LOW
**File:** N/A (missing infrastructure)
**Evidence:** No IndexNow key, no ping endpoint. When new stories are published, only Google's crawl schedule discovers them. Bing and Yandex are not pinged.
**Impact:** New stories take longer to index on Bing/Yandex. For a news site, rapid indexing is valuable.
**Fix:** Register an IndexNow key, add a webhook or post-deploy script that pings Bing/Yandex on new content.
**Effort:** 1–2 hours
**Traffic impact:** Low (Bing/Yandex minor for crypto)
**Revenue impact:** Low

### FINDING 14 — llms-full.txt misleading content promise
**Pillar:** 18 (AI/SGE)
**Severity:** LOW
**File:** `llms-full.txt:1-3`
**Evidence:** Header says "Full content of The DESI Sikka — every article, guide, and policy page, complete and unabridged" but the file contains only summaries (bullet points) for each article, not full text.
**Impact:** AI systems reading llms-full.txt expect full content. Getting summaries instead may cause the site to be penalized in AI citations or ignored in favor of sites with honest llms-full.txt files.
**Fix:** Either populate with actual full content (best) or change the header to "Site overview and content summaries" (quick fix)
**Effort:** 5 min (header change) or 1+ hour (populate full content)
**Traffic impact:** Low (AI citation is emerging)
**Revenue impact:** Low

### FINDING 15 — No skip-to-content link
**Pillar:** 20 (Accessibility)
**Severity:** LOW
**File:** `_includes/header.html`
**Evidence:** No `<a href="#content" class="skip-link">Skip to content</a>` present. Keyboard-only users must tab through the entire nav to reach article content.
**Impact:** Minor accessibility gap. WCAG 2.1 SC 2.4.1 requires a skip mechanism.
**Fix:** Add a visually hidden skip link at the top of `header.html` that becomes visible on focus.
**Effort:** 10 min
**Traffic impact:** None
**Revenue impact:** Low

### FINDING 16 — No related posts or "More from" section
**Pillar:** 11 (Internal Linking)
**Severity:** LOW
**File:** `_layouts/post.html`
**Evidence:** Posts end after the author bio and newsletter CTA. No "Related stories" or "More from [category]" section. Only 3 posts exist currently, so this is low priority now but will matter as content grows.
**Impact:** Missed internal linking opportunity. Reduces page depth and time-on-site.
**Fix:** Add a "More stories" section that pulls 2–3 posts from the same category (or recent posts if category is sparse).
**Effort:** 30 min
**Traffic impact:** Medium (as content grows)
**Revenue impact:** Low

### FINDING 17 — About page missing structured data
**Pillar:** 8 (Schema)
**Severity:** LOW
**File:** `about.md`
**Evidence:** The about page has `AboutPage` schema (correct) but lacks an `Organization` mainEntity. The Organization schema lives in `default.html` and is inherited, so this is technically covered. However, the about page should also have `datePublished` and `dateModified` for the AboutPage.
**Impact:** Minor schema completeness.
**Fix:** Add `datePublished` and `dateModified` to the AboutPage schema block.
**Effort:** 5 min
**Traffic impact:** None
**Revenue impact:** Low

### FINDING 18 — Learn guide Article schema missing datePublished
**Pillar:** 8 (Schema), 17 (Schema)
**Severity:** LOW
**File:** `pages/learn/bitcoin-tax-guide-india.md:72`
**Evidence:** The Article schema uses `page.date | default: page.last_modified_at` for datePublished. None of the learn guides have a `date` front matter, so it falls through to `last_modified_at`. This works but `last_modified_at` is not a standard YAML date field — it's a custom key. Jekyll may not parse it as a date.
**Impact:** Google may not recognize the publication date, weakening freshness signals for these YMYL pages.
**Fix:** Add `date: 2026-08-28` (or the actual publication date) to each learn guide's front matter.
**Effort:** 5 min
**Traffic impact:** Minimal
**Revenue impact:** Low

---

## Quick Wins (do now, <15 min total)

| # | Fix | File | Effort |
|---|-----|------|--------|
| 1 | "a exit-liquidity" → "an exit-liquidity" | `about.md:31` | 1 min |
| 2 | website_credit_url → f9xr.org | `_config.yml:18` | 1 min |
| 3 | Privacy Policy date → September 2026 | `legal/privacy-policy.md:11` | 1 min |
| 4 | Terms date → September 2026 | `legal/terms.md:11` | 1 min |
| 5 | Add width/height to cover img | `_layouts/post.html:35` | 2 min |
| 6 | llms-full.txt header → "summaries" | `llms-full.txt:1` | 1 min |
| 7 | Add date front matter to learn guides | 5 files | 5 min |

## Medium-Term Fixes (1–4 hours)

| # | Fix | Effort | Impact |
|---|-----|--------|--------|
| 1 | Generate favicon + apple-touch-icon + webmanifest | 30 min | AdSense reviewer perception |
| 2 | Add "not financial advice" disclaimer to predict.fun post | 5 min | YMYL compliance gate |
| 3 | Fix Muskaan author E-E-A-T (bio, schema, photo) | 1–2 hrs | AdSense review gate |
| 4 | Update about.md coverage list to 7 categories | 5 min | Trust accuracy |
| 5 | Resize logo to 120×120 for header/footer | 10 min | CWV |
| 6 | Self-host Google Fonts | 30 min | CWV + privacy |
| 7 | Add cover images to learn guides | 1–2 hrs | Discover eligibility |
| 8 | Add skip-to-content link | 10 min | Accessibility |

## Long-Term (as content scales)

| Fix | When | Impact |
|-----|------|--------|
| Related posts section | 10+ posts | Internal linking, time-on-site |
| IndexNow implementation | Regular publishing cadence | Bing/Yandex indexing speed |
| Minified CSS/JS build step | >100KB total payload | CWV |
| Full content in llms-full.txt | AI citation strategy | AI/SGE readiness |

---

## YMYL Confidence Score

| Factor | Score | Notes |
|--------|-------|-------|
| Financial disclaimer | 7/10 | Site-wide disclaimer excellent; predict.fun post missing body-level disclaimer |
| Author credibility | 5/10 | F9XR desk strong; Muskaan page weak |
| Editorial standards | 9/10 | Editorial policy, corrections, disclosures all present and thorough |
| Trust pages (About, Contact, Legal) | 9/10 | All present, well-written, schema-marked |
| Content freshness | 6/10 | Only 3 posts, all from same date; legal pages stale |
| Source citation | 8/10 | Tax guide cites incometax.gov.in; posts cite primary sources |
| Opinion vs fact separation | 8/10 | Editorial policy mandates it; infrastructure exists; no violations yet |
| India-specific accuracy | 8/10 | Tax sections (115BBH, 194S) correctly cited; TDS rules accurate |
| AI/SGE readiness | 7/10 | llms.txt present; structured data strong; llms-full.txt misleading |

**Overall YMYL Confidence: 72/100**

To reach 85+ (AdSense-ready): fix findings 2, 3, 4, 5, 6, 8, and 10. These are the minimum gates.

---

## Verdict

The DESI Sikka has a stronger foundation than most new crypto news sites. The legal trust stack (editorial policy, disclosures, disclaimer, corrections, privacy) is unusually complete for a launch-day site. The structured data coverage (9 schema types) exceeds what most competitors implement.

The two AdSense-readiness blockers are:
1. **predict.fun post missing a body-level "not financial advice" disclaimer** — a 5-minute fix that directly gates AdSense approval
2. **Muskaan Shaik author page lacking professional credibility signals** — requires a headshot and bio expansion, but blocks AdSense review for every post she writes

Once those two are closed, the site is ready for AdSense application. Google Discover eligibility will follow as more posts are published with distinctive cover images and fresh dates.
