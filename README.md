# 🎠 Claude Carousel Visual Standard Skill

A [Claude Code](https://claude.ai/code) skill that generates **cinematic, editorial-quality Instagram carousel cover images** using `gpt-image-2` via [kie.ai](https://kie.ai).

Instead of a plain character-on-background, every cover tells a story visually — think movie poster meets Instagram editorial.

---

## Examples

| V4 — Rooftop + Storm | V5 — Breakthrough | V6 — Open Cages |
|---|---|---|
| Mascot on rooftop, 4 fear-clouds retreating behind, golden city ahead | Mascot smashes through glass wall etched with 4 fears | 4 open birdcages, golden birds flying free, mascot triumphant |

> All three generated from the same skill with different visual concepts.

---

## How it Works

**Workflow:**

```
1. You describe the carousel topic + headline + subtitle
2. Claude proposes 3 cinematic visual concepts (text only, no generation yet)
3. You pick one (or request tweaks)
4. Claude generates the cover via gpt-image-2-image-to-image
```

This saves API credits and gives you control over the creative direction before spending anything.

---

## Installation

1. Copy `carousel-visual-standard.md` to your Claude skills folder:

```bash
cp carousel-visual-standard.md ~/.claude/skills/
```

2. Add this line to your `~/.claude/CLAUDE.md`:

```markdown
- `/carousel-visual-standard` — **Carousel visual standard** (auto-trigger): concepts → approval → generation. Cinematic cover with mascot via gpt-image-2. Required for every carousel build.
```

3. Get a [kie.ai API key](https://kie.ai) and update the `YOUR_KIE_API_KEY` placeholder in the skill file.

---

## Adapting to Your Brand

### Step 1 — Replace the Mascot

The skill uses a 3D cartoon shark by default. To use **your own mascot or character**:

1. Upload your character image to [catbox.moe](https://catbox.moe) (free, no account needed)
2. Replace the mascot URLs in the skill file:

```markdown
# In carousel-visual-standard.md, replace:
| default | `https://files.catbox.moe/YOUR_MASCOT.png` |
```

**Tips for mascot images:**
- Use a clean PNG with white/transparent background
- 3D cartoon style works best (Pixar aesthetic)
- Have 2–3 different poses if possible (e.g. proud, welcoming, thumbs-up)
- The model preserves the character's look — it only changes the pose and scene

**No mascot?** Remove the `image_input_urls` field and describe your cover character in the prompt text instead.

---

### Step 2 — Update Brand Colors

Find and replace the color palette in the skill file:

```markdown
# Default (navy + gold)          → Your brand
Navy:      #1E376E               → Your primary dark
Gold:      #FFC828               → Your accent/highlight
Dark Gold: #D4A03C               → Your secondary accent
Cream:     #F5F0E6               → Your text-on-dark color
```

The colors appear in:
- Starburst / graphic element
- Typography (headlines, subtitles)
- Footer chrome (dots, handles)
- Vignette borders

---

### Step 3 — Update Footer Chrome

Replace the static brand elements in the prompt template:

```
# Replace these in the FOOTER CHROME section:
@nadlan_lo_lekrishim  →  @your_handle
שמרו לאחר כך ←        →  Your CTA text (or remove)
```

For non-Hebrew carousels, remove the RTL instruction from the CRITICAL section.

---

### Step 4 — Choose Visual Archetypes

The skill includes 6 proven visual archetypes. Match them to your content:

| Archetype | Best for |
|-----------|----------|
| **Split World** | Before/after, comparisons, transformation stories |
| **Shadow Monsters** | Fears, myths, misconceptions, "the truth about X" |
| **The Corridor** | Step-by-step journeys, paths, stages of growth |
| **Rooftop + Storm** | Overcoming obstacles, leaving the past behind |
| **Breakthrough** | Breaking through barriers, launching, first steps |
| **Open Cages** | Freedom, unlocking potential, "it was never real" |

**For your own archetypes:** just describe the scene concept to Claude and it will adapt the prompt structure.

---

### Step 5 — Adjust for Your Language

The default skill assumes **Hebrew RTL** text. For other languages:

**English:**
- Remove all `RTL Hebrew` instructions from the prompt template
- Change font references: replace `Frank Ruhl Libre` (serif Hebrew) with your preferred font, e.g. `Playfair Display`, `Bebas Neue`
- Remove the `gershayim` and RTL critical rules

**Arabic:**
- Keep RTL instructions
- Change font references to Arabic-compatible fonts

**Example prompt typography block for English:**
```
Main headline: Playfair Display Black 88px, warm cream (#F5F0E6), centered, 2-3 lines:
EXACT TEXT: [YOUR HEADLINE]

Subtitle: Inter medium 34px #F5F0E6:
EXACT TEXT: [YOUR SUBTITLE]
```

---

## Technical Reference

### API Details

```
Model:     gpt-image-2-image-to-image
Platform:  kie.ai
Endpoint:  https://api.kie.ai/api/v1/jobs/createTask
Aspect:    3:4 (Instagram carousel format)
```

### Request Format

```json
{
  "model": "gpt-image-2-image-to-image",
  "input": {
    "prompt": "...",
    "input_urls": ["https://your-mascot-url.png"],
    "aspect_ratio": "3:4"
  }
}
```

### Polling

```json
GET https://api.kie.ai/api/v1/jobs/recordInfo?taskId={taskId}
→ data.state == "success"
→ JSON.parse(data.resultJson).resultUrls[0]
```

### Generation Script

See `generate.py` in this repo for a ready-to-run Python script that handles:
- Submitting the task
- Polling until complete
- Downloading the result

---

## Content Slides (Slides 2–N)

For text-heavy content slides, use `nano-banana-pro` (same kie.ai platform):

```json
{
  "model": "nano-banana-pro",
  "input": {
    "prompt": "...",
    "aspect_ratio": "3:4",
    "resolution": "2K",
    "output_format": "png"
  }
}
```

Even text-heavy slides should include at least one graphic element:
a decorative icon, a large background number, a colored accent, or a subtle texture.

---

## License

MIT — use freely, adapt for your brand, share with credit appreciated.
