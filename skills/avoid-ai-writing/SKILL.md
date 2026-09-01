---
name: avoid-ai-writing
description: Audit and rewrite DESI Sikka crypto news content to remove AI writing patterns ("AI-isms"). Use this skill when asked to "remove AI-isms," "clean up AI writing," "edit writing for AI patterns," "audit writing for AI tells," or "make this sound less like AI." Supports a detect-only mode, an edit-in-place mode for files, an optional voice profile (casual / professional / technical / warm / blunt), and an iterate-to-convergence pass. Adapted for crypto news publishing with Google Discover, AdSense, and AEO/GEO quality signals.
version: 3.10.0-desikka
license: MIT
metadata:
  author: Conor Bronsdon (adapted by The DESI Sikka)
  tags: writing editing voice quality crypto news
  agentskills_spec: "1.0"
---

# Avoid AI Writing — Audit & Rewrite (DESI Sikka Edition)

You are editing crypto news content to remove AI writing patterns ("AI-isms") that make text sound machine-generated. This edition is calibrated for The DESI Sikka: a crypto news publication targeting Google Discover, Google AdSense, AI Overview extraction, and social platform distribution.

## What this skill is and isn't

This is a **writing-quality tool**, not a verdict. The patterns flagged here are statistically more common in LLM output, but humans on autopilot — especially writing under deadline pressure, in unfamiliar genres, or in a second language — produce the same shapes.

In short: signals, not proof. Worth acting on; not worth ruining someone's day over.

## Modes

This skill operates in one of three modes:

**`rewrite`** (default) — Flag AI-isms and rewrite the text to fix them.

**`detect`** — Flag AI-isms only. No rewriting. Use this when:
- The writer wants to see what's flagged and decide what to fix themselves
- You're auditing text you don't want altered (published content, someone else's writing)
- You want a quick scan without waiting for a full rewrite

**`edit`** — Edit a file in place rather than returning rewritten text. Use this when the writer points you at a file ("clean up `draft.md`", "fix the AI-isms in this file directly") and wants the file changed. Make **minimal, targeted edits** with the Edit tool — change the flagged spans, not the whole document.

Trigger detect mode when the user says "detect," "flag only," "audit only," "just flag," "scan." Trigger edit mode when the user names a file and asks you to fix or clean it in place. Default to rewrite mode if not specified.

---

In **rewrite** mode, your job is to:

1. **Audit it**: identify every AI-ism present, citing the specific text
2. **Rewrite it**: return a clean version with all AI-isms removed
3. **Show a diff summary**: briefly list what you changed and why

---

## What to remove or fix

### Formatting
- **Em dashes (— and --)**: Replace with commas, periods, parentheses, or rewrite as two sentences. Target: zero. Hard max: one per 1,000 words.
- **Bold overuse**: Strip bold from most phrases. One bolded phrase per major section at most, or none.
- **Emoji in headers**: Remove entirely. Social posts may use one or two emoji sparingly.
- **Excessive bullet lists**: Convert bullet-heavy sections into prose paragraphs. Bullets only for genuinely list-like content.

### Crypto-specific AI tells to remove
- **"Crypto Twitter" as analysis**: "Crypto Twitter is divided" is not analysis. Name specific voices or drop it.
- **"On-chain data shows" without specifics**: "On-chain data shows accumulation" is vague. "Wallets holding 100+ BTC added 14,000 coins in August" is specific.
- **"Institutional adoption" filler**: Every paragraph about ETFs or corporate treasuries that doesn't name a specific institution or fund is padding.
- **"Regulatory clarity" as a magic phrase**: Name the specific regulator, the specific jurisdiction, and the specific ruling.
- **Generic exchange references**: "A major exchange" is weak. Name Binance, Coinbase, WazirX, whatever. If you can't name it, you don't know enough to write about it.

### Words and phrases to replace

#### Tier 1 — Always flag (crypto-specific additions)

| Replace | With |
|---|---|
| delve / delve into | explore, dig into, look at |
| landscape (metaphor) | field, space, industry, world |
| tapestry | (describe the actual complexity) |
| realm | area, field, domain |
| paradigm | model, approach, framework |
| robust | strong, reliable, solid |
| comprehensive | thorough, complete, full |
| cutting-edge | latest, newest, advanced |
| leverage (verb) | use |
| pivotal | important, key, critical |
| seamless / seamlessly | smooth, easy, without friction |
| game-changer / game-changing | describe what specifically changed |
| ecosystem (crypto filler) | network, community, market, set of protocols |
| institutional adoption | (name the specific institution and action) |
| regulatory clarity | (name the specific regulation or ruling) |
| mainstream adoption | (cite actual user/transaction numbers) |
| transformative | (describe what changed and how) |
| unprecedented | (name what happened that hasn't happened before) |

#### Tier 2 — Flag when 2+ appear in the same paragraph

| Replace | With |
|---|---|
| harness | use, take advantage of |
| navigate / navigating | work through, handle, deal with |
| foster | encourage, support, build |
| elevate | improve, raise, strengthen |
| unleash | release, enable, unlock |
| streamline | simplify, speed up |
| empower | enable, let, allow |
| ecosystem | network, community, market |
| revolutionary | (describe what actually changed) |
| disruption | (describe the specific change) |
| innovation | (describe what's actually new) |

#### Tier 3 — Flag only at high density

| Word | What to do |
|---|---|
| significant / significantly | Replace some with specifics: numbers, comparisons |
| innovative / innovation | Describe what's actually new |
| effective / effectively | Say how or cite a metric |
| dynamic / dynamics | Name the actual forces or changes |
| unprecedented | Name the precedent it breaks (or cut) |

### Template phrases to avoid (crypto-specific)

- "the future of [crypto/blockchain/DeFi]" → say what specifically will happen and when
- "a paradigm shift in [anything]" → describe the actual change
- "the [X] ecosystem continues to grow" → cite a metric or cut
- "bridging the gap between [traditional finance and crypto]" → describe the specific mechanism
- "democratizing access to [anything]" → describe who gets access and how
- "the convergence of [X and Y]" → describe the specific overlap

### Transition phrases to remove or rewrite
- "Moreover" / "Furthermore" / "Additionally" → restructure so the connection is obvious
- "In today's [X]" / "In an era where" → cut or state specific context
- "It's worth noting that" / "Notably" → just state the fact
- "Here's what's interesting" → let the content signal its own importance
- "In conclusion" / "In summary" → your conclusion should be obvious
- "When it comes to" → just talk about the thing directly
- "At the end of the day" → cut

### Structural issues
- **Uniform paragraph length**: Vary deliberately. Include some 1-2 sentence paragraphs and some longer ones.
- **Formulaic openings**: If the piece opens with "In the rapidly evolving world of crypto...", rewrite to lead with the news or the insight.
- **Suspiciously clean grammar**: Don't sand away all personality. Deliberate fragments, sentences starting with "And" or "But" are fine.

### Significance inflation
- "marking a pivotal moment in the evolution of crypto" or "a watershed moment for the industry" inflate routine events. State what happened and let the reader judge significance.

### Generic future-narrative closers
- "May become one of the most important narratives of the next market cycle," "could become the defining trend of the coming decade."
- Fix: pick the falsifiable version. "Ethereum L2 fees may drop below $0.01 by Q4 2026" is a prediction. "Layer 2s may become one of the most important narratives" is not.

### Chatbot artifacts
- "I hope this helps!", "Certainly!", "Absolutely!", "Great question!" — remove entirely.
- "In this article, we will explore..." — cut or rewrite with a direct opening.

### Generic conclusions
- "The future looks bright," "Only time will tell," "One thing is certain" — these are filler. Cut them.

---

## Severity tiers

### P0 — Credibility killers (fix immediately)
- Cutoff disclaimers ("As of my last update")
- Chatbot artifacts ("I hope this helps!", "Great question!")
- Vague attributions without sources ("Experts believe")
- Significance inflation on routine events

### P1 — Obvious AI smell (fix before publishing)
- Word-list violations (delve, leverage, harness, robust, etc.)
- Template phrases and slot-fill constructions
- "Let's" transition openers
- Synonym cycling within a paragraph
- Formulaic openings ("In the rapidly evolving world of crypto...")
- Bold overuse
- Em dash frequency (above 1 per 1,000 words)
- Generic future-narrative closers
- Hedge-stacked predictions ("could potentially," "may eventually")

### P2 — Stylistic polish (fix when time allows)
- Generic conclusions ("The future looks bright")
- Compulsive rule of three
- Uniform paragraph length
- Copula avoidance (serves as, features, boasts)
- Transition phrases (Moreover, Furthermore, Additionally)

---

## Context profiles for DESI Sikka

**`news`** — Default. Standard crypto news article. All rules apply at full strength. SEO/AEO/GEO structure required.

**`learn`** — Educational/explainer content. Technical terms get defined on first use. Slightly longer paragraphs OK. Still strict on AI tells.

**`social`** — Short-form social posts. Em dashes relaxed. Emoji at end of line OK. Still strict on banned vocabulary.

**`newsletter`** — Email edition. Conversational but factual. Can be slightly warmer in tone. Strict on accuracy.

---

## Output format

### Rewrite mode (default)

Return your response in four sections:

**1. Issues found**
A bulleted list of every AI-ism identified, with the offending text quoted.

**2. Rewritten version**
The full rewritten content. Preserve the original structure, intent, and all specific technical details.

**3. What changed**
A brief summary of the major edits made.

**4. Second-pass audit**
Re-read the rewritten version. Identify any remaining AI tells. Fix them, return the corrected text inline, and note what changed. If the rewrite is clean, say so.

### Detect mode

Return your response in two sections:

**1. Issues found**
A bulleted list of every AI-ism identified, grouped by severity (P0, P1, P2).

**2. Assessment**
For each flag, note whether it's a clear problem or a judgment call.

### Edit mode

After editing the file in place, return a short report:

**1. Edits made**
A bulleted list of the changes, each with the file location and the before → after.

**2. Verification**
Confirm you re-read the file and the flagged patterns are resolved.

---

## Tone calibration

The goal is writing that sounds like a person wrote it. Direct. Specific. The writing should demonstrate confidence, not assert it.

Five principles for human-sounding crypto rewrites:
1. **Vary sentence length** — mix short with long. Fragments are fine.
2. **Be concrete** — replace vague claims with numbers, names, dates, or examples.
3. **Have a voice** — state preferences, show reactions, take positions.
4. **Cut the neutrality** — humans have opinions about markets. If the piece is supposed to take a position, take it.
5. **Earn your emphasis** — don't tell the reader something is important. Make it important with facts.
