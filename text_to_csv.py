#!/usr/bin/env python3
import argparse
import csv
import re
from pathlib import Path

def guess_delimiter(sample: str) -> str | None:
    # common structured text delimiters
    candidates = [",", ";", "\t", "|"]
    counts = {d: sample.count(d) for d in candidates}
    best = max(counts, key=counts.get)
    return best if counts[best] >= 2 else None

def split_line(line: str, delim: str | None) -> list[str]:
    line = line.strip()
    if not line:
        return []
    if delim:
        return [c.strip() for c in line.split(delim)]
    # fallback: split on 2+ spaces (keeps single spaces inside names)
    return [c.strip() for c in re.split(r"\s{2,}", line)]

def main():
    p = argparse.ArgumentParser(description="Convert messy text into CSV.")
    p.add_argument("input", help="Input .txt file")
    p.add_argument("output", help="Output .csv file")
    p.add_argument("--header", default="", help="Comma-separated header, e.g. name,email,phone")
    args = p.parse_args()

    in_path = Path(args.input)
    out_path = Path(args.output)

    text = in_path.read_text(encoding="utf-8", errors="replace")
    lines = [ln.rstrip("\n") for ln in text.splitlines()]

    # find a non-empty sample for delimiter guessing
    sample = next((ln for ln in lines if ln.strip()), "")
    delim = guess_delimiter(sample)

    rows: list[list[str]] = []
    for ln in lines:
        cols = split_line(ln, delim)
        if cols:
            rows.append(cols)

    if not rows:
        raise SystemExit("No data found in input.")

    # Normalize to same number of columns
    max_cols = max(len(r) for r in rows)
    rows = [r + [""] * (max_cols - len(r)) for r in rows]

    header = []
    if args.header.strip():
        header = [h.strip() for h in args.header.split(",")]
        if len(header) < max_cols:
            header += [f"col_{i+1}" for i in range(len(header), max_cols)]
        header = header[:max_cols]

    with out_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header:
            w.writerow(header)
        w.writerows(rows)

    print(f"Done. Wrote {len(rows)} rows to {out_path} (delimiter={'none' if not delim else repr(delim)}).")

if __name__ == "__main__":
    main()
