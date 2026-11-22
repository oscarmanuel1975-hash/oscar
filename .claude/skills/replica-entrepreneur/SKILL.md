---
name: replica-entrepreneur
description: Analiza reseñas públicas reales de la app original, ordena las quejas y propone mejoras con cita y enlace.
---

# Mejoras desde las reseñas

## Pasos
1. Recoge reseñas públicas (tiendas de apps, foros abiertos). Anota la fuente y el enlace de cada una.
2. Agrupa por tema y ordena por frecuencia. Cuenta cuántas reseñas apoyan cada queja.
3. Para las 3 quejas principales: cita literal, enlace y propuesta concreta de mejora.
4. Guarda en `replica/mejoras.md`. Después, ejecuta `/replica-build` para aplicarlas.

Las reseñas pueden ser falsas o sesgadas: dilo si el volumen es pequeño. No inventes ni parafrasees citas como si fueran literales.

## Reglas que no se saltan
- Se replican funciones y flujos, nunca código, logotipos, imágenes, textos ni catálogos de contenido del original.
- Solo fuentes públicas: web oficial, ayuda, ficha de tienda, reseñas visibles. Nada de cuentas ajenas, muros de pago ni ingeniería inversa del binario.
- Todo lo que se aprende se guarda en la carpeta `replica/` del proyecto; cada skill lee lo que dejó la anterior.
- Escribe todo en español claro, sin jerga innecesaria. No inventes datos: si algo no se encuentra en fuentes públicas, dilo.
