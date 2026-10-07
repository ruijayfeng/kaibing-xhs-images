---
version: 1
watermark:
  enabled: true
  content: "凯冰"
  position: bottom-right
preferred_style:
  name: kaibing-editorial
  description: "沿用 minimal 的清晰层级与留白；中文白底编辑排版，少装饰，封面醒目，内页保留完整解释与具体例子，凯冰按内容参与。"
preferred_layout: null
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
    visual_elements: "内容关系决定视觉中心、空间组织与阅读路线；Q 版人物按当前事件参与提问、选择或验证；真实截图保留证据；颜色以角色参考为准；克制作者页脚与页码。"
    typography: "清楚的中文无衬线体系，封面大标题；内页标题贴近正文尺度、明显小于封面，长标题自然换行；正文保留完整段落并在手机宽度可读；制作按集成与内容表达规则执行。"
    best_for: "AI 科技内容、工具介绍、知识解释、操作教程与真实体验分享"
---

角色加载、作者页码组合与样张规则见项目 Skill 的 references/kaibing-integration.md。它们属于本地改装规则，不新增原版 EXTEND schema 字段。

视觉参考与认可范围：references/approved-style.md；保留2026-10-04样例，当前按2026-10-07确认的方向与内容表达规则制作。

正式发布图片偏好（2026-10-06 用户确认）：图片左下角不出现“概念示例”“非实际产品测试”等制作或测试说明。正式成品默认仅保留克制的作者页脚；素材来源、概念示意与实测结果的区别记录在内部制作资料中，不自动写到画面上。正文仍须准确表达，不将绘制示意描述为真实测试结果。
