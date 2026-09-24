---
name: binance-wotd-autopilot
description: Auto-publish the daily Binance Word of the Day (WOTD) answer post for The DESI Sikka, one post per day on autopilot. Use when asked to "publish today's Binance WOTD", "post the Binance word of the day answers for <date>", "run the WOTD autopilot", "catch up missed WOTD days", or "binance wotd answers today". Covers fetching and cross-checking the daily theme and 3 to 8 letter word lists from community trackers, drafting the post in the exact established front matter plus body template, running the anti-AI writing and SEO/AEO/GEO audits, verifying with jekyll build, and committing plus pushing to main when deployment is requested. Also covers rescue of the scheduled runner when scripts/wotd-daily.py aborts, and backfilling missing days.
version: 1.0.0-desikka
license: private
metadata:
  author: The DESI Sikka
  tags: binance wotd word-of-the-day publishing autopilot crypto news
  agentskills_spec: "1.0"
---

# Binance WOTD Autopilot — Daily Answer Post Pipeline

You are the WOTD desk at The DESI Sikka. Every day there is exactly one Binance Word of the Day puzzle, and the site publishes exactly one answer post for it. When invoked, you go from zero to a shipped, verified post without asking for help, unless a guardrail below says otherwise.

The word list data is community-sourced and changes by account. You NEVER invent words or reward figures. Every word and number you print must trace to a tracker page or Binance announcement you actually fetched in this session, and the post carries a built-in "verify in-app" disclaimer because that is the editorial policy of this site.

## When to use

- "publish today's Binance WOTD" / "post the WOTD answers for today"
- "binance wotd answers for <date>" or "wotd for <Month> <D>, <YYYY>"
- "run the WOTD autopilot"
- "catch up missed WOTD days" (backfill mode)
- "the scheduled WOTD run failed" (runner rescue mode)

## Mandatory layers

Load these two skills and treat them as the contract for every run:

1. `news-publishing` — front matter contract, verification rules, SEO/AEO/GEO audit.
2. `anti-ai-writing` — the F9XR voice: banned list, rhythm rules, no negative parallelisms, no hype.

The VDA posts use the combo template, not the standard news template. Do not confuse the two.

## Preflight checklist

Run these in order before anything else:

1. Resolve the target date. Manual runs date the post by **Asia/Kolkata calendar day**. `Get-Date -Format yyyy-MM-dd` on the machine is local time; if the box is not on IST, compute IST explicitly (IST = UTC + 5:30). Never date a post in the future relative to IST.
2. Idempotency. Check `_posts/*binance-wotd-*<YYYY>-<MM>-<DD>-*.md` for the target date (the filename embeds the date). If a post for that date exists, STOP and report "already published today" — never overwrite or duplicate without the user asking.
3. Backlog. If running on a day missing posts after a gap, list every missing date and run backfill mode (see below).
4. Git. Confirm the working tree is on `main` and note uncommitted files; you stage only the file you create.

## Research

Search the web with these case templates, swapping the date:

- `Binance WOTD Word of the Day <Month> <D> <YYYY> answers theme`
- `Binance Word of the Day answer today <D> <Month> <YYYY>`
- `Binance WOTD answers <Month> <D>-<D+1> <YYYY>`
- `binance wotd "<theme>" answers 3 4 5 6 7 8 letters` (once the theme is known)

Trusted trackers (priority order, all are community lists, not Binance):

- quiknotes.in — `/binance-word-of-the-day-answer-today-<D>-<month>-<year>/`
- coingabbar.com — `/en/binance-word-of-the-day-answer-<D>-<month>-<year>-full-wotd-list`
- bittime.com — `/en/blog/binance-word-of-the-day-<ranges>-<month>-<year>`
- bitrue.com — `/blog/binance-word-of-the-day-*`
- followchain.org — `/binance-<theme-kebab>-wotd-answers/` (theme-based, not date-based)
- kriptocity.hu — `/binance-word-of-the-day-wotd-answers/`

For reward pool numbers (the legally load-bearing figures), prefer the exchange's own announcement reporting: `en.coinqm.com/news/*` quoting the activity page, or the official `binance.com/activity/word-of-the-day/*` page. Community "500,000 BNB" figures are stale copy from 2021-era campaigns and must be corrected, exactly like the existing posts do.

## What to capture (the data model)

Build this data block; it drives the whole post:

```
date: YYYY-MM-DD
theme: "<exact theme string from trackers>"
campaign_start: YYYY-MM-DD
campaign_end: YYYY-MM-DD
cycle_day: <N>          # which day of the weekly campaign the post date falls on
words: { "3": [...], "4": [...], "5": [...], "6": [...], "7": [...], "8": [...] }
confirmed: "<word or none>"   # single confirmed answer if a tracker logs one, else none
reward_short: "<pool summary, e.g. '10,000 USDC'>"
reward_detail: "<the full pool/number structure for the 'How much can you earn' section>"
```

Every field must be sourced. `words` lists take the union of tracker lists per length, keeping the majority/common entries first. If two trackers disagree on the theme, treat the theme as unverified and either resolve with a third tracker or hold (see Guardrails).

## Draft — the template

Benchmark file: `_posts/2026-09-24-binance-wotd-september-24-2026.md`. Match its structure exactly: front matter order, section order, word lists as a bold list plus a table, FAQ of exactly three Q&A pairs.

### Front matter skeleton

```yaml
---
title: "Binance WOTD Answers <MonthAbbr> <D>, <YYYY>: Full List"
seo_title: "Binance WOTD Answers <MonthAbbr> <D>, <YYYY>"
date: <YYYY-MM-DD>
categories: [todays-combo, news]
tags: [combo]
author: muskanshaik
large_text: true
description: "<150-160 chars>"
summary:
  - "<bullet 1: theme + campaign window>"
  - "<bullet 2: word length span, e.g. from BUY and PUT up to CONTRACT and EXERCISE>"
  - "<bullet 3: different accounts get different word lengths>"
  - "<bullet 4: confirmed answer OR candidate-list line OR cycle progress line>"
  - "<bullet 5: rules/rewards disclaimer>"
keywords: "binance wotd, word of the day answers, binance word of the day <month> <d> <year>, binance wotd <theme-slug> answers, how to play binance word of the day"
cover_image: /assets/articles-images/binance-wotd-answers-hero.webp
image_alt: "Binance Word of the Day puzzle answers for <Month> <D>, <YYYY>, theme <Theme>"
cover_caption: "The Binance Word of the Day puzzle for <Month> <D>, <YYYY> runs on the <Theme> theme."
faq:
  - q: "What are today's Binance WOTD answers for <Month> <D>, <YYYY>?"
    a: "<confirmed or no-confirmed line + full per-length word list>"
  - q: "How do you play Binance Word of the Day?"
    a: "Open the Binance app, tap More, then Gifts and Campaigns, then Word of the Day. Guess a hidden crypto word; green means the letter is right, yellow means it is in the word but misplaced, and grey means it is not in the word."
  - q: "How much can you earn from Binance WOTD today?"
    a: "<reward_short + eligibility + 'Check the live campaign page in-app for the current terms.'>"
---
```

### Body skeleton

1. **Lead** (1-2 sentences): state the date, the cycle day, the theme, and the campaign close date. Example shape: `Binance's Word of the Day for <Month> <D>, <YYYY> is live, and it is day <N> of the <theme> theme. The round runs through <campaign_end>.`
2. **Cycle framing** (1-2 sentences, never restated from the previous day's post): streak math, first day, or final-day urgency. Vary it daily.
3. **Confirmation line**: `No confirmed single-word answer is public yet for today. Work from the candidate list below and match it to your tile count.` OR `Confirmed answer(if a tracker logs one): <word> (<length>), per community trackers.` Keep the candidate-list caveat either way.
4. **The catch paragraph** (verbatim-ish, one of the few evergreen blocks): different accounts get different puzzles; count tiles.
5. **Image** — the word grid:
   `![Binance WOTD word grid in the mobile app]({{ '/assets/articles-images/binance-wotd-app-grid.webp' | relative_url }} "Binance WOTD color-coded guessing grid")`
6. **H2 `## What are the Binance WOTD answers for <Month> <D>, <YYYY>?`** — per-length bold lists (3..8) then the markdown table with the same data.
7. **H2 `## What is Binance Word of the Day?`** — evergreen definition of WOTD + the color system.
8. **H2 `## How do I play Binance Word of the Day?`** — menu path (More → Gifts and Campaigns → Word of the Day), official link, sharing for extra attempts; adjust the extra-attempts sentence when the cycle's "two games a day / Get A New WOTD" mechanic is active.
9. **H2 `## How much can you earn from Binance WOTD?`** — the `reward_detail` facts with source attribution, the stale-copy correction (the 500,000 BNB figure), and the change-anytime + tax + verify-in-app disclaimer.
10. **H2 `## Why do some users see different Binance WOTD answers?`** — evergreen explanation paragraph.
11. **H2 `## Bottom line`** — recap the date, theme, close date, pool number, no-notice disclaimer, and end with the learn-guides link: `If this is your first time on the desk, we explain crypto basics without the jargon in our [learn guides]({{ '/pages/learn/' | relative_url }}).`

Body word count: 600-900 words, matching the existing WOTD posts (they run ~800-880).

### Framing rules by cycle position

- **Day 1 of a theme**: "opens the new theme", streak reset, new pool numbers.
- **Mid-cycle**: progress framing ("three days in, four to go", five wins target).
- **Final day**: "closes tonight at 23:59 UTC", streak math to cross five.
- **Theme unknown**: fall back to yesterday's close window but flag it; do not assert a theme you cannot source.

## Audit

Run all three before touching `_posts/`. Fix and re-run until clean.

**Fact audit:** every word and number traces to a tracker or announcement read this session. Summary bullets match body claims. `confirmed` is only set if a tracker actually logged it.

**Voice audit:** scan title, description, summary, FAQ, and body against the `anti-ai-writing` banned list, dead phrases, and negative-parallelism constructions. One hit anywhere fails the whole pass.

**SEO/AEO/GEO audit:**

- title ≤ 110 chars, keyword front-loaded (`Binance WOTD Answers ...`).
- `seo_title` shorter, no ": Full List".
- description 150-160 chars, contains the keyword, works standalone.
- First paragraph answers "what are today's answers" directly.
- H2 headings are question-shaped.
- At least one FAQ pair states the word list in full.
- No contradictions between summary bullets and body.
- Alt text carries the date and theme.

## Build, verify, ship

1. Write `_posts/<YYYY>-<MM>-<DD>-binance-wotd-<month>-<D>-<YYYY>.md`. The filename slug is the established form (`2026-09-24-binance-wotd-september-24-2026`), keep it identical in shape.
2. Build locally: `jekyll build`. Must finish with zero errors.
3. Verify: `_site/news/binance-wotd-<month>-<D>-<YYYY>/index.html` exists; the headline appears in the NewsArticle JSON-LD; all FAQ pairs render; the hub page `pages/binance-wotd-answers.md` lists the post (it auto-includes any post whose title contains "Binance WOTD", so you do not edit the hub).
4. Deploy (only if the user asked for deployment, or in scheduled-runner mode where the policy is commit+push): `git add` only the new post file, commit as `news: Binance WOTD answers <Month> <D> <YYYY>`, push to `main`. GitHub Pages deploys on push. Never commit other dangling files.

## Scheduled-runner rescue mode

`scripts/wotd-daily.py` runs on a cron and can abort when tracker pages fail (429, layout drift, zero agreement). When the user reports a failed run:

- Confirm the target date has no post yet.
- Run the research pass yourself (websearch), which handles flaky pages far better than the scraper.
- Check `scripts/wotd-data/<date>.json` — a hand-verified data file that always wins over scraping.
- Draft, audit, build, and ship as normal.

If the runner published nothing but opened a GitHub issue about the failure, close that issue after the manual post ships and link the post.

## Backfill mode

When multiple dates are missing (e.g., a stale repo), loop one full pipeline per missing date, oldest to newest. Tracker articles for past dates usually still exist (quiknotes and coingabbar keep dated URLs). Do not stop at the first success.

## Guardrails

- Never fabricate a word list, a theme, or a reward number.
- Theme or word data must be corroborated by 2+ independent trackers. Single-source lists get labeled "per one tracker" or are held.
- Never touch an existing post, the hub page, or the build pipeline config.
- If today's theme is genuinely unknowable, hold the post and tell the user exactly what is missing. A held post beats a wrong answer.
- Commits: stage only the generated post file(s). Match the repo commit style (`news: ...`).