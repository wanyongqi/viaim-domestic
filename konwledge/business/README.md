# 业务知识库说明（viaim）

> 版本：V2.1.0 | 最后更新：2026-04

本目录沉淀 viaim 产品的业务规则、功能规格与测试参考数据，供测试人员查阅和 AI 生成测试内容时引用。

---

## 一、目录结构说明

```
business/
├── README.md                          # 本文件（说明 + 完整性自查表）
│
├── product/                           # 产品层：术语定义
│   └── viaim/
│       └── glossary.md               # 术语表（记录/上云/空间/闪录等）
│
├── domain/                            # 领域规则层：跨模块共用的业务规则
│   ├── record-common-rules.md        # 记录通用规则（类型/来源/状态/卡片显示/排序/红点）
│   ├── subscription.md               # 套餐权益（Basic/Pro/Ultra 对比）
│   ├── upload-rules.md               # 上传入口、支持格式、限制、处理流程
│   ├── add-to-space-rules.md         # 添加到空间弹窗规则（冲突处理/回收站恢复优先/容量校验）
│   ├── delete-recycle-rules.md       # 删除行为、移除与删除区别、回收站规则
│   ├── export-rules.md               # 导出入口、格式差异（详情页 vs 批量）
│   ├── language-selection.md         # 语言选择弹窗（入口/单多语言/搜索/同步/付费）
│   ├── common-interaction.md         # 通用交互规则（弹窗关闭/按钮状态/防重复提交）
│   └── version-migration.md          # 新老版本数据同步（分组→空间迁移/祖父条款/示例空间）
│
├── features/                          # 功能规格层：单功能一文档
│   ├── viaim/                         # App（iOS / Android）功能规格
│   │   ├── recording/                # 4大录音功能（已拆分为子目录）
│   │   │   ├── README.md            # 入口总览：类型/耳机/功能矩阵/通用概览
│   │   │   ├── common-rules.md      # 通用规则：说话人/标记/暂停/保存/悬浮窗/画中画
│   │   │   ├── call.md              # 通话录音专属：静音/安心录/双路/佩戴提示
│   │   │   ├── translate.md         # 实时翻译与录音专属：UI/语种/播报/权限
│   │   │   └── text-live.md         # 文字直播 H5
│   │   ├── flash-record.md           # 闪录（模式/触发方式/时长上限/下载流程）
│   │   ├── record-list.md            # 记录列表功能（筛选/左滑/批量/上传入口）
│   │   ├── space.md                  # Space 空间（概念/操作/添加/置灰/排序/批量）
│   │   ├── vitana.md                 # Vitana AI 助理（入口/引用范围/大模型/对话）
│   │   ├── detail-page.md            # 详情页（三种类型/各 Tab 功能）
│   │   ├── bluetooth-headset.md      # 耳机型号与设置（5款型号差异、功能规格）
│   │   ├── bluetooth-gesture.md      # 耳机手势控制（更新弹窗规则、各型号键值）
│   │   ├── bluetooth-connect.md      # 耳机连接流程（首次/复连/MFI/国内耳机规则）
│   │   ├── account-settings.md       # 账号设置（绑定/解绑/换绑/删除账号）
│   │   ├── my-preferences.md         # 使用设置（录音/AI设置/权限/技术支持/隐私政策）
│   │   ├── widget.md                 # 小组件（Android悬浮窗/通知栏/iOS负一屏/灵动岛）
│   │   ├── search.md                 # 全局搜索
│   │   ├── message-center.md         # 消息中心（地区推送/有效期/未读角标）
│   │   └── login-register.md         # 登录注册
│   │
│   ├── viaim-web/                     # 海外 Web 端功能规格
│   │   ├── login.md                  # 登录
│   │   ├── left-sidebar-and-file-list.md # 左侧边栏与文件列表
│   │   ├── detail-page.md            # 详情页
│   │   ├── recycle-bin.md            # 回收站
│   │   ├── search.md                 # 搜索
│   │   ├── settings.md               # 设置
│   │   ├── space-grouping.md         # 空间/分组
│   │   ├── subscription.md           # 订阅
│   │   ├── billing.md                # 账单
│   │   └── upload.md                 # 上传
│   │
│   └── viaim-domestic-web/            # 国内 Web 端功能规格
│       ├── login.md                  # 登录
│       ├── left-sidebar-and-file-list.md # 左侧边栏与文件列表
│       ├── detail-page.md            # 详情页
│       ├── recycle-bin.md            # 回收站
│       ├── search.md                 # 搜索
│       ├── settings.md               # 设置
│       ├── space-grouping.md         # 空间/分组
│       ├── live-and-share.md         # 直播与分享
│       └── upload-and-capacity.md    # 上传与容量
│
├── reference-data/                    # 参考数据：结构化数据文件 + 说明文档
│   └── viaim/
│       ├── transcribe.csv            # 转写语种列表（145种，含地区变体、优先级）
│       ├── translate.csv             # 翻译语种列表（80种，无地区变体）
│       ├── 预制模版.csv              # 摘要预制模版数据
│       ├── 预制模版说明.md           # 🔲 待建：预制模版字段说明
│       └── 语种说明.md              # 🔲 待建：语种字段说明
│
└── test-focus/                        # 测试关注点
    └── viaim/
        ├── typical-defects.md         # 典型缺陷模式库（错误推测法输入）
        ├── testpoint-examples.md      # 高质量测试点样例库（格式与深度参考）
        ├── regression-focus.md        # 🔲 待建：回归关注点
        ├── risky-scenarios.md         # 🔲 待建：高风险场景
        └── platform-diff.md           # 🔲 待建：Android/iOS/Web 差异汇总
```

---

## 二、各维度说明

### product/（产品层）
- **用途**：描述产品定位、核心模块、术语定义、版本范围
- **写作原则**：面向"不了解产品的新人"，用简洁的语言说清楚"这个产品是什么"
- **引用场景**：AI 生成测试点时作为背景知识，避免对业务概念产生误解

### domain/（领域规则层）
- **用途**：沉淀跨模块、跨功能的共用业务规则
- **写作原则**：以表格为主，明确列出规则条件和结论；避免模糊描述
- **引用场景**：涉及删除/导出/套餐/上传等通用逻辑时，AI 直接引用此层

### features/（功能规格层）
- **用途**：描述单个功能模块的完整规格（入口/触发条件/交互逻辑/边界值）
- **写作原则**：按功能入口组织，覆盖正向流程、边界条件、型号/套餐差异
- **引用场景**：生成某功能测试点/用例时，AI 引用对应功能文档

### reference-data/（参考数据层）
- **用途**：存放结构化参考数据（CSV）及其说明文档（Markdown）
- **写作原则**：CSV 存原始数据，对应的 `说明.md` 解释字段含义和使用方式
- **引用场景**：需要语种列表、预制模版数据时引用

### test-focus/（测试关注点层）
- **用途**：沉淀回归重点、高风险场景、平台差异等测试经验
- **写作原则**：来源于测试过程中发现的规律，持续更新
- **引用场景**：版本回归、风险评估、制定测试策略时引用

---

## 三、完整性自查表

### 已完成（✅）

**领域规则**

| 文件 | 状态 | 说明 |
|------|------|------|
| `product/viaim/glossary.md` | ✅ | 术语表（含双路/单路通话录音） |
| `domain/record-common-rules.md` | ✅ | 记录通用规则（类型/来源/状态/卡片显示/排序/红点/时间格式）|
| `domain/subscription.md` | ✅ | 套餐权益（含转写时长扣除机制、AI模型权限、降级行为、升级弹窗交互）|
| `domain/upload-rules.md` | ✅ | 上传规则（含空间容量占用、校验优先级、多端并发服务端兜底）|
| `domain/add-to-space-rules.md` | ✅ | 添加到空间弹窗（冲突处理/回收站恢复优先/容量校验/弹窗优先级）|
| `domain/delete-recycle-rules.md` | ✅ | 删除与回收站（含移除弹窗勾选逻辑、置灰规则）|
| `domain/export-rules.md` | ✅ | 导出规则（含50条上限、命名规则、进度弹窗）|
| `domain/language-selection.md` | ✅ | 语言选择弹窗（入口/单多语言/搜索/推荐/同步/付费）|
| `domain/common-interaction.md` | ✅ | 通用交互规则（弹窗关闭方式/按钮状态/防重复提交）|
| `domain/version-migration.md` | ✅ | 新老版本数据同步（分组→空间/祖父条款/示例空间）|

**App（iOS / Android）功能规格**

| 文件 | 状态 | 说明 |
|------|------|------|
| `features/viaim/recording/` | ✅ | 4大录音（README 总览 + common-rules 通用规则 + call 通话专属 + translate 同传专属 + text-live 文字直播）|
| `features/viaim/flash-record.md` | ✅ | 闪录 |
| `features/viaim/record-list.md` | ✅ | 记录列表功能（筛选/左滑/批量操作/上传入口）|
| `features/viaim/space.md` | ✅ | Space 空间（添加冲突规则、快捷方式置灰、容量占用、批量操作）|
| `features/viaim/vitana.md` | ✅ | Vitana AI 助理（入口、引用范围、大模型权限、对话功能）|
| `features/viaim/detail-page.md` | ✅ | 详情页 |
| `features/viaim/bluetooth-headset.md` | ✅ | 耳机型号与设置（含语音指令清单、手势控制固件限制、录音提示音）|
| `features/viaim/bluetooth-gesture.md` | ✅ | 耳机手势控制（更新弹窗规则、各型号键值）|
| `features/viaim/bluetooth-connect.md` | ✅ | 耳机连接流程（首次/复连/MFI/国内耳机/封禁规则）|
| `features/viaim/account-settings.md` | ✅ | 账号与设置（含绑定/换绑/解绑邮箱手机三方、设置/修改密码、删除账号各场景规则）|
| `features/viaim/my-preferences.md` | ✅ | 使用设置（录音/AI设置/权限/技术支持/隐私政策）|
| `features/viaim/widget.md` | ✅ | 小组件 |
| `features/viaim/search.md` | ✅ | 全局搜索 |
| `features/viaim/message-center.md` | ✅ | 消息中心 |
| `features/viaim/login-register.md` | ✅ | 登录注册 |

**海外 Web 端功能规格**

| 文件 | 状态 | 说明 |
|------|------|------|
| `features/viaim-web/login.md` | ✅ | 登录 |
| `features/viaim-web/left-sidebar-and-file-list.md` | ✅ | 左侧边栏与文件列表 |
| `features/viaim-web/detail-page.md` | ✅ | 详情页 |
| `features/viaim-web/recycle-bin.md` | ✅ | 回收站 |
| `features/viaim-web/search.md` | ✅ | 搜索 |
| `features/viaim-web/settings.md` | ✅ | 设置 |
| `features/viaim-web/space-grouping.md` | ✅ | 空间/分组 |
| `features/viaim-web/subscription.md` | ✅ | 订阅 |
| `features/viaim-web/billing.md` | ✅ | 账单 |
| `features/viaim-web/upload.md` | ✅ | 上传 |

**国内 Web 端功能规格**

| 文件 | 状态 | 说明 |
|------|------|------|
| `features/viaim-domestic-web/login.md` | ✅ | 登录 |
| `features/viaim-domestic-web/left-sidebar-and-file-list.md` | ✅ | 左侧边栏与文件列表 |
| `features/viaim-domestic-web/detail-page.md` | ✅ | 详情页 |
| `features/viaim-domestic-web/recycle-bin.md` | ✅ | 回收站 |
| `features/viaim-domestic-web/search.md` | ✅ | 搜索 |
| `features/viaim-domestic-web/settings.md` | ✅ | 设置 |
| `features/viaim-domestic-web/space-grouping.md` | ✅ | 空间/分组 |
| `features/viaim-domestic-web/live-and-share.md` | ✅ | 直播与分享 |
| `features/viaim-domestic-web/upload-and-capacity.md` | ✅ | 上传与容量 |

**参考数据 & 测试关注点**

| 文件 | 状态 | 说明 |
|------|------|------|
| `reference-data/viaim/transcribe.csv` | ✅ | 转写语种列表（145种，含变体、优先级）|
| `reference-data/viaim/translate.csv` | ✅ | 翻译语种列表（80种，无变体）|
| `reference-data/viaim/预制模版.csv` | ✅ | 摘要预制模版数据 |
| `test-focus/viaim/typical-defects.md` | ✅ | 典型缺陷模式库 |
| `test-focus/viaim/testpoint-examples.md` | ✅ | 高质量测试点样例库 |

### 待补充（🔲）

| 文件 | 优先级 | 待补充内容 |
|------|--------|-----------|
| `product/viaim/overview.md` | ⭐⭐ | 产品概述与核心模块 |
| `product/viaim/scope.md` | ⭐⭐ | 版本与平台范围（iOS/Android/版本号）|
| `features/viaim/message-center.md` 消息类型 | ⭐⭐⭐ | 具体消息类型详细内容 |
| `reference-data/viaim/预制模版说明.md` | ⭐⭐ | 预制模版字段含义与使用方式 |
| `reference-data/viaim/语种说明.md` | ⭐⭐ | 语种字段说明 |
| `test-focus/viaim/regression-focus.md` | ⭐⭐⭐ | 回归测试关注点 |
| `test-focus/viaim/risky-scenarios.md` | ⭐⭐⭐ | 高风险场景清单 |
| `test-focus/viaim/platform-diff.md` | ⭐⭐⭐ | Android / iOS / Web 差异汇总 |

---

## 四、维护规范

1. **新增功能**：在 `features/viaim/` 下新建对应 `.md` 文件，同步更新本自查表和 `../README.md`
2. **业务规则变更**：直接修改对应文档，在文件顶部更新「最后更新」日期
3. **已确认修正**：不删除原内容，使用删除线标注（如 `~~旧内容~~`）并注明「已取消/已修正」
4. **数据文件更新**：CSV 覆盖替换，对应说明 `.md` 同步更新字段变化说明
5. **知识库同步**：每次 AI 对话中确认的业务规则，需在下次工作时补录到对应文档

---

## 五、AI 使用指引

生成测试内容时，按以下优先级引用文档：

| 优先级 | 文档层 | 说明 |
|--------|--------|------|
| 1（最高）| `features/` | 目标功能的具体规格 |
| 2 | `domain/` | 涉及的通用业务规则（删除/导出/套餐等）|
| 3 | `product/` | 产品背景与术语定义 |
| 4 | `reference-data/` | 需要具体数据时（语种列表/模版数据）|
| 5 | `test-focus/` | 风险识别与回归策略 |

**生成前必读**：
- 套餐差异 → 必读 `domain/subscription.md`
- 涉及添加到空间/冲突弹窗/回收站恢复优先 → 必读 `domain/add-to-space-rules.md`
- 涉及删除/移除 → 必读 `domain/delete-recycle-rules.md`
- 涉及导出 → 必读 `domain/export-rules.md`
- 涉及记录卡片显示/排序/红点/类型/状态 → 必读 `domain/record-common-rules.md`
- 涉及记录列表筛选/左滑/批量/上传入口 → 必读 `features/viaim/record-list.md`
- 涉及 Space → 必读 `features/viaim/space.md`
- 涉及 Vitana AI 助理 → 必读 `features/viaim/vitana.md`
- 涉及语言选择/语种切换/多语言付费 → 必读 `domain/language-selection.md`
- 涉及新老版本迁移/祖父条款 → 必读 `domain/version-migration.md`
- 涉及转写时长扣除/返还/AI模型权限 → 必读 `domain/subscription.md`（第四、五、六节）
- 涉及上传时空间容量占用/校验优先级 → 必读 `domain/upload-rules.md`（第八、九、十节）
- 涉及录音功能 → 必读 `features/viaim/recording/README.md`（入口），按需读 `common-rules.md`、`call.md`、`translate.md`
- 涉及文字直播 H5 → 必读 `features/viaim/recording/text-live.md`
- 涉及耳机型号/设置差异 → 必读 `features/viaim/bluetooth-headset.md`
- 涉及耳机手势控制/键值配置 → 必读 `features/viaim/bluetooth-gesture.md`
- 涉及耳机连接流程/权限/复连 → 必读 `features/viaim/bluetooth-connect.md`
