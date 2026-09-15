# Arquitectura · LoanOps

Fuente: [plan §2](../loanops-aws-mla-c02-v3.md).

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

## Mapa servicio AWS → carpeta

| Servicio AWS | Vía | Carpeta | Lab |
|---|---|---|---|
| S3 (raw / curated / docs) | Ambas | [data/](../../data/) (espejo local), [infra/security/](../../infra/security/) (KMS) | 1 |
| Glue Crawler, Glue jobs, Athena | A | [risk_scoring/data_prep/](../../services/risk-scoring/src/risk_scoring/data_prep/) | 1 |
| DataBrew, Glue Data Quality (DQDL) | A | [data_prep/](../../services/risk-scoring/src/risk_scoring/data_prep/), [data_quality/](../../services/risk-scoring/src/risk_scoring/data_quality/) | 2 |
| Clarify (sesgo pre y post) | A | [bias/](../../services/risk-scoring/src/risk_scoring/bias/) | 2, 5 |
| SageMaker XGBoost + AMT | A | [training/](../../services/risk-scoring/src/risk_scoring/training/) | 4 |
| Clarify SHAP, Model Card | A | [explainability/](../../services/risk-scoring/src/risk_scoring/explainability/) | 5 |
| Model Registry, MLflow | A | [registry/](../../services/risk-scoring/src/risk_scoring/registry/) | 5 |
| Endpoint real-time, Batch Transform | A | [inference/](../../services/risk-scoring/src/risk_scoring/inference/) | 9 |
| VPC, VPC endpoints | Transversal | [infra/network/](../../infra/network/) | 9 |
| Textract, Comprehend PII | B | [credit_assistant/ingestion/](../../services/credit-assistant/src/credit_assistant/ingestion/) | Tour 3 |
| Macie | B | [infra/security/](../../infra/security/) | Tour 3 |
| Bedrock FMs, Prompt Management | B | [fm_selection/](../../services/credit-assistant/src/credit_assistant/fm_selection/), [prompts/](../../services/credit-assistant/src/credit_assistant/prompts/) | 6 |
| Bedrock Knowledge Base (S3 Vectors o pgvector) | B | [knowledge_base/](../../services/credit-assistant/src/credit_assistant/knowledge_base/) | 7 |
| Bedrock Evaluations, LLM-as-a-judge | B | [evaluation/](../../services/credit-assistant/src/credit_assistant/evaluation/), [evals/](../../services/credit-assistant/evals/) | 8 |
| Bedrock Agents + action group (Lambda) | B → A | [agent/action_groups/](../../services/credit-assistant/src/credit_assistant/agent/action_groups/) | 10 |
| Bedrock Guardrails | B | [guardrails/](../../services/credit-assistant/src/credit_assistant/guardrails/) | 10 |
| Step Functions, EventBridge | Transversal | [orchestration/](../../orchestration/) | 11 |
| Model Monitor | A | [monitoring/](../../services/risk-scoring/src/risk_scoring/monitoring/) | 11 |
| CloudWatch | Transversal | [infra/observability/](../../infra/observability/) | 11 |
| IAM, KMS, CloudTrail | Transversal | [infra/iam/](../../infra/iam/), [infra/security/](../../infra/security/) | 11 |
| Budgets | Transversal | [infra/cost/](../../infra/cost/) | Día 1 |
| Cognito + JWT authorizer de API Gateway | Apps | [infra/auth/](../../infra/auth/), [apps/api/](../../apps/api/) | Futuro |

## Dependencias permitidas

```
apps/web ──HTTP + JWT──▶ apps/api ──IAM──▶ endpoint de scoring (A) · agente (B)
services/credit-assistant ──IAM (action group)──▶ endpoint de risk-scoring
services/*  ──import──▶ packages/loanops-core
labs/ (notebooks) ──import──▶ services/*, packages/*
```

- **Vía B → Vía A** es la única dependencia entre las dos vías: el action group del agente llama al endpoint de scoring.
- **Nada importa desde `labs/`.** Los notebooks consumen código del repo, pero ningún módulo depende de un notebook.
- **`apps/api` no importa código de entrenamiento.** Habla con los modelos ya desplegados (endpoint y agente).

## Autenticación

- **Personas** (web → api): JWT emitidos por Cognito y validados por API Gateway.
- **Servicios** (agente → endpoint, Step Functions → SageMaker): roles IAM.

Detalle en [ADR-0003](../adr/0003-auth-cognito-jwt.md).
