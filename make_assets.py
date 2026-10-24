import random, math, os
random.seed(7)
os.makedirs("assets", exist_ok=True)
FONT = "Consolas,Menlo,monospace"

def save(name, text):
    open(f"assets/{name}", "w", encoding="utf-8").write(text)

# ================= header.svg =================
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
save("header.svg", f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">
<defs>
<radialGradient id="bg" cx="80%" cy="50%" r="90%"><stop offset="0" stop-color="#1e1b4b"/><stop offset="1" stop-color="#020617"/></radialGradient>
<radialGradient id="core"><stop offset="0" stop-color="#fff"/><stop offset=".3" stop-color="#f0abfc" stop-opacity=".8"/><stop offset="1" stop-color="#7c3aed" stop-opacity="0"/></radialGradient>
</defs>
<rect width="{W}" height="{H}" rx="14" fill="url(#bg)"/>
{stars}
<g>{gal}<circle cx="{cx}" cy="{cy}" r="22" fill="url(#core)"/>
<animateTransform attributeName="transform" type="rotate" from="0 {cx} {cy}" to="360 {cx} {cy}" dur="60s" repeatCount="indefinite"/></g>
<text x="50" y="100" font-family="{FONT}" font-size="54" font-weight="700" fill="#fff">YOGESH</text>
<text x="52" y="135" font-family="{FONT}" font-size="17" fill="#67e8f9">LVL 2 CS &amp; IT student  //  wandering the galaxy</text>
<text x="52" y="165" font-family="{FONT}" font-size="14" fill="#94a3b8">chess &#x2022; formula 1 &#x2022; cards</text>
<text x="52" y="195" font-family="{FONT}" font-size="14" fill="#94a3b8">status: building things &#x2022; <tspan fill="#4ade80">online</tspan><tspan fill="#4ade80">_<animate attributeName="opacity" values="1;0;1" dur="1s" repeatCount="indefinite"/></tspan></text>
</svg>''')

# ================= stats.svg =================
stats = [("CURIOSITY", 96, "#22d3ee"), ("BUILD SPEED", 78, "#a78bfa"), ("SLEEP", 14, "#f87171"), ("BUGS CREATED", 88, "#fbbf24"), ("BUGS FIXED", 86, "#4ade80")]
rows = ""
for i, (n, v, c) in enumerate(stats):
    y = 40 + i * 34
    w = int(v / 100 * 300)
    rows += f'''<text x="24" y="{y+12}" font-family="{FONT}" font-size="13" fill="#cbd5e1">{n}</text>
<rect x="170" y="{y}" width="300" height="16" rx="8" fill="#1e293b"/>
<rect x="170" y="{y}" width="0" height="16" rx="8" fill="{c}"><animate attributeName="width" from="0" to="{w}" dur="1.6s" begin="{i*0.25}s" fill="freeze"/></rect>
<text x="482" y="{y+13}" font-family="{FONT}" font-size="13" fill="{c}">{v}</text>'''
save("stats.svg", f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 220" width="540" height="220">
<rect width="540" height="220" rx="14" fill="#0b1020" stroke="#1e293b"/>
<text x="24" y="26" font-family="{FONT}" font-size="14" font-weight="700" fill="#fff">CHARACTER STATS</text>
{rows}
</svg>''')

# ================= race.svg (Formula 1) =================
TRACK = "M430,225 L760,225 C830,225 850,170 800,140 C760,115 700,150 640,135 C580,120 570,95 510,100 C440,105 395,150 400,190 C403,212 415,225 430,225 Z"
lights = ""
for i in range(5):
    x = 500 + i * 50
    on = (1 + i * 0.8) / 9
    lights += (f'<circle cx="{x}" cy="40" r="15" fill="#2a0a0a" stroke="#475569" stroke-width="2"/>'
               f'<circle cx="{x}" cy="40" r="15" fill="#ef4444" opacity="0">'
               f'<animate attributeName="opacity" calcMode="discrete" values="0;1;0;0" keyTimes="0;{on:.4f};{6/9:.4f};1" dur="9s" repeatCount="indefinite"/></circle>')
save("race.svg", f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 260" width="900" height="260">
<rect width="900" height="260" rx="14" fill="#0b0f1a"/>
<text x="40" y="95" font-family="{FONT}" font-size="34" font-weight="700" fill="#fff">FORMULA</text>
<text x="40" y="135" font-family="{FONT}" font-size="34" font-weight="700" fill="#ef4444">YOGESH</text>
<text x="40" y="170" font-family="{FONT}" font-size="14" fill="#94a3b8">fastest lap: 1:23.456 (probably)</text>
<text x="40" y="195" font-family="{FONT}" font-size="14" fill="#94a3b8">team: 4 projects, 0 sponsors</text>
{lights}
<text x="600" y="80" text-anchor="middle" font-family="{FONT}" font-size="14" font-weight="700" fill="#4ade80" opacity="0">LIGHTS OUT AND AWAY WE GO!
<animate attributeName="opacity" calcMode="discrete" values="0;1;0;0" keyTimes="0;{6/9:.4f};{8.4/9:.4f};1" dur="9s" repeatCount="indefinite"/></text>
<path d="{TRACK}" fill="none" stroke="#1f2937" stroke-width="20" stroke-linejoin="round"/>
<path d="{TRACK}" fill="none" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="6 6"/>
<rect x="556" y="215" width="5" height="20" fill="#fff"/>
<g>
<rect x="-11" y="-5" width="22" height="10" rx="4" fill="#ef4444"/>
<rect x="1" y="-3.5" width="6" height="7" rx="2" fill="#fff" opacity=".85"/>
<rect x="-9" y="-7" width="5" height="2.5" fill="#111"/><rect x="-9" y="4.5" width="5" height="2.5" fill="#111"/>
<rect x="5" y="-7" width="5" height="2.5" fill="#111"/><rect x="5" y="4.5" width="5" height="2.5" fill="#111"/>
<animateMotion dur="6s" repeatCount="indefinite" rotate="auto" path="{TRACK}"/>
</g>
</svg>''')

# ================= chess.svg (mate in 1 puzzle) =================
FEN = "r1bqkb1r/pppp1ppp/2n2n2/4p2Q/2B1P3/8/PPPP1PPP/RNB1K1NR"
glyph = {'k': '\u265a', 'q': '\u265b', 'r': '\u265c', 'b': '\u265d', 'n': '\u265e', 'p': '\u265f'}
SQ, OFF = 50, 22
board = ""
pieces = ""
for r in range(8):
    for f in range(8):
        col = "#c9d1e8" if (r + f) % 2 == 0 else "#5b6b95"
        board += f'<rect x="{OFF+f*SQ}" y="{OFF+r*SQ}" width="{SQ}" height="{SQ}" fill="{col}"/>'
for r, row in enumerate(FEN.split('/')):
    f = 0
    for ch in row:
        if ch.isdigit():
            f += int(ch); continue
        x = OFF + f * SQ + SQ / 2
        y = OFF + r * SQ + SQ / 2 + 13
        white = ch.isupper()
        fill = "#ffffff" if white else "#111111"
        stroke = "#111111" if white else "#e5e7eb"
        pieces += (f'<text x="{x}" y="{y}" text-anchor="middle" font-size="38" '
                   f'font-family="Segoe UI Symbol,Apple Symbols,DejaVu Sans,Arial Unicode MS,sans-serif" '
                   f'fill="{fill}" stroke="{stroke}" stroke-width=".8">{glyph[ch.lower()]}&#xFE0E;</text>')
        f += 1
labels = ""
for i in range(8):
    labels += f'<text x="{OFF+i*SQ+SQ/2}" y="{OFF+8*SQ+15}" text-anchor="middle" font-family="{FONT}" font-size="12" fill="#94a3b8">{"abcdefgh"[i]}</text>'
    labels += f'<text x="9" y="{OFF+i*SQ+SQ/2+4}" text-anchor="middle" font-family="{FONT}" font-size="12" fill="#94a3b8">{8-i}</text>'
save("chess.svg", f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {OFF*2+SQ*8-10} {OFF+SQ*8+22}" width="444" height="444">
<rect width="100%" height="100%" rx="12" fill="#0b0f1a"/>
{board}{pieces}{labels}
</svg>''')

# ================= card_back.svg =================
pat = ""
for i in range(-14, 14):
    pat += f'<line x1="{i*10}" y1="0" x2="{i*10+140}" y2="140" stroke="#7c3aed" stroke-opacity=".35"/>'
    pat += f'<line x1="{i*10+140}" y1="0" x2="{i*10}" y2="140" stroke="#7c3aed" stroke-opacity=".35"/>'
save("card_back.svg", f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 140" width="100" height="140">
<defs><clipPath id="c"><rect x="8" y="8" width="84" height="124" rx="6"/></clipPath></defs>
<rect width="100" height="140" rx="10" fill="#f8fafc"/>
<rect x="8" y="8" width="84" height="124" rx="6" fill="#1e1b4b"/>
<g clip-path="url(#c)">{pat}</g>
<rect x="8" y="8" width="84" height="124" rx="6" fill="none" stroke="#a78bfa" stroke-width="2"/>
<circle cx="50" cy="70" r="20" fill="#0b0f1a" stroke="#22d3ee" stroke-width="2"/>
<text x="50" y="79" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="#22d3ee">?</text>
</svg>''')

print("Done! Created 5 files in the assets folder.")