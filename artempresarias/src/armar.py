"""Arma artempresarias/index.html.

Reutiliza de ../prosperas el CSS base, los logos SVG (firma "By Juli de Franco")
y los componentes compartidos (src/nuevo.css), los nuevos del design system
(../design-system/src/nuevos.css: .cg-incl) y suma src/estilos.css y src/cuerpo.html.
No usa JavaScript (Tiendup no lo ejecuta). Uso: python3 artempresarias/src/armar.py
"""
import base64
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
shared = shared.replace("url(assets/", "url(../prosperas/assets/")

header = """<!-- ============================================================
  LANDING ARTEMPRESARIAS · Cherry Glow by Juli de Franco
  Pegar completo en un bloque HTML de Tiendup. No usa JavaScript.
  Las líneas marcadas con PENDIENTE están comentadas para revisar.
============================================================ -->"""

out = "\n".join([
    header,
    "<style>",
    css,
    shared,
    (root / "src/estilos.css").read_text(encoding="utf-8"),
    (root.parent / "design-system/src/nuevos.css").read_text(encoding="utf-8"),
    "</style>",
    "",
    "\n".join(lines[svg_open:svg_close + 1]),
    "",
    (root / "src/cuerpo.html").read_text(encoding="utf-8"),
])


def uri(path):
    f = (root / path).resolve()
    mime = "image/png" if path.endswith(".png") else "image/jpeg"
    return "data:" + mime + ";base64," + base64.b64encode(f.read_bytes()).decode()


out = re.sub(r'src="((?:\.\./prosperas/)?assets/[^"]+\.(?:jpg|png))"', lambda m: 'src="' + uri(m.group(1)) + '"', out)
out = re.sub(r'url\(((?:\.\./prosperas/)?assets/[^)]+\.(?:jpg|png))\)', lambda m: 'url(' + uri(m.group(1)) + ')', out)
assert "<script" not in out.split("</style>", 1)[1]
(root / "index.html").write_text(out, encoding="utf-8")
print("index.html", len(out), "bytes")
