# Xiaohongshu Outline Template

Template for generating infographic series outlines with layout specifications.

## File Naming

Outline files use strategy identifier in the name:
- `outline-strategy-a.md` - Story-driven variant
- `outline-strategy-b.md` - Information-dense variant
- `outline-strategy-c.md` - Visual-first variant
- `outline.md` - Final selected (copied from chosen variant)

## Image File Naming

Images use meaningful slugs for readability:
```
NN-{type}-[slug].png
NN-{type}-[slug].md (in prompts/)
```

| Type | Usage |
|------|-------|
| `cover` | First image (cover) |
| `content` | Middle content images |
| `ending` | Last image |

**Examples**:
- `01-cover-ai-tools.png`
- `02-content-why-ai.png`
- `03-content-chatgpt.png`
- `04-content-midjourney.png`
- `05-content-notion-ai.png`
- `06-ending-summary.png`

**Slug rules**:
- Derived from image content (kebab-case)
- Must be unique within the series
- Keep short but descriptive (2-4 words)

## Layout Selection Guide

### Density-Based Layouts

下表的条目数与留白比例仅作布局起点。凯冰白底编辑图文按[内容表达规则](../editorial-content.md)决定正文密度，允许连续段落与完整解释，不以固定行数或比例截断内容。

| Layout | When to Use | Info Points | Whitespace |
|--------|-------------|-------------|------------|
| sparse | Covers, quotes, impact statements | 1-2 | 60-70% |
| balanced | Standard content, tutorials | 3-4 | 40-50% |
| dense | Knowledge cards, cheat sheets | 5-8 | 20-30% |

### Structure-Based Layouts

| Layout | When to Use | Structure |
|--------|-------------|-----------|
| list | Rankings, checklists, steps | Numbered/bulleted vertical |
| comparison | Before/after, pros/cons | Left vs right split |
| flow | Processes, timelines | Connected nodes with arrows |

### Position-Based Recommendations

| Position | Recommended | Reasoning |
|----------|-------------|-----------|
| Cover | sparse | Maximum impact, clear title |
| Setup | balanced | Context without overwhelming |
| Core | balanced/dense/list | Match content density |
| Payoff | balanced/list | Clear takeaways |
| Ending | balanced/list/dense/sparse | Match the actual conclusion, question or reusable template |

## Outline Format

```markdown
# Xiaohongshu Infographic Series Outline

---
strategy: a  # a, b, or c
name: Story-Driven
style: notion
default_layout: dense
image_count: 6
generated: YYYY-MM-DD HH:mm
---

## Image 1 of 6

**Position**: Cover
**Layout**: sparse
**Hook**: 打工人必看！
**Slug**: ai-tools
**Filename**: 01-cover-ai-tools.png

**Text Content**:
- Title: 「5个AI神器让你效率翻倍」
- Subtitle: 亲测好用，建议收藏

**Visual Concept**:
科技感背景，多个AI工具图标环绕，中心大标题，
霓虹蓝+深色背景，未来感十足

**Swipe Hook**: 第一个就很强大👇

---

## Image 2 of 6

**Position**: Content
**Layout**: balanced
**Core Message**: 为什么你需要AI工具
**Slug**: why-ai
**Filename**: 02-content-why-ai.png

**Text Content**:
- Title: 「为什么要用AI？」
- Points:
  - 重复工作自动化
  - 创意辅助不卡壳
  - 效率提升10倍

**Visual Concept**:
对比图：左边疲惫打工人，右边轻松使用AI的人
科技线条装饰，简洁有力

**Swipe Hook**: 接下来是具体工具推荐👇

---

## Image 3 of 6

**Position**: Content
**Layout**: dense
**Core Message**: ChatGPT使用技巧
**Slug**: chatgpt
**Filename**: 03-content-chatgpt.png

**Text Content**:
- Title: 「ChatGPT」
- Subtitle: 最强AI助手
- Points:
  - 写文案：给出框架，秒出初稿
  - 改文章：润色、翻译、总结
  - 编程：写代码、找bug
  - 学习：解释概念、出题练习

**Visual Concept**:
ChatGPT logo居中，四周放射状展示功能点
深色科技背景，霓虹绿点缀

**Swipe Hook**: 下一个更适合创意工作者👇

---

## Image 4 of 6

**Position**: Content
**Layout**: dense
**Core Message**: Midjourney绘图
**Slug**: midjourney
**Filename**: 04-content-midjourney.png

**Text Content**:
- Title: 「Midjourney」
- Subtitle: AI绘画神器
- Points:
  - 输入描述，秒出图片
  - 风格多样：写实/插画/3D
  - 做封面、做头像、做素材
  - 不会画画也能当设计师

**Visual Concept**:
展示几张MJ生成的不同风格图片
画框/画布元素装饰

**Swipe Hook**: 还有一个效率神器👇

---

## Image 5 of 6

**Position**: Content
**Layout**: balanced
**Core Message**: Notion AI笔记
**Slug**: notion-ai
**Filename**: 05-content-notion-ai.png

**Text Content**:
- Title: 「Notion AI」
- Subtitle: 智能笔记助手
- Points:
  - 自动总结长文
  - 头脑风暴出点子
  - 整理会议记录

**Visual Concept**:
Notion界面风格，简洁黑白配色
展示笔记整理前后对比

**Swipe Hook**: 最后总结一下👇

---

## Image 6 of 6

**Position**: Ending
**Layout**: sparse
**Core Message**: 总结与互动
**Slug**: summary
**Filename**: 06-ending-summary.png

**Text Content**:
- Title: 「工具只是工具」
- Subtitle: 关键是用起来！
- CTA: 收藏备用 | 转发给需要的朋友
- Interaction: 你最常用哪个？评论区见👇

**Visual Concept**:
简洁背景，大字标题
底部互动引导文字
收藏/分享图标

---
```

## Swipe Hook Strategies

Transitions are optional. For the Kaibing editorial default, prefer the next question in the argument over generic teaser copy; examples below are format references, not required image text:

| Strategy | Example |
|----------|---------|
| Teaser | "第一个就很强大👇" |
| Numbering | "接下来是第2个👇" |
| Superlative | "下一个更厉害👇" |
| Question | "猜猜下一个是什么？👇" |
| Promise | "最后一个最实用👇" |
| Urgency | "最重要的来了👇" |

## Strategy Differentiation

Three strategies should differ meaningfully:

| Strategy | Focus | Structure | Page Count |
|----------|-------|-----------|------------|
| A: Story-Driven | Emotional, personal | Hook→Problem→Discovery→Experience→Conclusion | 4-6 |
| B: Information-Dense | Factual, structured | Core→Info Cards→Comparison→Recommendation | 3-5 |
| C: Visual-First | Atmospheric, minimal text | Hero→Details→Lifestyle→CTA | 3-4 |

**Example for "AI工具推荐"**:
- `outline-strategy-a.md`: Warm + Balanced - Personal journey with AI
- `outline-strategy-b.md`: Notion + Dense - Knowledge card style
- `outline-strategy-c.md`: Minimal + Sparse - Sleek tech aesthetic


## 凯冰改装补充

上面的条目格式和布局词汇可供描述；位置推荐不决定实际构图，示例文案与视觉描述仅说明格式，不作为当前文章事实或默认科技配色。默认项目风格以 EXTEND.md 为准。

每页规划时补充下面项目；真实素材缺失在规划中写“待补”，人物缺席写“无人物，仅保留署名”。完整段落与清单都可用于Text Content，不把例子里的Points当作强制结构。

- **Page Question / Complete Copy**：本页回答的问题与准确完整文案，保留必要理由、例子、条件或后果。
- **Visual Contribution / Composition**：画面让读者看见什么，与正文如何分工；具体写清内容关系、视觉中心、空间安排与阅读路线，而不只填一个布局名称。
- **Character**：q / none；如出现，写所经历的事件、动作、目光、接触点和移除后失去的理解线索。
- **References**：实际身份 / 风格 / 证据文件与各自用途。
- **Evidence Status**：官方案例 / 本轮实际结果 / 概念示意 / 待补素材。
- **Render Mode**：full-card / real-font，按集成指南选择。
- **Review Focus**：本页特有的状态、选择结果、方向与来源检查，以及手机宽度阅读重点；结合整套检查重复构图是否有内容理由。

`Complete Copy` 对应本页的 `Text Content`，完整文案只在 `Text Content` 维护，不另存第二份。`Text Content` 是上图文字；`Evidence Status` 与其他制作字段按集成指南留在记录中。确需上图帮助读者判断素材时，可加 `Reader Disclosure`（该句原文）与 `Disclosure Reason`（必要原因）；不为普通插画自动填这两项。

不额外凑固定页数或自动追加品牌尾页，按内容选择每页布局；样张检查后按当前任务授权继续，已明确授权整套时不重复询问。

封面页在 `Visual Concept` 中增加 `Cover Brief`，内容按 [封面构思](../cover-concept.md#保存和检查) 记录；普通内页不必填写。封面的 sparse 表示信息集中，不强制大片留白或固定人物大小。
