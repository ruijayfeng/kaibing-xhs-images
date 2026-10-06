---
name: kaibing-xhs-images
description: 使用凯冰 IP 制作小红书封面与图文卡片，沿用 baoyu-xhs-images 的风格、分页和布局体系；在用户要求凯冰图文、凯冰封面或将凯冰融入小红书内容时使用。
metadata:
  upstream_version: "2.0.1"
  local_variant: "kaibing-1"
  openclaw:
    homepage: https://github.com/ruijayfeng/kaibing-xhs-images
---

# 凯冰小红书图文

项目级改装自 baoyu-xhs-images。保留原有 12 种风格、8 种布局、分析、分页和提示词资源；本项目默认采用白底凯冰编辑风格。角色设定来自 kevinbee-illustrations 的本地快照。

## 凯冰集成入口

每次规划或生成凯冰图片，先读取 [references/kaibing-integration.md](references/kaibing-integration.md)。该文件定义角色参考、封面与内页分工、文字制作、样张与验收；本文件定义原有内容与布局流程。默认风格规划与生成还须读取 [references/approved-style.md](references/approved-style.md)，按页任务查看用户确认的封面或内页样图。角色身份文档仅负责人物，整张卡片按本 Skill 的 3:4 画幅和内容布局执行。

本地改装来源与文件摘要见 [references/provenance.json](references/provenance.json)。用户当前要求与已确认偏好优先；不同时加载另外两个小红书 Skill 的全部流程。

分析、分页、组装提示词与验收时须读取 [references/editorial-content.md](references/editorial-content.md)：以完整问题和具体解释决定密度，设计文字与图像的分工，再检查手机阅读与场景语义。它优先于原有布局表中的条目数和留白比例建议；已确认视觉样例继续锁定身份、配色与整体气质。

## User Input Tools

When this skill prompts the user, follow this tool-selection rule (priority order):

1. **Prefer built-in user-input tools** exposed by the current agent runtime — e.g., `AskUserQuestion`, `request_user_input`, `clarify`, `ask_user`, or any equivalent.
2. **Fallback**: if no such tool exists, emit a numbered plain-text message and ask the user to reply with the chosen number/answer for each question.
3. **Batching**: if the tool supports multiple questions per call, combine all applicable questions into a single call; if only single-question, ask them one at a time in priority order.

Concrete `AskUserQuestion` references below are examples — substitute the local equivalent in other runtimes.

## Image Generation Tools

生成前核对当前工具列表以及参考图输入能力；工具名随运行环境变化。优先使用当前原生图像工具，并读取相应 imagegen Skill。

- 当前 Codex 内置 `image_gen.imagegen` / `image_gen__imagegen` 支持 `referenced_image_paths`。实际调用传入存在的绝对路径；提示词中的路径文字不能代替参考输入。
- 本地参考先用 `view_image` 查看；新图使用所选参考的 `referenced_image_paths`，不同时使用 `num_last_images_to_include`。
- 内置出图无需额外配置 `OPENAI_API_KEY`；可用权限与额度仍以本次工具结果为准。未调用时只报告能力可用，不报告已经生成。
- 工具若不支持角色参考，停止人物出图并说明阻塞点。普通质量或尺寸问题不触发另装 API 工具；新增付费后端或密钥配置先说明，并取得用户授权。
- 原生工具实际参数以当前接口为准，不添加不存在的 output_path、quality、sessionId 或 size 参数。先生成，再将结果复制到项目输出目录。

生成前保存完整提示词到 `prompts/NN-{type}-{slug}.md`。默认使用图像工具设计整张卡片；明确选择真实字体制作时，遵循集成指南中的完整排版分支。最终交付可查看图片。

## Batch Generation Policy

After every prompt file for the current generation group has been saved and verified, generate images in batches by default.

Priority order:

1. Use the chosen backend's native batch / multi-task interface if it exists. Each task must keep its own prompt file, output path, aspect ratio, session ID, and direct reference images.
2. If no native batch interface exists but the runtime can issue parallel tool calls, dispatch up to `generation_batch_size` images at a time. Default: `4`. An explicit user request in the current message, such as `--batch-size 4` or "并行 4 张一起生成", overrides EXTEND.md.
3. If neither native batch nor parallel tool calls are available, generate sequentially.

Rules:

- 先生成 1 张样张供用户审查；当前任务已确认可继续后，再批量生成其余图片。有人物页加载身份参考，整套一致性参考按集成指南选择。
- Never start a batch until every selected prompt file for that batch exists on disk.
- Retry failed items once without regenerating successful items.
- Do not use subagents merely to parallelize image rendering. Use subagents only for separate prompt iteration or creative exploration.

## Confirmation Policy

复用当前任务中已确认的主题、偏好与授权；已完成的确认不重复提问。新主题仅在内容、方向或范围缺失且影响结果时提出简短问题。只要求安装、改装、分析或规划时，完成对应工作，不额外生图。

用户要求直接生成时，说明所选风格、布局、页数与后端后继续；默认先生成一张样张。用户审查样张后再推进整套，除非当前任务已明确授权全部生成。生成授权不包含自动发布或修改全局配置。

## Language

Respond in the user's language across questions, progress, errors, and completion summary. Keep technical tokens (style names, file paths, code) in English.

## Options

| Option | Description |
|--------|-------------|
| `--style <name>` | Visual style (see Styles below) |
| `--layout <name>` | Information layout (see Layouts below) |
| `--palette <name>` | Color override: macaron / warm / neon |
| `--preset <name>` | Style + layout + optional palette shorthand (see Presets below; per-preset prompt fragments in `references/style-presets.md`) |
| `--ref <files...>` | Additional references; record identity / style / evidence roles |
| `--batch-size <n>` | Temporary generation batch size for this run. Default: `generation_batch_size` from EXTEND.md, otherwise 4. Clamp to 1-8. |
| `--yes` | Non-interactive: skip all confirmations, use EXTEND.md or built-in defaults, auto-confirm recommended plan (Path A) |

## Dimensions

Three independent knobs combine freely:

| Dimension | Controls | Options |
|-----------|----------|---------|
| **Style** | Visual aesthetics (lines, decorations, rendering) | 12 styles (see Styles below) |
| **Layout** | Information structure (density, arrangement) | 8 layouts (see Layouts below) |
| **Palette** (optional) | Color override, replaces the style's default colors | macaron / warm / neon (see Palettes below) |

Example: `--style notion --layout dense` makes an intellectual knowledge card; add `--palette macaron` to soften the colors without changing notion's rendering rules. A `--preset` is a shorthand for style + layout (+ optional palette).

**Palette behavior**: no `--palette` → style's built-in colors; `--palette <name>` → overrides colors only, rendering rules unchanged. Some styles declare a `default_palette` (e.g., sketch-notes defaults to macaron).

## Styles (12)

| Style | Description |
|-------|-------------|
| `cute` | Sweet, adorable, girly aesthetic |
| `fresh` | Clean, refreshing, natural |
| `warm` | Cozy, friendly, approachable |
| `bold` | High impact, attention-grabbing |
| `minimal` | Ultra-clean, sophisticated |
| `retro` | Vintage, nostalgic, trendy |
| `pop` | Vibrant, energetic, eye-catching |
| `notion` | Minimalist hand-drawn line art, intellectual |
| `chalkboard` | Colorful chalk on black board, educational |
| `study-notes` | Realistic handwritten photo style, blue pen + red annotations + yellow highlighter |
| `screen-print` | Bold poster art, halftone textures, limited colors, symbolic storytelling |
| `sketch-notes` | Hand-drawn educational infographic, macaron pastels on warm cream, wobble lines |

Per-style specifications: `references/presets/<style>.md`.

## Layouts (8)

| Layout | Description |
|--------|-------------|
| `sparse` | 1-2 points, maximum impact |
| `balanced` | 3-4 points, standard |
| `dense` | 5-8 points, knowledge-card style |
| `list` | Enumeration / ranking (4-7 items) |
| `comparison` | Side-by-side contrast |
| `flow` | Process / timeline (3-6 steps) |
| `mindmap` | Center-radial (4-8 branches) |
| `quadrant` | Four-quadrant / circular sections |

Layout specs: `references/elements/canvas.md`.

## Palettes (optional override)

Replaces the style's colors while keeping rendering rules (line treatment, textures) intact.

| Palette | Background | Zone Colors | Accent | Feel |
|---------|------------|-------------|--------|------|
| `macaron` | Warm cream #F5F0E8 | Blue #A8D8EA, Lavender #D5C6E0, Mint #B5E5CF, Peach #F8D5C4 | Coral #E8655A | Soft, educational |
| `warm` | Soft peach #FFECD2 | Orange #ED8936, Terracotta #C05621, Golden #F6AD55, Rose #D4A09A | Sienna #A0522D | Earth tones, cozy |
| `neon` | Dark purple #1A1025 | Cyan #00F5FF, Magenta #FF00FF, Green #39FF14, Pink #FF6EC7 | Yellow #FFFF00 | High-energy, futuristic |

Palette specs: `references/palettes/<palette>.md`.

## Presets (style + layout shortcuts)

Quick-start combos, grouped by scenario. Use `--preset <name>` or recommend during Step 2.

**Knowledge & Learning**:

| Preset | Style | Layout | Best For |
|--------|-------|--------|----------|
| `knowledge-card` | notion | dense | 干货知识卡、概念科普 |
| `checklist` | notion | list | 清单、排行榜 |
| `concept-map` | notion | mindmap | 概念图、知识脉络 |
| `swot` | notion | quadrant | SWOT 分析、四象限 |
| `tutorial` | chalkboard | flow | 教程步骤、操作流程 |
| `classroom` | chalkboard | balanced | 课堂笔记、知识讲解 |
| `study-guide` | study-notes | dense | 学习笔记、考试重点 |
| `hand-drawn-edu` | sketch-notes | flow | 手绘教程、流程图解 |
| `sketch-card` | sketch-notes | dense | 手绘知识卡 |
| `sketch-summary` | sketch-notes | balanced | 手绘总结、图文笔记 |

**Lifestyle & Sharing**:

| Preset | Style | Layout | Best For |
|--------|-------|--------|----------|
| `cute-share` | cute | balanced | 少女风分享、日常种草 |
| `girly` | cute | sparse | 甜美封面、氛围感 |
| `cozy-story` | warm | balanced | 生活故事、情感分享 |
| `product-review` | fresh | comparison | 产品对比、测评 |
| `nature-flow` | fresh | flow | 健康流程、自然主题 |

**Impact & Opinion**:

| Preset | Style | Layout | Best For |
|--------|-------|--------|----------|
| `warning` | bold | list | 避坑指南、重要提醒 |
| `versus` | bold | comparison | 正反对比 |
| `clean-quote` | minimal | sparse | 金句、极简封面 |
| `pro-summary` | minimal | balanced | 专业总结、商务内容 |

**Trend & Entertainment**:

| Preset | Style | Layout | Best For |
|--------|-------|--------|----------|
| `retro-ranking` | retro | list | 复古排行、经典盘点 |
| `throwback` | retro | balanced | 怀旧分享 |
| `pop-facts` | pop | list | 趣味冷知识 |
| `hype` | pop | sparse | 炸裂封面、惊叹分享 |

**Poster & Editorial**:

| Preset | Style | Layout | Best For |
|--------|-------|--------|----------|
| `poster` | screen-print | sparse | 海报风封面、影评书评 |
| `editorial` | screen-print | balanced | 观点文章、文化评论 |
| `cinematic` | screen-print | comparison | 电影对比、戏剧张力 |

Full prompt-fragment definitions: `references/style-presets.md`.

## Auto-Selection

Match content signals to the best combo. First row whose keywords appear wins; fall back to `cute-share` if nothing matches.

| Signals in source | Style | Layout | Recommended preset |
|-------------------|-------|--------|--------------------|
| beauty, fashion, cute, girl, pink | `cute` | sparse/balanced | `cute-share`, `girly` |
| health, nature, fresh, organic | `fresh` | balanced/flow | `product-review`, `nature-flow` |
| life, story, emotion, warm | `warm` | balanced | `cozy-story` |
| warning, important, must, critical | `bold` | list/comparison | `warning`, `versus` |
| professional, business, elegant | `minimal` | sparse/balanced | `clean-quote`, `pro-summary` |
| classic, vintage, traditional | `retro` | balanced | `throwback`, `retro-ranking` |
| fun, exciting, wow, amazing | `pop` | sparse/list | `hype`, `pop-facts` |
| knowledge, concept, productivity, SaaS | `notion` | dense/list | `knowledge-card`, `checklist` |
| education, tutorial, learning, classroom | `chalkboard` | balanced/dense | `tutorial`, `classroom` |
| notes, handwritten, study guide, realistic | `study-notes` | dense/list/mindmap | `study-guide` |
| movie, poster, opinion, editorial, cinematic | `screen-print` | sparse/comparison | `poster`, `editorial`, `cinematic` |
| hand-drawn, infographic, workflow, 手绘，图解 | `sketch-notes` | flow/balanced/dense | `hand-drawn-edu`, `sketch-card`, `sketch-summary` |

## Style × Layout Matrix

Compatibility scores (✓✓ highly recommended, ✓ works well, ✗ avoid). Use when the user picks a non-default combo and you want to flag a poor match.

|              | sparse | balanced | dense | list | comparison | flow | mindmap | quadrant |
|--------------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| cute         | ✓✓ | ✓✓ | ✓  | ✓✓ | ✓  | ✓  | ✓  | ✓  |
| fresh        | ✓✓ | ✓✓ | ✓  | ✓  | ✓  | ✓✓ | ✓  | ✓  |
| warm         | ✓✓ | ✓✓ | ✓  | ✓  | ✓✓ | ✓  | ✓  | ✓  |
| bold         | ✓✓ | ✓  | ✓  | ✓✓ | ✓✓ | ✓  | ✓  | ✓✓ |
| minimal      | ✓✓ | ✓✓ | ✓✓ | ✓  | ✓  | ✓  | ✓  | ✓  |
| retro        | ✓✓ | ✓✓ | ✓  | ✓✓ | ✓  | ✓  | ✓  | ✓  |
| pop          | ✓✓ | ✓✓ | ✓  | ✓✓ | ✓✓ | ✓  | ✓  | ✓  |
| notion       | ✓✓ | ✓✓ | ✓✓ | ✓✓ | ✓✓ | ✓✓ | ✓✓ | ✓✓ |
| chalkboard   | ✓✓ | ✓✓ | ✓✓ | ✓✓ | ✓  | ✓✓ | ✓✓ | ✓  |
| study-notes  | ✗  | ✓  | ✓✓ | ✓✓ | ✓  | ✓  | ✓✓ | ✓  |
| screen-print | ✓✓ | ✓✓ | ✗  | ✓  | ✓✓ | ✓  | ✗  | ✓✓ |
| sketch-notes | ✓  | ✓✓ | ✓✓ | ✓✓ | ✓  | ✓✓ | ✓✓ | ✓  |

## Outline Strategies

Three differentiated approaches — each produces a structurally different outline. The workflow recommends one; Path C generates all three and lets the user choose.

| Strategy | Concept | Best for | Structure |
|----------|---------|----------|-----------|
| **A — Story-Driven** | Personal experience as the thread, emotional resonance first | Reviews, personal shares, transformation | Hook → Problem → Discovery → Experience → Conclusion |
| **B — Information-Dense** | Value-first, efficient information delivery | Tutorials, comparisons, checklists | Core conclusion → Info card → Pros/Cons → Recommendation |
| **C — Visual-First** | Visual impact as core, minimal text | High-aesthetic products, lifestyle, mood content | Hero image → Detail shots → Lifestyle scene → CTA |

## Reference Images

角色身份、整套风格和真实素材分开记录。每张有人物的页面直接传入一张凯冰 Q 版身份参考；封面同样加载它。参考负责身份与形态，当前内容决定动作和构图。

用户提供的风格图片可提取布局规律；已确认的本套封面可作为风格参考。后续页面即便无人物，也可传入封面作为风格参考，并明确只继承字体层级、颜色和边距。每页角色有无与版式由该页任务决定。

具体参考选择、传参及记录格式见 `references/kaibing-integration.md`。素材文件先核实并查看，再复制到本轮 `refs/`；真实截图按原样保留，不把生成的示意界面当作实测。

## File Layout

```
output/小红书/{YYYY-MM-DD}/{topic-slug}/
├── source-{slug}.{ext}
├── analysis.md
├── outline-strategy-{a,b,c}.md    # Path C only
├── outline.md
├── prompts/NN-{type}-{slug}.md
├── NN-{type}-{slug}.png
└── refs/                          # only if --ref used
```

**Slug**: 2-4 words, kebab-case. "AI 工具推荐" → `ai-tools-recommend`. On collision, append `-YYYYMMDD-HHMMSS`.

**Backup rule** (applies throughout): before overwriting any file — source, outline, prompt, image — rename the existing one to `<name>-backup-YYYYMMDD-HHMMSS.<ext>`. This protects user edits.

## Workflow

```
- [ ] Step 0: Load project EXTEND.md and 凯冰集成指南
- [ ] Step 1: Analyze content → analysis.md
- [ ] Step 2: Reuse confirmed decisions; clarify only material gaps
- [ ] Step 3: Generate images
- [ ] Step 4: Completion report
```

### Step 0: Load Project Preferences

读取项目 `.baoyu-skills/kaibing-xhs-images/EXTEND.md`，摘要说明风格、布局、署名、语言和后端。该文件使用原 Skill 支持的配置字段；角色绑定在集成指南中，不冒充原生配置字段。

若配置缺失，读取 [随包默认配置](references/config/default-preferences.md)，直接用于本次任务；需要保存时仅复制到项目配置路径，已有配置不覆盖。仅保存到项目目录，不查找或修改全局配置。自定义 `kaibing-editorial` 沿用 minimal 的布局兼容性。

### Step 1: Analyze Content → `analysis.md`

1. Save the source (backup rule applies if `source.md` exists).
2. Run the deep analysis in `references/workflows/analysis-framework.md`: content type, hook potential, audience, engagement signals, visual opportunity map, swipe flow.
   同时按 `references/editorial-content.md` 写清每页要回答的问题、完整解释、画面贡献和来源身份，避免将观点文章直接拆成提纲。
3. Detect source language, pick recommended image count (2-10).
4. 用户选择优先，其次采用保存的风格与布局；只有未指定的维度才用 Auto-Selection 表推荐。封面 sparse，内页 balanced 为起点，按内容选 comparison / flow / list 等，不强制统一模块网格。
5. Write everything to `analysis.md`.

### Step 2: Smart Confirm

按 Confirmation Policy 复用已确认决定，先摘要主题、核心信息、策略、风格、逐页布局、图片数和素材缺失项。当前任务的直接生成授权继续有效，只澄清真正缺失且影响结果的部分。

规划深度可选：

- **Path A — Quick**：按推荐策略生成单一 `outline.md`，适合默认快速制作。
- **Path B — Custom**：将用户已明确的风格、布局、页数和补充要求合并进单一 `outline.md`；缺失项可推荐，不重新问整套偏好。
- **Path C — Detailed**：仅在用户需要多方案时生成不同内容结构的 `outline-strategy-a/b/c.md`，按 `references/workflows/outline-template.md` 记录；用户要求统一风格时三案共享该风格。复用用户选择后保存最终 `outline.md`。

如需要尚未完成的确认，可参考 `references/confirmation.md` 中相应路径的提问格式，删去本任务已回答的项目。确认完成后生成一张样张，不因选择规划路径自动生成整套。

### Step 3: Generate Images

With confirmed outline + style + layout + palette:

**Reference consistency**: follow `references/kaibing-integration.md`. Cover and all character pages receive the real Q identity file. An approved cover can additionally guide series style; it must not determine every later pose, character presence or page layout.

Generation flow:

1. Write each selected full prompt using `references/workflows/prompt-assembly.md`; record copy, layout and actual reference roles before invoking the tool.
2. Generate one sample (cover by default, or the user's chosen interior) with its real references. Save original and 1080×1440 final, then inspect character, text and phone-size readability.
3. Show the sample and wait for review unless continuation is already authorized. A technical pass does not imply the user approved its design.
4. Generate remaining authorized pages, recording direct identity refs on each character page and style/evidence refs when applicable. Use the approved cover as style anchor once available; if an interior was reviewed first, use that as temporary style reference until the cover is approved.
5. On failure, retry only the failed item once using a saved revised prompt and a new output filename; preserve earlier candidates and report any unresolved limitation.

**Footer**: follow the exact author and page-number rule in the integration guide; enabled watermark content comes from project EXTEND.md.

**Backend selection**: use the current native image tool according to Image Generation Tools. Explicit saved or current backend choices are recommendation inputs; unsupported choices or a switch to a paid API require disclosure and the user's authorization. Do not fall through to a CLI merely for missing size or quality parameters.

### Step 4: Completion Report

```
Image Card Series Complete!

Topic: [topic]
Mode: [Quick / Custom / Detailed]
Strategy: [A/B/C/Combined]
Style: [name]
Palette: [name or "default"]
Layout: [name or "varies"]
Location: [directory]
Images: N total

✓ analysis.md
✓ outline.md
✓ outline-strategy-a/b/c.md (detailed mode only)

- 01-cover-[slug].png ✓ Cover (sparse)
- 02-content-[slug].png ✓ Content (balanced)
- ...
- NN-ending-[slug].png ✓ Ending (sparse)
```

## Content Breakdown Principles

| Position | Purpose | Typical layout |
|----------|---------|----------------|
| Cover (image 1) | Hook + visual impact | `sparse` |
| Content (middle) | Core value per image | `balanced` / `dense` / `list` / `comparison` / `flow` |
| Ending (last) | 本篇总结、问题或可用模板 | 按内容选 `balanced` / `list` / `dense` / `sparse` |

For the style × layout compatibility matrix, see the **Style × Layout Matrix** above.

## Image Modification

| Action | How |
|--------|-----|
| Edit | Update `prompts/NN-{type}-{slug}.md` **first**, then generate a new candidate using the same identity references |
| Add | Specify position, create prompt, generate, renumber subsequent files `NN+1`, update outline |
| Delete | Remove files, renumber subsequent `NN-1`, update outline |

Always update the prompt file before regenerating — it's the source of truth and makes changes reproducible.

Text correction policy:

- 整页生成中的文字错误通过修订提示词重生成；确定性文字制作采用集成指南的无字母版与真实字体完整排版分支，不在已生成文字上逐块遮盖补丁。
- For text-correction regenerations, write a new prompt file and a new output path so the flawed candidate is preserved for comparison.
- 尺寸归一使用等比缩放与白底安全放置；完整保留人物和正文。真实字体排版须从无字母版制作并记录字体，保留原图。

## References

| File | Content |
|------|---------|
| `references/confirmation.md` | Optional question formats for genuinely missing decisions |
| `references/editorial-content.md` | 内容完整性、段落密度、图文分工、场景语义与手机阅读验收 |
| `references/style-presets.md` | Full preset shortcut definitions |
| `references/presets/<style>.md` | Per-style element definitions |
| `references/palettes/<name>.md` | Per-palette color definitions |
| `references/elements/canvas.md` | Aspect ratios, safe zones, grid layouts |
| `references/elements/image-effects.md` | Cutout, stroke, filters |
| `references/elements/typography.md` | Decorated text, tags, text direction |
| `references/elements/decorations.md` | Emphasis marks, backgrounds, doodles, frames |
| `references/workflows/analysis-framework.md` | Content analysis framework |
| `references/workflows/outline-template.md` | Outline template with layout guide |
| `references/workflows/prompt-assembly.md` | Prompt assembly guide |
| `references/config/preferences-schema.md` | EXTEND.md schema |
| `references/config/first-time-setup.md` | First-time setup flow |
| `references/config/watermark-guide.md` | Watermark configuration |

## Notes

- Auto-retry once on generation failure before reporting an error.
- For sensitive public figures, use stylized cartoon alternatives.
- 复用任务中已确认的选择，Detailed mode 仅在用户需要多方案比较时使用。

## Changing Preferences

编辑项目 `.baoyu-skills/kaibing-xhs-images/EXTEND.md` 即可修改风格、布局、语言或署名。格式沿用 `references/config/preferences-schema.md`；角色身份仍以凯冰原始文档为准。本改装仅使用项目配置。
