"""Arma design-system/index.html: la guía visual de las landings.

Usa exactamente el mismo CSS que las páginas (base de Prósperas, componentes
compartidos, ARTEMPRESARIAS e inicio) y le suma src/guia.css, que solo da forma
a la guía. Así los ejemplos se ven igual que en Tiendup.

Cada ejemplo marcado en src/cuerpo.html con
    <!--demo--> ... <!--/demo-->      (sección de ancho completo)
    <!--demo-in--> ... <!--/demo-in-->  (componente chico, dentro de un recuadro)
se muestra tal cual y debajo se agrega "Ver el código" con ese mismo HTML.

Uso: python3 design-system/src/armar.py
"""
import base64
import html
import re
import textwrap
from pathlib import Path

root = Path(__file__).resolve().parent.parent
pros = root.parent / "prosperas"
ae = root.parent / "artempresarias"
ci = root.parent / "inicio"
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

# mismo recorte del CSS base que hacen las otras páginas (sin estrellas)
drop = ("--st-", ".pr-star", "pr-pillist li i", "pr-pillist li:nth-child")
css = "\n".join(l for l in lines[style_open + 1:style_close] if not any(d in l for d in drop))
css = css.replace(".pr-mine2-star{display:none}", "").replace('content:"✦"', 'content:""')
css = re.sub(r"\.pr-mq-grp span(:nth-child\(3n\+?2?\))?::after\{[^}]*st-[^}]*\}\n?", "", css)

shared = (pros / "src/nuevo.css").read_text(encoding="utf-8").replace("url(assets/", "url(../prosperas/assets/")


def snippet(body):
    body = textwrap.dedent(body.strip("\n")).strip()
    # quote=True: así las rutas de imágenes del código no se reemplazan por la imagen incrustada
    return html.escape(body, quote=True)


def demo_full(m):
    body = m.group(1)
    return (body + '\n<div class="ds-codebar"><div class="pr-wrap"><details class="ds-code"><summary>Ver el código</summary>'
            '<pre><code>' + snippet(body) + '</code></pre></details></div></div>')


def demo_in(m):
    body = m.group(1)
    return (body + '\n<details class="ds-code"><summary>Ver el código</summary>'
            '<pre><code>' + snippet(body) + '</code></pre></details>')


cuerpo = (root / "src/cuerpo.html").read_text(encoding="utf-8")
cuerpo = re.sub(r"<!--demo-->(.*?)<!--/demo-->", demo_full, cuerpo, flags=re.S)
cuerpo = re.sub(r"<!--demo-in-->(.*?)<!--/demo-in-->", demo_in, cuerpo, flags=re.S)
assert "<!--demo" not in cuerpo and "<!--/demo" not in cuerpo

out = "\n".join([
    "<!doctype html>",
    '<html lang="es"><head><meta charset="utf-8">',
    '<meta name="viewport" content="width=device-width,initial-scale=1">',
    "<title>Design system · Landings Cherry Glow</title>",
    "<style>",
    "body{margin:0;background:#fff8fc}",
    css,
    shared,
    (ae / "src/estilos.css").read_text(encoding="utf-8"),
    (ci / "src/estilos.css").read_text(encoding="utf-8"),
    (root / "src/nuevos.css").read_text(encoding="utf-8"),
    (root / "src/guia.css").read_text(encoding="utf-8"),
    "</style></head><body>",
    "\n".join(lines[svg_open:svg_close + 1]),
    cuerpo,
    "</body></html>",
    "",
])


def uri(path):
    f = (root / path).resolve()
    mime = "image/png" if path.endswith(".png") else "image/jpeg"
    return "data:" + mime + ";base64," + base64.b64encode(f.read_bytes()).decode()


pat = r'(?:\.\./(?:prosperas|inicio)/)assets/[^"\)]+\.(?:jpg|png)'
out = re.sub(r'src="(' + pat + ')"', lambda m: 'src="' + uri(m.group(1)) + '"', out)
out = re.sub(r'url\((' + pat + r')\)', lambda m: 'url(' + uri(m.group(1)) + ')', out)
assert "<script" not in out
(root / "index.html").write_text(out, encoding="utf-8")
print("index.html", len(out), "bytes")
