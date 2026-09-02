---
name: mindmap
description: Create interactive, visual mind maps as standalone HTML files for crypto news content architecture. Use this skill whenever the user asks for a mind map, site map, topic map, content hierarchy, knowledge map, content cluster diagram, SEO architecture map, or any request to visualize relationships between crypto topics/pages/ideas. Also trigger for "map out", "visualize the structure of", "show connections between" crypto topics. Always produces a single .html file with pan, zoom, drag-to-rearrange, and clickable nodes.
---

# Mind Map Skill — DESI Sikka Crypto Content Architecture

Create beautiful, interactive mind maps rendered as standalone `.html` files. The maps look and feel like Miro/FigJam — white canvas, dot grid, colored curved rope connections, draggable nodes, tap-to-expand branches, and clickable leaf nodes.

## When to Use

- User asks for a **content architecture map** for crypto topics
- User wants to **visualize the site's topic clusters** (bitcoin, ethereum, altcoins, regulation, defi, exchanges)
- User wants to see **how crypto topics connect** to each other
- User asks for an **SEO content architecture** or **content cluster map**
- User wants to **map out** crypto coverage areas or **brainstorm visually**
- User provides a list of crypto topics/pages and wants them **organized spatially**

## Output

Always a single `.html` file saved to the workspace root. Never JSX or React — pure HTML + inline CSS + inline JS. No external dependencies.

## Step-by-Step Process

### Step 1: Gather Data

Determine the data source:

- **Site structure**: Read `_posts/` and `_config.yml` to map existing content
- **Category structure**: The site has 6 categories: bitcoin, ethereum, altcoins, regulation, defi, exchanges
- **Freeform request**: Ask clarifying questions if the structure is ambiguous, otherwise infer a logical hierarchy
- **URL list**: Group URLs by path segments into parent/child relationships

### Step 2: Organize into a Hierarchy

Structure the data into this mental model:

```
Root: The DESI Sikka
├── Bitcoin (orange)
│   ├── Price & Market Analysis
│   │   ├── Daily price movements
│   │   ├── Technical analysis
│   │   └── On-chain metrics
│   ├── Mining & Network
│   │   ├── Hash rate
│   │   ├── Halving events
│   │   └── Mining difficulty
│   ├── Institutional
│   │   ├── ETF updates
│   │   ├── Corporate treasuries
│   │   └── Whale movements
│   └── India angle
│       ├── Tax implications (30% + 1% TDS)
│       ├── RBI stance
│       └── Indian exchanges
├── Ethereum (blue)
│   ├── Layer 2 ecosystem
│   ├── DeFi on Ethereum
│   ├── NFTs & tokens
│   └── Upgrade roadmap
├── Altcoins (purple)
│   ├── Solana ecosystem
│   ├── Layer 1 competitors
│   ├── Meme coins
│   └── Token launches
├── Regulation (slate)
│   ├── India regulation
│   ├── US SEC/CFTC
│   ├── EU MiCA
│   └── Global policy
├── DeFi & Web3 (cyan)
│   ├── Protocols & TVL
│   ├── Yield & staking
│   ├── Cross-chain bridges
│   └── DAOs & governance
└── Exchanges & How-to (green)
    ├── Exchange reviews
    ├── P2P trading
    ├── Wallet security
    └── On-ramps for India
```

**Hierarchy rules:**
- **Max 4 levels deep**: Root → Category → Topic → Article/Leaf
- **Group by topic similarity**, not just URL path
- **6 main silos** (matching site categories) is the standard top ring
- **3–6 hubs per silo** to avoid visual overcrowding
- **Up to ~15 leaves per hub** (they fan out radially)

### Step 3: Build the HTML

Read the template at `templates/mindmap-template.html` in this skill's directory. This is your **base template** — use it as the foundation and customize:

1. **Copy the template** to your working directory
2. **Replace the `SILOS` data array** with the actual organized data
3. **Adjust colors** — use category colors: Bitcoin #f7931a, Ethereum #627eea, Altcoins #8b5cf6, Regulation #64748b, DeFi #06b6d4, Exchanges #10b981
4. **Adjust radii** if needed (R1/R2/R3 for the three rings)
5. **Set the initial expanded state** — expand 1–2 silos so the user sees ropes immediately
6. **Update the title and header** to "The DESI Sikka — Content Architecture"
7. Save to workspace root as `<name>-mindmap.html`

### Step 4: Present the File

Present the output HTML file to the user.

### Step 2.5: Content Gap Analysis

For every hub/branch, analyze what's missing and suggest new topics. This is the key value-add that makes the mind map an SEO strategy tool.

**How to find gaps — check each crypto category for these content archetypes:**

1. **Pillar / Definition post** — "What Is [Topic]?" (every silo MUST have one)
2. **Beginner guide** — "[Topic] for Beginners / First-Timers"
3. **India-specific guide** — "[Topic] Tax in India" or "India Regulation Guide"
4. **Comparison posts** — "[Exchange A] vs [Exchange B]" for each pair of related platforms
5. **Legal/regulatory guide** — "Is [Topic] Legal in India?" with current status
6. **Price prediction** — "[Asset] Price Prediction [Year]" (labeled as Opinion)
7. **How-to guide** — "How to Buy [Asset] in India"
8. **Best-of listicle** — "Best [Category] [Year]"
9. **Explainer** — "How [Protocol/Technology] Works"
10. **News analysis** — "[Event]: What It Means for [Audience]"

For each missing archetype, create a gap entry with target keyword and priority:
- **High priority**: Missing pillar page, missing comparison vs a direct competitor topic, high-volume "best of" listicle
- **Medium priority**: Missing use-case post, missing how-to, supplementary comparison
- **Low priority**: Nice-to-have niche content, long-tail variations

### Step 2.6: Internal Linking Map

For every existing post, determine which other pages it should link to. Follow these rules:

1. **Every post links UP to its category pillar** — always
2. **Every post links ACROSS to related category content** — especially cross-category stories
3. **Comparison posts link SIDEWAYS** — to both compared entities' pillar pages
4. **How-to posts link to the exchanges/tools** they reference
5. **India-specific posts link to the India regulation guide**
6. **Related posts within the same hub should cross-link**
7. **Learn guides link DOWN to relevant articles** (reverse direction)

Represent links as an array of target labels: `ln: ["Bitcoin Pillar", "India Regulation", "Exchange Reviews"]`

## Data Format

The `SILOS` array follows this structure:

```javascript
const SILOS = [
  {
    id: "bitcoin",
    n: "Bitcoin",
    c: "#f7931a",
    p: {
      t: "Bitcoin News & Analysis",
      u: "/category/bitcoin/"
    },
    b: [
      {
        h: "Price & Market",
        lk: "→ Bitcoin Pillar",
        ps: [
          {
            t: "Bitcoin drops 12% in liquidation cascade",
            u: "/news/bitcoin-liquidation-cascade/",
            ln: ["Bitcoin Pillar", "Exchanges", "India Tax Guide"]
          }
        ],
        gaps: [
          {
            t: "Bitcoin Price Prediction 2026",
            kw: "bitcoin price prediction 2026",
            pri: "high"
          }
        ]
      }
    ]
  }
];
```

## Color Palette

Use category-specific colors:

```
#f7931a  Bitcoin orange    #627eea  Ethereum blue   #8b5cf6  Altcoins purple
#64748b  Regulation slate  #06b6d4  DeFi cyan       #10b981  Exchanges green
```

## Visual Design Rules

### Canvas
- **White background** (#fff) with a **dot grid** (radial-gradient dots, 28px spacing, subtle gray)
- Full viewport, no scrollbars — pan and zoom only

### Ropes (Connection Lines)
- **SVG bezier curves** using cubic bezier (S-curve shape)
- The SVG element MUST be positioned at `left:0; top:0; width:1px; height:1px; overflow:visible`
- Each rope has **two layers**: a thick transparent glow layer + the main colored line
- **Endpoint dots** at both ends of each rope
- Width hierarchy: Root→Category: 5px, Category→Hub: 3.5px, Hub→Leaf: 2px
- Opacity: 0.55 for main rope, 0.08 for glow
- `stroke-linecap: round` always

### Bezier curve formula
```javascript
function bezier(x1, y1, x2, y2) {
  const dx = x2 - x1;
  return `M${x1} ${y1}C${x1+dx*.45} ${y1} ${x2-dx*.45} ${y2} ${x2} ${y2}`;
}
```

### Nodes
- **Root**: Dark rounded rect (140×70px), centered, bold white text, border glow
- **Category**: Colored pill (border-radius: 25px), white bold text, drop shadow matching category color
- **Hub**: White card with 5px colored left border, shows "→ links to" tag
- **Post/Leaf**: Small white card with colored dot, "↗ Open" link text
- **Gap (NEW)**: Green dashed-border card with "+" circle icon. Shows suggested title, target keyword, and priority badge

### Layout Algorithm
- Radial layout: categories evenly spaced in a circle around center
- R1 = 340–360px (center to categories)
- R2 = 260–270px (category to hubs)
- R3 = 175–185px (hub to leaves)
- Fan angle per category = `2π / categoryCount`

### Interactions
- **Tap category** → expand/collapse its branches
- **Tap hub** → expand/collapse its leaves
- **Tap leaf** → open URL in new tab
- **Drag node** → move it + all descendants, ropes redraw in real-time
- **Drag background** → pan the viewport
- **Pinch** → zoom (touch devices)
- **+/− buttons** → zoom (all devices)
- **↺ button** → reset view

### Click vs Drag Detection
```javascript
let totalMoved = 0;
// On pointer move: totalMoved += Math.abs(delta)
// On pointer up: if (totalMoved < 10) → treat as click; else → was a drag
```

### Top Bar
- Fixed position, white with backdrop blur, bottom border
- Title: "The DESI Sikka — Content Architecture"
- z-index above everything

### Controls
- Fixed bottom-right: +, −, ↺ buttons (44×44px, rounded, white, shadow)
- Fixed bottom-left: zoom percentage label

## Common Customizations

### For SEO / Sitemap Maps
- Add warning badges for URL issues (orphans, duplicates, wrong category)
- Show "→ links to" tags indicating internal linking strategy
- Category pillar pages get "★ PILLAR PAGE" tag
- Missing pillars get "⚠ MISSING PILLAR" in orange

### For Content Planning
- Show gap nodes with suggested articles and target keywords
- Color-code by content priority (red=high, amber=medium, green=low)
- Include search volume estimates where available

### For Editorial Calendar
- Add date nodes for planned publication dates
- Show content pipeline: draft → review → published
- Link to existing articles in `_posts/`
