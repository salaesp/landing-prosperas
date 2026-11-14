"""Arma index.html a partir de index-original.html (CSS base, logos SVG, script)
y de src/nuevo.css + src/cuerpo.html. Uso: python3 src/armar.py"""
import re
from pathlib import Path

root = Path(__file__).resolve().parent.parent
orig = (root / "index-original.html").read_text(encoding="utf-8")
lines = orig.split("\n")

def idx(pred, start=0):
    for i in range(start, len(lines)):
        if pred(lines[i]):
            return i
    raise SystemExit("no encontrado")

style_open = idx(lambda l: l.startswith("<style>"))
style_close = idx(lambda l: l.startswith("</style>"))
svg_open = idx(lambda l: l.startswith("<svg width=\"0\""))
svg_close = idx(lambda l: l.startswith("</svg>"), svg_open)
script_open = idx(lambda l: l.startswith("<script>"))
script_close = idx(lambda l: l.startswith("</script>"), script_open)

# CSS original sin estrellas
drop = ("--st-", ".pr-star", "pr-pillist li i", "pr-pillist li:nth-child")
css = [l for l in lines[style_open + 1:style_close] if not any(d in l for d in drop)]
css = "\n".join(css)
css = css.replace(".pr-mine2-star{display:none}", "").replace("content:\"✦\"", "content:\"\"")
css = re.sub(r"\.pr-mq-grp span(:nth-child\(3n\+?2?\))?::after\{[^}]*st-[^}]*\}\n?", "", css)
assert "base64" not in css and "st-pink" not in css

header = """<!-- ============================================================
  LANDING PRÓSPERAS · Cherry Glow by Juli de Franco · versión 2
  Pegar completo en un bloque HTML de Tiendup.
  Las líneas marcadas con PENDIENTE están comentadas para revisar.
============================================================ -->"""

script = "\n".join(lines[script_open:script_close + 1])
assert "2026-11-29T23:59:59-03:00" in script
script = script.replace("2026-11-29T23:59:59-03:00", "2027-01-01T23:59:59-03:00")

out = "\n".join([
    header,
    "<style>",
    css,
    (root / "src/nuevo.css").read_text(encoding="utf-8"),
    "</style>",
    "",
    "\n".join(lines[svg_open:svg_close + 1]),
    "",
    (root / "src/cuerpo.html").read_text(encoding="utf-8"),
    script,
    "</div>",
    "",
])
(root / "index.html").write_text(out, encoding="utf-8")
print("index.html", len(out), "bytes")
