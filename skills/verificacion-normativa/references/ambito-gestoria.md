# Verificación en proyectos de gestoría

Para cada área del despacho: qué datos normativos suelen hacer falta, quién es la fuente competente y qué errores se cometen con más frecuencia. Aquí no hay cifras ni plazos a propósito: cualquier valor se toma de la fuente en cada trabajo.

## Fiscal (AEAT)
- **Datos que suelen hacer falta:** tipos de gravamen, retenciones, módulos y reducciones, modelos y su periodo de presentación, plazos de prescripción, régimen de facturación y registro (Veri\*Factu, SII).
- **Fuente:** texto consolidado de la ley en el BOE para el dato sustantivo; sede electrónica de la AEAT para modelos, instrucciones y calendario.
- **Errores frecuentes:** usar el tipo o el límite de un ejercicio anterior; confundir territorio común con territorio foral; tomar de un resumen comercial una fecha de presentación sin mirar la orden del modelo.

## Laboral y Seguridad Social
- **Datos que suelen hacer falta:** convenio colectivo aplicable, categoría, jornada, bases y tipos de cotización del año, cotizaciones por contingencias, plazos de alta y baja, causas y requisitos de cada extinción.
- **Fuente:** REGCON y boletín oficial donde se publicó el convenio (texto y tablas salariales de la revisión vigente); BOE para Estatuto de los Trabajadores y LGSS; Seguridad Social para bases y tipos.
- **Errores frecuentes:** aplicar un convenio sin comprobar ámbito, vigencia y prórroga; usar una tabla salarial caducada; citar un artículo del Estatuto de memoria; calcular una indemnización a mano en lugar de la calculadora oficial del CGPJ.

## Mercantil y contable
- **Datos que suelen hacer falta:** plazos de formulación y aprobación de cuentas, depósito en el Registro Mercantil, obligaciones de libros, plazos de conservación.
- **Fuente:** BOE (Código de Comercio, Ley de Sociedades de Capital, plan contable) y Registro Mercantil.
- **Errores frecuentes:** aplicar plazos sin mirar modificaciones recientes del texto consolidado.

## Protección de datos y prevención del blanqueo
- **Fuente:** BOE (LOPDGDD, Ley 10/2010), EUR-Lex (RGPD), AEPD y SEPBLAC para criterios.
- **Nota:** la web de la AEPD bloqueó la lectura automática en la última prueba; si no abre, marcar el criterio como pendiente de contrastar.

## Administración gallega
- **Datos que suelen hacer falta:** procedimientos y plazos de la Xunta, requisitos de sede electrónica, Chave365, normas publicadas en el DOG.
- **Fuente:** DOG y sede electrónica de la Xunta.
- **Errores frecuentes:** tratar como estatal un trámite o ayuda que es autonómico, y al revés.

## Jurisprudencia
- **Fuente:** CENDOJ (Consejo General del Poder Judicial). Leer la resolución antes de citarla.

## Hábitos específicos del despacho

1. **Comprobar el periodo.** En gestoría casi todo depende del ejercicio, del mes de cotización o de la fecha del hecho. Anota siempre el periodo al que corresponde el dato.
2. **Un dato, una fuente.** Si dos fuentes oficiales discrepan, no elijas: expón las dos y señala cuál es la competente.
3. **Los cálculos se reproducen.** Si el resultado es un importe (nómina, indemnización, cuota), guarda los datos de entrada con su fuente, para que otra persona del despacho pueda repetir el cálculo.
4. **Lo que va al cliente va limpio.** El informe interno lleva el estado de verificación; la carta, el presupuesto o la infografía llevan solo la cita necesaria.
5. **Integración con las demás skills.** Cuando se use `calculo-nominas-es`, `despido-objetivo-cartas`, `gestoria-integraciones-aapp`, `infografia-normativa-calvario`, `presupuesto-cliente-gestoria` o `mandato-sepa-cliente-gestoria`, esta skill aporta la comprobación de los datos normativos y ellas aportan el proceso propio. Sus reglas más estrictas prevalecen.
6. **Software de gestoría.** Si el proyecto es una aplicación, los valores normativos (tipos, plazos, bases) no se escriben en el código: van en una tabla configurable con su fuente, su fecha de vigencia y la fecha de última verificación. Así se pueden actualizar sin tocar la lógica, y cada cálculo puede enseñar de dónde sale el dato.
