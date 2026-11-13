# Flujos típicos de una gestoría: rol, datos y puntos de control

Úsalo como guion cuando el proyecto sea de gestoría. Para cada flujo hay que confirmar el rol con el caso real, porque depende de cómo esté montado el servicio. Las bases jurídicas que aparecen son orientativas: las letras del artículo 6 del RGPD están pendientes de contrastar en EUR-Lex (ver `fuentes-y-estado.md`).

| Flujo | Rol habitual de la gestoría | Datos que aparecen | Puntos de control |
|---|---|---|---|
| Alta de cliente y presupuesto (web "Presupuestos Gestoría", skill `presupuesto-cliente-gestoria`) | Responsable | Identidad, contacto, tipo de actividad, a veces datos de empleados | Información al interesado en el formulario y en el documento; recoger solo lo necesario para presupuestar; plazo para borrar presupuestos no aceptados |
| Mandato y domiciliación SEPA (skill `mandato-sepa-cliente-gestoria`) | Responsable de los datos del cliente. Encargada de los datos de terceros que trate por su cuenta | Identidad, IBAN, firma dibujada, domicilio | El mandato es el sitio natural para las cláusulas del artículo 28 del RGPD si hay datos de terceros; IBAN y firma con protección reforzada; las plantillas se guardan en local, no en la nube, por decisión del usuario: respetarlo |
| Nóminas y seguros sociales (skill `calculo-nominas-es`) | Encargada por cuenta del empresario cliente | Identidad del trabajador, salario, situación familiar para el IRPF, bajas por enfermedad o accidente (categoría especial), embargos | Contrato de encargado con el cliente; acceso restringido a quien lleva laboral; datos de salud solo si son imprescindibles; envío de nóminas por canal seguro |
| Despidos y cartas (skill `despido-objetivo-cartas`) | Encargada por cuenta del empresario | Datos del trabajador, antigüedad, salario, causa del despido, posible afiliación sindical o salud | Circuito de revisión por abogado; borrar borradores y copias intermedias; conservar el documento final solo el tiempo que corresponda |
| Contabilidad, IVA, IRPF e Impuesto de Sociedades | Encargada por cuenta del cliente | Facturas con datos de terceros (clientes y proveedores del cliente), movimientos bancarios | Los datos de terceros llegan sin relación con la gestoría: se tratan solo para el encargo; conservación ligada a los plazos fiscales y mercantiles |
| Certificados digitales, apoderamientos y claves de sedes (AEAT, Seguridad Social, Xunta; skill `gestoria-integraciones-aapp`) | Encargada, con facultades de representación | Certificados con clave privada, claves de acceso, poderes | Es lo más delicado del despacho: cifrado, acceso nominal, registro de uso, revocación al terminar el encargo; no guardar claves en claro ni en el código |
| Portal o app de clientes | Responsable de las cuentas de usuario, encargada del contenido | Credenciales, documentos subidos | Autenticación fuerte, separación estricta entre clientes, registro de descargas, caducidad de enlaces |
| Correo y mensajería con clientes | Según el contenido | Adjuntos con datos personales | Evitar adjuntos sin protección; revisión de destinatario; aviso de confidencialidad no sustituye medidas |
| Plantilla del propio despacho y selección de personal | Responsable | Datos de empleados y candidatos | Información a candidatos, plazo de conservación de currículos, acceso limitado |
| Prevención del blanqueo de capitales | Responsable, como sujeto obligado | Documentación de identificación y diligencia debida | Plazo propio de conservación (verificado: diez años en el art. 25 de la Ley 10/2010) y acceso restringido pasado el quinto año |

## Cómo aplicarlo

1. Identifica en cuál de estos flujos cae el proyecto; muchos proyectos tocan varios.
2. Rellena para cada uno el rol, los datos y los puntos de control con las circunstancias reales del despacho.
3. Si el proyecto nuevo no encaja en ninguno, trátalo con el flujo general de la SKILL.md y anota el flujo nuevo para añadirlo aquí.
4. Cuando el flujo ya tiene su propia skill (nóminas, despidos, presupuesto, mandato, integraciones), no dupliques su lógica: remite a ella y limítate a la capa de protección de datos.
