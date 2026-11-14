"""Arma sahumerios/index.html (Taller de sahumerios para emprender).

Reutiliza de ../prosperas el CSS base, los logos SVG (firma "By Juli de Franco")
y los componentes compartidos (src/nuevo.css), los de ../artempresarias y ../inicio (src/estilos.css)
y suma src/estilos.css y src/cuerpo.html.
Los testimonios en pila se generan acá (marca <!-- TESTIMONIOS --> en cuerpo.html): sin JavaScript.
No usa JavaScript (Tiendup no lo ejecuta). Uso: python3 sahumerios/src/armar.py
"""
import re
from pathlib import Path

root = Path(__file__).resolve().parent.parent
pros = root.parent / "prosperas"
lines = (pros / "index-original.html").read_text(encoding="utf-8").split("\n")


def idx(pred, start=0):
    for i in range(start, len(lines)):
        if pred(lines[i]):
            return i
    raise SystemExit("no encontrado")


style_open = idx(lambda l: l.startswith("<style>"))
style_close = idx(lambda l: l.startswith("</style>"))
svg_open = idx(lambda l: l.startswith('<svg width="0"'))
svg_close = idx(lambda l: l.startswith("</svg>"), svg_open)

drop = ("--st-", ".pr-star", "pr-pillist li i", "pr-pillist li:nth-child")
css = "\n".join(l for l in lines[style_open + 1:style_close] if not any(d in l for d in drop))
css = css.replace(".pr-mine2-star{display:none}", "").replace('content:"✦"', 'content:""')
css = re.sub(r"\.pr-mq-grp span(:nth-child\(3n\+?2?\))?::after\{[^}]*st-[^}]*\}\n?", "", css)

shared = (pros / "src/nuevo.css").read_text(encoding="utf-8")
# las imágenes de nuevo.css no se usan acá: se sacan para no inflar el archivo
shared = re.sub(r"url\(assets/[^)]+\)", "none", shared)

# ---- testimonios: pila sin JavaScript (un botón de radio por testimonio) ----
TESTIMONIOS = [
    ("o_1k308uiugela1nmaah7ttt2v7s.png", "Testimonio de una alumna del Taller de Sahumerios"),
    ("o_1k3088gbipeh1sm31meqg6oglb5k.png", "Alumna mostrando sus primeros sahumerios realizados en el taller"),
    ("o_1k308e07i1qkg6phl31iqk1s3n5q.jpg", "Resultado de una alumna del Taller de Sahumerios"),
    ("o_1k308gjve17mv14urcvs1lv4uv36a.jpg", "Producción de sahumerios realizada por una alumna"),
    ("o_1k308lfedt341midloi4s51jhr74.jpg", "Mensaje de una alumna del Taller de Sahumerios"),
    ("o_1k308p7fl106ggjd1lc1r3nncc7m.jpg", "Testimonio real de una alumna del Taller de Sahumerios"),
]
CDN = "https://d3ekkp2oigezer.cloudfront.net/business/81221/themes/lite/assets/img/"
N = len(TESTIMONIOS)
PREV = '<svg viewBox="0 0 24 48" aria-hidden="true" focusable="false"><path d="M18 6 L6 24 L18 42" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg>'
NEXT = '<svg viewBox="0 0 24 48" aria-hidden="true" focusable="false"><path d="M6 6 L18 24 L6 42" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg>'

html = ['<div class="pr-tcar-wrap">']
for i in range(N):
    chk = " checked" if i == 0 else ""
    html.append(f'      <input type="radio" name="sh-t" id="sh-t{i}" class="pr-tr"{chk} aria-label="Testimonio {i + 1} de {N}">')
html.append('      <div class="pr-tstack">')
for i, (f, alt) in enumerate(TESTIMONIOS):
    html.append(f'        <label for="sh-t{i}" class="pr-tc"><img src="{CDN}{f}" alt="{alt}" loading="lazy"></label>')
html.append('      </div>')
html.append('      <div class="pr-tnavs">')
for i in range(N):
    html.append(f'        <label for="sh-t{(i - 1) % N}" class="pr-tnav prev sk{i}" aria-label="Testimonio anterior">{PREV}</label>'
                f'<label for="sh-t{(i + 1) % N}" class="pr-tnav next sk{i}" aria-label="Testimonio siguiente">{NEXT}</label>')
html.append('      </div>')
html.append('    </div>')
stack_html = "\n".join(html)

LOOK = {0: ("1", "0deg", "none", "1", 20, "default"),
        1: ("0.84", "3deg", "blur(2.5px) saturate(.4)", "0.85", 19, "pointer"),
        2: ("0.7", "6deg", "blur(5.0px) saturate(.4)", "0.5", 18, "pointer")}
rules = ["/* ---- testimonios en pila: estados generados por armar.py ---- */"]
for i in range(N):
    rules.append(f"#sh-t{i}:checked~.pr-tnavs .sk{i}{{display:grid}}")
    for off in (-2, -1, 0, 1, 2):
        sc, rot, flt, op, z, cur = LOOK[abs(off)]
        rot = rot if off >= 0 else "-" + rot
        if rot == "-0deg":
            rot = "0deg"
        n = (i + off) % N + 1
        rules.append(f"#sh-t{i}:checked~.pr-tstack .pr-tc:nth-child({n}){{transform:translate(-50%,-50%) translateX(calc(var(--g) * {off})) scale({sc}) rotate({rot});"
                     f"z-index:{z};filter:{flt};opacity:{op};pointer-events:auto;cursor:{cur}}}")
    rules.append(f"#sh-t{i}:focus-visible~.pr-tstack .pr-tc:nth-child({i + 1}){{outline:3px solid var(--cherry);outline-offset:4px}}")
stack_css = "\n".join(rules)

header = """<!-- ============================================================
  TALLER DE SAHUMERIOS PARA EMPRENDER · Cherry Glow by Juli de Franco
  Pegar completo en un bloque HTML de Tiendup. No usa JavaScript.
  Los comentarios REVISAR marcan cosas para confirmar.
============================================================ -->"""

body = (root / "src/cuerpo.html").read_text(encoding="utf-8")
assert "<!-- TESTIMONIOS -->" in body
body = body.replace("<!-- TESTIMONIOS -->", stack_html)

out = "\n".join([
    header,
    "<style>",
    css,
    shared,
    (root.parent / "artempresarias/src/estilos.css").read_text(encoding="utf-8"),
    (root.parent / "inicio/src/estilos.css").read_text(encoding="utf-8"),
    (root / "src/estilos.css").read_text(encoding="utf-8"),
    stack_css,
    "</style>",
    "",
    "\n".join(lines[svg_open:svg_close + 1]),
    "",
    body,
])

assert "<script" not in out.split("</style>", 1)[1]
(root / "index.html").write_text(out, encoding="utf-8")
print("index.html", len(out), "bytes")
