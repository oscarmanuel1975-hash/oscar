---
name: replica-backend
description: Añade guardado de datos y, solo si hace falta, cuentas, pagos o correos a la app replicada.
---

# Datos y servicios

Parte de lo que ya hay construido. Por defecto: guardar todo lo que el usuario registra, sin cuentas ni pagos.

## Pasos
1. Implementa persistencia (local primero; servidor solo si el plan lo exige).
2. Si se piden cuentas, pagos o correo: propón el proveedor, explica el coste y espera confirmación.
3. Nunca escribas claves o secretos en el código; usa variables de entorno.
4. Protege los datos personales según el RGPD: solo los necesarios, con finalidad clara.
5. Anota todo en `replica/backend.md`.

## Reglas que no se saltan
- Se replican funciones y flujos, nunca código, logotipos, imágenes, textos ni catálogos de contenido del original.
- Solo fuentes públicas: web oficial, ayuda, ficha de tienda, reseñas visibles. Nada de cuentas ajenas, muros de pago ni ingeniería inversa del binario.
- Todo lo que se aprende se guarda en la carpeta `replica/` del proyecto; cada skill lee lo que dejó la anterior.
- Escribe todo en español claro, sin jerga innecesaria. No inventes datos: si algo no se encuentra en fuentes públicas, dilo.
