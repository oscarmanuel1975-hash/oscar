---
name: verificacion-normativa
description: Regla de rigor para todo proyecto de gestoría o asesoría que dependa de normas, plazos, tipos, bases de cotización, convenios, sentencias o criterios de la Administración (BOE, DOG, EUR-Lex, AEAT, Seguridad Social, REGCON, AEPD, CENDOJ del CGPJ). Obliga a comprobar cada dato en la fuente oficial vigente, a citarlo con referencia y fecha, a separar lo verificado de lo pendiente y a no usar fuentes no fiables. Actívala SIEMPRE que se redacte, calcule o programe algo de gestoría con base normativa (nóminas, despidos, presupuestos, infografías, impuestos, plazos, apps que apliquen tipos o fechas), aunque no se pida verificar. Complementa a calculo-nominas-es, despido-objetivo-cartas, gestoria-integraciones-aapp, infografia-normativa-calvario, presupuesto-cliente-gestoria y rgpd-proteccion-datos.
---

# Verificación normativa con fuentes oficiales

Esta skill existe porque en trabajo jurídico, laboral y fiscal un dato inventado o desactualizado (un plazo, un tipo, un artículo mal numerado) tiene consecuencias reales para el cliente de la gestoría. La memoria del modelo sirve para orientarse, no para citar. Por eso la regla de fondo es simple: **ningún dato normativo llega a un documento, a un cálculo o a un código sin haber sido comprobado en una fuente oficial, o sin llevar una marca clara de que no lo ha sido.**

## Cómo trabajar

1. **Lista lo que vas a afirmar.** Antes de redactar, identifica cada dato normativo que el trabajo necesita: norma y artículo, plazo, porcentaje, importe, criterio de un organismo, sentencia, convenio aplicable. Esa lista es lo que hay que verificar.
2. **Busca cada dato en su fuente oficial** (ver `references/fuentes-oficiales.md`, que dice qué fuente es la competente para cada tipo de dato y qué se sabe de su acceso desde este entorno).
3. **Comprueba la vigencia.** Una norma puede estar derogada o modificada. Usa el texto consolidado del BOE y fíjate en la fecha de última actualización. Para ejercicios fiscales, años de cotización o convenios, confirma que el dato corresponde al año o periodo del caso.
4. **Registra la verificación.** Para cada dato anota: texto o cifra, fuente (nombre oficial y URL o identificador, por ejemplo `BOE-A-2018-16673`), fecha de consulta y estado.
5. **Etiqueta el estado con tres valores:**
   - **Verificado**: lo has leído tú en la fuente oficial durante este trabajo.
   - **Pendiente de contrastar**: lo conoces de memoria o de una fuente secundaria y no has podido abrir la oficial.
   - **No localizado**: lo buscaste y no lo encontraste. No lo sustituyas por una suposición.
6. **Si no puedes verificar, dilo.** Nunca rellenes el hueco con una cifra "razonable". Dile al usuario qué dato falta, dónde se consulta y, si procede, pídele el documento (por ejemplo el PDF del convenio) en lugar de adivinar.

## Qué fuentes valen y cuáles no

Valen: boletines oficiales (BOE, DOG, DOUE/EUR-Lex), webs de ministerios y organismos competentes (AEAT, Seguridad Social, Ministerio de Trabajo, AEPD, Xunta), la base de jurisprudencia del Consejo General del Poder Judicial (CENDOJ) y el registro de convenios (REGCON).

No valen como base de un dato: blogs, foros, redes sociales, resúmenes de despachos o de software comercial, ni respuestas generadas por IA sin fuente. Pueden servir para saber qué buscar, pero el dato se toma de la fuente oficial. Tampoco uses imágenes o capturas de terceros como prueba de una norma.

## En proyectos de gestoría

El uso principal de esta skill es el despacho. Consulta `references/ambito-gestoria.md`: por cada área (fiscal, laboral y Seguridad Social, mercantil, protección de datos, administración gallega) indica qué datos normativos suelen hacer falta, qué fuente es la competente y qué errores se repiten. Si el proyecto es una aplicación, los valores normativos no se escriben en el código sino en una tabla configurable con fuente, vigencia y fecha de verificación, de modo que cada cálculo pueda mostrar de dónde sale el dato. Las skills propias del despacho siguen mandando en su proceso; esta aporta la comprobación.

## Acceso real a las fuentes

Algunas webs oficiales bloquean la lectura automática o cambian de dirección. Si una fuente falla, prueba otra ruta oficial equivalente (por ejemplo, el texto consolidado del BOE o EUR-Lex en lugar de la página explicativa del organismo). Si sigue sin abrirse, no lo ocultes: marca el dato como **pendiente de contrastar** e indica la URL exacta para que el usuario o un profesional lo compruebe. Anota en el informe qué fuentes no se pudieron abrir.

## Jurisprudencia

Cita la resolución completa: órgano, fecha, número de recurso o resolución y su identificador en CENDOJ (ROJ/ECLI) cuando exista. Lee la resolución antes de citarla y no atribuyas doctrina a una sentencia que no has leído. Si no puedes abrirla, no la cites como apoyo; dilo.

## Formato de salida

Todo trabajo que use esta skill termina con una sección corta, escrita en lenguaje natural, con esta estructura:

- **Fuentes consultadas**, con referencia y fecha.
- **Datos verificados** y **datos pendientes de contrastar o no localizados**.
- **Conclusión final**: qué se puede afirmar con seguridad, qué no, y qué debe revisar un profesional antes de usarlo.

Los documentos para el cliente (cartas, informes, infografías) no deben mostrar el aparato de verificación entero; la tabla de estados va en el informe interno al usuario y el documento final lleva solo las citas necesarias. Redacta siempre con lenguaje natural, sin el tono de plantilla automática.

## Límites

Esta skill ordena la comprobación; no sustituye el criterio de un abogado, graduado social o asesor fiscal. Ante una cuestión interpretativa dudosa, expón las lecturas posibles con su fuente y recomienda revisión profesional en vez de elegir una en silencio.
