import random, math, os
random.seed(7)
os.makedirs("assets", exist_ok=True)

# ---------- header.svg ----------
W, H = 900, 240
stars = ""
for i in range(90):
    x = random.randint(0, W); y = random.randint(0, H)
    r = random.choice([0.6, 0.8, 1, 1.3])
    d = round(random.uniform(1.5, 5), 1); b = round(random.uniform(0, 4), 1)
    stars += f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" opacity=".2"><animate attributeName="opacity" values=".1;1;.1" dur="{d}s" begin="{b}s" repeatCount="indefinite"/></circle>'

cx, cy = 730, 120
gal = ""
for arm in range(2):
    for i in range(170):
        t = i / 170 * 3.6
        rad = 6 + t * 30
        ang = t * 1.9 + arm * math.pi
        x = cx + rad * math.cos(ang) + random.uniform(-5, 5)
        y = cy + rad * math.sin(ang) * 0.55 + random.uniform(-3, 3)
        c = random.choice(["#22d3ee", "#a78bfa", "#f0abfc", "#67e8f9", "#fff"])
        gal += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{random.choice([.7, 1, 1.4])}" fill="{c}" opacity="{random.uniform(.4, .95):.2f}"/>'

header = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">
<defs>
<radialGradient id="bg" cx="80%" cy="50%" r="90%"><stop offset="0" stop-color="#1e1b4b"/><stop offset="1" stop-color="#020617"/></radialGradient>
<radialGradient id="core"><stop offset="0" stop-color="#fff"/><stop offset=".3" stop-color="#f0abfc" stop-opacity=".8"/><stop offset="1" stop-color="#7c3aed" stop-opacity="0"/></radialGradient>
</defs>
<rect width="{W}" height="{H}" rx="14" fill="url(#bg)"/>
{stars}
<g>{gal}<circle cx="{cx}" cy="{cy}" r="22" fill="url(#core)"/>
<animateTransform attributeName="transform" type="rotate" from="0 {cx} {cy}" to="360 {cx} {cy}" dur="60s" repeatCount="indefinite"/></g>
<text x="50" y="105" font-family="Consolas,Menlo,monospace" font-size="54" font-weight="700" fill="#fff">YOGESH</text>
<text x="52" y="140" font-family="Consolas,Menlo,monospace" font-size="17" fill="#67e8f9">LVL 2 CS &amp; IT student  //  wandering the galaxy</text>
<text x="52" y="172" font-family="Consolas,Menlo,monospace" font-size="14" fill="#94a3b8">status: building things &#x2022; <tspan fill="#4ade80">online</tspan><tspan fill="#4ade80">_<animate attributeName="opacity" values="1;0;1" dur="1s" repeatCount="indefinite"/></tspan></text>
</svg>'''
open("assets/header.svg", "w", encoding="utf-8").write(header)

# ---------- stats.svg ----------
stats = [("CURIOSITY", 96, "#22d3ee"), ("BUILD SPEED", 78, "#a78bfa"), ("SLEEP", 14, "#f87171"), ("BUGS CREATED", 88, "#fbbf24"), ("BUGS FIXED", 86, "#4ade80")]
rows = ""
for i, (n, v, c) in enumerate(stats):
    y = 40 + i * 34
    w = int(v / 100 * 300)
    rows += f'''<text x="24" y="{y+12}" font-family="Consolas,Menlo,monospace" font-size="13" fill="#cbd5e1">{n}</text>
<rect x="170" y="{y}" width="300" height="16" rx="8" fill="#1e293b"/>
<rect x="170" y="{y}" width="0" height="16" rx="8" fill="{c}"><animate attributeName="width" from="0" to="{w}" dur="1.6s" begin="{i*0.25}s" fill="freeze"/></rect>
<text x="482" y="{y+13}" font-family="Consolas,Menlo,monospace" font-size="13" fill="{c}">{v}</text>'''
stats_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 220" width="540" height="220">
<rect width="540" height="220" rx="14" fill="#0b1020" stroke="#1e293b"/>
<text x="24" y="26" font-family="Consolas,Menlo,monospace" font-size="14" font-weight="700" fill="#fff">CHARACTER STATS</text>
{rows}
</svg>'''
open("assets/stats.svg", "w", encoding="utf-8").write(stats_svg)
print("Done! Created assets/header.svg and assets/stats.svg")