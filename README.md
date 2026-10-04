# 凯冰小红书图文 · Kaibing XHS Images

将文章、观点或工具素材制作成带凯冰 IP 的小红书封面与图文卡片。基于 baoyu-xhs-images 2.0.1 改装，默认使用已确认的「凯冰白底编辑图文 v1」。

这是供 AI 助手读取和执行的 Skill。实际出图需要当前环境提供支持参考图的图像工具。

## 已确认效果

封面大标题；内页标题克制、正文有具体信息。白底、深灰文字、暗红强调、冰蓝辅助。凯冰使用 Q 版，按内容任务出现；署名与页码统一。

<p>
<img src="kaibing-xhs-images/assets/approved-style-v1/01-封面.png" width="240" alt="封面：AI 做完了，你看懂了吗？">
<img src="kaibing-xhs-images/assets/approved-style-v1/03-选择解释形式.png" width="240" alt="内页：根据理解障碍选择解释形式">
<img src="kaibing-xhs-images/assets/approved-style-v1/06-检验理解.png" width="240" alt="内页：凯冰参与理解检验">
</p>

随包保留完整 8 页确认样例，用于按页面任务选择视觉参考。新文章的页数、文案、版式与角色动作重新规划。

## 可以做什么

- 从内容提炼主线、读者目标和封面钩子，安排 2–10 页图文；页数也可由用户指定。
- 制作 3:4 封面与内页，交付 1080×1440 图片、配文、提示词和生成记录。
- 用实际 Q 版身份图片锁定凯冰，以确认样例指导视觉系统。
- 根据页面任务选择对比、流程、清单、规则或模板；真实截图与证据页优先保留信息。
- 保留原版 12 种风格、8 种布局供明确选择，默认采用凯冰白底编辑风格。

## 项目级安装

在目标项目目录执行：

```bash
git clone https://github.com/ruijayfeng/kaibing-xhs-images.git
mkdir -p .agents/skills
cp -R kaibing-xhs-images/kaibing-xhs-images .agents/skills/
```

只安装 `kaibing-xhs-images/` 这个目录；不要把整个仓库当作 Skill 目录。已有同名 Skill 时先备份再更新。重新载入项目或开启新会话，让助手发现 Skill。

偏好文件读取路径为 `.baoyu-skills/kaibing-xhs-images/EXTEND.md`。新项目没有该文件时，Skill 使用[随包默认偏好](kaibing-xhs-images/references/config/default-preferences.md)；需要保存时复制到项目配置位置，保留已有配置。全局配置不参与本包流程。

## 使用

先出封面：

```text
使用 $kaibing-xhs-images，把下面内容做成小红书图文。
面向 AI 科技读者，沿用固定的凯冰白底编辑风格，先出封面。

<粘贴内容>
```

直接制作整套：

```text
使用 $kaibing-xhs-images，按已确认的凯冰风格制作下面内容。
文案和整套图片一起出；重点解释原理与边界，页数按内容确定。

<粘贴内容>
```

也可以只规划不生图，或要求修改指定页面。明确授权整套时，不重复询问已经确认的偏好。

## 如何运作

材料 → 提炼主线 → 分页与文案 → 选择角色任务和布局 → 保存提示词并加载实际参考 → 生成样张或已授权整套 → 核对文字、身份与手机阅读效果 → 整理交付。

默认署名为 `凯冰 · NN / TOTAL`。封面与有人物的内页都加载原始 Q 版身份图；参考负责身份，当前内容决定动作。无人页仅使用相应风格参考。官方案例、真实结果、生成样例和概念示意分别标明。

## 出图条件与限制

- 本包已在支持 `referenced_image_paths` 的 Codex 内置图像工具上实际生成并验收八页样例；这条已测试路径没有新增 API 密钥。运行时仍需检查工具、权限与额度。
- 其他环境须先核对图像工具及参考输入能力。没有工具或不能传入角色参考时，明确报告缺失；不把新设计的近似人物当作凯冰。
- 不附带 API 服务、密钥或 CLI 出图后端。更换付费服务与配置密钥需用户授权。
- 当前样例通过整页生成制作，中文字形由模型绘制，需要逐页核对。真实字体制作属于可选分支，依赖环境中可用的排版工具与字体。
- 最终图片等比整理到 1080×1440，保留原图；人物一致性和新文案排版仍需检查。固定样例不保证所有新主题一次生成合格。
- 不包含自动发布功能。

## 目录

```text
kaibing-xhs-images/
├── SKILL.md
├── LICENSE
├── references/             # 分页、风格、角色、出图与验收规则
│   └── config/default-preferences.md
└── assets/
    ├── identity/           # 实际附带的一张凯冰 Q 版身份参考
    └── approved-style-v1/  # 八页确认样例与清单
```

入口：[SKILL.md](kaibing-xhs-images/SKILL.md) · [凯冰集成规则](kaibing-xhs-images/references/kaibing-integration.md) · [固定视觉基准](kaibing-xhs-images/references/approved-style.md)

本仓库只收录这一个 Skill。测试日志、备份、文章素材、其他 Skill、环境目录及个人路径均未收录。

## 来源与许可

基于 [Jim Liu / baoyu-skills](https://github.com/JimLiu/baoyu-skills)；角色来自 [KevinBee Illustrations](https://github.com/ruijayfeng/kevinbee-illustrations)。此处效果是加入凯冰 IP 后的定制版本。详见 [NOTICE.md](NOTICE.md)、[LICENSE](LICENSE) 和 `LICENSES/` 中保留的上游许可。
