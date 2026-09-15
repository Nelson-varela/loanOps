# Checklist de skills · MLA-C02

**Regla para pasar (plan §5):** respondes la pregunta **en voz alta, en una o dos frases, sin notas**. Reconocer el nombre no alcanza.

Marca `[x]` solo cuando cumples esa regla. Las [compuertas](gates/) y el repaso de S7 usan esta lista.

## Resumen

| Dominio | Peso | Nuevos | Pasados | Hito de cobertura |
|---|---|---|---|---|
| D1 Datos | 28% | 10 | __ / 10 | Todos al 12 oct |
| D2 Modelos y FM | 24% | 11 | __ / 11 | Todos al 12 oct |
| D3 Despliegue | 24% | 15 | __ / 15 | 10 al 12 oct · 15 al 19 oct |
| D4 Ops y seguridad | 24% | 9 | __ / 9 | 2 al 19 oct · 7 en S6 |
| **Total** | | **45** | **__ / 45** | |

---

## Parte 1 · Los 45 skills nuevos (plan §5)

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

---

## Parte 2 · Los 62 skills heredados (plan §7)

🔨 = lo tocas en un lab · 📖 = tarjeta de decisión

### D1 (15)

- [ ] 1.1.1 🔨
- [ ] 1.1.2 🔨
- [ ] 1.1.3 📖
- [ ] 1.1.4 📖
- [ ] 1.1.5 🔨
- [ ] 1.1.6 🔨
- [ ] 1.1.9 📖
- [ ] 1.2.1 🔨
- [ ] 1.2.2 📖
- [ ] 1.2.3 📖
- [ ] 1.2.4 🔨
- [ ] 1.3.1 🔨
- [ ] 1.3.2 📖
- [ ] 1.3.3 🔨
- [ ] 1.3.5 🔨

### D2 (16)

- [ ] 2.1.3 📖
- [ ] 2.1.6 📖
- [ ] 2.1.8 📖 *(bajado de 🔨: el tour de consola no lo compra)*
- [ ] 2.2.1 🔨
- [ ] 2.2.2 📖
- [ ] 2.2.3 🔨
- [ ] 2.2.4 🔨
- [ ] 2.2.5 📖
- [ ] 2.2.6 📖
- [ ] 2.2.7 🔨
- [ ] 2.3.1 🔨
- [ ] 2.3.2 🔨
- [ ] 2.3.3 📖
- [ ] 2.3.4 🔨
- [ ] 2.3.5 📖
- [ ] 2.3.6 🔨

### D3 (15)

- [ ] 3.1.1 📖
- [ ] 3.1.2 📖
- [ ] 3.1.3 🔨
- [ ] 3.2.1 📖
- [ ] 3.2.2 📖
- [ ] 3.2.3 📖
- [ ] 3.2.4 🔨
- [ ] 3.2.5 🔨
- [ ] 3.2.6 📖
- [ ] 3.3.1 🔨
- [ ] 3.3.2 📖
- [ ] 3.3.3 🔨
- [ ] 3.3.4 📖
- [ ] 3.3.5 🔨
- [ ] 3.3.6 🔨

### D4 (16)

- [ ] 4.1.1 🔨
- [ ] 4.1.2 🔨
- [ ] 4.1.3 🔨
- [ ] 4.1.4 📖
- [ ] 4.2.1 📖
- [ ] 4.2.2 🔨
- [ ] 4.2.3 🔨
- [ ] 4.2.4 📖
- [ ] 4.2.5 🔨
- [ ] 4.2.6 📖
- [ ] 4.3.2 🔨
- [ ] 4.3.3 🔨
- [ ] 4.3.4 🔨
- [ ] 4.3.5 🔨
- [ ] 4.3.6 🔨
- [ ] 4.3.7 📖

---

## Parte 3 · Eliminado del temario (plan §6) — no lo estudies

Si aparece en un simulador, el simulador es material C01 reciclado.

- BYOC (bring your own container) con SageMaker
- SageMaker Neo y optimización en dispositivos edge
- Reducción de tamaño de modelo: cambio de tipos de dato, pruning, compresión
- Fine-tuning con datasets propios en Bedrock o JumpStart *como tarea práctica*. Migró a 1.2.9 y 2.1.2.
- Cargar datos de entrenamiento vía EFS y FSx
- Monitoreo de infraestructura con eventos de EventBridge. EventBridge **sigue** como disparador en 3.3.
- *Troubleshooting* de capacidad. El **diseño** de escalado sigue vivo: 3.2.6 y la concurrencia provisionada de la tabla 10.
