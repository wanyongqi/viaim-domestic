# 知识库索引

本目录为 viaim 项目知识库，沉淀业务说明、测试规范与标准，便于团队查阅和 AI 生成测试内容时引用。

> 最后更新：2026-04

---

## 目录结构

```
konwledge/
├── README.md                              # 本文件（总索引）
├── business/
│   ├── README.md                          # 业务知识库说明 + 完整性自查表
│   ├── product/                           # 产品层（术语/定义）
│   │   └── viaim/
│   │       └── glossary.md               ✅ 术语表（记录/上云/空间/闪录等）
│   │
│   ├── domain/                            # 领域规则层（跨模块共用规则）
│   │   ├── record-common-rules.md        ✅ 记录通用规则（类型/来源/状态/卡片显示/排序/红点/时间格式）
│   │   ├── subscription.md               ✅ 套餐权益 + 转写时长扣除 + AI模型权限 + 降级行为 + 升级弹窗
│   │   ├── viaim-domestic.md             ✅ 国内版专属规则（云空间开/关、无套餐层级、AI权限）
│   │   ├── upload-rules.md               ✅ 上传入口、格式、限制、流程、空间容量占用、校验优先级
│   │   ├── add-to-space-rules.md         ✅ 添加到空间弹窗（冲突处理/回收站恢复优先/容量校验）
│   │   ├── delete-recycle-rules.md       ✅ 删除行为与回收站规则（保留30天）
│   │   ├── export-rules.md               ✅ 导出入口、格式差异（详情页 vs 批量）
│   │   ├── language-selection.md         ✅ 语言选择弹窗（入口/单多语言/搜索/同步/付费）
│   │   ├── common-interaction.md         ✅ 通用交互规则（弹窗关闭/按钮状态/防重复提交）
│   │   └── version-migration.md          ✅ 新老版本数据同步（分组→空间/祖父条款/示例空间）
│   │
│   ├── features/                          # 功能规格层（单功能一文档）
│   │   ├── viaim/                         # 海外版 App（iOS / Android）功能规格
│   │   │   ├── recording/                   4大录音功能（拆分为子目录）
│   │   │   │   ├── README.md            ✅ 入口总览：类型/耳机/功能矩阵/通用概览
│   │   │   │   ├── common-rules.md      ✅ 通用规则：说话人/标记/暂停/保存/悬浮窗/画中画
│   │   │   │   ├── call.md              ✅ 通话录音专属：静音/安心录/双路/佩戴提示
│   │   │   │   ├── translate.md         ✅ 实时翻译与录音专属：UI/语种/播报/权限
│   │   │   │   └── text-live.md         ✅ 文字直播 H5
│   │   │   ├── flash-record.md           ✅ 闪录与下载（模式/触发/时长上限）
│   │   │   ├── record-list.md            ✅ 记录列表功能（筛选/左滑/批量/上传入口）
│   │   │   ├── space.md                  ✅ Space 空间（概念/操作/添加/置灰/排序/批量）
│   │   │   ├── vitana.md                 ✅ Vitana AI 助理（入口/引用范围/大模型/对话）
│   │   │   ├── detail-page.md            ✅ 详情页（三种类型/各Tab功能）
│   │   │   ├── bluetooth-headset.md      ✅ 耳机型号与设置（5款型号差异、功能规格）
│   │   │   ├── bluetooth-gesture.md      ✅ 耳机手势控制（更新弹窗规则、各型号键值）
│   │   │   ├── bluetooth-connect.md      ✅ 耳机连接流程（首次/复连/MFI/国内耳机规则）
│   │   │   ├── account-settings.md       ✅ 账号设置（绑定/解绑/换绑/删除账号）
│   │   │   ├── my-preferences.md         ✅ 使用设置（录音/AI设置/权限/技术支持/隐私政策）
│   │   │   ├── widget.md                 ✅ 小组件（Android悬浮窗/通知栏/iOS负一屏/灵动岛）
│   │   │   ├── search.md                 ✅ 全局搜索（点击触发/类型筛选/空结果）
│   │   │   ├── message-center.md         ✅ 消息中心（地区推送/有效期/未读角标）
│   │   │   └── login-register.md         ✅ 登录注册
│   │   │
│   │   ├── viaim-domestic/                # 国内版 App（iOS / Android）功能规格
│   │   │   ├── recording/                   4大录音功能
│   │   │   │   ├── README.md            ✅ 入口总览：类型/耳机/功能矩阵/通用概览
│   │   │   │   ├── common-rules.md      ✅ 通用规则：说话人/标记/暂停/保存/悬浮窗/画中画
│   │   │   │   ├── call.md              ✅ 通话录音专属：静音/安心录/双路/佩戴提示
│   │   │   │   ├── translate.md         ✅ 实时翻译与录音专属：UI/语种（仅中英）/播报/权限
│   │   │   │   └── text-live.md         ✅ 文字直播 H5
│   │   │   ├── flash-record.md           ✅ 闪录与下载（模式/触发/时长上限）
│   │   │   ├── record-list.md            ✅ 录音记录列表（筛选/左滑/批量，无上传入口）
│   │   │   ├── home.md                   🔲 首页（待补充内容）
│   │   │   ├── discover.md               🔲 发现页（待补充内容）
│   │   │   ├── wanmu-vitana.md           ✅ 万姆/Vitana AI 助理（名称/入口/引用范围/对话）
│   │   │   ├── detail-page.md            ✅ 详情页（两种类型/各Tab功能，无文档类型）
│   │   │   ├── bluetooth-headset.md      ✅ 耳机型号与设置（型号差异、功能规格）
│   │   │   ├── bluetooth-gesture.md      ✅ 耳机手势控制（更新弹窗规则、各型号键值）
│   │   │   ├── bluetooth-connect.md      ✅ 耳机连接流程（首次/复连/MFI）
│   │   │   ├── account-settings.md       ✅ 账号设置（手机号/删除账号/深色/语言）
│   │   │   ├── my-preferences.md         ✅ 使用设置（录音/AI/云空间/权限，仅深色/中英）
│   │   │   ├── widget.md                 ✅ 小组件（Android悬浮窗/通知栏/iOS负一屏/灵动岛）
│   │   │   ├── search.md                 ✅ 全局搜索（点击触发/无文档筛选/无Space范围）
│   │   │   ├── message-center.md         ✅ 消息中心（推送/有效期/未读角标）
│   │   │   └── login-register.md         ✅ 登录注册（手机号验证码/扫码登录）
│   │   │
│   │   ├── viaim-web/                     # 海外 Web 端功能规格
│   │   │   ├── login.md                  ✅ 登录
│   │   │   ├── left-sidebar-and-file-list.md ✅ 左侧边栏与文件列表
│   │   │   ├── detail-page.md            ✅ 详情页
│   │   │   ├── recycle-bin.md            ✅ 回收站
│   │   │   ├── search.md                 ✅ 搜索
│   │   │   ├── settings.md               ✅ 设置
│   │   │   ├── space-grouping.md         ✅ 空间/分组
│   │   │   ├── subscription.md           ✅ 订阅
│   │   │   ├── billing.md                ✅ 账单
│   │   │   └── upload.md                 ✅ 上传
│   │   │
│   │   └── viaim-domestic-web/            # 国内 Web 端功能规格
│   │       ├── login.md                  ✅ 登录
│   │       ├── left-sidebar-and-file-list.md ✅ 左侧边栏与文件列表
│   │       ├── detail-page.md            ✅ 详情页
│   │       ├── recycle-bin.md            ✅ 回收站
│   │       ├── search.md                 ✅ 搜索
│   │       ├── settings.md               ✅ 设置
│   │       ├── space-grouping.md         ✅ 空间/分组
│   │       ├── live-and-share.md         ✅ 直播与分享
│   │       └── upload-and-capacity.md    ✅ 上传与容量
│   │
│   ├── reference-data/                    # 参考数据
│   │   └── viaim/
│   │       ├── transcribe.csv            ✅ 转写语种列表（145种，含变体、优先级）
│   │       ├── translate.csv             ✅ 翻译语种列表（80种，无变体）
│   │       └── 预制模版.csv              ✅ 摘要预制模版数据
│   │
│   └── test-focus/                        # 测试关注点
│       └── viaim/
│           ├── typical-defects.md         ✅ 典型缺陷模式库（错误推测法输入）
│           ├── testpoint-examples.md      ✅ 高质量测试点样例库（格式与深度参考）
│           ├── regression-focus.md        🔲 回归关注点
│           ├── risky-scenarios.md         🔲 高风险场景
│           └── platform-diff.md           🔲 Android/iOS/Web 差异汇总
│
└── history/                               # 已归档的历史需求/知识
    └── upload-file.md
```

---

## AI 引用速查表

### 领域规则（全平台通用）

| 写什么用例 | 引用文档 |
|----------|---------|
| 上传音频/文档/空间容量占用/校验优先级 | `domain/upload-rules.md` |
| 添加到空间/冲突弹窗/回收站恢复优先 | `domain/add-to-space-rules.md` |
| 删除/移除/回收站 | `domain/delete-recycle-rules.md` |
| 套餐差异/升级弹窗/订阅续费/转写时长扣除/AI模型权限 | `domain/subscription.md` |
| 导出功能 | `domain/export-rules.md` |
| 记录卡片显示/排序/红点/类型/状态 | `domain/record-common-rules.md` |
| 语言选择弹窗/语种切换/多语言付费 | `domain/language-selection.md` |
| 弹窗关闭方式/按钮状态/防重复提交 | `domain/common-interaction.md` |
| 新老版本迁移/祖父条款/分组→空间 | `domain/version-migration.md` |

### App（iOS / Android）功能规格

| 写什么用例 | 引用文档 |
|----------|---------|
| 4大录音功能（总览） | `features/viaim/recording/README.md` |
| 4大录音（通用规则） | `features/viaim/recording/common-rules.md` |
| 4大录音（通话专属） | `features/viaim/recording/call.md` |
| 4大录音（同传专属） | `features/viaim/recording/translate.md` |
| 文字直播 H5 | `features/viaim/recording/text-live.md` |
| 闪录 | `features/viaim/flash-record.md` |
| 记录列表筛选/左滑/批量/上传入口 | `features/viaim/record-list.md` |
| Space 空间功能 | `features/viaim/space.md` |
| Vitana AI 助理 | `features/viaim/vitana.md` |
| 详情页各Tab（App） | `features/viaim/detail-page.md` |
| 耳机型号/设置差异 | `features/viaim/bluetooth-headset.md` |
| 耳机手势控制/键值配置 | `features/viaim/bluetooth-gesture.md` |
| 耳机连接流程/权限/复连/MFI | `features/viaim/bluetooth-connect.md` |
| 账号绑定/解绑/删除账号 | `features/viaim/account-settings.md` |
| 录音设置/AI设置/权限/技术支持 | `features/viaim/my-preferences.md` |
| 小组件（悬浮窗/通知栏/灵动岛）| `features/viaim/widget.md` |
| 全局搜索（App） | `features/viaim/search.md` |
| 消息中心 | `features/viaim/message-center.md` |
| 登录注册（App） | `features/viaim/login-register.md` |

### 海外 Web 端功能规格

| 写什么用例 | 引用文档 |
|----------|---------|
| 登录（海外Web） | `features/viaim-web/login.md` |
| 左侧边栏/文件列表（海外Web） | `features/viaim-web/left-sidebar-and-file-list.md` |
| 详情页（海外Web） | `features/viaim-web/detail-page.md` |
| 回收站（海外Web） | `features/viaim-web/recycle-bin.md` |
| 搜索（海外Web） | `features/viaim-web/search.md` |
| 设置（海外Web） | `features/viaim-web/settings.md` |
| 空间/分组（海外Web） | `features/viaim-web/space-grouping.md` |
| 订阅（海外Web） | `features/viaim-web/subscription.md` |
| 账单（海外Web） | `features/viaim-web/billing.md` |
| 上传（海外Web） | `features/viaim-web/upload.md` |

### 国内 App 端功能规格

| 写什么用例 | 引用文档 |
|----------|---------|
| 登录注册（国内App）| `features/viaim-domestic/login-register.md` |
| 4大录音（总览）| `features/viaim-domestic/recording/README.md` |
| 4大录音（通用规则）| `features/viaim-domestic/recording/common-rules.md` |
| 4大录音（通话专属）| `features/viaim-domestic/recording/call.md` |
| 4大录音（同传专属）| `features/viaim-domestic/recording/translate.md` |
| 文字直播 H5 | `features/viaim-domestic/recording/text-live.md` |
| 闪录 | `features/viaim-domestic/flash-record.md` |
| 录音记录列表筛选/左滑/批量 | `features/viaim-domestic/record-list.md` |
| 首页 | `features/viaim-domestic/home.md` |
| 发现页 | `features/viaim-domestic/discover.md` |
| 万姆/Vitana AI 助理 | `features/viaim-domestic/wanmu-vitana.md` |
| 详情页各Tab（国内App）| `features/viaim-domestic/detail-page.md` |
| 耳机型号/设置差异（国内）| `features/viaim-domestic/bluetooth-headset.md` |
| 耳机手势控制/键值配置（国内）| `features/viaim-domestic/bluetooth-gesture.md` |
| 耳机连接流程（国内）| `features/viaim-domestic/bluetooth-connect.md` |
| 账号设置（国内App）| `features/viaim-domestic/account-settings.md` |
| 使用设置/云空间/权限（国内）| `features/viaim-domestic/my-preferences.md` |
| 小组件（悬浮窗/通知栏/灵动岛）| `features/viaim-domestic/widget.md` |
| 全局搜索（国内App）| `features/viaim-domestic/search.md` |
| 消息中心（国内App）| `features/viaim-domestic/message-center.md` |
| 国内版专属规则/云空间 | `domain/viaim-domestic.md` |

### 国内 Web 端功能规格

| 写什么用例 | 引用文档 |
|----------|---------|
| 登录（国内Web） | `features/viaim-domestic-web/login.md` |
| 左侧边栏/文件列表（国内Web） | `features/viaim-domestic-web/left-sidebar-and-file-list.md` |
| 详情页（国内Web） | `features/viaim-domestic-web/detail-page.md` |
| 回收站（国内Web） | `features/viaim-domestic-web/recycle-bin.md` |
| 搜索（国内Web） | `features/viaim-domestic-web/search.md` |
| 设置（国内Web） | `features/viaim-domestic-web/settings.md` |
| 空间/分组（国内Web） | `features/viaim-domestic-web/space-grouping.md` |
| 直播与分享（国内Web） | `features/viaim-domestic-web/live-and-share.md` |
| 上传与容量（国内Web） | `features/viaim-domestic-web/upload-and-capacity.md` |

### 参考数据

| 写什么用例 | 引用文档 |
|----------|---------|
| 转写语种数据（145种） | `reference-data/viaim/transcribe.csv` |
| 翻译语种数据（80种） | `reference-data/viaim/translate.csv` |
| 预制模版数据 | `reference-data/viaim/预制模版.csv` |
| 典型缺陷模式（错误推测法） | `test-focus/viaim/typical-defects.md` |
| 高质量测试点样例 | `test-focus/viaim/testpoint-examples.md` |

---

## 待补充事项

| 事项 | 说明 | 优先级 |
|------|------|--------|
| `product/viaim/overview.md` | 产品概述与核心模块 | ⭐⭐ |
| `product/viaim/scope.md` | 版本与平台范围 | ⭐⭐ |
| `features/viaim/message-center.md` 消息类型 | 消息类型详细内容后续完善 | ⭐⭐⭐ |
| `reference-data/viaim/预制模版说明.md` | 预制模版字段说明 | ⭐⭐ |
| `reference-data/viaim/语种说明.md` | 语种数据字段说明 | ⭐⭐ |
| `test-focus/viaim/regression-focus.md` | 回归关注点 | ⭐⭐⭐ |
| `test-focus/viaim/risky-scenarios.md` | 高风险场景清单 | ⭐⭐⭐ |
| `test-focus/viaim/platform-diff.md` | Android / iOS / Web 差异汇总 | ⭐⭐⭐ |
| `features/viaim-domestic/home.md` | 首页功能规格（待补充内容）| ⭐⭐⭐ |
| `features/viaim-domestic/discover.md` | 发现页功能规格（待补充内容）| ⭐⭐⭐ |
| `features/viaim-domestic/my-preferences.md` AI模型列表 | 国内版 AI 模型具体型号待确认 | ⭐⭐⭐ |
| `features/viaim-domestic/wanmu-vitana.md` AI模型权限 | 国内版 AI 模型权限规则待确认 | ⭐⭐⭐ |
| `domain/viaim-domestic.md` 容量规则 | 云存储容量额度及满容量限制待确认 | ⭐⭐ |
| `features/viaim-domestic/message-center.md` 消息类型 | 国内版消息类型详细内容待补充 | ⭐⭐ |
