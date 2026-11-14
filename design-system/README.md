# Design system · qué opción usar

La guía visual completa está en `design-system/index.html` (se arma con `python3 design-system/src/armar.py`). Cada ejemplo tiene ahí su código para copiar. Este archivo es el resumen en texto.

La opción **A** es la de por defecto. Las clases `cg-` son componentes nuevos: viven en `design-system/src/nuevos.css` y hay que sumar ese archivo al `armar.py` de la página que los use.

## Presentación del producto

Lo primero que ve: qué es, para quién y el botón.

- **A · Hero partido — texto + foto sobre rayas**: Para una landing de producto con foto de Juli (o del producto). Es la opción por defecto.  
  Clases: header.pr-split.pr-hero › .pr-tx + .pr-stripes › .pr-seal, .pr-frame, .pr-chat.c1/.c2/.c3
- **B · Hero en tarjeta — centrado sobre rayas**: Para páginas que no venden un solo producto: inicio, “sobre mí”, un índice de talleres.  
  Clases: header.ci-hero › .pr-seal + .ci-card › .lbl, h1 em, .lead, .pr-btn, .pr-sig

## Explicar qué es y cómo funciona

Justo después del hero: la definición en pocas líneas.

- **A · Qué es — texto corto + fotos que cambian**: Si se explica en 3 líneas y tenemos 3 fotos lindas. Es la más liviana.  
  Clases: section.pr-qe2 › .pr-qe2-in › .pr-qe2-tx + .pr-swap › .pr-swap-ph (3 fotos)
- **B · Pantalla partida — foto de un lado, texto del otro**: Si hay un método con varias partes (ingredientes, pasos, preguntas) y una foto que acompañe.  
  Clases: section.pr-split(.rev) › .pr-ph (img) + .pr-tx.color

## Lo que le pasa (dolores y creencias)

Para que ella se reconozca antes de ver la solución.

- **A · Dolores como chatcitos**: Si son frases como ella las diría, de uno o dos renglones.  
  Clases: .ci-point-in (título fijo a la izquierda) + ul.ae-chats. Solas y centradas: ul.ae-chats dentro de .pr-wrap.
- **B · Dolores en tarjetas cortas**: Si cada dolor se puede resumir en un título de 3–4 palabras.  
  Clases: .pr-head + .ae-pains › div › .ae-pn, b, span + p.ae-close
- **C · Mito tachado y la realidad encima**: Si lo que la frena es una creencia (“primero tengo que saberlo todo”).  
  Clases: ol.ci-myths › li › .ci-m (.ci-mk + s) + .ci-r

## Listados

Beneficios, lo que incluye, temas, módulos sueltos.

- **A · Lo que recibe — 3 tarjetas sobre cereza**: Si son exactamente 3 cosas importantes que merecen título e imagen.  
  Clases: section.pr-sec.pr-get › .pr-gets › .pr-g › .pr-gi, .n, h3, p
- **B · Áreas — tarjetas con pregunta y desplegable**: Si son 4–5 temas con mucho detalle cada uno (el detalle queda en un desplegable).  
  Clases: .ae-grid › article.ae-area › .ae-num, h3, p.q, details
- **C · Lista con tildes en una caja**: Si son muchos ítems cortos del mismo tipo (lo que incluye, materiales). La más simple.  
  Clases: .pr-head + .cg-incl › ul.ae-checks

## Pasos y recorridos

Cuando importa el orden.

- **A · Pasos numerados — el cambio en 3 etapas**: 3 etapas de un cambio, sin tiempos.  
  Clases: section.pr-3m › .pr-head + .pr-steps › .pr-step › .n, h3, p
- **B · Línea de tiempo — un recorrido con etapas**: 4 o más etapas con duración o fecha (encuentros, semanas).  
  Clases: ol.ae-tl › li(.start) › .ae-dot, .ae-meta, h3, p

## Contenidos y productos

Qué hay adentro, o entre qué puede elegir.

- **A · Contenidos — tarjetas con imagen**: Los módulos o aulas de un producto, con imagen y una línea.  
  Clases: .pr-aulas › article.pr-au › .pr-au-img + .pr-au-tx
- **B · Catálogo — tarjetas con portada en fila**: Varios productos distintos para elegir, cada uno con su portada y su botón.  
  Clases: .ci-swipe + .ci-scroll › .ci-track › article.ci-card2.color (de a 2: .ci-scroll.ci-two)

## Testimonios

Lo que dicen las alumnas. Siempre reales, nunca reescritos.

- **A · Pila de capturas**: Si tenemos 10 capturas y es la landing principal. La más llamativa.  
  Clases: section.pr-tsec › .pr-tcar-wrap › input.pr-tr × 10 + .pr-tstack + .pr-tnavs
- **B · Testimonios en texto, con nombre**: Si los testimonios están por escrito (no en captura).  
  Clases: .cg-quotes › figure.cg-q › blockquote + figcaption[data-i]
- **C · Capturas en fila para deslizar**: Si tenemos cualquier cantidad de capturas o la pila ya se usó.  
  Clases: .ci-swipe + .ci-scroll.cg-shots › .ci-track › figure.cg-shot

## Para quién es

Para que se reconozca la que sí y se vaya la que no.

- **A · Para quién es — tarjeta sí + cajas al costado**: Si hay que explicar qué necesita, qué no y derivarla a otro producto.  
  Clases: .ae-fitgrid › .pr-card.yes + .ae-side › .ae-box, .ae-box.no
- **B · Dos tarjetas — es para vos / no es para vos**: Si alcanzan dos listas cortas del mismo peso.  
  Clases: section.cg-fit › .pr-cards › .pr-card.yes + .pr-card.no

## Quién está detrás

Juli, en primera persona.

- **A · Juli — foto en arco sobre bordó**: En una landing de producto: “quién te acompaña”, corto y cercano.  
  Clases: section.pr-mine2 + clase propia (.pr-who2) › .pr-mine2-in › .pr-arch + .pr-mine2-tx
- **B · Juli — foto redonda al centro**: En una página institucional, con botón a su historia.  
  Clases: section.pr-sec.ci-juli › .ci-face + .pr-narrow.ci-juli-tx

## Una pausa o frase fuerte

Para frenar entre dos secciones cargadas.

- **A · Frase de foco — una idea, nada más**: Una idea que resume lo anterior, con título y bajada.  
  Clases: section.pr-sec.pr-bg-wine + clase propia › .pr-narrow
- **B · Cinta grande — una frase que corre**: Una frase corta que anuncia lo que viene (puertas abiertas, preguntas).  
  Clases: .pr-mq.big › .pr-mq-track › .pr-mq-grp × 4

## Precio

Siempre después de la confianza, con una cinta antes.

- **A · Precio con varios planes**: Si hay 2 o 3 planes (mensual, trimestral…) o precio de lanzamiento.  
  Clases: section.pr-sec.pr-bg-cherry.pr-pay#unite › .pr-pay-head + .pr-plans3 › .pr-pc.a/.b/.c + .pr-pay-note
- **B · Precio único con lo que incluye**: Si hay un solo precio y conviene mostrar todo lo que incluye al lado.  
  Clases: section.pr-sec.pr-bg-cherry.ae-price › .ae-pcard › .ae-pmain + .ae-pinc

## Preguntas frecuentes

Las dudas que frenan la compra.

- **A · Preguntas frecuentes**: Hasta 7–8 preguntas. Es la opción por defecto.  
  Clases: section.pr-sec.pr-faqsec › .pr-head + .pr-faq › details › summary + p
- **B · Preguntas con el título fijo al costado**: Si son muchas preguntas o queremos ofrecer “escribime si tu duda no está”.  
  Clases: section.cg-faq2 › .ci-point-in › .ci-point-head + .pr-faq

## Cierre

El último empujón.

- **A · Cierre partido — foto + último empujón**: En una landing de producto: foto, frase y el último botón al precio.  
  Clases: section.pr-split.pr-end.rev › .pr-ph + .pr-tx.yellow
- **B · Cierre centrado — con accesos directos**: En una página institucional: accesos directos a cada producto.  
  Clases: section.pr-sec.pr-bg-wine.ci-end › .pr-wrap › h2, p, ul.ci-quick, .pr-btn.cream

## Reglas rápidas

- Texto bordó sobre claros, crema sobre oscuros. Nunca negro ni gris.
- Una palabra destacada por título: cereza sobre claros, amarillo sobre cereza o bordó.
- Nunca dos secciones seguidas con el mismo fondo; las cintas (`.pr-mq`) cosen dos claros.
- Botón cereza sobre claros, `.pr-btn.cream` sobre oscuros.
- Rayas solo en el hero. Rosa (`--pink`) solo para detalles, nunca fondo de sección.
- Sin estrellas decorativas (solo el sello del hero y las estrellitas PNG de Juli), nada caricaturesco, todo en castellano con voseo, sin depender de JavaScript.
- Textos escritos por nosotros: comentario `REVISAR`. Datos que faltan: comentario `PENDIENTE`.
