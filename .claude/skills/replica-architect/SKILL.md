---
name: replica-architect
description: Elige tecnología, diseña la base de datos y fija el orden de construcción a partir de replica/mapa.md.
---

# Arquitectura

Lee `replica/mapa.md`. Propón la opción más sencilla y de coste inicial cero o mínimo (por ejemplo web app instalable/PWA con almacenamiento local antes que servidor).

## Salida: `replica/plan.md`
- Tecnología elegida y por qué, con alternativa descartada.
- Modelo de datos (tablas/campos y relaciones).
- Orden de construcción por pantallas, empezando por la función núcleo.
- Riesgos y decisiones que debe tomar la persona.

## Reglas que no se saltan
- Se replican funciones y flujos, nunca código, logotipos, imágenes, textos ni catálogos de contenido del original.
- Solo fuentes públicas: web oficial, ayuda, ficha de tienda, reseñas visibles. Nada de cuentas ajenas, muros de pago ni ingeniería inversa del binario.
- Todo lo que se aprende se guarda en la carpeta `replica/` del proyecto; cada skill lee lo que dejó la anterior.
- Escribe todo en español claro, sin jerga innecesaria. No inventes datos: si algo no se encuentra en fuentes públicas, dilo.
