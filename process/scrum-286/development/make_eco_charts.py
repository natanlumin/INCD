#!/usr/bin/env python3
"""SCRUM-286 subtask 2, ecosystem version: charts comparing the repositories, from tables/<date>/eco_*.csv.
Standard library only; SVG + HTML, rendered to PNG with headless Chrome. Usage: python3 make_eco_charts.py --date 2026-10-12
"""
import csv, os, sys, collections, datetime, math
a = sys.argv[1:]; date = a[a.index("--date") + 1] if "--date" in a else datetime.date.today().isoformat()
here = os.path.dirname(os.path.abspath(__file__)); tdir = os.path.join(here, "tables", date); cdir = os.path.join(here, "charts", date); os.makedirs(cdir, exist_ok=True)
def rd(n): return list(csv.DictReader(open(os.path.join(tdir, n))))
PAL = {"Hugging Face Hub": "#1b4f72", "ModelScope": "#f39c12", "Kaggle Models": "#85c1e9"}
W, H, L, R, T, B = 1000, 560, 90, 30, 70, 110
def nice(v):
    e = 10 ** math.floor(math.log10(v)); m = v / e
    return e * (1 if m <= 1 else 2 if m <= 2 else 2.5 if m <= 2.5 else 5 if m <= 5 else 10)
def frame(title, sub): return [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="Helvetica, Arial, sans-serif" style="background:#fff">', f'<text x="{L}" y="30" font-size="16" font-weight="bold" fill="#111">{title}</text>', f'<text x="{L}" y="50" font-size="11.5" fill="#444">{sub}</text>']
def yaxis(out, ymax, fmt):
    for i in range(6):
        v = ymax * i / 5; y = T + (H - T - B) * (1 - i / 5); out.append(f'<line x1="{L}" y1="{y:.1f}" x2="{W-R}" y2="{y:.1f}" stroke="#ddd"/><text x="{L-8}" y="{y+4:.1f}" font-size="11" text-anchor="end" fill="#333">{fmt(v)}</text>')
def legend(out, names, y0):
    for i, n in enumerate(names): out.append(f'<rect x="{L+i*190}" y="{y0}" width="12" height="12" fill="{PAL[n]}"/><text x="{L+i*190+16}" y="{y0+10}" font-size="11" fill="#222">{n}</text>')
def save(name, out):
    open(os.path.join(cdir, name + ".svg"), "w").write("\n".join(out)); open(os.path.join(cdir, name + ".html"), "w").write('<!doctype html><html><head><meta charset="utf-8"><style>body{margin:0;background:#fff}</style></head><body>' + "\n".join(out) + "</body></html>")
def grouped(name, title, sub, cats, series, data, fmt, note, ymax=None):
    out = frame(title, sub); ymax = ymax or nice(max(data.values()) * 1.05); yaxis(out, ymax, fmt); n = len(cats); step = (W - L - R) / n; bw = step * 0.8 / len(series)
    for i, c in enumerate(cats):
        for j, s in enumerate(series):
            v = data.get((s, c), 0); h = v / ymax * (H - T - B); x = L + i * step + step * 0.1 + j * bw; y = T + (H - T - B) - h
            out.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{bw-2:.1f}" height="{h:.1f}" fill="{PAL[s]}"/>')
        out.append(f'<text x="{L+i*step+step/2:.1f}" y="{H-B+16}" font-size="10.5" text-anchor="middle" fill="#333">{c}</text>')
    legend(out, series, H - B + 36); out.append(f'<text x="{L}" y="{H-B+72}" font-size="10.5" fill="#555">{note}</text></svg>'); save(name, out)
years = ["2022", "2023", "2024", "2025", "2026"]
vol = collections.Counter()
for r in rd("eco_volume_by_year.csv"):
    if r["platform"] != "Kaggle Models": vol[(r["platform"], r["year"])] += int(r["models"])
series = [p for p in ("Hugging Face Hub", "ModelScope") if any(k[0] == p for k in vol)]
grouped("eco1_volume_by_year_repository", "Model repositories created per year, by model repository", f"Five task tags of the report's segmentation; creation date of the repository record. Pulls of {date}.", years, series, vol, lambda v: f"{v:,.0f}", "2026 covers 1 January to 12 October. Higher = more models created.")
kind = collections.Counter(); tot = collections.Counter()
for r in rd("eco_kind_by_year.csv"):
    tot[(r["platform"], r["year"])] += int(r["models"])
    if r["kind"] != "no typed relation": kind[(r["platform"], r["year"])] += int(r["models"])
share = {k: kind[k] / tot[k] for k in tot if tot[k]}
grouped("eco2_derivative_share_by_year_repository", "Share of new repositories that declare a typed parent relation, by model repository", f"Fine-tune, quantised, adapter or merged, as the repository records it; the rest are base models and derivatives with no declared parent. Pulls of {date}.", years, series, share, lambda v: f"{v*100:.0f}%", "A declared relation is the uploader's statement, not verified by the repository. Higher = more declared derivatives.", ymax=1.0)
out = frame("Account concentration, by model repository", f"Cumulative share of each repository's index held by its largest accounts. Pulls of {date}.")
yaxis(out, 1.0, lambda v: f"{v*100:.0f}%")
for r in rd("eco_account_concentration.csv"):
    pass
conc = collections.defaultdict(list)
for r in rd("eco_account_concentration.csv"):
    if r["top_n_accounts"].isdigit(): conc[r["platform"]].append((int(r["top_n_accounts"]), float(r["share"])))
for p, pts in conc.items():
    xy = [(L + math.log10(n) / 4 * (W - L - R), T + (H - T - B) * (1 - s), n, s) for n, s in pts]
    out.append('<polyline points="' + " ".join(f"{x:.1f},{y:.1f}" for x, y, _, _ in xy) + f'" fill="none" stroke="{PAL[p]}" stroke-width="2.5"/>')
    for x, y, n, s in xy: out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4" fill="{PAL[p]}"/><text x="{x+(-8 if n==10000 else 8):.1f}" y="{y-8:.1f}" font-size="10.5" text-anchor="{"end" if n==10000 else "start"}" fill="#111">{s*100:.0f}%</text>')
for n in (1, 10, 100, 1000, 10000): out.append(f'<text x="{L + math.log10(n) / 4 * (W - L - R):.1f}" y="{H-B+16}" font-size="10.5" text-anchor="middle" fill="#333">{n:,}</text>')
out.append(f'<text x="{(L+W-R)/2}" y="{H-B+36}" font-size="11" text-anchor="middle" fill="#333">accounts, ranked by number of models (log scale)</text>'); legend(out, list(conc.keys()), H - B + 50)
out.append(f'<text x="{L}" y="{H-B+84}" font-size="10.5" fill="#555">An account is the platform account that holds the repository: a producer, a converter or an individual. Higher = more concentrated.</text></svg>'); save("eco3_account_concentration_repository", out)
print("charts in", cdir)
