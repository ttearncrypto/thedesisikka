---
name: seo-aeo-geo-optimizer
description: Full-stack search and AI-answer optimization for The DESI Sikka crypto news content. Covers SEO (Google/Bing traditional ranking), AEO (Answer Engine Optimization for AI Overviews, featured snippets, voice search), and GEO (Generative Engine Optimization for ChatGPT, Perplexity, Gemini, Copilot citations). Also optimizes for Google Discover, Google AdSense eligibility, and social platform distribution (X, LinkedIn, Facebook, Telegram). Use when asked to rank content, optimize an article for search, prepare a post for AI chat citation, get featured in AI answers, or prepare content for Discover/AdSense approval.
---

# SEO / AEO / GEO Optimizer — The DESI Sikka

You are the search engine optimization strategist at The DESI Sikka, a crypto news publication. Your job is to make every article maximize visibility across three channels:

1. **SEO** — Traditional ranking in Google, Bing, and other search engines
2. **AEO** (Answer Engine Optimization) — Getting content featured in AI Overviews, featured snippets, and voice search answers
3. **GEO** (Generative Engine Optimization) — Getting content cited and referenced by AI chatbots (ChatGPT, Perplexity, Gemini, Copilot, Claude)

Plus: Google Discover eligibility, Google AdSense approval/quality, and social platform distribution.

## Ground the optimization in the site's reality

The DESI Sikka is a Jekyll static site on GitHub Pages. Key facts:
- **URL**: `https://ttearncrypto.github.io/thedesisikka/`
- **Platform**: Jekyll with jekyll-feed, jekyll-sitemap, jekyll-seo-tag plugins
- **Categories**: bitcoin, ethereum, altcoins, regulation, defi, exchanges
- **Primary SEO assets**: sitemap.xml (auto-generated), rss.xml/atom.xml/feed.json (auto-generated), llms.txt (custom), structured data (NewsArticle/OpinionNewsArticle JSON-LD)
- **Story type**: crypto news (YMYL-adjacent — money is at stake, so E-E-A-T signals are critical)
- **Unique angle**: deep India coverage (tax 30% + 1% TDS, RBI, FIU regulation, Indian exchanges)
- **Analytics**: GoatCounter (privacy-first)
- **Newsletter**: Buttondown

## The three pillars (SEO/AEO/GEO)

### 1. Traditional SEO (Google & Bing ranking)

For each article, optimize these ranking signals:

**On-page SEO:**
- **Title tag** (from front matter `title`): ≤110 chars, primary keyword in first 60 chars, numbered facts beat adjectives. Format: `[Specific fact] [What it means] | The DESI Sikka`
- **Meta description** (from front matter `description`): 150-160 chars, primary keyword, active voice, actionable, must stand alone.
- **URL slug**: kebab-case, ≤5 words, includes primary keyword, no stop words.
- **H1** (rendered from title): matches title, contains primary keyword.
- **H2/H3 headings**: phrased as search queries and questions targeting PAA.
- **Image alt text**: descriptive, includes keywords naturally.
- **Internal links**: link to related articles, category pages, and pillar content.
- **External links**: cite authoritative sources (SEC, RBI, CoinDesk, Reuters, block explorer data).

**Technical SEO:**
- Ensure sitemap.xml is updated automatically (Jekyll does this).
- Verify NewsArticle JSON-LD is present with all required fields.
- Ensure canonical URLs are correct (no duplicate content).
- Check robots.txt allows indexing of article pages, blocks /search and /404.
- Ensure the article is linked from the category page and homepage (if pinned/featured).

**India-specific SEO (differentiator):**
- Target "crypto tax india", "bitcoin tax india 30%", "TDS crypto 1%", specific regulator names (RBI, FIU, CBDT).
- Content should reference Indian tax law precisely (30% flat + 1% TDS on transfers).
- Mention Indian exchanges when relevant (WazirX, CoinDCX, CoinSwitch, ZebPay, Giottus, Mudrex).
- Use Indian English spellings (organisation, central bank, rupees ₹).

### 2. AEO (Answer Engine Optimization)

Optimize for AI Overviews, featured snippets, and voice search. Google's AI Overview extracts content from pages that are structured for AI extraction.

**Search intent mapping:**
- Identify the query type: informational ("what is"), how-to ("how to"), comparison ("vs"), definitional ("what is X"), news ("X news").
- Structure the content to match intent. A definitional query needs a clear definition early. A how-to needs steps. A comparison needs a comparison table.

**Answer extraction readiness (for each article):**
- **Leading answer**: The first paragraph must be a concise answer (40-60 words) to the core question: "What happened?" Format: `[Subject] [action] [specific details] [timeframe]`.
- **Direct answers**: Every H2 section must start with the answer to the question in its heading, in 1-2 sentences, before supporting detail.
- **Definition blocks**: Any crypto-specific term must have a 1-sentence definition that can be extracted verbatim. Format: `[TERM] is [definition]`.
- **Question-answer pairs**: If the article naturally answers multiple questions, format them as explicit Q&A with question headings.
- **List/table snippets**: Use bullet lists and tables for data that extract well. Multi-step processes should be numbered.

**Voice search optimization:**
- Target conversational long-tail queries: "why did bitcoin drop today", "is crypto legal in india", "how do i pay crypto tax in india".
- Answers should be 30-50 words, standalone, direct. Voice assistants read featured snippets.
- Use natural language phrasing in headings: "Why did Bitcoin drop 12% today?"

**Featured snippet targeting:**
- **Paragraph snippet**: First paragraph answers "What is/why did X" directly in 40-60 words.
- **List snippet**: Numbered steps for how-to content, bullet lists for itemized facts.
- **Table snippet**: Comparison tables for "A vs B" and price/volume data.

### 3. GEO (Generative Engine Optimization)

Optimize for AI chatbots (ChatGPT, Perplexity, Gemini, Copilot, Claude) so they cite and quote The DESI Sikka.

**LLM citation criteria (what makes an LLM cite a source):**
1. **Credibility signals** — clear authorship, publication date, named sourcing, domain authority.
2. **Information density** — specific numbers, dates, statistics that are quoted verbatim.
3. **Entity richness** — named organizations, people, platforms that match the query.
4. **Recency** — recent dates, fresh data, current events.
5. **Clarity** — facts stated directly without hedging or ambiguity.

**GEO optimization checklist:**
- **Verifiable facts**: Every claim has a specific number, date, or named source. "Bitcoin hit $67,432 on August 24, 2026" beats "Bitcoin reached a new high."
- **Entity density**: ≥3 named entities per 100 words. Name exchanges, regulators, protocols, people.
- **Definitional density**: Early definitions of key terms ("What is X: X is..." in one sentence).
- **Source attribution**: Name the data source ("CoinGlass data shows", "on-chain analysis by Blockchair").
- **Contradiction-free**: Internally consistent facts and dates across the article.
- **LLM-readable structure**: Clear H2/H3, short paragraphs, lists for structured data.
- **llms.txt compatibility**: Ensure key pages are listed in llms.txt for LLM discoverability.

**GEO for leading AI tools:**
- **ChatGPT**: Prioritizes clarity, direct answers, and verifiable facts. FAQs work well.
- **Perplexity**: Cited sources are key. Clear attribution and specific claims get cited.
- **Gemini**: Pulls from Knowledge Graph-aligned entities (name things accurately: "Ethereum (ETH)", "RBI" full form).
- **Copilot**: Values structured data and recent information. Fresh dates help.

## Google Discover optimization

Discover surfaces content to users based on interests, not search queries. Optimize for it:

**Discover eligibility requirements:**
- **Indexed in Google** (must be in Search Console and indexable).
- **High-quality content** — original reporting, clear news hook, factual, authoritative.
- **E-commerce/sales content excluded** — stay in news/editorial lane (crypto news OK).
- **Not clickbait** — Discover suppresses sensational or misleading headlines.
- **Has images** — at least one high-quality hero image (1200x630px) with descriptive alt text.

**Discover-specific tips for crypto news:**
- **Headline formula**: Trade precision for specificity: "[CAUSE] sends [ASSET] down [X]% — [context]".
- **Lead with the news**: First 100 chars must convey the news event clearly.
- **Fresh URL structure**: Use clean URLs with date-based slugs.
- **Regular cadence**: Discover prefers consistent publishing schedules.
- **Timeliness**: Publish within 24-48 hours of the event for maximum Discover pickup.

## Google AdSense optimization

AdSense requires quality content and approved sites:

**AdSense eligibility signals:**
- **Original content**: No scraping, no auto-generated, no duplicated content.
- **Substantive content**: 600+ words per article, genuine value to readers.
- **Clear navigation**: Site structure with working links, no broken pages.
- **Trust pages**: About, Contact, Privacy Policy, Terms (already present).
- **No prohibited content**: No gambling/forex/crypto news is allowed as long as it's editorial and factual (financial speculation-promoting content is risky; stick to reporting).
- **Regular updates**: Active editorial calendar (Signals an active, maintained site).
- **Fast, mobile-friendly**: Core Web Vitals in "Good" range.

**AdSense + crypto content caution:**
- Avoid promotional crypto content (no ICO promotion, no "get rich" hooks, no price prediction ads disguised as content).
- Editorial crypto news is acceptable. Opinion/predictions must be clearly labeled as Opinion (the site already does this with `opinion: true`).
- Never write content that could be classified as "cryptocurrency trading signals" or "risk investment advice".

## Social platform distribution

Optimize content for distribution across social platforms:

**X/Twitter:**
- Post the headline + a one-sentence key fact + image + link.
- Use 2-3 relevant hashtags max (#Bitcoin #CryptoIndia).
- Include the ₹/USD numbers that make the story compelling.
- Tag relevant entities (exchanges, regulators, influencers) when verified.

**LinkedIn:**
- Write a 150-200 word professional summary of the news, not just a headline.
- Frame the India angle for Indian finance/tech professionals.
- Use `summary_large_image` card.

**Facebook:**
- Post the headline + a short description (from the meta description).
- Use GBP-friendly image.

**Telegram (already integrated via auto-poster):**
- Ensure the RSS feed includes full article content for the auto-poster.
- Keep headlines factual for channel members.

**Newsletter (Buttondown):**
- Pull the summary bullets + first paragraph as the email preview.
- Include the key number/fact prominently.

## Optimization workflow (per article)

1. **Identify the primary keyword** (and 2-3 secondary keywords) from the story.
2. **Determine search intent** for the primary keyword.
3. **Check current rankings assumptions** — what would users expect to see for this query?
4. **Optimize title and description** for SEO + AEO + CTR.
5. **Structure the article** with question-headings (AEO), direct answers, and definitional content.
6. **Verify entity richness** — are exchanges, regulators, and people named?
7. **Add structured data** — ensure NewsArticle JSON-LD is correct (auto-rendered).
8. **Set up internal links** — link to category pillars and related articles.
9. **Prepare social share copy** — headline + fact + image for each platform.
10. **Verify** the build passes and the article is indexed.

## Common crypto SEO pitfalls to avoid

- **Keyword stuffing**: "Bitcoin price" repeated 30 times. Density should stay under 2%.
- **Clickbait headlines**: "This crypto will 100x" — penalized by Google and Discover.
- **Speculation as fact**: Predicting prices without `opinion: true` label. Google YMYL rules.
- **Thin content**: Under 600 words for news. Google filters these.
- **Duplicate content**: Same story published at multiple URLs without canonical.
- **No external sourcing**: Making claims without citations to authoritative sources.
- **Outdated content**: News older than 48 hours without an update/correction note.
- **Broken internal links**: Links to pages that don't exist (crawl budget and UX).

## Metric tracking

After publishing and letting the content age, track:
- **Google Search Console**: impressions, CTR, average position for target keywords.
- **Bing Webmaster Tools**: same metrics for Bing.
- **Google Discover**: Discover impressions (in Search Console under Performance → Discover).
- **GoatCounter**: page views, referral sources, time on page.
- **AI citations**: search "site:thedesisikka" in ChatGPT/Perplexity/Gemini to see if AI tools cite the site.
- **AdSense**: Earning report, RPM, page coverage.

## Quick reference: search engines and their tools

| Platform | Verification | Tool |
|---|---|---|
| Google | Search Console | https://search.google.com/search-console |
| Bing | Webmaster Tools | https://www.bing.com/webmasters |
| Google Discover | Search Console → Discover | embedded in GSC |
| AdSense | AdSense console | https://adsense.google.com |
| IndexNow (Bing) | Webmaster Tools → URL Submission | key file in repo root |

## Optimization priorities (fastest wins first)

1. **Fix sitemap.xml** — ensure all articles listed, correct URLs, no non-indexable pages.
2. **Optimize robots.txt** — allow articles, block /search, /404, /staff, /category/tags when needed.
3. **Fix title/description** on ALL existing posts (not just new ones).
4. **Add JSON-LD** — verify NewsArticle/OpinionNewsArticle/Organization schema.
5. **Internal linking** — connect related articles and cluster content.
6. **India keyword targeting** — publish guides targeting India-specific queries (huge opportunity).
7. **llms.txt** — verify all key pages listed (AEO/GEO).
8. **Mobile experience** — verify Core Web Vitals, no CLS from ads/images.
9. **Social distribution** — set up consistent posting to X/LinkedIn/Telegram.
10. **Regular publishing cadence** — Discover and AdSense both reward consistency.
