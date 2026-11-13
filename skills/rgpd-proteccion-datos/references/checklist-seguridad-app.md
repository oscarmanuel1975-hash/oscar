# Lista de revisión de seguridad para aplicaciones de gestoría

El artículo 32 del RGPD exige medidas técnicas y organizativas adecuadas al riesgo. No fija una lista cerrada, así que esta es una lista de buenas prácticas para evaluar cada punto como cumple, no cumple o no aplica. Para cada fallo, proponer la corrección concreta.

## Acceso y autenticación
- Cada persona tiene su usuario propio; no hay cuentas compartidas.
- Contraseñas almacenadas con función de derivación adecuada (bcrypt, scrypt o argon2), nunca en claro ni con hash simple.
- Segundo factor de autenticación, al menos para administradores y para cualquier acceso desde fuera de la oficina.
- Permisos por rol y por expediente: cada trabajador ve solo los clientes que lleva. Un administrador técnico no necesita ver el contenido de las nóminas.
- Cierre de sesión por inactividad y bloqueo tras intentos fallidos.
- Baja inmediata de accesos cuando alguien deja el despacho.

## Protección de los datos
- Cifrado en tránsito (HTTPS con certificado válido en toda la aplicación).
- Cifrado en reposo de la base de datos y de las copias de seguridad.
- Cifrado adicional o enmascarado de campos de alto riesgo: IBAN, DNI/NIE, número de afiliación. Mostrar el dato completo solo cuando hace falta.
- Certificados digitales de clientes, claves de sedes electrónicas y apoderamientos guardados cifrados, con acceso restringido y registrado; nunca en el código ni en el repositorio.
- Firmas manuscritas escaneadas tratadas como dato personal, con el mismo nivel de protección que el documento al que acompañan.
- Secretos (claves de API, contraseñas de base de datos) en variables de entorno o un gestor de secretos, no en el código fuente.

## Trazabilidad
- Registro de accesos y de acciones sobre datos sensibles (consulta, descarga, modificación, borrado), con fecha y usuario, protegido frente a alteración.
- Alertas ante accesos anómalos (descargas masivas, accesos fuera de horario).
- Conservación de los registros durante un tiempo razonable y definido.

## Desarrollo y entornos
- Entornos de prueba y desarrollo sin datos reales; si hacen falta datos parecidos, usar datos ficticios o anonimizados.
- Dependencias actualizadas y revisadas; sin credenciales en el historial del repositorio.
- Validación de todas las entradas y protección frente a inyección y subida de archivos peligrosos.
- Mensajes de error que no revelen datos personales ni detalles internos.

## Ciclo de vida de los datos
- Cada categoría de dato tiene un plazo de conservación definido (ver `fuentes-y-estado.md`).
- La aplicación permite bloquear y, vencido el plazo, borrar o destruir de forma comprobable, incluidas las copias de seguridad.
- Exportación de los datos de un interesado en formato legible, para atender acceso y portabilidad.
- Función de rectificación y supresión que deje constancia de cuándo se hizo.

## Disponibilidad y recuperación
- Copias de seguridad periódicas, cifradas y probadas con restauración real.
- Plan básico de recuperación ante fallo, pérdida o ataque con cifrado malicioso.

## Comunicaciones
- Envío de documentos con datos personales por canal seguro (portal con acceso, o archivo cifrado con la clave por otra vía) en lugar de correo sin protección.
- Revisión de direcciones antes de enviar, para evitar el error más frecuente en la práctica: mandar el documento a otra persona.

## Terceros
- Lista de proveedores que tocan datos (alojamiento, correo, firma, copias, servicios de IA), con contrato de encargado firmado, ubicación del tratamiento y subencargados conocidos.
- Si hay transferencia fuera del Espacio Económico Europeo, base jurídica verificada para esa transferencia.

## Personas
- Quienes acceden a los datos están sujetos a confidencialidad por escrito y han recibido formación básica.
- Procedimiento claro para comunicar una sospecha de brecha de seguridad dentro del propio despacho, de manera que llegue pronto a quien decide.
