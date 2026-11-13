---
name: rgpd-proteccion-datos
description: Cumplimiento del RGPD (Reglamento UE 2016/679) y la LOPDGDD (LO 3/2018) en aplicaciones, documentos y procesos de una gestoría o asesoría que trata datos de clientes y trabajadores (DNI, IBAN, nóminas, bajas médicas, firmas, certificados, expedientes). Fija quién es responsable y quién encargado, revisa la seguridad de la app, la información al interesado, el registro de actividades, los contratos de encargado, la conservación y el bloqueo, las brechas y los derechos. Actívala SIEMPRE que se pida crear o revisar una app, base de datos, formulario, mandato, presupuesto o flujo que recoja, guarde o comparta datos personales, o se mencione RGPD, LOPD, AEPD, brecha, cláusula informativa, encargado del tratamiento, DPO o privacidad, aunque no se usen esas palabras. Úsala con equipo-desarrollo-software y apóyate en verificacion-normativa para citar artículos y plazos.
---

# RGPD y protección de datos en la gestoría

Una gestoría guarda justo los datos que más daño hacen si se filtran: identidad, cuentas bancarias, salarios, situación familiar y, a veces, salud. Por eso el cumplimiento no se deja para el final: se decide al diseñar. Esta skill sirve para eso: que cada aplicación o documento salga con la protección de datos incorporada, y que el usuario sepa con claridad qué ha quedado cubierto y qué debe revisar un profesional.

Todo dato normativo (artículo, plazo, cuantía) se comprueba siguiendo `verificacion-normativa`. En `references/fuentes-y-estado.md` está lo que ya se verificó en el BOE y lo que queda pendiente de contrastar; no cites como verificado nada que no esté ahí o que no hayas leído tú en la fuente durante el trabajo.

## Flujo de trabajo

### 1. Fija los roles antes de nada

De los roles depende todo lo demás (quién firma qué, quién responde ante la AEPD). En una gestoría suelen darse dos situaciones distintas, y conviene tratarlas por separado:

- **La gestoría como responsable**: datos de sus propios trabajadores, de sus clientes como contacto y facturación, de candidatos a empleo, de proveedores, de la web.
- **La gestoría como encargada del tratamiento**: datos que trata por cuenta de sus clientes (nóminas y altas de los trabajadores del cliente, contabilidad, libros de IVA, declaraciones). Aquí hace falta un contrato o acto jurídico que cumpla el artículo 28 del RGPD. El "Mandato" de la gestoría es el lugar natural para recoger esas cláusulas; si el mandato vigente no las contiene, es un hallazgo que hay que señalar.

Si el usuario no deja claro el rol, pregunta o deja el supuesto escrito. Si un proveedor externo toca datos (nube, correo, firma electrónica, un servicio de IA), la gestoría pasa a ser quien lo contrata como encargado y necesita su propio contrato con él.

### 2. Haz el mapa de datos

Para la aplicación o el proceso, anota qué datos se recogen, de quién, con qué finalidad, dónde se guardan, quién accede y a quién se comunican. Marca sobre todo:

- **Categorías especiales** (art. 9 RGPD): bajas por enfermedad o accidente, grado de discapacidad, afiliación sindical, datos de salud en una nómina o en un despido. Requieren condición específica de tratamiento y más cautela.
- **Datos de alto impacto, aunque no sean categoría especial**: DNI/NIE, IBAN, firma manuscrita, certificados digitales y apoderamientos, claves de acceso a sedes electrónicas, datos de menores (hijos en IRPF).
- **Datos que no hacen falta.** Cada campo que se pueda no pedir es un riesgo menos (minimización).

### 3. Revisa el diseño de la aplicación

Recorre `references/checklist-seguridad-app.md` y evalúa cada punto como cumple, no cumple o no aplica. Los puntos que más suelen fallar en herramientas internas de despacho son el control de acceso por expediente, el almacenamiento de certificados y claves, los entornos de prueba con datos reales, los registros de acceso y la ausencia de procedimiento de borrado. Propón la corrección concreta junto a cada fallo, no solo el aviso.

### 4. Comprueba los documentos que deben acompañar

Una aplicación cumple de verdad cuando existen, además del código, estos documentos. Indica cuáles faltan y ofrece redactarlos (modelos orientativos en `references/plantillas.md`):

- Registro de actividades de tratamiento.
- Información al interesado (en el formulario, en el mandato, en el presupuesto, en la web).
- Contrato de encargado del tratamiento, en los dos sentidos descritos arriba.
- Política de conservación y bloqueo.
- Procedimiento de brechas de seguridad (notificación a la AEPD en 72 horas desde que se tiene constancia, salvo que sea improbable que haya riesgo para las personas) y registro interno de incidentes.
- Procedimiento de atención de derechos (acceso, rectificación, supresión, oposición, limitación, portabilidad) con respuesta en el plazo de un mes.
- Valoración de si hace falta evaluación de impacto o delegado de protección de datos. La LOPDGDD lista entidades obligadas a designarlo; las gestorías no figuran como tales por su mera actividad, pero hay que valorar el caso concreto (tratamiento a gran escala, categorías especiales) y dejar la valoración por escrito.

### 5. Conservación y bloqueo

Los datos no se guardan "por si acaso". Cada categoría necesita un plazo y una razón. La LOPDGDD obliga a **bloquear** los datos cuando se rectifican o suprimen: se reservan, sin poder verlos ni tratarlos, solo a disposición de jueces, Ministerio Fiscal y Administraciones competentes durante el plazo de prescripción de las responsabilidades, y pasado ese plazo se destruyen. Los plazos de prescripción que sirven de referencia (tributarios, de Seguridad Social, mercantiles, de prevención del blanqueo) están en `references/fuentes-y-estado.md` con su estado de verificación. Si la aplicación no tiene función de bloqueo y borrado, hay que señalarlo.

### 6. Aplicaciones con inteligencia artificial o servicios externos

Si la aplicación envía datos personales a un servicio de IA, a un proveedor de nube o a una API de terceros, compruebe: contrato de encargado con ese proveedor, ubicación del tratamiento y posibles transferencias fuera del Espacio Económico Europeo, uso de los datos para entrenar modelos, y si pueden pseudonimizarse o quitarse antes de enviar. Si no se puede asegurar, la recomendación por defecto es no enviar datos identificativos.

## Informe final

Termina siempre con un informe en lenguaje natural, claro para alguien que no es informático, con esta estructura:

1. **Resumen en dos o tres frases** del estado de cumplimiento.
2. **Roles y datos tratados**, tal como los has entendido.
3. **Hallazgos**, ordenados por gravedad: qué falla, por qué importa y cómo se corrige.
4. **Documentos que faltan** y cuáles has preparado.
5. **Fuentes y estado de verificación** de cada dato normativo (verificado, pendiente de contrastar, no localizado).
6. **Conclusión final**: si la aplicación o el documento puede ponerse en uso tal cual, con cambios, o no todavía, y qué debe revisar un profesional (abogado o delegado de protección de datos) antes.

Si el entorno permite crear el documento, entrégalo en Word con el membrete de la gestoría, con las skills de documentos disponibles.

## Sanciones: cómo hablar de ellas

Menciona las sanciones solo para explicar por qué algo importa, nunca como amenaza vaga ni con cifras de memoria. Las cuantías máximas están en el artículo 83 del RGPD y deben contrastarse en EUR-Lex antes de citarlas. Los plazos de prescripción de las infracciones (tres años las muy graves, dos las graves, uno las leves) están verificados en la LOPDGDD, como consta en `references/fuentes-y-estado.md`.

## Límites

Esta skill ayuda a diseñar y revisar, pero no emite un dictamen jurídico. El cumplimiento real depende de cómo se use la aplicación en el día a día (quién accede, qué se envía por correo, qué se imprime). Indícalo en el informe. Ante dudas de interpretación, expón las alternativas con su fuente y recomienda consultar con un profesional o con la AEPD.
