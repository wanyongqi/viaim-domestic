import json
import re
from collections import defaultdict

with open(r'd:\cursorwj\GN_viaim\630版本\excel_data2.json', encoding='utf-8') as f:
    data = json.load(f)

rows = data['work items']
headers = rows[0]

def get_platform(title):
    # 只取第一个【】标签判断平台
    match = re.match(r'[【\[]([^】\]]+)[】\]]', title)
    if not match:
        return '未知'
    tag = match.group(1).upper()
    if '服务端' in tag or 'SERVER' in tag:
        return '服务端'
    if 'ANDROID' in tag:
        return 'Android'
    if 'IOS' in tag:
        return 'iOS'
    return '未知'

def get_severity(s):
    s = s.strip()
    if '致命' in s or s.startswith('1'):
        return '致命'
    elif '严重' in s or s.startswith('2'):
        return '严重'
    elif '一般' in s or s.startswith('3'):
        return '一般'
    elif '轻微' in s or s.startswith('4'):
        return '轻微'
    return s or '未知'

def get_status(s):
    s = s.strip()
    if s in ('已关闭', '已关闭（未修复）'):
        return '已闭环'
    elif s == '暂不修复':
        return '暂不修复'
    elif s in ('待修复', '处理中', '重新打开'):
        return '待修复'
    return s

bugs = []
for row in rows[1:]:
    d = dict(zip(headers, row))
    if d.get('工作项类型', '') not in ('缺陷', '缺陷（产品/设计）'):
        continue
    bugs.append({
        'title':    d.get('标题', ''),
        'status':   get_status(d.get('状态', '')),
        'priority': d.get('优先级', ''),
        'severity': get_severity(d.get('严重程度', '')),
        'platform': get_platform(d.get('标题', '')),
    })

total = len(bugs)
print(f'总缺陷数: {total}')
print()

# 各端数量
platform_count = defaultdict(int)
for b in bugs:
    platform_count[b['platform']] += 1
print('=== 各端数量 ===')
for p in ['Android', 'iOS', '服务端', '未知']:
    if platform_count[p]:
        print(f'  {p}: {platform_count[p]}')
print()

# 严重程度 × 状态
print('=== 严重程度 × 状态 ===')
sev_stat = defaultdict(lambda: defaultdict(int))
for b in bugs:
    sev_stat[b['severity']][b['status']] += 1

statuses   = ['暂不修复', '待修复', '已闭环']
severities = ['致命', '严重', '一般', '轻微']
print('严重程度\t暂不修复\t待修复\t已闭环\t合计')
for sev in severities:
    vals = [sev_stat[sev][st] for st in statuses]
    print(f'{sev}\t' + '\t'.join(str(v) for v in vals) + f'\t{sum(vals)}')
col_totals = [sum(sev_stat[sev][st] for sev in severities) for st in statuses]
print(f'合计\t' + '\t'.join(str(v) for v in col_totals) + f'\t{sum(col_totals)}')
print()

# 各端 × 优先级
print('=== 各端 × 优先级 ===')
plat_pri = defaultdict(lambda: defaultdict(int))
for b in bugs:
    plat_pri[b['platform']][b['priority']] += 1

priorities = ['紧急', '高', '中', '低']
platforms  = ['Android', 'iOS', '服务端']
print('端\t紧急\t高\t中\t低\t合计\t占比')
for plat in platforms:
    vals = [plat_pri[plat][p] for p in priorities]
    t = sum(vals)
    print(f'{plat}\t' + '\t'.join(str(v) for v in vals) + f'\t{t}\t{t/total*100:.1f}%')
print()

# 暂不修复列表
print('=== 暂不修复问题列表 ===')
not_fix = [b for b in bugs if b['status'] == '暂不修复']
print(f'共 {len(not_fix)} 个')
for i, b in enumerate(not_fix, 1):
    print(f'{i}. [{b["platform"]}][{b["severity"]}][{b["priority"]}] {b["title"]}')
