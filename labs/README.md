# Labs · Bitácora

Once labs con **caja de tiempo dura** (plan §3). Total: **23.0 h**.

> **Regla de time-box:** si a la hora indicada no funciona, escribes en la bitácora qué falló, lees 20 minutos la documentación del servicio y sigues. **Nunca lo arrastras a la sesión siguiente.** Si en una semana los labs se pasan de su caja, se corta el lab, no el estudio.

## Índice

| # | Lab | Caja | Semana | Skills que compra | Código |
|---|---|---|---|---|---|
| 1 | [Fundación de datos](lab-01-data-foundation/) | 2 h | S1 | 1.1.1 · 1.1.2 · 1.1.5 · 1.1.6 · 1.2.1 · 1.3.7 | [data_prep/](../services/risk-scoring/src/risk_scoring/data_prep/) |
| 2 | [Calidad y sesgo](lab-02-quality-and-bias/) | 2.25 h | S1 | 1.3.1 · 1.3.3 · 1.3.4 | [data_quality/](../services/risk-scoring/src/risk_scoring/data_quality/) · [bias/](../services/risk-scoring/src/risk_scoring/bias/) |
| 3 | [Tour de consola: documentos y PII](lab-03-console-tour-docs-pii/) | 0.75 h | S1 | 1.1.8 · 1.2.8 | [ingestion/](../services/credit-assistant/src/credit_assistant/ingestion/) |
| 4 | [Entrenamiento](lab-04-training/) | 2.5 h | S2 | 1.3.5 · 2.2.1 · 2.2.3 · 2.2.4 · 2.2.7 · 2.3.6 | [training/](../services/risk-scoring/src/risk_scoring/training/) |
| 5 | [Explicabilidad y registro](lab-05-explainability-registry/) | 2 h | S2 | 2.3.1 · 2.3.4 · 3.3.6 | [explainability/](../services/risk-scoring/src/risk_scoring/explainability/) · [registry/](../services/risk-scoring/src/risk_scoring/registry/) |
| 6 | [Bedrock: FMs y prompts](lab-06-bedrock-fms-prompts/) | 1.5 h | S3 | 2.1.1 · 2.2.8 · 3.3.7 | [fm_selection/](../services/credit-assistant/src/credit_assistant/fm_selection/) · [prompts/](../services/credit-assistant/src/credit_assistant/prompts/) |
| 7 | [Knowledge Base](lab-07-knowledge-base/) | 2 h | S3 | 1.1.7 · 1.2.5 · 1.2.7 · 3.1.8 · 3.2.7 · 3.2.8 · 3.3.11 | [knowledge_base/](../services/credit-assistant/src/credit_assistant/knowledge_base/) |
| 8 | [Evaluación de IA](lab-08-ai-evaluation/) | 2 h | S3 | 2.2.9 · 2.3.9 · 2.3.10 · 3.3.9 · 4.1.6 | [evaluation/](../services/credit-assistant/src/credit_assistant/evaluation/) · [evals/](../services/credit-assistant/evals/) |
| 9 | [Inferencia y red](lab-09-inference-and-network/) | 2.5 h | S4 | 3.1.3 · 3.2.4 · 3.2.5 · 4.3.6 | [inference/](../services/risk-scoring/src/risk_scoring/inference/) · [infra/network/](../infra/network/) |
| 10 | [Agentes y guardarraíles](lab-10-agents-and-guardrails/) | 2.5 h | S5 | 3.1.6 · 3.2.9 · 3.3.8 · 4.3.9 | [agent/](../services/credit-assistant/src/credit_assistant/agent/) · [guardrails/](../services/credit-assistant/src/credit_assistant/guardrails/) |
| 11 | [Orquestación, monitoreo y seguridad](lab-11-orchestration-monitoring-security/) | 3 h | S6 | 2.3.2 · 3.3.1 · 3.3.3 · 3.3.5 · 4.1.1 · 4.1.2 · 4.1.3 · 4.2.3 · 4.2.5 · 4.3.2 · 4.3.3 · 4.3.4 · 4.3.5 | [orchestration/](../orchestration/) · [monitoring/](../services/risk-scoring/src/risk_scoring/monitoring/) · [infra/](../infra/) |

**No se construye** (pasa a lectura y tabla): CodePipeline, CodeBuild, CodeDeploy, auto scaling, Feature Store, Lambda de streaming, CloudFormation, EMR y contenedores.

## Reglas de notebooks

Detalle en [ADR-0004](../docs/adr/0004-notebooks-policy.md).

1. **Un notebook por lab, y ya está creado** con el nombre de su carpeta. No crees otro.
2. **Solo importa y llama.** Si una función se usa dos veces, se mueve a `services/` o `packages/`.
3. **Ningún nombre de recurso a mano.** Bucket, región y ARN salen de `loanops_core.config`.
4. **En SageMaker Studio, clona el repo con git.** Nunca subas ni descargues un `.ipynb` a mano.
5. **Outputs:** `nbstripout` los limpia al hacer commit (se activa en el Lab 1). Los archivos generados van a `outputs/` (ignorada por git) o a S3.
6. **Lo que importa del resultado** se escribe en la sección Bitácora del README del lab.

## Flujo de un lab

1. Lee el README del lab: objetivo, caja y skills.
2. Abre **su** notebook.
3. Pon el código reutilizable en la carpeta enlazada en "Dónde va el código".
4. Al terminar, o cuando se acabe la caja, llena la **Bitácora**.
5. Haz la **limpieza** que indica el README. Cada viernes, además, la [limpieza general](../scripts/cleanup/).

Instancias: `ml.m5.large` para entrenar y `ml.t3.medium` para notebooks. **Nunca GPU** (plan §9).
