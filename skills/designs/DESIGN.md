## Overview

The DESI Sikka reads like a serious crypto news publication — closer to CoinDesk or The Hindu BusinessLine in atmosphere than a crypto trading app. Clean white canvas, strong readable type, one trusted blue accent, and category-color coding that makes the site's six beats scannable at a glance. The tagline "Crypto news, zero jargon" drives every choice: text-first, no decoration that gets in the way of reading.

**Key Characteristics:**
- Single trusted accent: Google Blue `{colors.primary}` (#1a73e8) for links, CTAs, active states.
- Category colors carry the wayfinding: each of the six beats (Bitcoin, Ethereum, Altcoins, Regulation, DeFi, Exchanges) owns one color used in badges, section accents, and card chips.
- Light-first design with a proper dark mode. Headline-focused, generous whitespace.
- Inter everywhere; monospace only for numbers and code (prices, addresses, code blocks).
- 8px radii, subtle 1px borders, minimal shadows. Professional, not flashy.
- Content-first: 680px article column, explicit reserved ad slots, no layout shift.

## Colors

### Brand & Accent
- **Trust Blue** (`{colors.primary}` — #1a73e8): Links, primary CTAs, active states, focus rings.
- **Trust Blue Active** (`{colors.primary-active}` — #1557b0): Press/hover state.
- **Trust Blue Soft** (`{colors.primary-soft}` — #e8f0fe): Selection backgrounds, link underlines, tag fill.

### Dark-mode Brand
- **Trust Blue Light** (`{colors.primary-dark}` — #60a5fa): Links, CTAs on dark backgrounds.
- **Trust Blue Light Active** (`{colors.primary-dark-active}` — #93bbfd): Press/hover state on dark.

### Category (Beat) Colors
- **Bitcoin** (`{colors.bitcoin}` — #f7931a): Bitcoin orange.
- **Ethereum** (`{colors.ethereum}` — #627eea): Ethereum blue.
- **Altcoins** (`{colors.altcoins}` — #8b5cf6): Purple.
- **Regulation** (`{colors.regulation}` — #64748b): Slate (serious, governmental).
- **DeFi** (`{colors.defi}` — #06b6d4): Cyan (tech-forward).
- **Exchanges** (`{colors.exchanges}` — #10b981): Emerald (money, trading).

### Surface (Light)
- **Canvas** (`{colors.canvas}` — #ffffff): Page floor.
- **Surface** (`{colors.surface}` — #f8f9fa): Cards, sidebars, elevated surfaces.
- **Hairline** (`{colors.hairline}` — #e9ecef): Dividers and card borders.

### Surface (Dark)
- **Canvas Dark** (`{colors.canvas-dark}` — #0f172a): Dark-mode page floor.
- **Surface Dark** (`{colors.surface-dark}` — #1e293b): Dark-mode cards.
- **Hairline Dark** (`{colors.hairline-dark}` — #334155): Dark-mode dividers.

### Text
- **Ink** (`{colors.ink}` — #1a1a2e): Headlines and body (light mode).
- **Body Muted** (`{colors.body-muted}` — #6c757d): Metadata, timestamps, bylines.
- **Ink Dark** (`{colors.ink-dark}` — #f1f5f9): Headlines and body (dark mode).
- **Body Muted Dark** (`{colors.body-muted-dark}` — #94a3b8): Dark-mode metadata.

### Semantic
- **Success / Up** (`{colors.success}` — #0d9488 light, #34d399 dark): Positive price movement, verified.
- **Error / Down** (`{colors.error}` — #dc2626 light, #f87171 dark): Negative price movement, errors.
- **Warning** (`{colors.warning}` — #f59e0b): Cautions, Opinion labels.

## Typography

### Font Family
Inter across every text role. Code, prices, and addresses switch to **JetBrains Mono** (fallback `'Fira Code', monospace`). Fallback: `ui-sans-serif, system-ui, -apple-system, sans-serif`.

### Hierarchy

| Token | Size | Weight | Line Height | Use |
|---|---|---|---|---|
| `{typography.display}` | 36px | 700 | 1.2 | Homepage hero |
| `{typography.h1}` | 30px | 700 | 1.25 | Article headline |
| `{typography.h2}` | 24px | 600 | 1.3 | Section headings |
| `{typography.h3}` | 20px | 600 | 1.4 | Sub-section headings |
| `{typography.body}` | 16px | 400 | 1.6 | Article body |
| `{typography.small}` | 14px | 400 | 1.5 | Metadata, captions |
| `{typography.tiny}` | 12px | 500 | 1.4 | Badges, labels, timestamps |
| `{typography.mono}` | 14px | 400 | 1.5 | Prices, addresses, code — JetBrains Mono |

### Principles
- **Sentence case headings.** "Bitcoin drops 12% after liquidation cascade", not title case.
- **Body at 16px minimum** to prevent iOS zoom on input focus.
- **Line height 1.6 for body** — optimized for long-form reading.
- **`font-variant-numeric: tabular-nums`** on every price and number display.

## Layout

### Grid & Container
- **Max content width:** 1200px.
- **Article body:** 680px max (optimal reading width).
- **Sidebar:** 320px on desktop, right side.
- **Gap:** 32px between content and sidebar.
- **Section padding:** 64px vertical, responsive down to 32px on mobile.

### Page Templates
- **Homepage:** Hero (featured story) → category sections (3 cards each) → sidebar (trending + newsletter).
- **Article:** Full-width hero → 680px body → sidebar (related + ads) → footer.
- **Category:** Category header → grid of article cards → pagination.
- **Learn:** Table of contents sidebar → full-width content area.

## Shapes

### Border Radius Scale

| Token | Value | Use |
|---|---|---|
| `{rounded.none}` | 0px | Reserved |
| `{rounded.sm}` | 6px | Tags inline |
| `{rounded.md}` | 8px | Cards, buttons, inputs, share icons |
| `{rounded.lg}` | 12px | Large cards, code blocks |
| `{rounded.pill}` | 9999px | Category badges, labels |

Bullet-journal radii — 8px is the default surface radius. Clean and neutral, not pill-happy.

## Components

### Top Navigation
Background `{colors.canvas}`, ink text, 64px. Wordmark left, primary menu (News / Bitcoin / Ethereum / Altcoins / Regulation / DeFi / Exchanges / Learn), search + newsletter right. Collapses to hamburger below 768px.

### Article Card
Image (16:9) → category badge → title → 2-line excerpt → meta row (author, date, read time). Hover: subtle shadow + 1.03 image zoom. 1px hairline border, 8px radius, 16px padding.

### Category Badge
Pill, `{rounded.pill}`, category color background, white text. 12px font, 4px × 10px padding. Overlaid on card image (bottom-left) or inline with headline.

### Price Ticker
Symbol + price + change (percent + absolute). Green up / red down with arrow glyphs. Monospace numbers. Smooth transitions, never jarring.

### Share Buttons
Icon-only with tooltip, subtle background, 8px radius. Platforms: X, LinkedIn, Facebook, Telegram, WhatsApp, copy link. Fixed right sidebar on desktop, bottom bar on mobile.

### Newsletter Signup
Headline + description + email input + subscribe button. Card with accent top-border, inline validation, no page reload.

### Ad Slots
Clearly labeled "Advertisement" above. Explicit reserved height (prevents CLS). Placed after 3rd paragraph, at article end, and in sidebar. Subtle border to distinguish from content.

### Sources Box
Article-level card listing external citations. Renders above the copyright notice. Inline eyebrow text, hairline top border.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 640px | Single column, hamburger nav, stacked cards, share bar bottom |
| Tablet | 640–1024px | 2-column cards, sidebar below content |
| Desktop | 1024–1280px | Full layout with sidebar |
| Wide | > 1280px | Content caps at 1200px centered |

### Dark Mode
- `color-scheme: dark` on `<html>`.
- All surfaces/inks/borders switch via CSS custom properties.
- Category colors lighten for dark backgrounds.
- Every color pair meets WCAG AA (4.5:1 body, 3:1 large text).

## Do's and Don'ts

### Do
- Use sentence case for all headings.
- Keep the article body at 680px for readability.
- Reserve `{colors.primary}` for links and CTAs; keep category colors for wayfinding.
- Reserve explicit space for ad slots to prevent layout shift.
- Use monospace (`{typography.mono}`) for every price, address, and number.
- Provide a full light and dark surface set via tokens.

### Don't
- Don't make it look like a crypto trading platform — this is a news site.
- Don't use title case headings (except the article headline itself if desired).
- Don't use heavy gradients, neon glows, or excessive shadow tiers.
- Don't let ads dominate or resemble content.
- Don't use placeholder images for articles (use category glyph covers).
- Don't sacrifice reading comfort for visual flair.

## Known Gaps

- Animation timings out of scope (keep motion minimal and `prefers-reduced-motion`-aware).
- Social card template should be 1200×630 with minimal text overlay.
- Category hero images for Discover are recommended ≥1200×630.
