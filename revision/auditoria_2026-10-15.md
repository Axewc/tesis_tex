# Auditoría del borrador de tesis

**Tesis:** Sesgo socioeconómico en modelos de clasificación automática de texto: un enfoque sociotécnico para su detección y medición  
**Tesista:** Axel Casas Espinosa · **Director:** M. en C.I.C. Manuel Soto Romero  
**Fecha de revisión:** 15 de octubre de 2026 · **Versión revisada:** [`49e5633`](https://github.com/Axewc/tesis_tex/tree/49e5633e159625aaf7cc4c2c3bd3bf21262be788)

> Lectura crítica preparada por Claude en el papel de asesor. Complementa la revisión de tu director de tesis; no la sustituye.
>
> Versión interactiva, con filtros y seguimiento del estado de cada observación: https://claude.ai/artifact/MZtvi81Zs6LDQRmfo8hhHk

**52 observaciones:** 6 críticas, 33 mayores, 13 menores. Las líneas citadas remiten a la versión revisada.

## Lo que entiendo que propones

Propones auditar clasificadores de texto en español con un diseño de pares: el mismo contenido (por ejemplo, un currículum) escrito en dos registros, uno estándar y otro asociado a posiciones sociales estigmatizadas. Si el modelo decide distinto ante los dos textos, eso cuenta como evidencia de sesgo sociolectal. El Índice de Neutralidad Sociolectal (INS) resume esa consistencia: la proporción de pares con la misma decisión, o uno menos la divergencia media entre las probabilidades. Una encuesta a jóvenes de 18 a 30 años aporta el contexto social y, a través de la pregunta A3, los rasgos lingüísticos que entrarán al benchmark.

*Si esta lectura no coincide con lo que quieres hacer, esa diferencia es la primera observación que hay que discutir.*

## Dictamen

El proyecto es viable para una licenciatura y ya tiene una parte madura: el Capítulo 5 piensa con cuidado qué mide y qué no mide el índice. Lo que falta son decisiones de diseño, más que redacción. Hoy no está definida la tarea de clasificación, no está sostenido el paso de «registro» a «nivel socioeconómico» que da título a la tesis, y el experimento no tiene una condición de control que permita atribuir los cambios de decisión al registro. Mientras esas tres decisiones sigan abiertas, los capítulos 4, 6 y 7 no se pueden escribir y es probable que haya que rehacer parte del Capítulo 3.

### Lo que ya funciona

- El Capítulo 5 anticipa las objeciones fuertes: el clasificador constante con INS = 1, la falta de dirección, la dependencia del benchmark y el no determinismo de los LLM.
- Anclar el estudio en un daño concreto (el filtrado de currículums), siguiendo a Blodgett et al., le da a la pregunta un porqué.
- El instrumento de encuesta está cuidado: viñetas para reducir la deseabilidad social, preguntas abiertas de lo concreto a lo abstracto y Likert tratado como ordinal.
- La sección de ética considera el uso dual del benchmark, algo poco común en tesis de licenciatura.
- La infraestructura es sólida: compilación en CI, pruebas unitarias del calculador y datos de participantes fuera del control de versiones.

## Por dónde empezar

En este orden: cada paso depende del anterior.

1. Define la tarea, las etiquetas y los modelos concretos. Todo lo demás depende de esto. (P-02)
2. Decide el constructo: sensibilidad al registro o sesgo socioeconómico. Si eliges lo segundo, agrega un chequeo con jueces de la posición social percibida. (P-01)
3. Escribe el protocolo del benchmark con tres condiciones: texto idéntico, paráfrasis en el mismo registro y variación de registro. (B-01, X-01)
4. Agrega una medida con dirección y un experimento que valide el índice con sesgo conocido. (I-02, I-04)
5. Consigue la bibliografía mexicana de O1 y prepara una tipología de rasgos que no dependa del calendario de la encuesta. (M-02, E-02)
6. Resuelve el aval ético y el aviso de privacidad antes de difundir el piloto. (ET-01)

## La cadena argumental

| # | Eslabón | Estado | Por qué |
|---|---|---|---|
| 1 | Las personas sancionan socialmente ciertas formas de hablar y escribir. | Sostenido | Literatura general citada (Weissler 2022; Drożdżowicz 2024). Falta evidencia del caso mexicano. |
| 2 | En el español escrito de México, rasgos concretos funcionan como marcadores de clase. | Sin sustento | Tres marcas [FUENTE MX] abiertas. Hoy se apoya en conocimiento común (naco, fresa, anglicismos). |
| 3 | Los modelos de PLN aprenden de texto humano y pueden heredar esas sanciones. | Sostenido | Sap et al. 2019; Caliskan et al. 2017; Hovy y Prabhumoye 2021. |
| 4 | Un par controlado cambia el registro sin cambiar el contenido. | Sin sustento | Supuesto sin protocolo: no se dice quién escribe las variantes ni cómo se valida la equivalencia. |
| 5 | Si el modelo decide distinto ante el par, la causa es el registro. | Débil | Falta una condición de control con paráfrasis del mismo registro. |
| 6 | Ese cambio perjudica a personas de menor nivel socioeconómico. | Sin sustento | El INS no tiene dirección y no se valida que la variante se perciba como de otra clase social. |
| 7 | El INS mide la neutralidad del sistema. | Débil | Mide consistencia; un clasificador constante resulta «neutral». El propio Cap. 5 lo reconoce. |

## Estado del borrador

| Parte | Estado | Prosa (≈ palabras) | Marcas | En blanco |
|---|---|---:|---:|---:|
| Resumen | Redactado como plan | 370 | 0 | 0 |
| 1 · Introducción | Redactado; faltan hipótesis | 910 | 0 | 0 |
| 2 · Marco teórico | Redactado; faltan fuentes mexicanas y trabajo relacionado | 2,610 | 5 | 4 |
| 3 · Metodología | Parcial: encuesta y ética redactadas; revisión documental, benchmark y experimentos en blanco | 1,880 | 12 | 15 |
| 4 · Resultados | Plantilla | 85 | 0 | 9 |
| 5 · Índice INS | Redactado salvo 5.4 (aplicación a resultados) | 2,430 | 2 | 2 |
| 6 · Discusión | Plantilla | 50 | 0 | 8 |
| 7 · Conclusiones | Plantilla | 75 | 0 | 5 |
| Ap. A · Encuesta | Completo, listo para discutir | 735 | 3 | 2 |
| Ap. B · Corpus | Plantilla | 10 | 0 | 2 |

«Marcas» cuenta [DECIDIR], [PENDIENTE], [VERIFICAR] y [FUENTE] visibles en el PDF; «En blanco», los párrafos de plantilla entre corchetes.

## Observaciones

Severidad: **Crítico**, compromete la validez de la tesis; **Mayor**, resolver antes de la entrega; **Menor**, pulido y consistencia.

### Planteamiento

#### P-01 · Crítico · El título dice «socioeconómico»; el experimento mide «registro»

- [ ] Atendida

El título habla de sesgo socioeconómico. La pregunta habla de registro «o» sociolecto, como si fueran lo mismo. Tu propio Capítulo 2 los distingue: el registro es la variación de un mismo hablante según la situación (formal o coloquial) y el sociolecto es la variedad de un grupo social. Los rasgos que planeas manipular (léxico coloquial, ortografía, anglicismos, longitud de oración) son sobre todo de registro: cualquier persona, de cualquier origen, escribe informal en algún contexto. Que un modelo penalice lo informal muestra sensibilidad al registro. Para llamarlo sesgo socioeconómico falta un eslabón: evidencia de que la variante t′ se lee como escrita por alguien de menor nivel socioeconómico.

**Preguntas para ti**

- ¿Tu tesis estudia la sensibilidad de los modelos al registro, o el sesgo contra rasgos que indexan clase social? Son dos tesis distintas.
- Si una persona de clase alta escribe su CV en registro coloquial, ¿el par resultante mide sesgo socioeconómico?
- ¿Qué evidencia, dentro de tu diseño, mostrará que t′ se percibe como de clase baja y no solo como informal?

**Qué haría.** Elige el constructo y alinea título, pregunta, objetivos y resumen. Opción A: hablar de sensibilidad al registro; es más defendible y no exige probar el vínculo con la clase social. Opción B: mantener «socioeconómico» y agregar un chequeo de manipulación, en el que jueces humanos estiman la posición social percibida de quien escribió cada variante y solo entran al benchmark las variantes con una diferencia percibida clara. La opción B convierte el benchmark en un matched guise (M-05); es más fuerte y cuesta más.

**Dónde:** [`portada.tex:30-33`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/portada.tex#L30-L33) · [`resumen.tex:15-18`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/frontmatter/resumen.tex#L15-L18) · [`01_introduccion.tex:56-63`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/capitulos/01_introduccion.tex#L56-L63) · [`02_marco_teorico.tex:256-264`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/capitulos/02_marco_teorico.tex#L256-L264)

#### P-02 · Crítico · La tarea de clasificación no está definida

- [ ] Atendida

«Definición exacta de la tarea» sigue siendo un marcador. De esa decisión dependen el tipo de texto del benchmark, los modelos posibles, las etiquetas, las métricas de desempeño y, sobre todo, si la sensibilidad al registro es un defecto. El escenario que motiva la tesis es el filtrado de currículums, pero la Sección 3.6 dice que evaluarás «modelos preentrenados disponibles públicamente». No conozco clasificadores públicos de CVs en español; lo publicado son modelos de sentimiento, discurso de odio o tópico. Si entrenas uno propio, necesitas datos con etiquetas «apto / no apto», que no existen en abierto. Y en una tarea como «detectar tono profesional» el modelo debe ser sensible al registro, de modo que un INS bajo sería lo correcto.

**Preguntas para ti**

- ¿Qué tarea, qué conjunto de etiquetas y qué modelos concretos (nombre, versión, origen)?
- ¿Por qué en esa tarea el registro no debería influir en la decisión?
- Si la tarea no es filtrado de CVs, ¿cómo conectas los resultados con la motivación del Capítulo 1?

**Qué haría.** Decide esto antes que cualquier otra cosa. Para una licenciatura hay dos rutas viables: (a) un LLM usado como evaluador de CVs con una rúbrica fija y un puesto definido, que es realista y no requiere datos de entrenamiento; (b) modelos públicos en español de sentimiento u odio como segundo escenario, con la limitación declarada. Documenta la elección en la Sección 3.5 con nombre y versión de cada modelo.

**Dónde:** [`03_metodologia.tex:270-282`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/capitulos/03_metodologia.tex#L270-L282) · [`03_metodologia.tex:337-340`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/capitulos/03_metodologia.tex#L337-L340) · [`05_indice_ins.tex:239-243`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/capitulos/05_indice_ins.tex#L239-L243)

#### P-03 · Mayor · No hay hipótesis contrastables

- [ ] Atendida

«¿En qué medida…?» admite cualquier resultado como respuesta. Sin predicciones explícitas los datos no pueden contradecirte, y un sinodal lo va a notar.

**Preguntas para ti**

- ¿Qué esperas encontrar?
- ¿Qué resultado te haría concluir que los modelos no tienen sesgo sociolectal?

**Qué haría.** Formula dos o tres hipótesis operativas antes de correr experimentos. Por ejemplo: H1, para al menos un modelo, la tasa de cambio de decisión en pares de registro supera a la de pares de paráfrasis del mismo registro; H2, los cambios favorecen sistemáticamente a la variante estándar; H3, la magnitud difiere entre familias de modelos. Fija de antemano la prueba y el umbral con que las evaluarás.

**Dónde:** [`01_introduccion.tex:56-63`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/capitulos/01_introduccion.tex#L56-L63)

#### P-04 · Mayor · «No afecta el contenido sustantivo» es un supuesto que hay que defender

- [ ] Atendida

Afirmas que si dos textos comunican el mismo contenido «no existe ninguna variación legítima» que justifique un trato distinto. Eso depende del contexto. En un puesto donde redactar es parte del trabajo, la forma es información. Tu propia encuesta lo reconoce: el ítem L9 pregunta si es justo filtrar por «calidad de redacción». Las faltas de ortografía son el caso más delicado: se relacionan con el acceso a la educación, pero muchos evaluadores las considerarían una señal legítima.

**Preguntas para ti**

- ¿Las faltas de ortografía en un CV son registro o información relevante? ¿Para qué puestos?
- ¿Con qué criterio separas la variación estigmatizada de la variación con relevancia legítima?

**Qué haría.** Agrega un argumento normativo explícito y acota el escenario a puestos donde la escritura no es una competencia evaluada. En el benchmark, separa los rasgos claramente irrelevantes (léxico coloquial, marcadores discursivos) de los discutibles (ortografía) y repórtalos por separado.

**Dónde:** [`resumen.tex:15-18`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/frontmatter/resumen.tex#L15-L18) · [`02_marco_teorico.tex:81-89`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/capitulos/02_marco_teorico.tex#L81-L89) · [`02_marco_teorico.tex:266-270`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/capitulos/02_marco_teorico.tex#L266-L270)

#### P-05 · Mayor · El objetivo general promete medir equidad; el INS mide consistencia

- [ ] Atendida

El objetivo general dice que el INS medirá «el grado de equidad lingüística». El Capítulo 5 dice, con razón, que el INS no es una medida completa de equidad y que un clasificador constante obtiene INS = 1. El objetivo promete más de lo que el capítulo entrega.

**Qué haría.** Reformula, por ejemplo: «…proponer un indicador que mida la consistencia de dichos sistemas ante variaciones de registro, como componente de una evaluación de equidad».

**Dónde:** [`01_introduccion.tex:68-75`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/capitulos/01_introduccion.tex#L68-L75)

#### P-06 · Menor · Referencias cruzadas y nombres que no coinciden

- [ ] Atendida

Varias piezas del documento se contradicen en detalles:

- Alcances dice que el benchmark se describe en el capítulo de resultados; su diseño está en la Sección 3.4.
- Contribuciones promete «un protocolo experimental reproducible» y la sección de reproducibilidad (3.5) está vacía.
- El Capítulo 2 menciona BETO como candidato; el 3 agrega «RoBERTa en español» sin decir cuál.
- El par controlado se define dos veces: en la Sección 3.4 y en la Definición 5.1.
- La portada dice «Director de tesis»; el README y `tesis.tex` dicen «Asesor». Usa la nomenclatura de la Facultad.

**Qué haría.** Deja una sola definición de par controlado y referénciala. Revisa estas referencias cuando cierres el diseño.

**Dónde:** [`01_introduccion.tex:100-104`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/capitulos/01_introduccion.tex#L100-L104) · [`01_introduccion.tex:115-129`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/capitulos/01_introduccion.tex#L115-L129) · [`portada.tex:60`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/portada.tex#L60)

### Marco teórico

#### M-01 · Mayor · Falta una sección de trabajo relacionado y la novedad no está demostrada

- [ ] Atendida

Afirmas que la variación sociolectal del español mexicano está «sistemáticamente ausente» de los benchmarks de equidad. Puede ser cierto, pero hay que mostrarlo. El Capítulo 2 es conceptual y no revisa los trabajos más cercanos al tuyo: sesgo dialectal en PLN (Blodgett et al., 2016; Sap et al., 2019), prejuicio dialectal encubierto en LLM con decisiones de empleabilidad (Hofmann et al., 2024), equidad contrafáctica en clasificación de texto (Garg et al., 2019), sensibilidad a perturbaciones (Prabhakaran et al., 2019), pruebas de invariancia (Ribeiro et al., 2020) y benchmarks de robustez dialectal (Ziems et al., 2022 y 2023).

**Preguntas para ti**

- ¿Qué búsqueda hiciste para afirmar que no existe trabajo equivalente en español?
- ¿En qué se distingue tu propuesta de Hofmann et al. (2024), que compara decisiones de un LLM ante el mismo contenido en inglés afroamericano y en inglés estándar?

**Qué haría.** Agrega una sección de trabajo relacionado con una tabla comparativa: trabajo, lengua, variedad, tarea, método y métrica. Tu aporte queda definido por lo que ninguna fila cubre (por ejemplo: español de México, registro asociado a clase, filtrado de CVs).

**Dónde:** [`02_marco_teorico.tex:153-160`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/capitulos/02_marco_teorico.tex#L153-L160) · [`01_introduccion.tex:35-47`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/capitulos/01_introduccion.tex#L35-L47)

#### M-02 · Crítico · El núcleo del objetivo O1 no tiene ninguna fuente

- [ ] Atendida

La Sección 2.4 sostiene el objetivo O1 y hoy no cita nada. La caracterización de marcadores (léxico, anglicismos como capital cultural, «naco» y «fresa») descansa en conocimiento común, y de ella sale la tipología del benchmark. Hay tres marcas [FUENTE MX] abiertas. Sin estas fuentes O1 no se cumple y el segundo eslabón de la cadena argumental queda vacío.

**Preguntas para ti**

- ¿Qué rasgos del español escrito en México tienen documentación empírica como marcadores de clase y cuáles son solo estereotipo?
- ¿Hay trabajo sobre escritura, además de habla? La mayor parte de la sociolingüística variacionista estudia pronunciación.

**Qué haría.** Revisa la lista de lecturas sugeridas al final de este documento: encuestas nacionales sobre discriminación, sociolingüística del español de México y trabajos sobre clase y color de piel. Verifica cada referencia antes de citarla.

**Dónde:** [`02_marco_teorico.tex:288-291`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/capitulos/02_marco_teorico.tex#L288-L291) · [`02_marco_teorico.tex:313-328`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/capitulos/02_marco_teorico.tex#L313-L328) · [`02_marco_teorico.tex:330-351`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/capitulos/02_marco_teorico.tex#L330-L351)

#### M-03 · Mayor · La definición de sesgo necesita tolerancia y un puente del texto a la persona

- [ ] Atendida

La Definición 2.1 tiene tres problemas:

- La desigualdad μ(f | A = a) ≠ μ(f | A = a′) se cumple casi siempre en una muestra finita. Hace falta una tolerancia ε o un criterio estadístico.
- μ queda sin especificar: ¿tasa de clase favorable, exactitud, calibración?
- A se define «sobre la población de entradas». El registro es un atributo del texto y el daño recae en personas. El paso del texto al grupo social es justo el que P-01 señala como faltante.

**Qué haría.** Define el sesgo con un umbral o una prueba, fija μ para tu caso (por ejemplo, la tasa de decisión favorable) y explicita el supuesto que liga el registro del texto con el grupo social de quien escribe.

**Dónde:** [`02_marco_teorico.tex:68-79`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/capitulos/02_marco_teorico.tex#L68-L79)

#### M-04 · Mayor · Comparar «complejidad creciente» no permite atribuir efectos a la complejidad

- [ ] Atendida

Un clasificador TF-IDF, BETO ajustado y un LLM zero-shot difieren en datos de entrenamiento, tamaño, tokenización y forma de producir la decisión. Si el INS cambia entre ellos, no puedes atribuirlo a la complejidad. Además, la afirmación de que los modelos amplifican las regularidades del entrenamiento necesita cita (por ejemplo, Zhao et al., 2017).

**Qué haría.** Presenta la comparación como descriptiva entre sistemas representativos de cada familia y retira la promesa de observar si el sesgo «varía con la complejidad».

**Dónde:** [`02_marco_teorico.tex:140-151`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/capitulos/02_marco_teorico.tex#L140-L151) · [`02_marco_teorico.tex:219-233`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/capitulos/02_marco_teorico.tex#L219-L233)

#### M-05 · Mayor · Faltan los antecedentes metodológicos directos: matched guise y estudios de correspondencia

- [ ] Atendida

Tu diseño de pares es una versión computacional de dos métodos clásicos. La técnica de matched guise de la psicología social del lenguaje (Lambert et al., 1960) presenta el mismo contenido en dos variedades y compara los juicios. Los estudios de correspondencia con currículums en economía laboral (Bertrand y Mullainathan, 2004; para México, Arceo-Gómez y Campos-Vázquez, 2014) envían CVs equivalentes que difieren en un solo atributo. Ambas tradiciones tienen décadas de discusión sobre confusores, chequeos de manipulación y validez ecológica que te ahorran trabajo y te dan legitimidad ante el jurado.

**Qué haría.** Presenta el benchmark como un matched guise aplicado a clasificadores y toma de esa literatura los controles de diseño (B-01, B-02).

**Dónde:** [`03_metodologia.tex:241-251`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/capitulos/03_metodologia.tex#L241-L251)

#### M-06 · Menor · Citas que no respaldan exactamente lo afirmado y marcas [VERIFICAR]

- [ ] Atendida

Bender et al. (2021) se usa para afirmar que los LLM zero-shot son «especialmente difíciles de auditar» ante el registro; el artículo trata riesgos de escala y de datos, no clasificación zero-shot. La marca [VERIFICAR] sobre tamaño y diversidad parece corresponder a una sección de ese mismo artículo («Size Doesn't Guarantee Diversity»); confírmalo y cierra la marca. La caracterización de Drożdżowicz (2024) sigue sin verificar.

**Qué haría.** Lee las fuentes primarias de las tres afirmaciones y ajusta la redacción a lo que dicen. Para la dificultad de auditar LLM, busca literatura sobre sensibilidad al prompt.

**Dónde:** [`02_marco_teorico.tex:107-110`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/capitulos/02_marco_teorico.tex#L107-L110) · [`02_marco_teorico.tex:228-231`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/capitulos/02_marco_teorico.tex#L228-L231) · [`02_marco_teorico.tex:279-283`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/capitulos/02_marco_teorico.tex#L279-L283)

#### M-07 · Menor · Dialecto, sociolecto y registro se definen sin cita

- [ ] Atendida

Son conceptos con tradiciones teóricas distintas y conviene anclarlos en un manual de sociolingüística. La frase «estas dimensiones se entrecruzan» es donde se esconde el problema de P-01: merece un párrafo propio.

**Qué haría.** Cita un manual (por ejemplo, Moreno Fernández) y desarrolla el cruce entre registro y sociolecto, porque tu diseño depende de él.

**Dónde:** [`02_marco_teorico.tex:256-264`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/capitulos/02_marco_teorico.tex#L256-L264)

### Encuesta

#### E-01 · Mayor · La parte Likert no responde a ninguna pregunta de la tesis

- [ ] Atendida

La única conexión de la encuesta con el experimento es A3. Los doce ítems Likert y las comparaciones por nivel socioeconómico (Mann–Whitney, Kruskal–Wallis) no alimentan el benchmark ni el INS, y ningún objetivo específico las pide. El riesgo es entregar dos trabajos pegados: uno de percepción y otro computacional.

**Preguntas para ti**

- ¿Qué cambia en tus conclusiones si los grupos de D6 y D7 difieren, o no, en L1 a L4?
- ¿A qué objetivo específico responde cada bloque del cuestionario?

**Qué haría.** Hay dos salidas. Recortar la encuesta a lo que alimenta el diseño (A2, A3 y la caracterización), o integrarla de verdad: L7 es una predicción lega del experimento («el filtro las evaluaría igual»), y en la discusión puedes contrastarla con el comportamiento medido del modelo. Comparar percepción con comportamiento medido es lo que justificaría llamar sociotécnico al estudio.

**Dónde:** [`03_metodologia.tex:54-65`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/capitulos/03_metodologia.tex#L54-L65) · [`03_metodologia.tex:159-178`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/capitulos/03_metodologia.tex#L159-L178) · [`03_metodologia.tex:192-200`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/capitulos/03_metodologia.tex#L192-L200)

#### E-02 · Mayor · A3 recoge creencias sobre lo que se penaliza, no marcadores sociolectales

- [ ] Atendida

«¿Qué palabras crees que una empresa vería mal?» produce opiniones sobre lo que castigan las empresas (groserías, faltas de ortografía, emojis), no una descripción de cómo escriben distintos grupos. Con una muestra que nace en una red universitaria, además, recogerás la idea que personas con escolaridad alta tienen de cómo escriben otras. Derivar la tipología solo de A3 puede producir un benchmark de estereotipos. Y el diseño actual hace que el benchmark espere a que termine la encuesta.

**Preguntas para ti**

- ¿Qué harás si A3 trae respuestas escasas, vagas o solo groserías?
- ¿Quién decide qué rasgos entran a la tipología, y con qué regla?

**Qué haría.** Usa A3 como una de tres fuentes (literatura sociolingüística, corpus reales y A3) y escribe desde ya una tipología preliminar basada en la literatura, para no depender del calendario de la encuesta. Una idea: las respuestas A1 y A2 son escritura auténtica de personas con origen socioeconómico conocido (D6, D7). Si el consentimiento lo cubre, compararlas te daría rasgos observados en lugar de rasgos imaginados.

**Dónde:** [`03_metodologia.tex:141-149`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/capitulos/03_metodologia.tex#L141-L149) · [`A_encuesta.tex:152-154`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/apendices/A_encuesta.tex#L152-L154)

#### E-03 · Mayor · La muestra tendrá poca variación en la variable que te interesa

- [ ] Atendida

La bola de nieve desde tus contactos en la UNAM concentrará la muestra en escolaridad alta. «Dirigir deliberadamente la difusión» no es un procedimiento que alguien pueda verificar o repetir. Si los grupos de menor nivel socioeconómico quedan con pocas personas, las comparaciones de la Sección 3.3.3 no serán interpretables.

**Qué haría.** Fija cuotas mínimas por categoría de D6 y D7, nombra los canales concretos de difusión y, al cerrar, compara la composición de la muestra con una referencia nacional para mostrar cuánto se desvía.

**Dónde:** [`03_metodologia.tex:80-98`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/capitulos/03_metodologia.tex#L80-L98)

#### E-04 · Mayor · Alfa de Cronbach sobre bloques que no son escalas

- [ ] Atendida

Los bloques mezclan constructos. L5 a L9 incluyen una creencia (L5), una preocupación (L6), una predicción ante un escenario (L7), una sospecha (L8) y un juicio normativo (L9). Alfa supone una escala unidimensional; con dos a cuatro ítems heterogéneos dará valores bajos o engañosos. Además, la Tabla 3.1 agrupa L5 a L9 como un solo constructo y el texto los divide en dos bloques.

**Qué haría.** Analiza ítem por ítem (frecuencias, mediana, rango intercuartílico) y omite alfa. Si quieres escalas, diseña al menos cuatro ítems por constructo y pruébalas en el piloto.

**Dónde:** [`03_metodologia.tex:183-190`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/capitulos/03_metodologia.tex#L183-L190) · [`03_metodologia.tex:170-172`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/capitulos/03_metodologia.tex#L170-L172)

#### E-05 · Mayor · Contrastes por grupo sin tamaño muestral ni corrección

- [ ] Atendida

Doce ítems por dos variables proxy son al menos 24 pruebas con α = 0.05: cabe esperar alrededor de un falso positivo aunque no exista ninguna diferencia real. No hay tamaño muestral objetivo ni reglas para agrupar las cinco categorías de D6 y las cuatro de D7.

**Preguntas para ti**

- ¿Cuál es la n mínima por grupo?
- ¿Qué tamaño de efecto vas a reportar?

**Qué haría.** Fija la n objetivo y las reglas de agrupación antes de levantar. Corrige por comparaciones múltiples (Holm o Benjamini–Hochberg), o declara el análisis exploratorio y reporta solo tamaños de efecto con intervalos de confianza.

**Dónde:** [`03_metodologia.tex:192-200`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/capitulos/03_metodologia.tex#L192-L200)

#### E-06 · Mayor · Modelado de temas y sentimiento en un corpus pequeño

- [ ] Atendida

Con decenas o pocos cientos de respuestas cortas, LDA y BERTopic producen temas inestables que cambian con la semilla. El análisis de sentimiento de relatos sobre discriminación dará, previsiblemente, «negativo». Y la normalización (minúsculas, lematización, quitar palabras funcionales) borra justo los rasgos de registro que te interesan.

**Preguntas para ti**

- ¿Cuántas respuestas abiertas esperas?
- ¿Qué decisión de la tesis depende del análisis de sentimiento?

**Qué haría.** Usa análisis temático cualitativo con libro de códigos (Braun y Clarke, 2006) y doble codificación de una submuestra con acuerdo reportado. Las técnicas automáticas pueden quedar como apoyo exploratorio.

**Dónde:** [`03_metodologia.tex:202-239`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/capitulos/03_metodologia.tex#L202-L239)

#### E-07 · Menor · Ajustes puntuales al instrumento

- [ ] Atendida

Antes del piloto conviene corregir:

- L7 no es la inversión de un ítem del bloque: es una viñeta. Con dos ítems invertidos no se detecta la aquiescencia de forma confiable.
- L9 junta dos ideas («es justo» y «aunque el puesto no requiera escribir») y pide un juicio normativo, no una percepción.
- L10 pregunta por exposición (sí o no) en una escala de acuerdo; conviene una pregunta dicotómica o de frecuencia.
- L11 depende de L10: quien no ha usado estos sistemas no puede responderla. Agrega un salto lógico o la opción «no aplica».
- D2 como texto libre generará variantes («CDMX», «Ciudad de México», «DF»). Usa la lista de las 32 entidades.
- D4 pregunta por el último nivel concluido; entre los 18 y 22 años casi todos tienen la licenciatura en curso. Agrega «en curso».
- El rango de 18 a 30 años se justifica como el de «mayor exposición» a evaluación automatizada, sin fuente.
- El consentimiento no tiene correo de contacto ni dice dónde y por cuánto tiempo se guardan los datos.

**Dónde:** [`A_encuesta.tex:52-73`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/apendices/A_encuesta.tex#L52-L73) · [`A_encuesta.tex:89-138`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/apendices/A_encuesta.tex#L89-L138) · [`A_encuesta.tex:44`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/apendices/A_encuesta.tex#L44)

### Benchmark

#### B-01 · Crítico · No hay protocolo para verificar que el par difiera solo en registro

- [ ] Atendida

Cambiar el registro casi siempre cambia algo más: longitud, especificidad, connotación. «Chambeé en un changarro» y «laboré en un comercio pequeño» no comunican lo mismo a un reclutador. Hoy la equivalencia se verifica «mediante revisión humana y similitud semántica», sin decir cuántos jueces, con qué instrucciones, con qué acuerdo mínimo, con qué modelo de similitud ni con qué umbral. La validez de todo el INS depende de esta operación, y el propio Capítulo 5 lo reconoce.

**Preguntas para ti**

- ¿Quién juzga la equivalencia, con qué escala y con qué acuerdo mínimo entre jueces?
- ¿Qué haces con los pares que no pasan el filtro?
- Si validas los pares con un modelo de embeddings y después evalúas modelos parecidos, ¿no es circular?

**Qué haría.** Escribe el protocolo antes de construir: al menos tres jueces; juicios de equivalencia de contenido, de naturalidad y, si mantienes «socioeconómico», de posición social percibida; umbrales definidos de antemano; acuerdo reportado con α de Krippendorff. La similitud semántica, con un modelo distinto de los evaluados y solo como filtro auxiliar.

**Dónde:** [`03_metodologia.tex:244-268`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/capitulos/03_metodologia.tex#L244-L268) · [`05_indice_ins.tex:25-31`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/capitulos/05_indice_ins.tex#L25-L31) · [`05_indice_ins.tex:323-330`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/capitulos/05_indice_ins.tex#L323-L330)

#### B-02 · Mayor · ¿Quién escribe las variantes estigmatizadas?

- [ ] Atendida

El documento no dice cómo se generan las variantes. Si las escribes tú, reflejarán tu idea de cómo escribe alguien de otro origen social. Si las genera un LLM, reflejarán los estereotipos del LLM, que son parte de lo que quieres medir. En ambos casos el benchmark puede medir la reacción del modelo a una caricatura y no a escritura real.

**Qué haría.** Ancla las variantes en ejemplos reales (corpus, o las respuestas abiertas de la encuesta si el consentimiento lo permite) y pide a hablantes que juzguen su naturalidad. Si usas un LLM para generar o reescribir, decláralo y valida cada variante con personas.

**Dónde:** [`03_metodologia.tex:260-263`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/capitulos/03_metodologia.tex#L260-L263)

#### B-03 · Mayor · Rasgos aislados o combinados

- [ ] Atendida

Si un par cambia léxico, ortografía y marcadores a la vez, no podrás decir cuál de ellos movió la decisión. Si cambia un solo rasgo, el texto puede sonar artificial. El INS desagregado INS(f, B | v) supone que cada par tiene un único tipo de variación v, y el diseño todavía no lo garantiza.

**Qué haría.** Construye dos subconjuntos: pares de un solo rasgo, para atribuir efectos, y pares realistas con rasgos combinados, para validez ecológica. Etiqueta cada par con el conjunto de rasgos alterados.

**Dónde:** [`03_metodologia.tex:253-258`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/capitulos/03_metodologia.tex#L253-L258) · [`05_indice_ins.tex:91-105`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/capitulos/05_indice_ins.tex#L91-L105)

#### B-04 · Mayor · El tamaño del benchmark no está justificado

- [ ] Atendida

Si un modelo cambia de decisión en el 10 % de los pares, con 50 pares el intervalo de confianza al 95 % va de 4.3 % a 21.4 %; con 200 pares, de 6.6 % a 14.9 % (intervalo de Wilson). Con 50 pares por tipo de variación no podrás distinguir modelos ni tipos. Además, los pares que comparten un mismo CV base no son independientes.

**Preguntas para ti**

- ¿Cuántos contenidos base distintos y cuántas variantes por contenido?
- ¿Qué precisión necesitas para que una diferencia entre modelos sea interpretable?

**Qué haría.** Calcula N por tipo a partir de la precisión deseada y del costo de la validación humana. Calcula los intervalos con bootstrap por contenido base, no por par.

**Dónde:** [`03_metodologia.tex:265-268`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/capitulos/03_metodologia.tex#L265-L268)

#### B-05 · Mayor · El registro no es binario y el orden del par no se usa

- [ ] Atendida

Hay más de dos niveles posibles (estándar formal, neutro, coloquial, coloquial con faltas). Si cada contenido tiene k variantes, ¿qué pares formas? La Definición 5.1 habla de par ordenado, pero ninguna fórmula usa el orden.

**Qué haría.** Fija una variante de referencia (la estándar) y forma los pares referencia–variante. El orden te permite definir la medida con dirección de I-02.

**Dónde:** [`05_indice_ins.tex:25-35`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/capitulos/05_indice_ins.tex#L25-L35)

#### B-06 · Mayor · El INS depende de qué tan cerca del umbral están los ejemplos

- [ ] Atendida

Si los CVs base son claramente aptos o claramente no aptos, ningún cambio de registro moverá la decisión y el INS saldrá alto por diseño. Un benchmark de casos fáciles hace ver neutral a cualquier modelo.

**Qué haría.** Incluye contenidos base de calidad intermedia, cerca de la frontera de decisión, y reporta el INS estratificado por el margen de la predicción en la variante de referencia.

**Dónde:** [`05_indice_ins.tex:341-353`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/capitulos/05_indice_ins.tex#L341-L353)

### Experimento

#### X-01 · Crítico · Sin condición de control no puedes atribuir los cambios al registro

- [ ] Atendida

Cualquier modelo cambia algo ante cualquier reescritura. Si obtienes INS = 0.85, ¿es mucho? Depende de cuánto cambia el mismo modelo ante una paráfrasis en el mismo registro. Sin esa línea base, «sesgo sociolectal» y «fragilidad general ante la reformulación» son indistinguibles. Lo mismo pasa con la ortografía: ¿el modelo reacciona a las faltas típicas de un grupo o a cualquier ruido tipográfico?

**Qué haría.** Usa tres condiciones por contenido base: (i) texto idéntico, como prueba de cordura (INS = 1 en modelos deterministas); (ii) paráfrasis en registro estándar, como línea base de fragilidad; (iii) variación de registro. El efecto sociolectal es la diferencia entre (ii) y (iii), con su intervalo. Para ortografía, compara las faltas típicas contra el mismo número de errores aleatorios.

**Dónde:** [`03_metodologia.tex:284-293`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/capitulos/03_metodologia.tex#L284-L293)

#### X-02 · Mayor · ¿Con qué datos se entrenan los modelos?

- [ ] Atendida

Un clasificador lineal sobre TF-IDF y BETO no clasifican nada hasta que se ajustan a una tarea con datos etiquetados. ¿Cuáles? Un TF-IDF entrenado sin vocabulario coloquial asignará peso cero a esas palabras, y su INS reflejará la cobertura del vocabulario más que un sesgo social.

**Preguntas para ti**

- ¿Qué corpus de entrenamiento usarás y tiene variación de registro?
- ¿Cómo vas a reportar el desempeño de cada modelo en su tarea?

**Qué haría.** Si no hay datos defendibles para entrenar, prioriza modelos ya ajustados y públicos (con su ficha técnica) y LLM con rúbrica.

**Dónde:** [`03_metodologia.tex:273-278`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/capitulos/03_metodologia.tex#L273-L278)

#### X-03 · Mayor · LLM: no determinismo, sensibilidad al prompt y probabilidades

- [ ] Atendida

El capítulo lo contempla, pero falta concretarlo. Temperatura cero no garantiza determinismo en las API. El resultado cambia con la redacción del prompt, a veces más que con el registro del texto. Para INS_prob con un LLM, ¿de dónde sale p_f(· | t)? Las log-probabilidades de los tokens de etiqueta no siempre están disponibles y la confianza verbalizada no está calibrada. Los modelos de API, además, cambian de versión sin aviso.

**Qué haría.** Fija la versión exacta y la fecha de consulta, usa al menos tres redacciones del prompt y reporta la variación entre prompts como otra línea base, define cómo obtienes probabilidades (o limita los LLM a INS_dec) y guarda todas las salidas crudas.

**Dónde:** [`05_indice_ins.tex:125-131`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/capitulos/05_indice_ins.tex#L125-L131)

#### X-04 · Mayor · El INS se reporta sin incertidumbre

- [ ] Atendida

El protocolo reporta el INS como un número puntual. Comparar 0.82 contra 0.87 entre dos modelos no significa nada sin intervalos.

**Qué haría.** Usa intervalos bootstrap remuestreando contenidos base. Para decisiones pareadas, prueba de McNemar; para probabilidades, prueba de Wilcoxon de rangos con signo sobre las diferencias. Corrige por comparaciones múltiples entre tipos de variación y modelos.

**Dónde:** [`03_metodologia.tex:284-293`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/capitulos/03_metodologia.tex#L284-L293) · [`05_indice_ins.tex:157-163`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/capitulos/05_indice_ins.tex#L157-L163)

#### X-05 · Menor · Las métricas por registro necesitan etiquetas verdaderas

- [ ] Atendida

Para calcular exactitud o F1 por condición de registro necesitas la etiqueta correcta de cada contenido base. ¿Quién la asigna y con qué criterio? Se relaciona con I-05.

**Dónde:** [`03_metodologia.tex:290-291`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/capitulos/03_metodologia.tex#L290-L291)

### Índice INS

#### I-01 · Mayor · El nombre promete más de lo que mide y la novedad hay que acotarla

- [ ] Atendida

Tú mismo muestras que un clasificador constante es perfectamente «neutral». INS_dec es uno menos la tasa de cambio de decisión, una cantidad muy cercana a métricas existentes: la brecha contrafáctica de Garg et al. (2019), la tasa de fallo en pruebas de invariancia de CheckList y el análisis de sensibilidad a perturbaciones de Prabhakaran et al. (2019). Un sinodal preguntará qué es nuevo.

**Preguntas para ti**

- ¿Cuál es exactamente tu aporte: la fórmula, la perturbación anclada sociolingüísticamente, el benchmark o el protocolo de reporte?

**Qué haría.** Ubica el aporte en el benchmark anclado en el español de México, en el protocolo de reporte (global, perfil, desempeño, línea base y dirección) y en su aplicación, y di explícitamente que la fórmula adapta métricas existentes. Considera un nombre como «Índice de Consistencia Sociolectal», o define «neutralidad» de forma explícita.

**Dónde:** [`05_indice_ins.tex:7-20`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/capitulos/05_indice_ins.tex#L7-L20) · [`05_indice_ins.tex:307-312`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/capitulos/05_indice_ins.tex#L307-L312)

#### I-02 · Crítico · Sin una medida con dirección no puedes hablar de sesgo «contra» nadie

- [ ] Atendida

El capítulo reconoce que el INS no tiene dirección y remite a la Sección 4.2 para un análisis complementario que no está definido. Para tu pregunta, la dirección es el resultado principal. Cincuenta cambios repartidos a favor y en contra describen un modelo inestable; cincuenta cambios en contra de la variante coloquial describen un modelo sesgado. Los dos casos dan el mismo INS.

**Qué haría.** Define formalmente, junto al INS, un índice con signo. Para decisiones, con t como variante de referencia: Δ = P(f(t) = favorable, f(t′) ≠ favorable) − P(f(t) ≠ favorable, f(t′) = favorable), contrastado con la prueba de McNemar. Para probabilidades, la media de p_fav(t) − p_fav(t′). Reporta el INS como estabilidad y Δ como dirección.

**Dónde:** [`05_indice_ins.tex:314-321`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/capitulos/05_indice_ins.tex#L314-L321)

#### I-03 · Mayor · INS_dec e INS_prob pueden contradecirse, e INS_prob depende de la calibración

- [ ] Atendida

Lo comprobé con tu propio calculador: un par que cambia de decisión (de 0.51 a 0.49) tiene JSD ≈ 0.0003, mientras que un par que no cambia (de 0.99 a 0.70) tiene JSD ≈ 0.141. Las dos formulaciones pueden ordenar a los modelos al revés. Además, un modelo sobreconfiado, con probabilidades cerca de 0 y de 1, produce divergencias mayores ante el mismo cambio que uno subconfiado; comparar INS_prob entre modelos mezcla sesgo con calibración.

**Qué haría.** Discute esta discordancia en la Sección 5.5. Calibra los modelos (por ejemplo, con temperature scaling) o reporta su error de calibración junto a INS_prob. Considera usar la diferencia en la probabilidad de la clase favorable, que tiene signo y se interpreta directamente.

**Dónde:** [`05_indice_ins.tex:54-74`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/capitulos/05_indice_ins.tex#L54-L74) · [`05_indice_ins.tex:332-339`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/capitulos/05_indice_ins.tex#L332-L339)

#### I-04 · Mayor · El indicador no tiene validación propia

- [ ] Atendida

La mitad de la pregunta de investigación es «cómo puede diseñarse un indicador». Hoy la validación del indicador queda como trabajo futuro, así que esa mitad se queda sin responder. No hay evidencia de que el INS detecte sesgo cuando existe ni de que no lo invente cuando no existe.

**Qué haría.** Agrega un experimento de validación con verdad conocida, que es barato: (a) un modelo con sesgo inyectado a propósito (un LLM instruido para penalizar lo coloquial, o un clasificador con una regla explícita) debe dar un INS bajo y un Δ con el signo esperado; (b) pares idénticos y paráfrasis deben dar un INS cercano a la línea base. Con eso, «preliminar» pasa a «validado en condiciones controladas».

**Dónde:** [`01_introduccion.tex:56-63`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/capitulos/01_introduccion.tex#L56-L63) · [`06_discusion.tex:45-49`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/capitulos/06_discusion.tex#L45-L49) · [`07_conclusiones.tex:28-32`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/capitulos/07_conclusiones.tex#L28-L32)

#### I-05 · Mayor · Contradicción sobre la verdad de terreno

- [ ] Atendida

En la Sección 5.5.1 exiges reportar el INS siempre junto al desempeño en la tarea, para descartar el clasificador constante. En la 5.5.3 presentas como ventaja que el INS no requiere etiquetas de verdad de terreno. Pero el desempeño requiere esas etiquetas.

**Qué haría.** Separa los dos casos. Con etiquetas, reporta desempeño. Sin etiquetas, sustitúyelo por una prueba de no degeneración, por ejemplo la entropía de las predicciones sobre el benchmark o una tasa de clase favorable lejos de 0 y de 1.

**Dónde:** [`05_indice_ins.tex:298-312`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/capitulos/05_indice_ins.tex#L298-L312) · [`05_indice_ins.tex:420-424`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/capitulos/05_indice_ins.tex#L420-L424)

#### I-06 · Mayor · El INS global depende de la composición del benchmark

- [ ] Atendida

El INS global promedia sobre todos los pares, así que cada tipo de variación pesa según cuántos pares tiene. Si el 60 % de los pares son de ortografía, el global es casi el INS de ortografía. El punto está anotado como pendiente en la Sección 5.2.3.

**Qué haría.** Demuestra la descomposición INS = Σ_v (N_v / N) · INS_v y usa un macropromedio por tipo, o reporta solo el perfil desagregado.

**Dónde:** [`05_indice_ins.tex:44-46`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/capitulos/05_indice_ins.tex#L44-L46) · [`05_indice_ins.tex:87-89`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/capitulos/05_indice_ins.tex#L87-L89)

#### I-07 · Menor · La línea base aleatoria de 0.5 solo vale para un azar uniforme

- [ ] Atendida

Un clasificador aleatorio que asigna la clase favorable con probabilidad q tiene un INS_dec esperado de q² + (1 − q)², que siempre es mayor o igual que 0.5: con q = 0.9 da 0.82. Con K clases uniformes, 1/K. La línea base debe salir de la tasa marginal del modelo evaluado.

**Qué haría.** Reporta el INS esperado por azar con la tasa marginal observada y, si quieres, un índice corregido por azar al estilo de kappa: (INS − INS_azar) / (1 − INS_azar). Para un clasificador constante el denominador es cero, lo que señala la degeneración de forma automática.

**Dónde:** [`05_indice_ins.tex:345-349`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/capitulos/05_indice_ins.tex#L345-L349)

#### I-08 · Menor · Proposiciones triviales y propiedades útiles sin demostrar

- [ ] Atendida

La acotación y la invariancia ante permutaciones son inmediatas; enunciarlas como proposiciones sin demostración se ve débil ante un jurado de Ciencias. Las propiedades interesantes no están: la descomposición del global en el perfil (I-06), la relación entre INS_dec e INS_prob (I-03), el valor esperado bajo azar (I-07) y el efecto de pares no independientes.

**Qué haría.** Demuestra dos o tres de esas propiedades, o presenta las dos actuales como observaciones.

**Dónde:** [`05_indice_ins.tex:76-89`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/capitulos/05_indice_ins.tex#L76-L89)

#### I-09 · Menor · El cruce entre consistencia y corrección necesita su tabla

- [ ] Atendida

«El INS distingue las columnas de este cruce, no las filas» es difícil de seguir sin ver el cruce. Una tabla de 2 × 2 con los cuatro escenarios lo resuelve de un vistazo.

**Dónde:** [`05_indice_ins.tex:298-305`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/capitulos/05_indice_ins.tex#L298-L305)

### Estructura y redacción

#### R-01 · Mayor · El INS se usa antes de definirse y los resultados quedan partidos

- [ ] Atendida

La metodología (Cap. 3) y los resultados (Cap. 4) usan el INS; el Cap. 5 lo define y además incluye «Aplicación a los resultados experimentales». El lector llega a los resultados sin conocer la métrica y después encuentra más resultados tras la definición.

**Qué haría.** Mueve la definición del INS (5.1 a 5.3 y 5.5) antes de la metodología experimental y concentra todos los resultados en un capítulo. La sección «Estructura propuesta» muestra un orden posible.

**Dónde:** [`tesis.tex:67-73`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/tesis.tex#L67-L73) · [`04_resultados.tex:70-75`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/capitulos/04_resultados.tex#L70-L75) · [`05_indice_ins.tex:277-282`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/capitulos/05_indice_ins.tex#L277-L282)

#### R-02 · Mayor · Se narra como hecho lo que todavía no ocurre

- [ ] Atendida

«El muestreo fue…», «se aplicó», «se verificó que no contuviera detalles…». Ni el piloto ni la encuesta se han levantado. En un borrador es aceptable, pero una frase así puede sobrevivir a la versión final sin haberse cumplido, y en la sección de ética eso es grave.

**Qué haría.** Escribe en futuro o como protocolo hasta que ocurra, o deja una marca [PENDIENTE] junto a cada afirmación.

**Dónde:** [`03_metodologia.tex:80-88`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/capitulos/03_metodologia.tex#L80-L88) · [`03_metodologia.tex:151-154`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/capitulos/03_metodologia.tex#L151-L154) · [`03_metodologia.tex:307-326`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/capitulos/03_metodologia.tex#L307-L326)

#### R-03 · Mayor · La revisión documental se anuncia y está vacía

- [ ] Atendida

El resumen anuncia una revisión documental y la Sección 3.2 tiene tres apartados en blanco: criterios de inclusión, cadenas de búsqueda y síntesis. Prometer criterios de inclusión y cadenas de búsqueda te compromete a algo muy cercano a una revisión sistemática.

**Preguntas para ti**

- ¿Harás una revisión sistemática (con un protocolo tipo PRISMA) o una narrativa?

**Qué haría.** Para una licenciatura basta una revisión narrativa bien documentada: un párrafo con bases consultadas, periodo, idiomas y criterios, sin prometer exhaustividad.

**Dónde:** [`03_metodologia.tex:33-49`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/capitulos/03_metodologia.tex#L33-L49) · [`resumen.tex:20-23`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/frontmatter/resumen.tex#L20-L23)

#### R-04 · Menor · Marcas abiertas y notas internas en el código fuente

- [ ] Atendida

Hay 22 marcas [DECIDIR], [PENDIENTE], [VERIFICAR] y [FUENTE] visibles en el PDF y unos 47 párrafos entre corchetes. Los comentarios «NOTA PARA AXEL» (por ejemplo, «No inventé referencias») sugieren que partes del texto se redactaron con ayuda de una herramienta. Es válido, y tiene dos consecuencias: revisa los lineamientos de la Facultad sobre uso de IA generativa y decláralo si corresponde, y asegúrate de poder defender cada párrafo en el examen oral.

**Dónde:** [`02_marco_teorico.tex:1-13`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/capitulos/02_marco_teorico.tex#L1-L13) · [`A_encuesta.tex:1-14`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/apendices/A_encuesta.tex#L1-L14)

#### R-05 · Menor · El resumen se reescribe al final

- [ ] Atendida

El resumen hoy describe un plan («uno o más modelos», «se define y calcula»). La versión final debe decir qué modelos, cuántos pares, qué valores de INS y qué concluyes. Es normal en esta etapa; anótalo para el cierre.

**Dónde:** [`resumen.tex:9-29`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/frontmatter/resumen.tex#L9-L29)

### Fuentes

#### F-01 · Mayor · Errores en referencias.bib

- [ ] Atendida

Encontré estos problemas en la bibliografía:

- `Blodgett2020Survey` está como @article con journal = «Proceedings…»; debe ser @inproceedings con booktitle.
- `Drozdzowicz2024` no tiene volumen, número, páginas ni DOI.
- `CanetePilar2020BETO` dice 2020 y apunta a arXiv:2308.02976, depositado en 2023. Cita la versión del taller de 2020 o ajusta el año y la nota.
- `BuolamwiniGebru2018` está en el archivo y no se cita en ningún capítulo.
- Ninguna entrada tiene DOI ni URL.
- Siguen pendientes Kusner et al. (2017) y Ribeiro et al. (2020), marcados [FUENTE] en el Cap. 5.

**Dónde:** [`referencias.bib:61-70`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/referencias.bib#L61-L70) · [`referencias.bib:31-36`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/referencias.bib#L31-L36) · [`referencias.bib:136-142`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/referencias.bib#L136-L142) · [`referencias.bib:72-82`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/referencias.bib#L72-L82)

#### F-02 · Mayor · Afirmaciones que necesitan cita

- [ ] Atendida

Estas afirmaciones aparecen sin fuente:

- Que el grupo de 18 a 30 años es el de mayor exposición a evaluación automatizada (3.3.1).
- Que D6 y D7 son proxies «de uso común en encuestas sociales» (3.3.2).
- Que los modelos amplifican las regularidades del entrenamiento (2.1.3); por ejemplo, Zhao et al. (2017).
- La «práctica de documentación de conjuntos de datos discutida en la literatura» (3.6); por ejemplo, Gebru et al., Datasheets for Datasets.
- La equidad individual (5.5.3); Dwork et al. (2012).
- Las herramientas y métodos: spaCy, LDA (Blei et al., 2003), BERTopic (Grootendorst, 2022), pysentimiento, alfa de Cronbach y la regla AMAI.
- Las definiciones de dialecto, sociolecto y registro (2.3.1).

**Dónde:** [`03_metodologia.tex:70-78`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/capitulos/03_metodologia.tex#L70-L78) · [`03_metodologia.tex:111-118`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/capitulos/03_metodologia.tex#L111-L118) · [`02_marco_teorico.tex:142-146`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/capitulos/02_marco_teorico.tex#L142-L146) · [`03_metodologia.tex:333-337`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/capitulos/03_metodologia.tex#L333-L337) · [`05_indice_ins.tex:386-392`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/capitulos/05_indice_ins.tex#L386-L392)

### Código y reproducibilidad

#### C-01 · Menor · El calculador acepta entradas inválidas en silencio

- [ ] Atendida

`divergencia_js` acepta probabilidades negativas (con [1.2, −0.2] contra [0.5, 0.5] devuelve 0.54) y con un vector de ceros devuelve NaN con apenas una advertencia. `ins_por_variacion` no tiene versión probabilística y nada calcula intervalos de confianza. Las pruebas cubren los casos felices.

**Qué haría.** Valida que cada distribución sea no negativa, que sume más que cero y que tenga la misma longitud que su pareja; si no, lanza ValueError. Agrega pruebas para esas entradas, la versión probabilística desagregada y una función de bootstrap.

**Dónde:** [`ins_calculator.py:26-44`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/research/scripts/ins_calculator.py#L26-L44)

#### C-02 · Menor · El Listado 5.1 es una copia manual del archivo

- [ ] Atendida

El código del Capítulo 5 y `ins_calculator.py` ya difieren en las docstrings y van a divergir más. Las docstrings citan «Definición 5.2» y «5.3», números que cambiarán si reordenas capítulos (R-01).

**Qué haría.** Incluye el código con `\lstinputlisting` y un rango de líneas, y refiérete a las definiciones por nombre o etiqueta.

**Dónde:** [`05_indice_ins.tex:198-235`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/capitulos/05_indice_ins.tex#L198-L235) · [`ins_calculator.py:47-80`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/research/scripts/ins_calculator.py#L47-L80)

#### C-03 · Mayor · El plan de reproducibilidad está pendiente

- [ ] Atendida

La sección de reproducibilidad está en blanco y `requirements.txt` no fija versiones. Con modelos de API la reproducibilidad depende de guardar las salidas crudas, porque no podrás volver a consultar la misma versión del modelo. El diseño del Cap. 5, que separa la obtención de salidas del cálculo, lo facilita; falta escribirlo.

**Qué haría.** Fija versiones (pip freeze o un lockfile), registra semillas, guarda cada salida cruda con modelo, versión, prompt y fecha, y decide qué publicarás del benchmark y del código.

**Dónde:** [`03_metodologia.tex:295-298`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/capitulos/03_metodologia.tex#L295-L298) · [`requirements.txt:1-13`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/research/requirements.txt#L1-L13)

### Ética

#### ET-01 · Mayor · Aval ético y protección de datos antes del piloto

- [ ] Atendida

La pregunta de si la Facultad requiere el aval de un comité está marcada [DECIDIR] y debe resolverse antes del piloto. Faltan además el correo de contacto, un aviso de privacidad (consulta con la Facultad qué exige la normativa de datos personales aplicable a la UNAM), dónde se alojan las respuestas (un formulario comercial guarda los datos en servidores de terceros) y un plazo de conservación concreto. Las respuestas abiertas pueden contener datos sensibles, como experiencias de discriminación u origen étnico, y el consentimiento debería advertirlo.

**Qué haría.** Lleva esta lista a la próxima reunión con tu director y resuélvela antes de difundir el piloto. Si vas a usar las respuestas abiertas como muestra de escritura (E-02), el consentimiento debe decirlo.

**Dónde:** [`03_metodologia.tex:300-326`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/capitulos/03_metodologia.tex#L300-L326) · [`A_encuesta.tex:44`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/apendices/A_encuesta.tex#L44)

#### ET-02 · Menor · Concretar el uso previsto del benchmark

- [ ] Atendida

El riesgo de uso dual está bien identificado. Falta concretar si se publicará el benchmark, con qué licencia y con una ficha de datos (datasheet) que declare el uso previsto.

**Qué haría.** Decide publicación y licencia, y redacta la ficha de datos como apéndice.

**Dónde:** [`03_metodologia.tex:328-340`](https://github.com/Axewc/tesis_tex/blob/49e5633e159625aaf7cc4c2c3bd3bf21262be788/tesis/capitulos/03_metodologia.tex#L328-L340)

## Estructura propuesta

Hoy el índice se define después de usarse (R-01). Un orden posible:

| Actual | Propuesta |
|---|---|
| 1. Introducción | 1. **Introducción**. Con hipótesis explícitas (P-03). |
| 2. Marco teórico | 2. **Marco teórico y trabajo relacionado**. Agrega la tabla comparativa y las fuentes mexicanas (M-01, M-02). |
| 3. Metodología | 3. **Propuesta del índice**. Definición, propiedades, medida con dirección e interpretación (actuales 5.1–5.3 y 5.5, más I-02). |
| 4. Resultados | 4. **Metodología**. Encuesta, benchmark con condiciones de control, experimentos y validación del índice. |
| 5. Propuesta del INS | 5. **Resultados**. Encuesta, benchmark construido, INS y Δ por modelo, validación. Absorbe la actual 5.4. |
| 6. Discusión | 6. **Discusión**. Incluye el contraste entre la percepción (L7) y el comportamiento medido (E-01). |
| 7. Conclusiones | 7. **Conclusiones**. Una conclusión por objetivo, como ya está planteado. |

## Para la próxima reunión con tu director

- [ ] ¿Qué tarea y qué modelos concretos se van a evaluar? (P-02)
- [ ] ¿Se mantiene «socioeconómico» en el título o se reformula hacia el registro? (P-01)
- [ ] ¿La Facultad requiere aval de un comité para la encuesta? ¿Qué aviso de privacidad aplica? (ET-01)
- [ ] ¿Se confirma el rango de 18 a 30 años? ¿Proxies D6 y D7 o regla AMAI? (E-07)
- [ ] ¿Revisión documental narrativa o sistemática? (R-03)
- [ ] ¿Se reordena el capítulo del INS antes de la metodología? (R-01)
- [ ] ¿Se publicará el benchmark y con qué licencia? (ET-02)
- [ ] Si el tiempo se acorta, ¿cuál es el alcance mínimo aceptable: cuántos modelos y cuántos pares? (B-04)

## Lecturas sugeridas

> Referencias sugeridas de memoria por el revisor. Antes de citar cualquiera, confirma autores, año, título y lugar de publicación, y lee lo suficiente para saber que dice lo que necesitas.

### Antecedentes directos en PLN

- Blodgett, S. L., Green, L. y O'Connor, B. (2016). Demographic dialectal variation in social media: A case study of African-American English. EMNLP.
- Hofmann, V., Kalluri, P. R., Jurafsky, D. y King, S. (2024). AI generates covertly racist decisions about people based on dialect. Nature.
- Garg, S., Perot, V., Limtiaco, N., Taly, A., Chi, E. H. y Beutel, A. (2019). Counterfactual fairness in text classification through robustness. AIES.
- Prabhakaran, V., Hutchinson, B. y Mitchell, M. (2019). Perturbation sensitivity analysis to detect unintended model biases. EMNLP-IJCNLP.
- Ribeiro, M. T., Wu, T., Guestrin, C. y Singh, S. (2020). Beyond accuracy: Behavioral testing of NLP models with CheckList. ACL.
- Ziems, C. et al. (2022). VALUE: Understanding dialect disparity in NLU. ACL. Y Multi-VALUE (2023).

### Equidad y documentación

- Kusner, M. J., Loftus, J., Russell, C. y Silva, R. (2017). Counterfactual fairness. NeurIPS.
- Dwork, C., Hardt, M., Pitassi, T., Reingold, O. y Zemel, R. (2012). Fairness through awareness. ITCS.
- Gebru, T. et al. (2021). Datasheets for datasets. Communications of the ACM.
- Zhao, J., Wang, T., Yatskar, M., Ordonez, V. y Chang, K.-W. (2017). Men also like shopping: Reducing gender bias amplification using corpus-level constraints. EMNLP.

### Método: pares, juicios y análisis cualitativo

- Lambert, W. E., Hodgson, R. C., Gardner, R. C. y Fillenbaum, S. (1960). Evaluational reactions to spoken languages. Journal of Abnormal and Social Psychology.
- Bertrand, M. y Mullainathan, S. (2004). Are Emily and Greg more employable than Lakisha and Jamal? American Economic Review.
- Arceo-Gómez, E. O. y Campos-Vázquez, R. M. (2014). Race and marriage in the labor market: A discrimination correspondence study in a developing country. American Economic Review (Papers & Proceedings).
- Braun, V. y Clarke, V. (2006). Using thematic analysis in psychology. Qualitative Research in Psychology.

### Sociolingüística y contexto mexicano

- Labov, W. The Social Stratification of English in New York City (1966; 2.ª ed. 2006).
- Milroy, J. y Milroy, L. Authority in Language: Investigating Standard English (sobre la ideología de la lengua estándar).
- Moreno Fernández, F. Principios de sociolingüística y sociología del lenguaje. Ariel.
- Martín Butragueño, P. y Lastra, Y. (coords.). Corpus Sociolingüístico de la Ciudad de México (CSCM). El Colegio de México.
- INEGI y CONAPRED. Encuesta Nacional sobre Discriminación (ENADIS), ediciones 2017 y 2022.
- Centro de Estudios Espinosa Yglesias. Encuesta ESRU de Movilidad Social en México (ESRU-EMOVI), útil para justificar la escolaridad de los padres como proxy.
- Solís, P. et al. (2019). Por mi raza hablará la desigualdad. Oxfam México.
