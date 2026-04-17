---
name: test-report-generation
description: 基于缺陷Excel和功能点文档，自动解析统计数据并生成完整版迭代测试报告Markdown。Use when the user asks to 生成测试报告、写测试报告、输出测试报告、生成报告、出测试报告。
---

# Test Report Generation

## Quick Start

当用户要求生成测试报告时，按以下顺序执行：

1. 确认三项输入已就位（缺陷 Excel / 功能点文档 / 版本基本信息）。
2. 运行 `parse_bugs.py` 解析 Excel，获得三张统计表 + 暂不修复列表。
3. 读取功能点简约描述文档（`xxx简约版测试点.md`）。
4. 按 V6.3.0 报告结构组装完整 Markdown 报告。
5. 输出文件：`xxx版本/测试报告_国内viaim_Vx.x.x.md`

---

## Core Workflow

### Step 1：确认输入

向用户确认（若未提供则询问）：
- [ ] 缺陷 Excel 文件路径（格式同 `iFLYBUDS--xxxx-xx-xx.xlsx`，需含 `严重程度` 列）
- [ ] 功能点简约描述文件路径（`xxx简约版测试点.md`）
- [ ] 版本号（如 `V6.4.0`）、测试周期（如 `2026.4.14 - 2026.5.10`）
- [ ] 参与人员是否有变动（无变动则沿用上版本）

---

### Step 2：解析 Excel

将以下脚本写入 `xxx版本/parse_bugs.py` 后运行，获取统计结果：

```python
import openpyxl, json, re
from collections import defaultdict

# ── 修改此处指向当前版本的 Excel 文件 ──
EXCEL_PATH = r'xxx版本\iFLYBUDS--xxxx-xx-xx.xlsx'
JSON_PATH  = r'xxx版本\excel_data.json'
OUT_PATH   = r'xxx版本\parse_result.txt'

wb = openpyxl.load_workbook(EXCEL_PATH)
ws = wb['work items']
rows = list(ws.iter_rows(values_only=True))
headers = [str(c) if c else '' for c in rows[0]]

def get_platform(title):
    m = re.match(r'[【\[]([^】\]]+)[】\]]', title)
    if not m: return '未知'
    tag = m.group(1).upper()
    if '服务端' in tag: return '服务端'
    if 'ANDROID' in tag: return 'Android'
    if 'IOS' in tag: return 'iOS'
    return '未知'

def get_severity(s):
    s = s.strip()
    for kw, label in [('致命','致命'),('1-','致命'),('严重','严重'),('2-','严重'),
                      ('一般','一般'),('3-','一般'),('轻微','轻微'),('4-','轻微')]:
        if kw in s: return label
    return s or '未知'

def get_status(s):
    s = s.strip()
    if s in ('已关闭', '已关闭（未修复）'): return '已闭环'
    if s == '暂不修复': return '暂不修复'
    return '待修复'

bugs = []
for row in rows[1:]:
    d = dict(zip(headers, [str(c) if c else '' for c in row]))
    if d.get('工作项类型','') not in ('缺陷','缺陷（产品/设计）'): continue
    bugs.append({
        'title':    d.get('标题',''),
        'status':   get_status(d.get('状态','')),
        'priority': d.get('优先级',''),
        'severity': get_severity(d.get('严重程度','')),
        'platform': get_platform(d.get('标题','')),
    })

total = len(bugs)
sev_stat  = defaultdict(lambda: defaultdict(int))
plat_pri  = defaultdict(lambda: defaultdict(int))
for b in bugs:
    sev_stat[b['severity']][b['status']] += 1
    plat_pri[b['platform']][b['priority']] += 1

lines = [f'总缺陷数: {total}', '']
lines += ['=== 严重程度×状态 ===',
          '严重程度\t暂不修复\t待修复\t已闭环\t合计']
for sev in ['致命','严重','一般','轻微']:
    v = [sev_stat[sev][s] for s in ['暂不修复','待修复','已闭环']]
    lines.append(f'{sev}\t'+'\t'.join(str(x) for x in v)+f'\t{sum(v)}')
cv = [sum(sev_stat[s][st] for s in ['致命','严重','一般','轻微']) for st in ['暂不修复','待修复','已闭环']]
lines.append(f'合计\t'+'\t'.join(str(x) for x in cv)+f'\t{sum(cv)}')

lines += ['', '=== 各端×优先级 ===', '端\t紧急\t高\t中\t低\t合计\t占比']
for plat in ['Android','iOS','服务端']:
    v = [plat_pri[plat][p] for p in ['紧急','高','中','低']]
    t = sum(v)
    lines.append(f'{plat}\t'+'\t'.join(str(x) for x in v)+f'\t{t}\t{t/total*100:.1f}%')

lines += ['', '=== 暂不修复列表 ===']
nf = [b for b in bugs if b['status']=='暂不修复']
lines.append(f'共 {len(nf)} 个')
for i,b in enumerate(nf,1):
    lines.append(f'{i}. [{b["platform"]}][{b["severity"]}][{b["priority"]}] {b["title"]}')

with open(OUT_PATH,'w',encoding='utf-8') as f:
    f.write('\n'.join(lines))
print('Done ->', OUT_PATH)
```

运行后读取 `parse_result.txt`，从中提取：
- **总缺陷数**、**各端数量**
- **严重程度 × 状态** 分布表（填入报告"缺陷等级分布"章节）
- **各端 × 优先级** 分布表（填入报告"缺陷各端占比"章节）
- **暂不修复列表**（填入报告"已知问题列表"章节）

---

### Step 3：读取功能点文档

读取 `xxx简约版测试点.md`，提取每个功能模块的：
- 功能点名称（作为表格"功能点"列）
- 覆盖要点描述（作为表格"评估结果"列，逐条以 `- **标签**：描述` 格式呈现）

---

### Step 4：组装测试报告

按以下模板填充，**所有统计数字必须来自 Step 2 的解析结果**：

```markdown
# 国内viaim V{版本号} 测试报告

**安徽艾德未来智能科技有限公司  发布**
**{年}年{月}月**

---

## 版本记录

| 版本号 | 时间 | 记录人 | 变更原因 |
|---|---|---|---|
| （沿用历史版本记录行） |
| {新版本行} | {日期} | {记录人} | V{版本号}版本 |

---

## 引言

本报告为国内版viaim App的测试结果分析报告，主要说明国内版viaim App的测试范围和测试结果，围绕测试结果评估、测试执行情况及已知问题几个方面综合描述测试结果及产品质量，测试报告将主要从功能来描述。

**参与人员：**
- 产品：{姓名}
- 视觉：{姓名}
- 研发：{姓名列表}
- 测试：{姓名列表}

---

## 测试版本信息

- **版本号**：V{版本号}
- **测试对象**：viaim APP（Android & iOS端）
- **测试周期**：{开始日期} - {结束日期}

---

## 测试结论

### 整体质量评估

- Android & iOS端迭代测试已完成，需求功能均实现并全量测试通过
- 产品 & 视觉验收通过，具备现网发布更新条件

### 缺陷概览

- 本次测试总缺陷数量 **{总数}个**
- Android端 **{Android数}个**，iOS端 **{iOS数}个**，服务端 **{服务端数}个**
- 缺陷状态符合预期，版本质量良好

### 风险评估

- 遗留 **{暂不修复数}个** 暂不修复问题，非【严重】缺陷，主要为{原因概述}

---

## 测试详情

### 目标质量要求

| 检查项 | 指标细则 | 指标完成情况 | 是否通过 | 问题 |
|---|---|---|---|---|
| 缺陷情况 | 版本发布时核心功能的BUG得到有效解决 | 完成 | 通过 | / |
| 缺陷情况 | 发布时不存在影响系统运行的BUG | 完成 | 通过 | / |
| 缺陷情况 | 产品发布前，BUG的修复过程没有引入额外的缺陷 | 完成 | 通过 | / |
| 缺陷情况 | 产品新版本发布时，旧版本反馈的问题得到有效解决 | 完成 | 通过 | / |
| 缺陷情况 | P1、P2致命、严重级别缺陷修复率 | 完成 | 通过 | / |
| 缺陷情况 | P3一般级别缺陷修复率 | 完成 | 通过 | / |
| 缺陷情况 | P4细微优化级别缺陷率 | 完成 | 通过 | / |
| 缺陷情况 | 未修复问题，已组织已知问题review，经过产品/项目关键角色确认达成一致，并有替代解决方法 | 完成 | 通过 | / |
| 测试完成度 | 用例覆盖100%产品需求 | 完成 | 通过 | / |
| 测试完成度 | 全功能用例执行覆盖度 | 完成 | 通过 | / |
| 测试完成度 | 交付产物完整性 | 完成 | 通过 | / |
| 测试完成度 | 内部验收情况 | 完成 | 通过 | / |

### 测试范围（功能点评估）

| 序号 | 功能点 | 评估结果 | 测试结果 |
|---|---|---|---|
| 1 | {功能点名称} | {插入简约版测试点覆盖描述} | 通过 |
| 2 | ... | ... | 通过 |

### 缺陷分析

#### 缺陷等级分布

总缺陷 **{总数}个**，其中"暂不修复"缺陷无【严重】缺陷：

| 严重性 | 暂不修复 | 待修复 | 已闭环 | 总计 |
|---|---|---|---|---|
| 致命缺陷 | {数} | {数} | {数} | {数} |
| 严重缺陷 | {数} | {数} | {数} | {数} |
| 一般缺陷 | {数} | {数} | {数} | {数} |
| 轻微缺陷 | {数} | {数} | {数} | {数} |
| **总计** | **{数}** | **{数}** | **{数}** | **{数}** |

#### 缺陷各端占比

| 优先级 | 紧急 | 高 | 中 | 低 | 合计 | 占比 |
|---|---|---|---|---|---|---|
| Android端 | {数} | {数} | {数} | {数} | {数} | {%} |
| iOS端 | {数} | {数} | {数} | {数} | {数} | {%} |
| 服务端 | {数} | {数} | {数} | {数} | {数} | {%} |

### 已知问题列表

#### 软件侧问题

| 序号 | 问题描述 | 严重程度 | 原因分析 | 解决方案 | 对用户的影响 |
|---|---|---|---|---|---|
| 1 | {标题} | {严重程度} | {原因} | 暂不处理 | / |
| ... | | | | | |
```

---

### Step 5：输出文件

将完整报告保存至：`xxx版本/测试报告_国内viaim_Vx.x.x.md`

---

## 注意事项

- **统计数字来源唯一**：所有数字从 `parse_result.txt` 读取，不得手动估算或凑整。
- **功能点描述直接插入**：简约版测试点中的 `-` 列表内容原样插入评估结果列。
- **遗留问题描述保留完整标题**：含版本号、模块名的完整标题直接复制，不缩写。
- **版本记录追加，不覆盖**：历史版本记录行全部保留，新版本追加在最后一行。
- **参与人员默认沿用**：如用户未说明变动，直接复用上版本人员列表。

## Additional Resources

- 解析规则详见 [test-report-generation.mdc](mdc:.cursor/rules/test-report-generation.mdc)
- 报告格式参考 `630版本/测试报告_国内viaim_V6.3.0.docx`
- Excel 解析脚本参考 `630版本/parse_bugs.py`
