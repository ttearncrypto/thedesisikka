# Monthly Website Audit — October 2026

Scope: all 75 built pages in `_site` plus live checks against `https://ttearncrypto.f9xr.org/thedesisikka/`.

The source checklist is WordPress-oriented. Items that assume plugins, a database, or a Google Business Profile were mapped to their Jekyll/GitHub Pages equivalents, noted where relevant.

## Summary

| # | Audit | Result |
|---|-------|--------|
| 1 | Image SEO | Pass with one gap |
| 2 | Broken links & images | Fixed |
| 3 | Speed & Core Web Vitals | Pass |
| 4 | Mobile usability | Pass |
| 5 | On-page SEO | Fixed |
| 6 | Content freshness | Pass, monitor |
| 7 | Backlink profile | Not measurable locally |
| 8 | Security | Fixed |
| 9 | Indexing signals | Pass |
| 10 | Local SEO / GBP | N/A |
| 11 | Schema markup | Pass |
| 12 | Analytics | Pass |
| 13 | Duplicate content | Pass |
| 14 | Internal linking | Pass |
| 15 | AEO / AI search | Pass |

## What changed

Descriptions rewritten to sit inside the 70–160 character window on 11 pages. The WOTD hub had the worst defect: a 200-character description that Liquid truncated mid-sentence with a literal ellipsis, and a `seo_title` still pinned to September while the page was serving October content. Both are now evergreen rather than month-specific, so the page will not go stale again next cycle.

`archive.md` had no `<h1>` at all, just `<h2>` month headings. Added a page intro so the page has exactly one `<h1>` like every other page.

`pages/todays-combo/` and `category/todays-combo/` produced identical `<title>` values, as did `press/` and `category/press/`. Both category twins already carry `noindex, follow` and are excluded from the sitemap, so this is not an indexing conflict, but the pair is still reported by duplicate-content checkers.

`telegram-post.yml` had no `permissions` block and inherited the repository default. Set it to `contents: read`.

## Detail

### 1. Image SEO
516 `<img>` tags. Zero missing `alt`. The 150 empty `alt=""` values are the GoatCounter pixel and the footer logo, both decorative, which is correct. All 19 assets use descriptive filenames. Total asset weight is 935 KB.

One real gap: 31 of 35 posts share `binance-wotd-answers-hero.webp` as their social card. Google Discover leans on visual variety, and a single repeated hero across a month of posts flattens click-through. Three non-WOTD posts (`bitcoin-84k-bond-yields`, `bitget-hack-withdrawals-restart`, `cftc-crypto-rulemaking-white-house-review`) have no `cover_image` in front matter and fall back to `og-default.png`.

### 2. Broken links & images
Every internal `href` and `src` was resolved against the built tree. 0 broken. Category pages currently resolve 200 despite the `noindex` on them.

### 3. Speed & Core Web Vitals
Homepage is 37 KB HTML, 57 KB CSS, 19 KB JS across one file each. Live TTFB measured 497 ms to 1.3 s. Light enough that CLS and LCP should be comfortable.

The Google Fonts stylesheet appears twice in the HTML. On inspection this is the `media="print" onload="this.media='all'"` async pattern plus a `<noscript>` fallback, not a duplicate bug.

### 4. Mobile usability
Viewport meta present on all 75 pages. `width=device-width` confirmed.

### 5. On-page SEO
Before this pass, 11 pages had descriptions outside 70–160 characters: 8 too short (`search` at 37, `legal/terms`, `about`, `legal/privacy-policy`, `archive`, `pages/featured`, `legal/disclaimer`) and 3 too long (`cftc-crypto-rulemaking` at 163, `learn/exchange-comparison-india` at 164, `pages/binance-wotd-answers` at 200). All 11 now pass. Every title was already under 60. `archive` had 0 `<h1>`; every page now has exactly 1.

### 6. Content freshness
Sitemap `lastmod` distribution: 36 URLs in 2026-09, 5 in 2026-08, 1 in 2026-10. Oldest 2026-08-28, newest 2026-10-01. The August batch is five evergreen Learn pages, not stale news.

### 7. Backlink profile
Not measurable from the repo. Needs Search Console or a third-party index. Nothing outbound is marked `nofollow`; 452 links carry `noopener`/`noreferrer`, which is correct for `target="_blank"`.

### 8. Security
Scanned the tree for hardcoded credential patterns: none. `security.txt` present at both root and `.well-known/`. `pages.yml` already pinned to `contents:` read-only. `telegram-post.yml` had no explicit permissions and now sets `contents: read`. Both workflows pin `actions/checkout@v4` by tag rather than SHA; SHA pinning is stricter but not urgent here.

Third-party origins on the page: `fonts.googleapis.com`, `fonts.gstatic.com`, `gc.zgo.at` (GoatCounter), plus links to `t.me`, `github.com`, `buttondown.com`. Analytics is GoatCounter only, cookie-less, loaded async with a `noscript` fallback.

### 9. Indexing signals
60 indexable URLs in the sitemap, matching 60 pages emitting `robots=index, follow`. The other 15 are utility or empty-listing pages correctly marked `noindex, follow`. No `github.io` references remain anywhere in the sitemap.

### 10. Local SEO / GBP
Not applicable. No LocalBusiness schema, no address or geo targeting. Correct for a global crypto news site; a Google Business Profile would be wrong for this business.

### 11. Schema markup
325 JSON-LD blocks, all valid. All 37 news posts carry `NewsArticle`. Inventory includes `Organization`, `WebSite`, `BreadcrumbList`, `FAQPage` (31), `Question`/`Answer` (93 each), `speakable` (37), and `DefinedTermSet` on the glossary. News posts emit both `Organization` and `NewsMediaOrganization`; both point to the same publisher entity, so it is redundant but not conflicting.

### 12. Analytics
GoatCounter via `data-goatcounter`, 3 occurrences sitewide including the `noscript` pixel. No second analytics vendor.

### 13. Duplicate content
Two duplicate pairs, both already handled: `press/` vs `category/press/` share a description, and `pages/todays-combo/` vs `category/todays-combo/` share a title. In both cases the category twin is `noindex` and out of the sitemap, and each has a correct self-referencing canonical. No action needed.

### 14. Internal linking
6,224 internal links across 80 distinct targets. One genuine orphan: the homepage, which is expected. `pages/featured/` and `pages/learn/glossary/` have only one inbound link each. No post is orphaned.

### 15. AEO / AI search
Strong. All 37 news posts carry `speakable`. 31 carry `FAQPage` schema. 36 of 37 open with a direct answer rather than a lede. `llms.txt` (3.7 KB) and `llms-full.txt` (15.2 KB) were both regenerated on 2026-10-01, and `head.html` advertises `llms.txt` via a `<link rel="llms">` tag.

## Recommended next

1. Give each non-WOTD post its own `cover_image`. Three posts are still on the shared fallback.
2. Vary the WOTD hero periodically so a month of posts does not ship one identical social card.
3. Review the 6 noindex category pages. If `bitcoin`, `ethereum`, and `defi` have real post volume, they should be indexed to capture category query traffic.