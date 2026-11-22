---
name: replica-test
description: Prueba caminos normales y raros de la app, corrige los fallos graves y deja las pruebas guardadas.
---

# Pruebas

## Casos mínimos
Flujo normal, campos vacíos, textos muy largos, decimales y redondeos, doble clic, cantidades negativas o cero, recarga a mitad de operación, y datos antiguos.

## Pasos
1. Escribe pruebas automáticas para la lógica y comprueba la interfaz de verdad cuando sea posible.
2. Corrige los fallos graves y repite hasta que pasen.
3. Informa con sinceridad de lo que falla o no se pudo probar.
4. Resumen en `replica/pruebas.md`.

## Reglas que no se saltan
- Se replican funciones y flujos, nunca código, logotipos, imágenes, textos ni catálogos de contenido del original.
- Solo fuentes públicas: web oficial, ayuda, ficha de tienda, reseñas visibles. Nada de cuentas ajenas, muros de pago ni ingeniería inversa del binario.
- Todo lo que se aprende se guarda en la carpeta `replica/` del proyecto; cada skill lee lo que dejó la anterior.
- Escribe todo en español claro, sin jerga innecesaria. No inventes datos: si algo no se encuentra en fuentes públicas, dilo.
