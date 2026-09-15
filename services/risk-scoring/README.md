# risk-scoring · Vía A

Calcula el riesgo de incumplimiento de un solicitante con ML clásico. La explicabilidad y la detección de sesgo son **requisitos del negocio**: *"un banco debe justificar por qué negó un crédito"*.

## Módulos

| Módulo | Qué va aquí | Servicios AWS | Lab |
|---|---|---|---|
| [data_prep/](src/risk_scoring/data_prep/) | Script del Glue job (PySpark): limpieza, imputación, deduplicación, CSV → Parquet. Recetas de DataBrew | Glue, DataBrew, Athena | 1 |
| [data_quality/](src/risk_scoring/data_quality/) | Reglas DQDL | Glue Data Quality | 2 |
| [bias/](src/risk_scoring/bias/) | Configuración de Clarify pre y post-entrenamiento | Clarify | 2, 5 |
| [training/](src/risk_scoring/training/) | Entrenamiento con XGBoost built-in y configuración de AMT | SageMaker Training, AMT | 4 |
| [explainability/](src/risk_scoring/explainability/) | SHAP y Model Card | Clarify, Model Cards | 5 |
| [registry/](src/risk_scoring/registry/) | Registro de modelos y corridas | Model Registry, MLflow | 5 |
| [inference/](src/risk_scoring/inference/) | Despliegue real-time y Batch Transform | SageMaker Endpoints | 9 |
| [monitoring/](src/risk_scoring/monitoring/) | Baseline y schedule de Model Monitor | Model Monitor | 11 |
| [tests/](tests/) | Tests del servicio | — | — |

## Contratos

- **Consumidor del endpoint:** el action group de [credit-assistant](../credit-assistant/) lo invoca con permisos IAM. Si cambias el formato de entrada o salida del endpoint, actualiza el esquema OpenAPI en `credit-assistant/src/credit_assistant/agent/action_groups/`.
- La configuración (región, buckets, ARNs) se importa de `loanops_core.config`.

## Reglas

- Aquí no van notebooks: esos viven en [labs/](../../labs/).
- Para entrenar, `ml.m5.large`. **Nunca GPU.**
