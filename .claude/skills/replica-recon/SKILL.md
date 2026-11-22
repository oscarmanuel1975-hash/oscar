---
name: replica-recon
description: Estudia una app existente con fuentes públicas y extrae pantallas, funciones y flujos para replicarla. Primer paso del flujo de réplica.
---

# Reconocimiento de la app original

Pregunta qué app se quiere replicar, para qué plataforma y qué funciones son imprescindibles.

## Pasos
1. Busca la web oficial, el centro de ayuda y la ficha de App Store / Google Play.
2. Lista pantallas, acciones del usuario, datos que se guardan y modelo de precios (qué es gratis y qué de pago).
3. Marca cada función como **núcleo**, **secundaria** o **extra**.
4. Escribe `replica/mapa.md` con: resumen, pantallas, flujos paso a paso, funciones por prioridad y fuentes consultadas (con enlace).

## Reglas que no se saltan
- Se replican funciones y flujos, nunca código, logotipos, imágenes, textos ni catálogos de contenido del original.
- Solo fuentes públicas: web oficial, ayuda, ficha de tienda, reseñas visibles. Nada de cuentas ajenas, muros de pago ni ingeniería inversa del binario.
- Todo lo que se aprende se guarda en la carpeta `replica/` del proyecto; cada skill lee lo que dejó la anterior.
- Escribe todo en español claro, sin jerga innecesaria. No inventes datos: si algo no se encuentra en fuentes públicas, dilo.
