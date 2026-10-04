# 凯冰：角色唯一真值

本文只定义凯冰是谁。画幅、构图、文章标注和输出规则由对应场景文件决定，不要写回这里。

## 核心身份

凯冰是一位清新、安静、有主见的日系休闲少女。她略带距离感和倔强，但不冷酷；Q 版可以有显幼态的视觉比例，性格不因此变成撒娇或甜腻的儿童角色。

她没有固定职业。进入文章配图时，她可以经历、观察、选择、跟随、靠近或影响抽象世界，但不是内容助理、维修员、现场操作员或服务者。

## 识别优先级

1. 略有生活感的白色棒球帽，正面一枚清晰、居中的红色五角星。
2. 冰蓝色、耳下至下巴长度的轻盈短发，发梢稍向外。
3. 柔和暗红色针织开衫形成稳定红色色块。
4. 克制的红橙色眼睛与平静、专注的表情。
5. 象牙白上衣、藏青 A 字短裙、深灰短袜和浅色休闲鞋。

任何画幅至少清楚保留前三项。红星白帽是第一识别点，但必须是休闲棒球帽，不得变成军帽或制服帽。

## 默认形态

### 正文形态

- 使用正文 Q 版形象：大头帽、紧凑躯干、短腿、小手和可自然活动的关节。显幼态的视觉比例、圆厚膝盖或鞋可以成立。
- Q 感来自内部造型重构及同步简化的服装，不是把标准形象整体缩小。肩线窄而柔和，开衫保留轻松的针织体量，不撑成宽方形。
- 开衫下摆在高胯附近，裙摆在大腿中上段；帽、发、脸、红色衣块和动作关系在不同角度保持一致。
- 常规视角使用 `assets/identity/article-q/master-front.png`；特殊角度使用 `assets/identity/article-q/views/` 中的对应单图。标准形态母版用于身份核对，不与正文 Q 版全身图默认混载。

### 标准形态

- 约 5–5.5 头身。
- 可增加发丝、服装结构和表情细节，但保持轻盈、休闲。
- 文章封面当前默认采用这一形态：允许近景突出脸、自然肩颈、手势和衣服材质，保持成年身体比例；不从正文 Q 版推导封面身体。
- 使用 `assets/identity/standard/master.png` 作为标准形象身份母版；角度结构按 `references/character-model.md` 选择对应视图。

两种形态是同一角色，正文 Q 版允许明显重构头身与四肢。年龄感不由头身数字判定；优先保住凯冰的识别特征、安静独立的气质与动作可读性。

## 默认服装

- 白色红星棒球帽。
- 象牙白或浅米色圆领宽松上衣。
- 腰部至胯部长度的柔和暗红色针织开衫；轻微落肩、自然松量的袖子、简单罗纹、完整下摆。开衫可以柔软，但上臂外轮廓不应把肩膀撑成方形宽块。
- 藏青或炭灰 A 字短裙；动作幅度较大时可替换为同色宽松短裤。
- 深灰短袜。
- 米白或浅灰系带休闲鞋，深炭灰鞋底。

服装可以因季节和场景产生小幅变化，但不得同时改变帽子、发型和红色色块。

## 性格与表情

常用表情：平静、专注、轻微疑惑、若有所思、小幅开心、轻微无奈、安静倔强、平和满足。

避免大哭大喊、星星眼、夸张害羞、颜艺、战斗怒容和持续面无表情。

## 自然动作

适合：站、走、坐、蹲、靠、回头、探身、踮脚、观察、等待、思考、跟随、保持平衡、抱住、牵住、推开、轻拉、扶起、接住或放下。

修理、分拣、操作机器等动作只有在文章隐喻确实要求时才出现，不能沉淀为她的职业身份。

## 默认禁止

- 刀、剑、剑鞘、枪械或其他武器。
- 战斗服、战术腰带、颈圈、重甲、长斗篷、破损披风和厚重军靴。
- 军事、女仆、职业制服、服务人员或工具人造型。
- 偶像、甜妹、无人物行动能力的圆团吉祥物、表情包或粉色公主风。
- 英雄落地、迎战、冲锋、警戒等战斗构图。
- “赤星”或 `CHIXING`；角色名始终是“凯冰”或 `KevinBee`。

旧战斗版本属于历史或特殊世界观形态，不进入默认生成上下文。

## 提示词身份片段

需要文字描述身份时，从本段取用，不在其他文件维护第二份版本：

```text
KevinBee, the same calm independent Japanese-casual illustrated character in a distinctly redesigned strong-chibi editorial form: an oversized lived-in white baseball cap with one clear centered red five-point star, airy chin-length ice-blue bob hair, restrained red-orange eyes, a compact torso, short rounded movable limbs and small hands, a muted dark-red short knit cardigan, ivory crew-neck top, navy A-line skirt, charcoal ankle socks, and light casual sneakers. Her visual proportions may be childlike in chibi style; she remains a complete character with no fixed occupation or mascot behavior.
```
