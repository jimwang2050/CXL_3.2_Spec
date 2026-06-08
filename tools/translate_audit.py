#!/usr/bin/env python3
"""Translation audit for Ch3 + Ch11 (and extendable to any chapter).

Scans all bilingual <tr><td>EN</td><td style="background-color:#e8e8e8">ZH</td></tr> rows
in the chapter MD and reports:
  - Empty Chinese translations
  - Placeholder leftovers (TODO, FIXME, etc)
  - ZH/EN length statistics
  - Key terminology consistency
  - Per-row issues with context
"""
import re
import sys
from pathlib import Path
from collections import Counter

ROW_RE = re.compile(
    r'<tr><td[^>]*>(.*?)</td><td[^>]*style="background-color:#e8e8e8"[^>]*>(.*?)</td></tr>',
    re.DOTALL
)

# Key terminology expected to be consistent across chapters
KEY_TERMS = {
    "transaction": ["事务", "交易"],
    "protocol": ["协议", "规约"],
    "cache": ["缓存"],
    "memory": ["内存", "存储器"],
    "coherent": ["一致性", "相干"],
    "request": ["请求", "要求"],
    "response": ["响应", "回应"],
    "poison": ["毒化", "污染", "Poison"],
    "IDE": ["IDE", "完整性", "数据完整性"],
    "flit": ["flit", "Flit"],
    "MCTP": ["MCTP"],
    "PCIe": ["PCIe"],
}

def audit(filepath, name=None):
    if name is None:
        name = Path(filepath).stem
    text = Path(filepath).read_text()
    print(f"\n========== {name} 翻译审计 ==========")

    rows = list(ROW_RE.finditer(text))
    print(f"  total bilingual rows: {len(rows)}")

    issues = []
    en_lens, zh_lens = [], []
    for m in rows:
        en = re.sub(r'<[^>]+>', '', m.group(1)).strip()
        zh = re.sub(r'<[^>]+>', '', m.group(2)).strip()
        en_lens.append(len(en))
        zh_lens.append(len(zh))

        if not zh or zh in ('&nbsp;', ' '):
            issues.append(("EMPTY ZH", en[:80]))
        if en and not zh:
            issues.append(("ZH MISSING", en[:80]))
        if re.search(r'\[待译\]|TODO|placeholder', zh, re.IGNORECASE):
            issues.append(("PLACEHOLDER", f"EN={en[:60]} ZH={zh[:60]}"))

    print(f"  real issues: {len(issues)}")
    for i in issues[:10]:
        print(f"    {i[0]}: {i[1]}")
    if len(issues) > 10:
        print(f"    ... and {len(issues) - 10} more")

    if en_lens:
        print(f"  EN length: min={min(en_lens)}, max={max(en_lens)}, avg={sum(en_lens)//len(en_lens)}")
        print(f"  ZH length: min={min(zh_lens)}, max={max(zh_lens)}, avg={sum(zh_lens)//len(zh_lens)}")
        if sum(en_lens):
            print(f"  ZH/EN ratio: avg={sum(zh_lens)/sum(en_lens):.2f}")

    # Term consistency
    print(f"\n  Key term usage:")
    for term_en, candidates in KEY_TERMS.items():
        en_count = text.count(term_en)
        zh_counts = {zh: text.count(zh) for zh in candidates}
        print(f"    {term_en!r:18} EN={en_count:4}  ZH: {zh_counts}")

    return len(issues)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: translate_audit.py <md-file> [name] ...")
        sys.exit(1)
    total_issues = 0
    for i in range(1, len(sys.argv), 2):
        fp = sys.argv[i]
        name = sys.argv[i+1] if i+1 < len(sys.argv) else None
        total_issues += audit(fp, name)
    print(f"\n========== 全部 audit 完成, 总真问题: {total_issues} ==========")
