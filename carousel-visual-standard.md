# Carousel Visual Standard Skill

## When to Trigger
On every request to build an Instagram carousel — automatic, no need to ask.

---

## Core Principle — Cover Image

> **Not a character on a plain background. A cinematic scene that tells the story.**

The cover is the scroll-stopper. It should communicate the topic visually — before the user reads a single word.

---

## Required Workflow

### Step 1 — Gather Inputs
Before anything else, collect:
- **Carousel topic** (what is the core message?)
- **Main headline** (exact text)
- **Subtitle** (exact text)
- **Number of slides** (for `01 / XX` footer)
- **Mascot on/off?** (default: **on**)
- **Which mascot pose?** (default: `proud`)

### Step 2 — 3 Visual Concepts (text only, no generation yet)
Present 3 concept descriptions — NO image generation yet. Each: name + 2-3 line scene description + what it communicates.

Format:
```
**V1 — [Concept Name]**
[2-3 lines: what you see, where, what's the visual drama, what it says]

**V2 — ...**
**V3 — ...**
```

Every concept must have:
- Photographic/cinematic background (no plain or gradient backgrounds)
- Visual metaphor connected to the topic
- Clear differentiation: all 3 concepts must be visually distinct

### Step 3 — Approval
Ask: "Which concept to generate? (or describe changes)"

### Step 4 — Generate
Run generation with the model and standard below.

---

## Visual Standard — Cover Image

### Model & API
```
Model:    gpt-image-2-image-to-image
Endpoint: https://api.kie.ai/api/v1/jobs/createTask
API Key:  YOUR_KIE_API_KEY   ← replace with your kie.ai key
Aspect:   3:4
```

### Mascot Reference URLs
Replace these with your own character images:
| Pose | URL |
|------|-----|
| proud (default) | `YOUR_MASCOT_URL_PROUD` |
| welcoming | `YOUR_MASCOT_URL_WELCOME` |
| thumbs-up | `YOUR_MASCOT_URL_THUMBSUP` |

Upload your character PNG to https://catbox.moe to get a public URL.

### Color Palette (customize for your brand)
```
Primary Dark:  #1E376E  — dark backgrounds, text-on-light
Accent:        #FFC828  — starburst, navigation dots, highlights
Dark Accent:   #D4A03C  — pill badge, dividers
Light:         #F5F0E6  — main text on dark backgrounds
```

### Fixed Elements on Every Cover
1. **Starburst** — 8-pointed asterisk in Accent color behind the character. 4 long rays at cardinal + 4 short at intercardinal.
2. **Pill badge** — small rounded badge, Dark Accent background, centered at top
3. **Footer chrome:**
   - TOP-LEFT: `01 / [XX]` monospace 22px
   - TOP-RIGHT: small starburst 60px in Accent color
   - BOTTOM-LEFT: `@your_handle` 20px
   - BOTTOM-RIGHT: your CTA text (e.g. `Save this ←`) 20px
   - BOTTOM-CENTER: navigation dots (dot 1 solid Accent, rest faded 8px)
4. **Vignette** — Primary Dark borders on all edges

### Prompt Template — Cover Image

```
Take the EXACT [character/mascot] shown in the supplied reference image
and place it in a new dramatic cinematic scene. PRESERVE THE CHARACTER PRECISELY:
• [describe your character style: 3D cartoon / illustrated / etc.]
• [describe colors, proportions, key visual features]
• NO changes to character design — only change pose and scene

NEW POSE: [describe specific pose for this concept]

BACKGROUND — [scene name]:
[Detailed description of the scene — photographic quality, cinematic lighting, dramatic atmosphere]

GRAPHIC ELEMENT: Large bold 8-pointed starburst in [Accent color], ~280px,
centered behind the character — 4 long rays at cardinal + 4 shorter at intercardinal.

TYPOGRAPHY — UPPER ZONE:
Small rounded pill badge with [Dark Accent] fill, centered: [Font] [size]
— EXACT TEXT: [PILL TEXT]

Main headline: [Font] Black [88-96]px, [Light color], centered, [language direction]:
EXACT TEXT: [HEADLINE]

Subtitle: [Font] medium [34-38]px [Light color]: EXACT TEXT: [SUBTITLE]

FOOTER CHROME:
Top-left: monospace LTR [01 / XX] [Light] 22px
Top-right: 8-pointed asterisk ~60px [Accent]
Bottom-left: @[your_handle] [Font] 20px [Light]
Bottom-right: [your CTA] [Font] 20px 20px
Bottom-center: [N] dots; dot 1 solid [Accent] 12px, rest faded [Light] 8px

CRITICAL: [add language-specific rendering rules here]
3D cartoon character must match reference exactly.
```

---

## Visual Archetypes — Reference

| Archetype | Scene Description | Best For |
|-----------|------------------|----------|
| **Split World** | Old world left + new world right, character breaks chains in center | Comparisons, before/after, transformation |
| **Shadow Monsters** | Tiny harmless objects cast giant scary shadows, character stands fearless in spotlight | Fears, myths, misconceptions |
| **The Corridor** | Long corridor with 4 locked doors, golden light at the end | Journeys, steps, stages |
| **Rooftop + Storm** | Character on rooftop, 4 storm clouds retreating behind, golden skyline ahead | Overcoming obstacles |
| **Breakthrough** | Character smashes through glass wall with fears etched on it, warm city beyond | Breaking barriers, launching |
| **Open Cages** | 4 open empty cages, golden birds flying free, character triumphant | Freedom, unlocked potential |

---

## Hard Rules

- Never: character on plain/gradient background only
- Never: skip the concept approval step
- Never: alter character proportions/colors/style
- Always: scene tells the story visually
- Always: dramatic lighting (spotlight / golden hour / chiaroscuro)
- Always: cinematic depth — foreground + midground + background layers
