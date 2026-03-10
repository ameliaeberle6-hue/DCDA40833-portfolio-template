#
#!/usr/bin/env python3
#
"""Clean FIFA ranking CSV: normalize numeric/date types and write cleaned CSV."""
#
import csv
#
import os
#
from datetime import datetime
#

#
IN_FILE = "data/raw/fifa_ranking.csv"
#
OUT_DIR = "data/clean"
#
OUT_FILE = os.path.join(OUT_DIR, "fifa_ranking_clean.csv")
#

#
NUMERIC_FIELDS = [
#
    "rank",
#
    "total_points",
#
    "previous_points",
#
    "rank_change",
#
    "cur_year_avg",
#
    "cur_year_avg_weighted",
#
    "last_year_avg",
#
    "last_year_avg_weighted",
#
    "two_year_ago_avg",
#
    "two_year_ago_weighted",
#
    "three_year_ago_avg",
#
    "three_year_ago_weighted",
#
]
#

#
DATE_FIELDS = ["rank_date"]
#

#

#
def to_number(s):
#
    if s is None:
#
        return ""
#
    s = s.strip()
#
    if s == "":
#
        return ""
#
    s = s.replace(',', '')
#
    try:
#
        if '.' in s:
#
            return float(s)
#
        return int(s)
#
    except Exception:
#
        try:
#
            return float(s)
#
        except Exception:
#
            return s
#

#

#
def to_date(s):
#
    if s is None:
#
        return ""
#
    s = s.strip()
#
    if s == "":
#
        return ""
#
    # Attempt ISO first
#
    for fmt in ("%Y-%m-%d", "%Y/%m/%d", "%m/%d/%Y"):
#
        try:
#
            return datetime.strptime(s, fmt).date().isoformat()
#
        except Exception:
#
            continue
#
    # If parsing fails, return original trimmed value
#
    return s
#

#

#
def main():
#
    os.makedirs(OUT_DIR, exist_ok=True)
#
    seen = set()
#
    rows_out = []
#
    with open(IN_FILE, newline='', encoding='utf-8') as fin:
#
        reader = csv.DictReader(fin)
#
        fieldnames = [f.strip() for f in reader.fieldnames]
#
        for i, r in enumerate(reader, start=1):
#
            # normalize keys
#
            row = {k.strip(): (v.strip() if v is not None else '') for k, v in r.items()}
#
            # convert numeric fields
#
            for nf in NUMERIC_FIELDS:
#
                if nf in row:
#
                    row[nf] = to_number(row[nf])
#
            # convert date fields
#
            for df in DATE_FIELDS:
#
                if df in row:
#
                    row[df] = to_date(row[df])
#
            # deduplicate exact rows
#
            key = tuple(row.get(fn, '') for fn in fieldnames)
#
            if key in seen:
#
                continue
#
            seen.add(key)
#
            rows_out.append(row)
#

#
    # Write cleaned CSV with same header order
#
    with open(OUT_FILE, 'w', newline='', encoding='utf-8') as fout:
#
        writer = csv.DictWriter(fout, fieldnames=fieldnames)
#
        writer.writeheader()
#
        for r in rows_out:
#
            writer.writerow(r)
#

#
    print(f"Cleaned {len(rows_out)} rows written to {OUT_FILE}")
#

#

#
if __name__ == '__main__':
#
    main()
