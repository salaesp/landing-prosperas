# Landings · Cherry Glow by Juli de Franco

Cada landing tiene su carpeta. El archivo para pegar en el bloque HTML de Tiendup es siempre el `index.html` de esa carpeta.

| Carpeta | Landing | Archivo para Tiendup |
|---|---|---|
| `prosperas/` | Prósperas (membresía) | `prosperas/index.html` |
| `artempresarias/` | ARTEMPRESARIAS (acompañamiento 1:1 de 90 días) | `artempresarias/index.html` |
| `inicio/` | Página de inicio de la Academia | `inicio/index.html` |
| `sahumerios/` | Taller de sahumerios para emprender | `sahumerios/index.html` |

## Cómo se arma cada página

Los `index.html` se generan, no se editan a mano:

```bash
python3 prosperas/src/armar.py
python3 artempresarias/src/armar.py
python3 inicio/src/armar.py
python3 sahumerios/src/armar.py
```

- `prosperas/index-original.html`: la página original de Prósperas, sin tocar. De ahí salen el CSS base y los logos.
- `prosperas/src/nuevo.css`: estilos compartidos (chatcitos, cintas, estrellas, tarjetas, preguntas frecuentes). ARTEMPRESARIAS también los usa.
- `*/src/cuerpo.html`: el contenido de cada página.
- `artempresarias/src/estilos.css`: estilos propios de ARTEMPRESARIAS. El inicio también los usa.
- `inicio/src/estilos.css`: estilos propios del inicio.
- `inicio/assets/`: portadas de cada producto (se incrustan dentro del `index.html`).
- `sahumerios/src/estilos.css`: estilos propios del taller de sahumerios (usa también los de Prósperas, ARTEMPRESARIAS e inicio). Su `armar.py` genera la pila de testimonios.
- `sahumerios/original/`: las secciones del taller como estaban en Tiendup (solo de referencia).
- `inicio/original/`: las secciones del inicio como estaban en Tiendup antes de pasarlo a git (solo de referencia).
- `prosperas/assets/`: imágenes de las aulas y estrellitas; se incrustan dentro del `index.html`.

Tiendup no ejecuta JavaScript dentro del bloque HTML, así que todo lo importante funciona solo con HTML y CSS.
