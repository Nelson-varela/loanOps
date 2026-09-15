# credit-assistant · Vía B

Asistente para el analista de crédito: responde sobre la política de crédito y los documentos del solicitante, con RAG, un agente de pre-underwriting y guardrails.

## Módulos

| Módulo | Qué va aquí | Servicios AWS | Lab |
|---|---|---|---|
| [ingestion/](src/credit_assistant/ingestion/) | Extracción de documentos y detección de PII (solo si se automatiza más adelante) | Textract, Comprehend PII | Tour 3 |
| [knowledge_base/](src/credit_assistant/knowledge_base/) | Configuración de chunking, creación de la KB, filtros por metadatos, sincronización | Bedrock Knowledge Bases | 7 |
| [prompts/](src/credit_assistant/prompts/) | Plantillas de prompt (espejo de lo que versionas en Prompt Management) | Bedrock Prompt Management | 6 |
| [fm_selection/](src/credit_assistant/fm_selection/) | Comparación de 3 FMs por latencia, costo y calidad | Bedrock | 6 |
| [agent/action_groups/](src/credit_assistant/agent/action_groups/) | Esquema OpenAPI y Lambda que llama al endpoint de [risk-scoring](../risk-scoring/) | Bedrock Agents, Lambda | 10 |
| [guardrails/](src/credit_assistant/guardrails/) | Configuración de los guardrails: PII y tema denegado (asesoría financiera) | Bedrock Guardrails | 10 |
| [evaluation/](src/credit_assistant/evaluation/) | LLM-as-a-judge y precisión de recuperación | Bedrock Evaluations | 8 |
| [evals/](evals/) | **Datos**, no código: las 20 preguntas de política con su respuesta esperada y la suite de regresión de 20 prompts | — | 8 |
| [tests/](tests/) | Tests del servicio | — | — |

## Contratos

- **Depende de la Vía A** a través del action group, que invoca el endpoint de scoring con un **rol IAM** (no JWT, ver [ADR-0003](../../docs/adr/0003-auth-cognito-jwt.md)).
- La configuración se importa de `loanops_core.config`.

## Reglas

- Almacén vectorial: **S3 Vectors o RDS pgvector**. **Nunca OpenSearch Serverless** (plan §9).
- Aquí no van notebooks: esos viven en [labs/](../../labs/).
