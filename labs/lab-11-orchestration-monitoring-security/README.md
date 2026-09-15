# Lab 11 · Orquestación, monitoreo y seguridad *(sesión doble)*

| Caja | Semana | Skills que compra |
|---|---|---|
| **3 h** | S6 · 20–26 oct | 2.3.2 · 3.3.1 · 3.3.3 · 3.3.5 · 4.1.1 · 4.1.2 · 4.1.3 · 4.2.3 · 4.2.5 · 4.3.2 · 4.3.3 · 4.3.4 · 4.3.5 |

> Si la [compuerta 1](../../study/gates/gate-1-2026-10-12.md) dio **< 24/32**, este lab se recorta a la mitad.

## Objetivo (plan §3)

- **Step Functions:** reentrenar → evaluar → registrar → desplegar, disparado por EventBridge.
- **Model Monitor** con baseline y deriva inyectada a propósito.
- **Dashboard de CloudWatch.**
- **Seguridad:** rol IAM de menor privilegio, KMS en los buckets, CloudTrail y Budgets.

## Dónde va el código

- [orchestration/step-functions/](../../orchestration/step-functions/) y [orchestration/eventbridge/](../../orchestration/eventbridge/)
- [services/risk-scoring/src/risk_scoring/monitoring/](../../services/risk-scoring/src/risk_scoring/monitoring/): baseline y schedule
- [infra/observability/](../../infra/observability/), [infra/iam/](../../infra/iam/), [infra/security/](../../infra/security/) y [infra/cost/](../../infra/cost/)

## Notebook

[lab-11-orchestration-monitoring-security.ipynb](lab-11-orchestration-monitoring-security.ipynb) es el único notebook de este lab. Solo importa y llama ([reglas](../README.md#reglas-de-notebooks)).

## Tablas relacionadas

- [13 · Orquestación](../../study/decision-tables/13-orchestration.md)
- [15 · Tipos de Model Monitor](../../study/decision-tables/15-model-monitor-types.md)
- [16 · Reducción de costos](../../study/decision-tables/16-cost-reduction.md)

## ⚠️ Limpieza al terminar

- Borra el **monitoring schedule** y el **endpoint**.
- Desactiva la regla de **EventBridge** para que no reentrene sola.

## Bitácora

- **Fecha:**
- **Tiempo real:** __ h de 3 h
- **¿Model Monitor detectó la deriva inyectada? ¿Qué tipo?:**
- **Qué falló** (si se acabó la caja: qué falló → 20 min de documentación → seguir):
- **Lo que me llevo para el examen:**
- **Costo aproximado (USD):**
