# 凯冰形态与角度参考

本文件决定标准封面与正文 Q 版如何选择人物参考。凯冰的固定身份见 `ip-core.md`；隐喻、动作和构图先由文章决定。

## 两种用途

- **标准封面形态**：`assets/identity/standard/master.png` 校准脸、白帽红星、冰蓝短发、暗红开衫和成年比例。默认用于封面，也可用于标准形态展示与头肩近景。
- **正文 Q 版**：`assets/identity/article-q/master-front.png` 校准大头帽、紧凑躯干、短腿、小手和圆厚鞋。它是独立造型，不是把标准人物等比缩小。成年气质来自身份与神情，不强迫 Q 版采用标准骨架。

封面默认选标准母版；正文全身默认选 Q 版相应角度。不要用两种全身图同时约束一张正文图。封面 Q 版尚未通过视觉验收，不作为默认封面形态。

## 按角度选图

普通生成只加载最接近目标视角的一张人物图；需要额外校准脸、帽型或背影时，再补一张直接相关的参考。

| 用途 | 角度 | 图片 |
|---|---|---|
| 标准封面 | 通用 | `assets/identity/standard/master.png` |
| 标准封面 | 正面 | `assets/identity/standard/views/front.png` |
| 标准封面 | 左侧 | `assets/identity/standard/views/left-profile.png` |
| 标准封面 | 后侧 | `assets/identity/standard/views/rear-three-quarter.png` |
| 标准封面 | 背面 | `assets/identity/standard/views/back.png` |
| 正文 Q 版 | 正面 | `assets/identity/article-q/master-front.png` |
| 正文 Q 版 | 正面三分之四 | `assets/identity/article-q/views/front-three-quarter.png` |
| 正文 Q 版 | 左侧 | `assets/identity/article-q/views/left-profile.png` |
| 正文 Q 版 | 背面 | `assets/identity/article-q/views/back.png` |

标准形态近景仍以母版或相应全身视图确定肩袖与身体比例；需要更清楚地校准脸、发和帽时，才从 `assets/identity/standard/head/` 补充对应头部单图。头部图下缘含旧肩部局部且没有完整上臂，不能单独作为头肩近景的人物参考，也不决定肩袖轮廓。

帽子正面只有一枚红星；侧面仅显示透视可见的部分，背面显示帽扣。动作会改变透视和四肢压缩程度，检查跨角度识别与动作重心，不追求固定头身数字。

## 肩袖与剪影

标准母版与各角度全身图采用同一肩袖关系：骨架保持轻盈成年比例，肩峰窄而柔和；开衫仍有针织松量，但落肩线靠近自然肩点，上臂袖量与肩到臂的外轮廓收敛。近景动作或前景透视放大手臂时，仍要检查两侧肩头是否变成宽方形，不能因参考图合格而跳过最终画面验收。正文 Q 版按自身结构验收，不借用标准形态的骨架。

参考图不提供默认姿势、隐喻物件或版式。先定当前文章的事件，再确定人物视角、重心、接触点和表情；只有实际出现身份漂移时才增加参考。
