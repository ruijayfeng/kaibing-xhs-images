---
version: 1
watermark:
  enabled: true
  content: "凯冰"
  position: bottom-right
preferred_style:
  name: kaibing-editorial
  description: "沿用 minimal 的清晰层级与留白；中文白底编辑排版，少装饰，标题清楚，不堆 Emoji。封面醒目，内页有具体信息，凯冰按内容参与。"
preferred_layout: balanced
language: zh
preferred_image_backend: auto
generation_batch_size: 1
custom_styles:
  - name: kaibing-editorial
    description: "minimal 的凯冰项目定制风格：白底杂志排版与内容型 Q 版人物，封面与内页有不同信息密度。"
    color_palette:
      primary: ["#292929"]
      background: "#FFFFFF"
      accents: ["#9F4140", "#A6C9DE"]
    visual_elements: "一个清楚的视觉中心，必要的简洁物件与细线；Q 版人物按页面任务出现，步骤与截图页优先信息；颜色以角色参考为准；克制作者页脚与页码。"
    typography: "清楚的中文无衬线体系，封面大标题；内页标题默认单行、明显小于封面，正文手机宽度可读；真实字体制作按集成指南执行。"
    best_for: "AI 科技内容、工具介绍、知识解释、操作教程与真实体验分享"
---

角色加载、作者页码组合与样张规则见项目 Skill 的 references/kaibing-integration.md。它们属于本地改装规则，不新增原版 EXTEND schema 字段。

已确认默认视觉参考：references/approved-style.md（凯冰白底编辑图文 v1，2026-10-04 用户确认）。
