# Lab 05 · Explicabilidad y registro

| Caja | Semana | Skills que compra |
|---|---|---|
| **2 h** | S2 · 22–28 sep | 2.3.1 · 2.3.4 · 3.3.6 |

## Objetivo (plan §3)

Clarify SHAP post-entrenamiento para responder *"por qué se negó este préstamo"*. Genera el Model Card. Registra el modelo en Model Registry. Registra 3 corridas en MLflow en SageMaker.

## Dónde va el código

- [services/risk-scoring/src/risk_scoring/explainability/](../../services/risk-scoring/src/risk_scoring/explainability/): SHAP y Model Card
- [services/risk-scoring/src/risk_scoring/registry/](../../services/risk-scoring/src/risk_scoring/registry/): Model Registry y MLflow
- [services/risk-scoring/src/risk_scoring/bias/](../../services/risk-scoring/src/risk_scoring/bias/): configuración de Clarify post-entrenamiento

## Notebook

[lab-05-explainability-registry.ipynb](lab-05-explainability-registry.ipynb) es el único notebook de este lab. Solo importa y llama ([reglas](../README.md#reglas-de-notebooks)).

## Tablas relacionadas

- [02 · Métricas de sesgo de Clarify](../../study/decision-tables/02-clarify-bias-metrics.md) (post-entrenamiento)

## ⚠️ Limpieza al terminar

- Si creaste un **tracking server de MLflow**, se cobra por hora mientras existe. Detenlo o bórralo.

## Bitácora

- **Fecha:**
- **Tiempo real:** __ h de 2 h
- **"Por qué se negó este préstamo" (top features SHAP):**
- **Qué falló** (si se acabó la caja: qué falló → 20 min de documentación → seguir):
- **Lo que me llevo para el examen:**
- **Costo aproximado (USD):**
