---
name: designs
description: Guidance for building distinctive, accessible UIs for The DESI Sikka crypto news site. Covers brand identity, typography, layout, components, responsive design, dark/light mode, and performance. Use when building new pages, redesigning components, or creating social share graphics for the site.
license: MIT
---

# Frontend Design — The DESI Sikka

Approach this as the design lead for a crypto news publication that needs to look trustworthy, modern, and readable across every device. The DESI Sikka's visual identity must communicate: serious journalism, accessible to everyone, zero jargon walls. The design should feel like a premium news outlet, not a crypto bro blog.

## Brand identity

**The DESI Sikka** is a crypto news publication with the tagline "Crypto news, zero jargon." The design must balance:
- **Trustworthiness**: Clean typography, generous whitespace, professional layout. Readers should feel this is a credible news source, not a hype machine.
- **Accessibility**: High contrast, readable fonts, clear hierarchy. Content-first design that prioritizes reading experience.
- **Modernity**: Subtle animations, dark mode support, contemporary component design. Not stuck in 2015, but not chasing every trend.
- **Crypto-native**: Enough visual sophistication to signal expertise without alienating newcomers.

## Color system

### Light mode (default)
- **Background**: `#ffffff` (white) — clean, professional, AdSense-friendly
- **Surface**: `#f8f9fa` (light gray) — cards, sidebars, elevated surfaces
- **Border**: `#e9ecef` (subtle gray) — dividers, card borders
- **Text primary**: `#1a1a2e` (near-black) — headlines, body text
- **Text secondary**: `#6c757d` (gray) — metadata, timestamps, bylines
- **Accent primary**: `#1a73e8` (Google Blue) — links, CTAs, active states
- **Accent hover**: `#1557b0` (darker blue) — hover states
- **Success**: `#0d9488` (teal) — positive price movement, verified badges
- **Error**: `#dc2626` (red) — negative price movement, errors
- **Warning**: `#f59e0b` (amber) — cautions, opinion labels

### Dark mode
- **Background**: `#0f172a` (dark navy) — reduces eye strain for evening reading
- **Surface**: `#1e293b` (slate) — cards, elevated surfaces
- **Border**: `#334155` (slate border) — dividers
- **Text primary**: `#f1f5f9` (light gray) — headlines, body text
- **Text secondary**: `#94a3b8` (muted) — metadata, timestamps
- **Accent primary**: `#60a5fa` (lighter blue) — links, CTAs (adjusted for dark bg contrast)
- **Accent hover**: `#93bbfd` — hover states
- **Success**: `#34d399` — positive price movement
- **Error**: `#f87171` — negative price movement

### Category colors (used for category badges, section accents)
- Bitcoin: `#f7931a` (Bitcoin orange)
- Ethereum: `#627eea` (Ethereum blue)
- Altcoins: `#8b5cf6` (purple)
- Regulation: `#64748b` (slate — serious, governmental)
- DeFi & Web3: `#06b6d4` (cyan — tech-forward)
- Exchanges: `#10b981` (emerald — money, trading)

## Typography

### Font stack
- **Headlines**: `Inter, system-ui, -apple-system, sans-serif` at weight 700
- **Body**: `Inter, system-ui, -apple-system, sans-serif` at weight 400
- **Meta/data**: `Inter, system-ui, -apple-system, sans-serif` at weight 500
- **Code/numbers**: `'JetBrains Mono', 'Fira Code', monospace` (for prices, addresses, code blocks)

### Type scale
| Role | Size | Weight | Line Height | Use |
|---|---|---|---|---|
| Display | 36px / 2.25rem | 700 | 1.2 | Homepage hero headline |
| H1 | 30px / 1.875rem | 700 | 1.25 | Article headline |
| H2 | 24px / 1.5rem | 600 | 1.3 | Section headings |
| H3 | 20px / 1.25rem | 600 | 1.4 | Sub-section headings |
| Body | 16px / 1rem | 400 | 1.6 | Article body text |
| Small | 14px / 0.875rem | 400 | 1.5 | Metadata, captions |
| Tiny | 12px / 0.75rem | 500 | 1.4 | Badges, labels, timestamps |

### Principles
- **Sentence case for headings**: "Bitcoin drops 12% after liquidation cascade" not "Bitcoin Drops 12% After Liquidation Cascade"
- **Body text at 16px minimum**: Prevents iOS zoom on input focus
- **Line height 1.6 for body**: Optimized for long-form reading
- **Tabular nums for prices**: `font-variant-numeric: tabular-nums` on all price/number displays

## Layout

### Grid
- **Max content width**: 1200px
- **Article body**: 680px max (optimal reading width)
- **Sidebar**: 320px (on desktop, right side)
- **Gap**: 32px between content and sidebar
- **Section padding**: 64px vertical, responsive down to 32px on mobile

### Page templates
- **Homepage**: Hero (featured story) → Category sections (3 cards each) → Sidebar (trending + newsletter)
- **Article**: Full-width hero → 680px body → Sidebar (related + ads) → Footer
- **Category**: Category header → Grid of article cards → Pagination
- **Learn**: Table of contents sidebar → Full-width content area

### Responsive breakpoints
| Name | Width | Layout changes |
|---|---|---|
| Mobile | < 640px | Single column, hamburger nav, stacked cards |
| Tablet | 640–1024px | 2-column cards, sidebar below content |
| Desktop | 1024–1280px | Full layout with sidebar |
| Wide | > 1280px | Content caps at 1200px centered |

## Components

### Article card
- **Layout**: Image (16:9 aspect) → Category badge → Title → Excerpt (2 lines max) → Meta row (author + date + read time)
- **Hover**: Subtle shadow elevation + image zoom (scale 1.03)
- **Border**: 1px solid border-radius: 8px
- **Spacing**: 16px internal padding

### Category badge
- **Style**: Pill shape (border-radius: 9999px), category color background, white text
- **Size**: 12px font, 4px × 10px padding
- **Position**: Overlaid on article card image (bottom-left) or inline with headline

### Price ticker
- **Format**: Symbol + Price + Change (% + absolute)
- **Colors**: Green for positive, red for negative
- **Font**: Monospace for numbers (`JetBrains Mono`)
- **Animation**: Smooth number transitions, not jarring updates

### Share buttons
- **Platforms**: Twitter/X, LinkedIn, Facebook, Telegram, WhatsApp, Copy Link
- **Style**: Icon-only with tooltip labels, subtle background, rounded (8px)
- **Position**: Fixed right sidebar on desktop, bottom bar on mobile

### Newsletter signup
- **Layout**: Headline + description + email input + subscribe button
- **Style**: Card with accent border-top, clean input field
- **Validation**: Inline error messages, no page reload

### Ad slots
- **Design**: Clearly labeled "Advertisement" above the slot
- **Reserved space**: Explicit height to prevent CLS (Cumulative Layout Shift)
- **Placement**: After 3rd paragraph in article body, bottom of article, sidebar
- **Styling**: Subtle border to distinguish from content

## Dark mode

- Implement with `prefers-reduced-motion` respect and `color-scheme: dark` on `<html>`
- Use CSS custom properties for all colors (switch via `[data-theme="dark"]` or media query)
- Ensure all text meets WCAG AA contrast ratios (4.5:1 for body, 3:1 for large text)
- Category colors must be adjusted for dark backgrounds (lighter variants)
- Images should have subtle border or shadow to separate from dark backgrounds

## Performance

- **Images**: Use WebP format with `<picture>` fallback. Always set `width` and `height` to prevent CLS.
- **Lazy loading**: `loading="lazy"` on all below-fold images. Never lazy-load the hero/LCP image.
- **Fonts**: Preload Inter (primary font). Use `font-display: swap` to prevent FOIT.
- **CSS**: Inline critical CSS. Defer non-critical. No render-blocking stylesheets in `<head>`.
- **JavaScript**: Defer all non-essential JS. Use `async` for analytics. No render-blocking scripts.
- **CLS prevention**: Explicit dimensions on all media, reserved ad slots, font-display: swap.

## Accessibility

- Full keyboard navigation with visible focus rings (`:focus-visible`)
- Skip-to-content link as first focusable element
- All images have descriptive alt text
- Color is never the only indicator (price changes have arrows + text)
- `aria-label` on all icon-only buttons
- `prefers-reduced-motion` disables all animations
- Form inputs have associated labels
- Touch targets ≥ 44px on mobile

## E-E-A-T design signals

- **Author bylines** prominently displayed with author photo and bio link
- **Publication date** clearly visible, formatted as "Published August 24, 2026"
- **Sources box** for articles with external citations
- **Related articles** section to demonstrate topical depth
- **About page** linked from footer and navigation
- **Corrections page** linked from footer (transparency signal)

## AdSense-friendly design

- Content must be the primary focus (ads are secondary, clearly labeled)
- No deceptive ad placement (ads must not look like content)
- Clear navigation structure (main nav + footer links)
- Responsive layout that works on all devices
- Fast loading (Core Web Vitals in "Good" range)
- No intrusive interstitials or pop-ups
- Privacy policy, terms, and contact pages accessible from footer

## Do's and Don'ts

### Do
- Use sentence case for all headings
- Keep article body at 680px max for readability
- Use category colors consistently across badges, accents, and section headers
- Implement dark mode with proper contrast ratios
- Reserve explicit space for ad slots to prevent layout shift
- Use monospace fonts for all numerical/price displays

### Don't
- Use title case for headings (unless it's the article headline itself)
- Make the design look like a crypto trading platform (this is a news site)
- Use excessive gradients, glows, or neon effects
- Sacrifice readability for visual flair
- Use placeholder images for articles (use category glyph covers)
- Let ads dominate the layout (content first, always)
