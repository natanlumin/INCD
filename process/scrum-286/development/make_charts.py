#!/usr/bin/env python3
"""SCRUM-286 subtask 2: three charts as SVG from tables/<date>/*.csv, standard library only.
Render to PNG with: chrome --headless --screenshot=<png> --window-size=1000,560 charts/<date>/<name>.html
Usage: python3 make_charts.py --date 2026-10-12
"""
import csv, os, sys, collections, datetime
args = sys.argv[1:]; date = args[args.index("--date") + 1] if "--date" in args else datetime.date.today().isoformat()
here = os.path.dirname(os.path.abspath(__file__)); tdir = os.path.join(here, "tables", date); cdir = os.path.join(here, "charts", date); os.makedirs(cdir, exist_ok=True)
def rd(n): return list(csv.DictReader(open(os.path.join(tdir, n))))
PAL = ["#1b4f72", "#2e86c1", "#85c1e9", "#f39c12", "#c0392b", "#7d3c98"]   # colour-blind-safe blues/orange/red/purple
W, H, L, R, T, B = 1000, 560, 90, 30, 70, 110
def frame(title, sub):
    return [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="Helvetica, Arial, sans-serif" style="background:#fff">',
            f'<text x="{L}" y="30" font-size="16" font-weight="bold" fill="#111">{title}</text>', f'<text x="{L}" y="50" font-size="11.5" fill="#444">{sub}</text>']
def nice(v):
    import math
    if v <= 1: return v
    e = 10 ** math.floor(math.log10(v)); m = v / e
    return e * (1 if m <= 1 else 2 if m <= 2 else 2.5 if m <= 2.5 else 5 if m <= 5 else 10)
def yaxis(out, ymax, fmt=lambda v: f"{v:,.0f}"):
    for i in range(6):
        v = ymax * i / 5; y = T + (H - T - B) * (1 - i / 5)
        out.append(f'<line x1="{L}" y1="{y:.1f}" x2="{W-R}" y2="{y:.1f}" stroke="#ddd"/><text x="{L-8}" y="{y+4:.1f}" font-size="11" text-anchor="end" fill="#333">{fmt(v)}</text>')
def legend(out, names, x0, y0):
    for i, n in enumerate(names):
        out.append(f'<rect x="{x0+i*170}" y="{y0}" width="12" height="12" fill="{PAL[i]}"/><text x="{x0+i*170+16}" y="{y0+10}" font-size="11" fill="#222">{n}</text>')
def stacked(name, title, sub, cats, series, data, note):
    out = frame(title, sub); tot = [sum(data[(c, s)] for s in series) for c in cats]; ymax = nice(max(tot) * 1.05)
    yaxis(out, ymax); n = len(cats); bw = (W - L - R) / n * 0.72; step = (W - L - R) / n
    for i, c in enumerate(cats):
        y = T + (H - T - B); x = L + i * step + (step - bw) / 2
        for j, s in enumerate(series):
            h = data[(c, s)] / ymax * (H - T - B); y -= h
            out.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{bw:.1f}" height="{h:.1f}" fill="{PAL[j]}"/>')
        out.append(f'<text x="{x+bw/2:.1f}" y="{H-B+16}" font-size="10.5" text-anchor="middle" fill="#333">{c}</text>')
    legend(out, series, L, H - B + 36); out.append(f'<text x="{L}" y="{H-B+72}" font-size="10.5" fill="#555">{note}</text></svg>')
    open(os.path.join(cdir, name + ".svg"), "w").write("\n".join(out)); open(os.path.join(cdir, name + ".html"), "w").write('<!doctype html><html><head><meta charset="utf-8"><style>body{margin:0;background:#fff}</style></head><body>' + "\n".join(out) + "</body></html>")
# chart 1: models created per quarter by task tag, 2023Q1 to 2026Q3
q = collections.Counter()
for r in rd("volume_by_month_tag.csv"):
    m = r["month"]; y = int(m[:4]); qq = f"{y}Q{(int(m[5:])-1)//3+1}"; q[(qq, r["task_tag"])] += int(r["models_created"])
tags = ["text-generation", "image-text-to-text", "text-classification", "feature-extraction", "sentence-similarity"]
cats = [c for c in sorted({a for a, _ in q}) if "2023Q1" <= c <= "2026Q3"]
stacked("chart1_volume_by_quarter", "Models created on the Hub per quarter, by task tag",
        f"Five task tags of the report's segmentation; {sum(q[(c,t)] for c in cats for t in tags):,} repositories created 2023Q1 to 2026Q3; creation date of the Hub record. Pull of {date}.",
        cats, tags, q, "2026Q4 omitted (12 days). Method: process/scrum-286/method-note.md. Higher = more models created.")
# chart 2: derivative kind by year
k = collections.Counter()
for r in rd("volume_by_month_kind.csv"): k[(r["month"][:4], r["derivative_kind"])] += int(r["models_created"])
kinds = ["no typed relation", "fine-tune", "quantised", "adapter", "merged"]; years = [y for y in sorted({a for a, _ in k}) if y >= "2022"]
stacked("chart2_derivatives_by_year", "Models created per year, by declared derivative kind",
        f"Typed base-model relation in the model card (fine-tune, quantised, adapter, merged); 'no typed relation' = base models and derivatives with no declared parent. Pull of {date}.",
        years, kinds, k, "2026 covers 1 January to 12 October. A declared relation is the uploader's statement, not verified by the Hub. Higher = more models created.")
# chart 3: producer concentration, cumulative share of the index by producer rank (log x)
conc = [(int(r["top_n_accounts"]), float(r["share_of_index"])) for r in rd("account_concentration.csv") if r["top_n_accounts"].isdigit()]
nprod = next(r["models"] for r in rd("account_concentration.csv") if r["top_n_accounts"] == "number of accounts")
out = frame("Account concentration: share of the index held by the accounts with most models", f"{nprod} Hub accounts hold 631,129 models; cumulative share by account rank. Pull of {date}.")
yaxis(out, 1.0, lambda v: f"{v*100:.0f}%"); import math
xs = [1, 10, 100, 1000, 10000]; pts = []
for n, sh in conc:
    x = L + (math.log10(n) / 4) * (W - L - R); y = T + (H - T - B) * (1 - sh); pts.append((x, y, n, sh))
out.append('<polyline points="' + " ".join(f"{x:.1f},{y:.1f}" for x, y, _, _ in pts) + f'" fill="none" stroke="{PAL[1]}" stroke-width="2.5"/>')
for x, y, n, sh in pts:
    anchor = "end" if n == 10000 else "start"; dx = -8 if n == 10000 else 8
    out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4" fill="{PAL[0]}"/><text x="{x+dx:.1f}" y="{y-8:.1f}" font-size="11" text-anchor="{anchor}" fill="#111">top {n:,}: {sh*100:.0f}%</text><text x="{x:.1f}" y="{H-B+16}" font-size="10.5" text-anchor="middle" fill="#333">{n:,}</text>')
out.append(f'<text x="{(L+W-R)/2}" y="{H-B+36}" font-size="11" text-anchor="middle" fill="#333">accounts, ranked by number of models (log scale)</text>')
out.append(f'<text x="{L}" y="{H-B+72}" font-size="10.5" fill="#555">An account is the Hub account that holds the repository: a producer, a converter or an individual. Higher = more concentrated.</text></svg>')
open(os.path.join(cdir, "chart3_account_concentration.svg"), "w").write("\n".join(out)); open(os.path.join(cdir, "chart3_account_concentration.html"), "w").write('<!doctype html><html><head><meta charset="utf-8"><style>body{margin:0;background:#fff}</style></head><body>' + "\n".join(out) + "</body></html>")
print("charts in", cdir)
