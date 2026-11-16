"""Arma ebook-velas/index.html (Pack de velas: 2 ebooks, calculadora de precios y recursos de IA).

Reutiliza de ../prosperas el CSS base, los logos SVG (firma "By Juli de Franco")
y los componentes compartidos (src/nuevo.css), los de ../artempresarias y ../inicio (src/estilos.css),
los componentes nuevos del design system (../design-system/src/nuevos.css)
y suma src/estilos.css y src/cuerpo.html.
No usa JavaScript (Tiendup no lo ejecuta). Uso: python3 ebook-velas/src/armar.py
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

header = """<!-- ============================================================
  PACK DE VELAS · EBOOKS + CALCULADORA + IA · Cherry Glow by Juli de Franco
  Pegar completo en un bloque HTML de Tiendup. No usa JavaScript.
  Los comentarios REVISAR y PENDIENTE marcan cosas para confirmar o completar.
============================================================ -->"""

body = (root / "src/cuerpo.html").read_text(encoding="utf-8")

out = "\n".join([
    header,
    "<style>",
    css,
    shared,
    (root.parent / "artempresarias/src/estilos.css").read_text(encoding="utf-8"),
    (root.parent / "inicio/src/estilos.css").read_text(encoding="utf-8"),
    (root.parent / "design-system/src/nuevos.css").read_text(encoding="utf-8"),
    (root / "src/estilos.css").read_text(encoding="utf-8"),
    "</style>",
    "",
    "\n".join(lines[svg_open:svg_close + 1]),
    "",
    body,
])

assert "<script" not in out.split("</style>", 1)[1]
(root / "index.html").write_text(out, encoding="utf-8")
print("index.html", len(out), "bytes")
