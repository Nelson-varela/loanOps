# LoanOps v3 — Plan para AWS Certified Machine Learning Engineer – Associate (MLA-C02 beta)

**Versión:** 3.0 · 14 de septiembre de 2026 · datos verificados contra la guía oficial del MLA-C02
**Examen:** MLA-C02 beta (ME1-C02), finales de octubre de 2026
**Presupuesto total:** 84 horas en 7 semanas

---

## 0. Qué cambió respecto a v2

| Fallo de v2 | Corrección en v3 |
|---|---|
| El disparador del 12 de octubre medía contra 45 skills cuando solo 32 estaban cubiertos ese día. La regla "<35 → reprograma" se disparaba con certeza matemática. | **Dos compuertas** (§10): el 12 de octubre decide *alcance* sobre base 32; el **19 de octubre** decide *fecha* sobre base 38. |
| Los labs sumaban 24.5 h, no 23. El ratio real era 71/29. | **23.0 h exactas** tras recortar el lab de PII y el de FMs. La suma está en §3 y ahora sí cuadra. |
| S1 y S3 no tenían hueco para preguntas pese a que la nota final las declara prioritarias. | **Piso de 40 preguntas semanales** (§4), con el tiempo verificado semana por semana. |
| §6 decía "no leas auto scaling". La introducción de la guía oficial lo lista como tarea validada. | Bullet reescrito (§6): se borró el *troubleshooting de capacidad*, no el *diseño* de escalado. |
| 1.3.4 reducido a métricas tabulares de Clarify. El skill oficial es multimodal. | Corregido en §5 y en el Lab 2. |
| §8 prometía 15 tablas; el calendario programaba 19. | **17 tablas**, programadas 17. |
| El diagnóstico del día 2 no alimentaba ninguna decisión. | Se le asigna un consumidor real (§4, S1). |
| No mencionaba que la beta se presenta una sola vez. | En §1 y en la aritmética de riesgo de §10. |

**Nota sobre una corrección propia:** en la discusión previa a este documento dije que la base de la compuerta 2 era 37. Son **38**. El Lab 10 compra 4.3.9 (Guardrails), que yo había contado como pendiente, y 3.3.10 se incorpora a la lectura de S5. Quedan 7 skills sin medir el 19 de octubre, todos de D4.

---

## 1. El examen y la aritmética del plan

### Datos oficiales (verificados en la guía del MLA-C02)

| Dato | Valor |
|---|---|
| Dominios | D1 Preparación de datos para ML e IA **28%** · D2 Desarrollo de modelos ML y FM **24%** · D3 Despliegue y orquestación de flujos ML e IA **24%** · D4 Operación, monitoreo y seguridad **24%** |
| Tipos de pregunta | **Solo dos**: opción múltiple (1 correcta de 4) y respuesta múltiple (2+ correctas de 5+, todas o nada). El C01 tenía además *ordering* y *matching*; el C02 los eliminó. |
| Preguntas | **50 puntuadas** según la guía. La beta entrega **85 en 170 minutos**. La diferencia son ítems de evaluación estadística. |
| Puntaje | 720/1000, modelo compensatorio — **pero la guía lleva una nota al pie: la designación de aprobado/reprobado no aplica a la versión beta.** El corte de la beta se fija por análisis estadístico posterior. No trates 720 como tu objetivo numérico. |
| Resultados | Dentro de **cinco días hábiles**, también para beta. Ya no es el modelo de 90 días. |
| **Intentos** | **La beta se presenta una sola vez.** Si no apruebas, esperas a la GA. Verifícalo en la página de políticas *antes de testing*. |
| Servicios | La guía trae páginas de servicios *en alcance* y *fuera de alcance*. Léelas una vez en S1. No memorices nombres. |
| GA | 14 de enero de 2027 |

### El panorama que gobierna todo el plan

Conteo verificado, skill por skill, contra la página oficial de comparación C01 → C02:

| Dominio | Skills | Nuevos | % nuevo | Peso | Semanas |
|---|---|---|---|---|---|
| D1 Datos | 25 | 10 | 40% | 28% | 1 |
| D2 Modelos y FM | 27 | 11 | 41% | 24% | 2 |
| **D3 Despliegue** | **30** | **15** | **50%** | **24%** | **2** |
| D4 Ops y seguridad | 25 | 9 | 36% | 24% | 1 |
| **Total** | **107** | **45** | **42%** | 100% | 6 + 1 consolidación |

**El 42% del examen es contenido que no existía hace un mes.** Esa cifra explica por qué el plan está organizado como está y por qué ningún simulador te sirve como termómetro.

**D1 recibe una semana pese a pesar 28%** porque 3 de sus 10 skills nuevos (1.1.7 bases vectoriales, 1.2.5 embeddings, 1.2.7 chunking para RAG) ya los construiste con tus manos. Tu contenido nuevo real en D1 son 7 skills, no 10.

**D3 recibe dos semanas** porque de sus 15 skills nuevos solo 4 son RAG (terreno tuyo) y los otros 11 son agentes, AgentCore, Custom Model Import, versionado de agentes y despliegue de FMs. Terreno virgen, y el peor cubierto por material de terceros.

### Aritmética del 70/30

| Concepto | Horas | % |
|---|---|---|
| Labs (10, con time-box) + 1 tour de consola | 23.0 | 27% |
| Guía oficial, documentación, tablas de decisión, preguntas | 61.0 | 73% |
| **Total** | **84.0** | **100%** |

Si en alguna semana los labs se pasan de su caja, **el lab se corta**, no el estudio.

### Orden de recorte, escrito de antemano

Cuando pierdas una semana — y vas a perder una — recortas en este orden, sin deliberar:

1. **El lab de la semana.** Lo reemplazas por 30 minutos de consola sin construir nada.
2. **El bloque de lectura**, a la mitad.
3. **Nunca** las tablas de decisión.
4. **Nunca** el piso de 40 preguntas.

---

## 2. LoanOps: el proyecto

Un banco que (A) puntúa el riesgo de incumplimiento de un solicitante y (B) le da al analista un asistente que responde sobre la política de crédito y los documentos del solicitante.

Crédito regulado es el único vertical donde explicabilidad, detección de sesgo, redacción de PII, guardarraíles y rastro de auditoría son requisitos **del negocio**, no temario que memorizas. Cuando el examen diga *"un banco debe justificar por qué negó un crédito"*, tu cabeza va a ir directo a Clarify sin pasar por el razonamiento.

**Qué no es.** A 23 horas, LoanOps es un dispositivo mnemotécnico, no una pieza de portafolio. No va a quedar presentable, ni documentado, ni desplegado de forma estable. Esa es una decisión deliberada, no un efecto secundario: el portafolio y la certificación compiten por las mismas horas y aquí gana la certificación.

```
              S3: loanops-raw / -curated / -docs
                            │
        ┌───────────────────┴───────────────────┐
   VÍA A — riesgo de default            VÍA B — asistente de crédito
        │                                        │
  Glue · DataBrew · Glue DQ              Textract · Comprehend PII · Macie
  Clarify (sesgo pre-entrenamiento)      Chunking + embeddings
  XGBoost + AMT                          Bedrock Knowledge Base
  Clarify SHAP · Model Registry          (S3 Vectors o pgvector)
  MLflow en SageMaker                    Bedrock: FMs, Prompt Mgmt, Evaluations
        │                                        │
  Endpoint real-time · Batch Transform   Agente de pre-underwriting + Guardrails
        └───────────────────┬───────────────────┘
                 Step Functions · Model Monitor
                 CloudWatch · IAM · KMS · VPC · CloudTrail · Budgets
```

### Datos (minúsculos a propósito)

| Qué | Fuente | Tamaño |
|---|---|---|
| Solicitudes de crédito | **German Credit** (UCI) | 1.000 filas. Jobs en minutos, centavos de costo, y trae atributos protegidos → los labs de sesgo salen solos. |
| Desbalance realista | "Give Me Some Credit" (Kaggle), opcional | 150k filas, ~7% default |
| Política de crédito | Genérala con un LLM: criterios DTI, LTV, excepciones, matriz de aprobación | 10–15 páginas PDF |
| Documentos del solicitante | Recibos de nómina sintéticos | 5–10 archivos |

---

## 3. Los 10 labs y el tour

Cada uno tiene caja de tiempo dura. Si a la hora indicada no funciona: escribes qué falló, lees 20 minutos la documentación del servicio, y sigues. Nunca lo arrastres a la sesión siguiente.

| # | Lab | Caja | Skills que compra |
|---|---|---|---|
| **1** | **Fundación de datos.** 3 buckets S3 (raw/curated/docs) → Glue Crawler → Glue job (limpieza, imputación, deduplicación, CSV→Parquet particionado) → consulta en Athena. | 2 h | 1.1.1, 1.1.2, 1.1.5, 1.1.6, 1.2.1, 1.3.7 |
| **2** | **Calidad y sesgo.** DataBrew profile job → 5 reglas de Glue Data Quality en DQDL → reporte de Clarify de sesgo pre-entrenamiento por edad y género. Entiende CI, DPL, KL, JS. **+15 min: lee cómo cambia la medición de sesgo sobre texto e imagen** (eso es la mitad de 1.3.4). | 2.25 h | 1.3.1, 1.3.3, 1.3.4 |
| **3** | **Tour de consola: documentos y PII.** *No es un lab.* Textract sobre un recibo → Comprehend PII → una pasada de Macie. Mira las salidas, no construyas pipeline. El skill real se compra escribiendo la tabla 3, no haciendo clic. | 0.75 h | 1.1.8, 1.2.8 |
| **4** | **Entrenamiento.** XGBoost built-in sobre German Credit. Entrena dos veces, con y sin corrección de desbalance. Compara accuracy contra AUC-PR y entiende por qué accuracy miente. Luego AMT bayesiano, 10 jobs, con early stopping. | 2.5 h | 1.3.5, 2.2.1, 2.2.3, 2.2.4, 2.2.7, 2.3.6 |
| **5** | **Explicabilidad y registro.** Clarify SHAP post-entrenamiento → "por qué se negó este préstamo". Genera el Model Card. Registra en Model Registry. Registra 3 corridas en MLflow en SageMaker. | 2 h | 2.3.1, 2.3.4, 3.3.6 |
| **6** | **Bedrock: FMs y prompts.** Compara 3 FMs en la misma tarea midiendo latencia, costo y calidad. Versiona el prompt del asistente en Prompt Management. *Recortado de 2 h: una tarea, tres modelos, una tabla de resultados.* | 1.5 h | 2.1.1, 2.2.8, 3.3.7 |
| **7** | **Knowledge Base.** Bedrock KB sobre la política de crédito usando **S3 Vectors o RDS pgvector** (ver §9). Prueba dos estrategias de chunking. Agrega filtros por metadatos. Haz una sincronización incremental. | 2 h | 1.1.7, 1.2.5, 1.2.7, 3.1.8, 3.2.7, 3.2.8, 3.3.11 |
| **8** | **Evaluación de IA.** Bedrock Evaluations sobre 20 preguntas de política. Monta un LLM-as-a-judge. Mide precisión de recuperación. Arma una suite de regresión de 20 prompts. | 2 h | 2.2.9, 2.3.9, 2.3.10, 3.3.9, 4.1.6 |
| **9** | **Inferencia y red.** Despliega el endpoint real-time. Corre Batch Transform sobre la cartera completa. Compara costo y latencia con tus propios ojos. Redespliega el endpoint dentro de una VPC con VPC endpoints y sin salida a internet. | 2.5 h | 3.1.3, 3.2.4, 3.2.5, 4.3.6 |
| **10** | **Agentes y guardarraíles.** Agente de Bedrock de pre-underwriting con un action group que invoque el endpoint de scoring. Agrega Guardrails: bloqueo de PII y tema denegado (asesoría financiera). Crea una versión y un alias. | 2.5 h | 3.1.6, 3.2.9, 3.3.8, 4.3.9 |
| **11** | **Orquestación, monitoreo y seguridad.** *(sesión doble)* Step Functions: reentrenar → evaluar → registrar → desplegar, disparado por EventBridge. Model Monitor con baseline y deriva inyectada a propósito. Dashboard de CloudWatch. Rol IAM de menor privilegio, KMS en los buckets, CloudTrail, Budgets. | 3 h | 2.3.2, 3.3.1, 3.3.3, 3.3.5, 4.1.1, 4.1.2, 4.1.3, 4.2.3, 4.2.5, 4.3.2, 4.3.3, 4.3.4, 4.3.5 |

**Total: 23.0 horas.** (2 + 2.25 + 0.75 + 2.5 + 2 + 1.5 + 2 + 2 + 2.5 + 2.5 + 3)

**No se construye** (pasan a leer + tabla): CodePipeline/CodeBuild/CodeDeploy, auto scaling, Feature Store, Lambda de streaming, CloudFormation, EMR, contenedores.

---

## 4. Calendario

**Piso no negociable: 40 preguntas por semana.** Cada error se clasifica en una de dos cubetas — *no sabía el servicio* vs. *no leí bien el requisito* — desde la semana 1, no solo en el simulacro. La proporción entre las dos cubetas es el mejor predictor que vas a tener de qué te va a tumbar el examen, y cada cubeta tiene un remedio distinto.

Formato de sesión estándar de 90 min: **20 min documentación oficial → 45 min lab o preguntas → 20 min preguntas de práctica → 5 min escribir la tarjeta del día.**

### S1 · 15–21 sep · Diagnóstico + Dominio 1 · 12 h

- **Día 1 (2 h):** cuenta AWS, usuario IAM sin root, MFA, Budget con alertas en $50 y $100, etiqueta `Project=LoanOps`. **Solicita acceso a los modelos de Bedrock hoy** — no es instantáneo y S3 es tu primera semana de Bedrock. **Elige la región verificando que tenga Bedrock KB, S3 Vectors y AgentCore a la vez**; esa intersección no está en todas partes y descubrirlo en la semana 5 te cuesta el Lab 10. Lee la guía oficial de punta a punta, incluidas las páginas de servicios en alcance y fuera de alcance.
- **Día 2 (2 h): DIAGNÓSTICO — y esto es lo que mide.** 20 preguntas del Official Practice Question Set + 40 de terceros, cronometradas. Estas preguntas son material C01, así que **miden cuánto de los 62 skills heredados ya tienes**, no tu preparación para el C02. Actúa sobre el resultado el mismo día:
  - **>70%** → tu base está sólida. S2 y S3 pueden cederle una sesión cada una a S5 (agentes).
  - **50–70%** → el plan queda como está.
  - **<50%** → el problema no es el 42% nuevo, es la base. Replantea: 7 semanas no alcanzan y la decisión correcta es apuntar a la GA de enero, no a la beta.
- **Labs 1 y 2, Tour 3.**
- 📖 Lectura (2 h, sin construir): Kinesis Data Streams vs. Firehose vs. Managed Flink vs. MSK · EMR · Lake Formation · Ground Truth · Feature Store · formatos de archivo.
- Tablas: **1** procesamiento de datos · **2** métricas de sesgo de Clarify · **3** seguridad de datos.
- *Preguntas: cubiertas por las 60 del diagnóstico.*

### S2 · 22–28 sep · Dominio 2A: ML clásico · 12 h
Tu brecha real. Aquí no aceleras.
- **Labs 4 y 5** (4.5 h).
- 📖 (~3 h) Overfitting, underfitting y olvido catastrófico: síntomas y remedios · script mode · entrenamiento distribuido (data vs. model parallel) · Debugger · ensembles y multi-model endpoints · shadow variants.
- Tablas: **4** streaming · **5** métricas de clasificación · **6** algoritmos built-in.
- *Preguntas: 4.25 h disponibles. Haz 80, no 40.*

### S3 · 29 sep–5 oct · Dominio 2B: FM, RAG y evals · 10 h
**Tu carril rápido.** Ya entiendes chunking, top-k, reranking y medición de recuperación. No lo re-aprendas: tradúcelo a nombres de AWS.
- **Labs 6, 7, 8** (5.5 h).
- 📖 (~2.5 h) Fine-tuning vs. pre-entrenamiento continuo vs. destilación: formato JSONL y cuándo cada uno · BLEU / ROUGE / BERTScore / similitud semántica · A2I y human-in-the-loop · patrones de arquitectura RAG.
- Tablas: **7** RAG vs. fine-tuning vs. prompt engineering · **8** almacén vectorial · **9** métricas NLP.
- *Preguntas: 1.75 h ≈ 50.*

### S4 · 6–12 oct · Dominio 3A: inferencia, red y despliegue de FMs · 12 h
- **Lab 9** (2.5 h).
- 📖 (~4 h) Los 4 tipos de inferencia a fondo · blue/green vs. canary vs. linear vs. all-at-once · opciones de despliegue de FM (on-demand, Provisioned Throughput, JumpStart, Custom Model Import) · unidades de throughput · familias GPU e Inferentia · **concurrencia provisionada y auto scaling desde el ángulo de diseño** (ver §6).
- Tablas: **10 los 4 tipos de inferencia** (la más preguntada) · **11** estrategias de despliegue · **12** despliegue de FMs.
- **→ 12 de octubre: COMPUERTA 1. Ver §10.**
- *Preguntas: 5.25 h menos 30 min de compuerta ≈ 140.*

### S5 · 13–19 oct · Dominio 3B: agentes y orquestación · 12 h
Tu punto ciego y el peor cubierto por simuladores.
- **Lab 10** (2.5 h).
- 📖 (~4 h) Agentes de Bedrock: action groups, esquemas OpenAPI, orquestación, memoria de sesión · **AgentCore y sus componentes** (runtime, identidad, memoria, observabilidad, gateway) · protocolos de comunicación entre agentes · versionado y alias · **3.3.10 versionado y despliegue de FMs fine-tuneados** · CodeBuild / CodeCommit / CodeDeploy / CodePipeline / CodeConnections (solo qué hace cada uno) · MWAA vs. Step Functions.
- Tablas: **13** orquestación · **14** agentes.
- **→ 19 de octubre: COMPUERTA 2 — decide la fecha. Ver §10.**
- *Preguntas: 5.4 h menos 40 min de compuerta ≈ 140.*

### S6 · 20–26 oct · Dominio 4 + primer simulacro · 14 h
- **Lab 11** (3 h, sesión doble).
- 📖 (~3 h) Familias de instancias de inferencia · opciones de compra (Spot, Savings Plans) · Inspector vs. CodeGuru vs. Macie · API keys de Bedrock vs. IAM · observabilidad GenAI de CloudWatch · AgentCore Observability · costos de tokens, embeddings y almacenamiento vectorial.
- **Simulacro completo cronometrado** (2.83 h) + **revisión** (1.5 h). Úsalo para calibrar ritmo y lectura de enunciados, **no como medida de preparación**. Clasifica cada error en las dos cubetas.
- Tablas: **15** tipos de Model Monitor · **16** reducción de costos · **17** servicios de IA gestionados.
- *Preguntas: 3.4 h además del simulacro.*

### S7 · 27 oct–examen · Consolidación. Cero construcción. · 12 h
- Recorre el **checklist completo de los 45 skills** (§5). Los que no pases son tu lista de repaso.
- Repasa las 17 tablas.
- Segundo simulacro + revisión (4.3 h).
- Últimas 48 horas: solo tarjetas. Nada nuevo. Duerme.

---

## 5. El instrumento de medición: los 45 skills nuevos

Regla: pasas un ítem si puedes responder la pregunta **en voz alta, en una o dos frases, sin notas**. No basta reconocer el nombre.

### Dominio 1 — 10 nuevos *(todos cubiertos al 12 de octubre)*

- [ ] **1.1.7** Bases vectoriales: ¿cuándo OpenSearch, cuándo RDS pgvector, cuándo S3?
- [ ] **1.1.8** Tipos diversos: ¿dónde se almacena texto, imagen y audio y qué servicio procesa cada uno?
- [ ] **1.2.5** Embeddings: ¿qué es la dimensionalidad y qué modelos de embedding ofrece Bedrock?
- [ ] **1.2.6** Pre-procesamiento avanzado: ¿qué es tokenización y qué es aumento específico de dominio?
- [ ] **1.2.7** Chunking para RAG: ¿qué estrategias ofrece Bedrock (fijo, por defecto, jerárquico, semántico) y cuándo cada una?
- [ ] **1.2.8** Enmascarar, redactar, anonimizar: ¿qué hace Macie, qué hace Comprehend PII, qué hacen los Guardrails?
- [ ] **1.2.9** Datos para personalizar FMs: ¿qué formato piden fine-tuning, pre-entrenamiento continuo y destilación, y en qué se diferencian?
- [ ] **1.3.4** Sesgo **multimodal**: ¿cómo se aplican métricas de sesgo sobre activos numéricos, de texto y de imagen, y qué cambia en cada caso?
- [ ] **1.3.6** Integridad de datos de IA: ¿qué se valida en un par prompt-respuesta y qué es content safety screening?
- [ ] **1.3.7** Limpieza: ¿cómo detecto outliers, imputo faltantes y deduplico, y con qué servicio?

### Dominio 2 — 11 nuevos *(todos cubiertos al 12 de octubre)*

- [ ] **2.1.1** Selección de FM: ¿qué criterios uso para elegir modelo en Bedrock?
- [ ] **2.1.2** Estrategias de fine-tuning: ¿cuándo fine-tuning y cuándo pre-entrenamiento continuo?
- [ ] **2.1.4** Custom vs. gestionado vs. pre-entrenado vs. FM: ¿cómo se decide?
- [ ] **2.1.5** Patrones RAG: naive, híbrido, con reranking — ¿qué problema resuelve cada uno?
- [ ] **2.1.7** Trade-off: ¿qué palancas bajan latencia sin destruir calidad, y qué cuestan?
- [ ] **2.2.8** Personalización: ¿cuándo basta prompt engineering y cuándo hay que fine-tunear?
- [ ] **2.2.9** Optimizar recuperación: ¿qué muevo primero, tamaño de chunk, top-k o reranker?
- [ ] **2.3.7** Human-in-the-loop: ¿qué es A2I y en qué punto del flujo entra el humano?
- [ ] **2.3.8** Métricas NLP: BLEU, ROUGE, BERTScore, similitud semántica — ¿cuál para qué tarea?
- [ ] **2.3.9** Evaluación de IA: ¿qué es LLM-as-a-judge y cuáles son sus límites?
- [ ] **2.3.10** Monitoreo de RAG: ¿cómo mido precisión de recuperación en producción?

### Dominio 3 — 15 nuevos ⚠️ *(10 al 12 de octubre · los 15 al 19)*

*Cubiertos al 12 oct:*
- [ ] **3.1.4** Despliegue de FM: on-demand vs. Provisioned Throughput vs. JumpStart — ¿cuándo cada uno?
- [ ] **3.1.5** Modelos externos: ¿qué es Bedrock Custom Model Import y qué limitaciones tiene?
- [ ] **3.1.7** Hosting de FM: ¿qué es una unidad de throughput y cuándo la necesito?
- [ ] **3.1.8** Configuración RAG: ¿qué hace el reranking y cuándo lo agrego?
- [ ] **3.2.7** Knowledge Bases: ¿qué fuentes acepta y cómo se sincroniza?
- [ ] **3.2.8** Pipelines de recuperación: ¿cómo filtro por metadatos y por qué importa?
- [ ] **3.2.10** GPU: ¿qué familias hay y cuándo Inferentia en su lugar?
- [ ] **3.3.7** Prompt Management: ¿cómo se versiona un prompt y qué es una variante?
- [ ] **3.3.9** Prompt testing: ¿cómo se monta una suite de regresión de prompts?
- [ ] **3.3.11** Refresco de KB: ¿sincronización completa vs. incremental, y qué la dispara?

*Añadidos en S5:*
- [ ] **3.1.6** Agentes: ¿qué es un action group, cómo se define, qué protocolos de comunicación hay?
- [ ] **3.2.9** Estado de agentes: ¿qué es la memoria de sesión y dónde vive?
- [ ] **3.2.11** AgentCore: ¿qué problema resuelve y cuáles son sus componentes?
- [ ] **3.3.8** Pipelines de agentes: ¿qué es un alias y cómo se promueve una versión?
- [ ] **3.3.10** FMs fine-tuneados: ¿cómo se versiona y despliega un modelo personalizado?

### Dominio 4 — 9 nuevos *(2 al 19 de octubre · los 7 restantes en S6)*

*Cubiertos al 19 oct:*
- [ ] **4.1.6** Monitoreo de FMs: ¿qué evalúa Bedrock Model Evaluation en producción?
- [ ] **4.3.9** Guardrails: ¿cuáles son sus políticas y qué bloquea cada una?

*Pendientes hasta S6 — el riesgo aceptado de la compuerta 2:*
- [ ] **4.1.5** Monitoreo de agentes: ¿qué son fallo de coordinación, streaming truncado y fallo de herramienta?
- [ ] **4.2.7** Costo de FMs: ¿cómo estimo el costo mensual de un asistente en producción?
- [ ] **4.2.8** Recursos de agentes: ¿qué se dispara cuando un agente entra en bucle?
- [ ] **4.2.9** Optimizar inferencia de FM: ¿caché de prompts, routing por modelo o batch — qué ahorra más?
- [ ] **4.2.10** Costos de IA: ¿tokens, cómputo de embeddings o almacenamiento vectorial — cuál domina la factura?
- [ ] **4.3.1** Seguridad de CI/CD: ¿qué escanea CodeGuru y qué escanea Inspector?
- [ ] **4.3.8** Credenciales: ¿API key de Bedrock o IAM — cuándo cada una?

**De esos 7, cuatro son de costo de FMs y agentes: tu punto más débil y el que menos te transfiere desde Salesforce.** 4.3.1 y 4.3.8 sí te transfieren. Esa asimetría es exactamente el riesgo que aceptas al cerrar la decisión el 19 de octubre en vez del 26.

---

## 6. Lo que AWS borró del temario

Confirmado en la página oficial de comparación. Siete eliminaciones, ni una más. Si aparecen en un simulador, es porque el simulador es C01 reciclado.

- **BYOC (bring your own container) con SageMaker** — eliminado de 3.2
- **SageMaker Neo y optimización en dispositivos edge** — eliminado de 3.1
- **Reducción de tamaño de modelo**: cambio de tipos de dato, pruning, compresión — eliminado de 2.2
- **Fine-tuning con datasets propios en Bedrock / JumpStart como tarea práctica** — eliminado de 2.2. *No desapareció: migró aguas arriba a 1.2.9 (preparar los datos) y 2.1.2 (elegir la estrategia), ambos nuevos.*
- **Cargar datos de entrenamiento vía EFS y FSx** — eliminado de 1.3
- **Monitoreo de infraestructura con eventos de EventBridge** — eliminado de 4.2. *EventBridge sigue vivo como disparador de orquestación en 3.3; lo que se fue es el ángulo de monitoreo.*
- **Troubleshooting de capacidad**: concurrencia provisionada, cuotas de servicio, auto scaling — eliminado de 4.2. **Leer con cuidado:** lo que se borró es *diagnosticar problemas* de capacidad. La introducción de la guía del C02 sigue listando "configurar auto scaling según requisitos" entre las tareas que el examen valida, 3.2.6 sobrevive, y **la concurrencia provisionada es la perilla que define Serverless Inference en la tabla 10**, la más preguntada del examen. Estudia el diseño; ignora el diagnóstico.

---

## 7. Cobertura de los 62 skills heredados

🔨 = lo tocas en un lab · 📖 = tarjeta de decisión.

**D1:** 1.1.1 🔨 · 1.1.2 🔨 · 1.1.3 📖 · 1.1.4 📖 · 1.1.5 🔨 · 1.1.6 🔨 · 1.1.9 📖 · 1.2.1 🔨 · 1.2.2 📖 · 1.2.3 📖 · 1.2.4 🔨 · 1.3.1 🔨 · 1.3.2 📖 · 1.3.3 🔨 · 1.3.5 🔨

**D2:** 2.1.3 📖 · 2.1.6 📖 · **2.1.8 📖** *(bajado de 🔨: el tour de consola no lo compra)* · 2.2.1 🔨 · 2.2.2 📖 · 2.2.3 🔨 · 2.2.4 🔨 · 2.2.5 📖 · 2.2.6 📖 · 2.2.7 🔨 · 2.3.1 🔨 · 2.3.2 🔨 · 2.3.3 📖 · 2.3.4 🔨 · 2.3.5 📖 · 2.3.6 🔨

**D3:** 3.1.1 📖 · 3.1.2 📖 · 3.1.3 🔨 · 3.2.1 📖 · 3.2.2 📖 · 3.2.3 📖 · 3.2.4 🔨 · 3.2.5 🔨 · 3.2.6 📖 · 3.3.1 🔨 · 3.3.2 📖 · 3.3.3 🔨 · 3.3.4 📖 · 3.3.5 🔨 · 3.3.6 🔨

**D4:** 4.1.1 🔨 · 4.1.2 🔨 · 4.1.3 🔨 · 4.1.4 📖 · 4.2.1 📖 · 4.2.2 🔨 · 4.2.3 🔨 · 4.2.4 📖 · 4.2.5 🔨 · 4.2.6 📖 · 4.3.2 🔨 · 4.3.3 🔨 · 4.3.4 🔨 · 4.3.5 🔨 · 4.3.6 🔨 · 4.3.7 📖

---

## 8. Las 17 tablas de decisión

Escríbelas a mano. El acto de escribirlas **es** el estudio. Las 17 están programadas en §4: 3 en S1, 3 en S2, 3 en S3, 3 en S4, 2 en S5, 3 en S6.

1. **Procesamiento de datos** — Glue / DataBrew / Data Wrangler / EMR / Athena / Lambda.
2. **Métricas de sesgo de Clarify** — pre-entrenamiento (CI, DPL, KL, JS, KS) y post-entrenamiento (DPPL, DI, RD). Incluye qué cambia en datos multimodales.
3. **Seguridad de datos** — Macie / Comprehend PII / Guardrails / KMS / Secrets Manager. Qué detecta, qué bloquea, qué cifra.
4. **Streaming** — Kinesis Data Streams / Firehose / Managed Flink / MSK.
5. **Métricas de clasificación** — accuracy / precision / recall / F1 / ROC-AUC / AUC-PR. Regla: *desbalance → AUC-PR, nunca accuracy*.
6. **Algoritmos built-in de SageMaker** — cuál para qué caso de uso.
7. **RAG vs. fine-tuning vs. prompt engineering vs. pre-entrenamiento continuo.**
8. **Almacén vectorial** — OpenSearch Serverless / RDS pgvector / S3 Vectors. Ejes: costo base, escala, latencia.
9. **Métricas NLP** — BLEU (traducción) / ROUGE (resumen) / BERTScore (similitud semántica) / perplejidad.
10. **Los 4 tipos de inferencia de SageMaker** — Real-time / Serverless / Asíncrona / Batch Transform. Ejes: latencia, tamaño de payload, patrón de tráfico, si escala a cero, **concurrencia provisionada**, costo. *La más preguntada del examen.*
11. **Estrategias de despliegue** — all-at-once / blue-green / canary / linear / shadow.
12. **Despliegue de FMs** — on-demand / Provisioned Throughput / batch / JumpStart / Custom Model Import.
13. **Orquestación** — Step Functions / SageMaker Pipelines / MWAA / EventBridge.
14. **Agentes** — agente de Bedrock vs. AgentCore vs. Step Functions con Lambda. Ejes: estado, herramientas, observabilidad, versionado, cuándo cada uno.
15. **Tipos de Model Monitor** — data quality / model quality / bias drift / feature attribution drift.
16. **Reducción de costos** — Spot (entrenamiento) / Savings Plans (endpoints) / Serverless (tráfico intermitente) / batch / right-sizing / caché de prompts.
17. **Servicios de IA gestionados** — Textract / Rekognition / Comprehend / Transcribe / Translate / Polly / Personalize / Lex. Una frase cada uno.

*Fuera de la lista canónica respecto a v2:* clases de almacenamiento S3 e hiperparámetros base. Son memorización, no decisión. Van en las tarjetas de repaso de S7, no en las tablas.

---

## 9. Costos y guardarraíles

Estimado con disciplina: **USD 40–90** en las 7 semanas.

**Las tres trampas caras:**

1. **OpenSearch Serverless** factura OCUs mínimas aunque no lo uses. Una colección olvidada un mes cuesta cientos de dólares. **Para el Lab 7 usa S3 Vectors o pgvector en una RDS `db.t3.micro`.** OpenSearch lo estudias en la documentación.
2. **Endpoints de SageMaker** se facturan por hora, encendidos o no. `ml.m5.large` un mes ≈ USD 80. **Bórralos al terminar cada sesión.** Redesplegar toma 6 minutos — y presupuéstalos dentro de la caja del Lab 10, que necesita el endpoint de scoring vivo para el action group.
3. **Aplicaciones de SageMaker Studio** siguen corriendo después de cerrar el navegador. Apágalas explícitamente.

**Higiene:**
- Budget con alertas en $50 y $100, **el día 1**
- Etiqueta `Project=LoanOps` en todo → Cost Explorer filtrado por esa etiqueta
- `ml.m5.large` para entrenamiento, `ml.t3.medium` para notebooks. Nunca GPU en este proyecto.
- **Viernes de limpieza**, 10 minutos: endpoints, apps de Studio, colecciones, clústeres. Sin excepción.
- Una sola región, verificada el día 1. Los recursos huérfanos en otra región es como se pierden $200 sin darse cuenta.

---

## 10. Las dos compuertas

La palanca que más mueve la probabilidad de aprobar, y no es de estudio.

**La ventana de la beta va del 29 de septiembre al 14 de enero de 2027.** Tu cita de finales de octubre no es la única fecha posible dentro de esa ventana. Verifica la política de reprogramación en tu confirmación de Pearson VUE **esta semana**, no en octubre.

**Por qué dos compuertas.** Un umbral único contra los 45 skills no se puede evaluar antes de haber cubierto los 45. Cada compuerta mide solo lo que ya estudiaste, y cada una decide una cosa distinta.

### Compuerta 1 — 12 de octubre (fin de S4) · base: 32 skills · decide *alcance*

| Resultado | Decisión |
|---|---|
| **≥ 24 / 32** (75%) | El plan sigue como está. |
| **< 24 / 32** | No reprogramas todavía. **Recortas los labs 10 y 11 a la mitad** y conviertes ese tiempo en lectura y preguntas. Llegas a la compuerta 2 con menos construido y más sabido. |

### Compuerta 2 — 19 de octubre (fin de S5) · base: 38 skills · decide *la fecha*

| Resultado | Decisión |
|---|---|
| **≥ 30 / 38** (79%) | **Mantén la fecha.** S6 y S7 cierran D4 y consolidan. |
| **< 30 / 38** | **Reprograma a principios de diciembre.** Vinculante. No es fracaso, es aritmética. |

Los umbrales del 75% y el 79% son juicio, no derivación: el examen es compensatorio y el 58% heredado juega a tu favor, pero llegar al día del examen con menos de cuatro quintas partes del contenido nuevo dominado deja poco margen cuando el 42% nuevo es justamente el que ningún simulador te preparó.

**La aritmética de riesgo que v2 no tenía.** La beta se presenta **una sola vez**. Si no apruebas, no hay retoma de beta: esperas a la GA del 14 de enero. Reprogramar dentro de la ventana es gratis; sentarte corto cuesta tres meses. Eso es lo que convierte la compuerta 2 en vinculante en vez de orientativa.

Cuatro o cinco semanas extra sobre una base de 6 no son un 70% más de preparación: son la diferencia entre llegar justo y llegar con margen, y salen gratis. Tomar esa decisión el 19 de octubre con un criterio escrito es una cosa; tomarla el 25 con adrenalina es otra.

---

## 11. El día del examen

- **170 min / 85 preguntas ≈ 2 min por pregunta.** Se va a sentir largo. Se va a sentir pesado sobre el minuto 120. Es normal.
- **Primera pasada rápida:** responde lo que sabes, marca lo dudoso, no te detengas. Meta: llegar a la 85 con 35 minutos libres.
- **La guía dice 50 puntuadas; la beta entrega 85.** La diferencia son ítems en evaluación, no identificados. Vas a encontrarte preguntas raras, ambiguas o mal calibradas, y una buena parte de ellas no cuenta. No significan que estés fallando. Márcalas y sigue.
- **Lee el requisito antes que las opciones.** El examen entierra la respuesta en calificadores: *"con el mínimo esfuerzo operativo"*, *"la solución más rentable"*, *"con los menores cambios de código"*, *"cumpliendo requisitos regulatorios"*. Esas frases eliminan dos opciones antes de que pienses en tecnología.
- **"Mínimo esfuerzo operativo" casi siempre = servicio gestionado.** Si dos opciones son técnicamente válidas y una es gestionada, es la gestionada.
- **Desconfía de las opciones con EKS, contenedores propios o entrenar desde cero** salvo que el requisito lo pida. Suelen ser distractores por sobre-ingeniería. Además, BYOC fue eliminado del temario.
- **Respuesta múltiple:** todas o nada, así que elimina primero las claramente falsas. Las de "elige 2" rara vez son dos sabores de lo mismo; suelen ser dos capas distintas, por ejemplo una de cómputo y una de red.
- **Nunca dejes nada en blanco.** No hay penalización por adivinar.

---

## Nota final

El 42% del temario es nuevo, tú llegas con un cuarto de ese contenido nuevo ya construido con tus manos, y el modelo de puntuación es compensatorio. Las condiciones son buenas.

Lo que hay que proteger es el calendario, y para eso están el 12 y el 19 de octubre — con bases que sí se pueden medir el día que toca.

Si en alguna semana tienes que elegir entre terminar un lab y hacer 40 preguntas de práctica, **haz las preguntas**.
