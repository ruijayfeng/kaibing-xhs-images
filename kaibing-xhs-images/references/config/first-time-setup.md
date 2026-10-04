# 凯冰项目偏好初始化

项目配置路径为 `.baoyu-skills/kaibing-xhs-images/EXTEND.md`，格式见 `preferences-schema.md`。只使用项目路径。

本项目已确认中文、白底 minimal 编辑风格、balanced 内页、封面与内页 Q 版角色、轻量凯冰署名，具体集成规则见 `references/kaibing-integration.md`。配置已存在时直接读取，不重新提问。

配置缺失时读取同目录的 [default-preferences.md](default-preferences.md)，直接用于本次任务；需要保存时复制到项目配置路径，已有配置不覆盖。仅保存原 schema 支持的字段：watermark、preferred_style、preferred_layout、language、preferred_image_backend、generation_batch_size、custom_styles、version。新增角色绑定保存在集成指南，不添加不受支持的字段。

当用户明确调整偏好时，只修改本项目配置中对应项。缺少主题或素材只在本次内容工作中澄清，不触发一轮偏好初始化。
