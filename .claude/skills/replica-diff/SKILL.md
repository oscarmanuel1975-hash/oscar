---
name: replica-diff
description: Compara la réplica con el mapa de la original: porcentaje de funciones cubiertas y qué falta, por importancia.
---

# Comparación con el original

Contrasta `replica/mapa.md` con lo construido, función por función.

## Salida: `replica/diff.md`
- Tabla: función, prioridad, estado (hecha / parcial / falta).
- Porcentaje de funciones núcleo y totales cubiertas, mostrando la cuenta.
- Lo que falta, de más a menos importante.

## Reglas que no se saltan
- Se replican funciones y flujos, nunca código, logotipos, imágenes, textos ni catálogos de contenido del original.
- Solo fuentes públicas: web oficial, ayuda, ficha de tienda, reseñas visibles. Nada de cuentas ajenas, muros de pago ni ingeniería inversa del binario.
- Todo lo que se aprende se guarda en la carpeta `replica/` del proyecto; cada skill lee lo que dejó la anterior.
- Escribe todo en español claro, sin jerga innecesaria. No inventes datos: si algo no se encuentra en fuentes públicas, dilo.
