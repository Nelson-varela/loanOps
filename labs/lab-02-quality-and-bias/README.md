# Lab 02 · Calidad y sesgo

| Caja | Semana | Skills que compra |
|---|---|---|
| **2.25 h** | S1 · 15–21 sep | 1.3.1 · 1.3.3 · 1.3.4 |

## Objetivo (plan §3)

DataBrew profile job → 5 reglas de Glue Data Quality en DQDL → reporte de Clarify de sesgo pre-entrenamiento por edad y género. Entiende CI, DPL, KL y JS.

**+15 min:** lee cómo cambia la medición de sesgo sobre texto e imagen (esa es la mitad de 1.3.4).

## Dónde va el código

- [services/risk-scoring/src/risk_scoring/data_quality/](../../services/risk-scoring/src/risk_scoring/data_quality/): las 5 reglas DQDL
- [services/risk-scoring/src/risk_scoring/bias/](../../services/risk-scoring/src/risk_scoring/bias/): configuración de Clarify pre-entrenamiento

## Notebook

[lab-02-quality-and-bias.ipynb](lab-02-quality-and-bias.ipynb) es el único notebook de este lab. Solo importa y llama ([reglas](../README.md#reglas-de-notebooks)).

## Tablas relacionadas

- [02 · Métricas de sesgo de Clarify](../../study/decision-tables/02-clarify-bias-metrics.md)
- [01 · Procesamiento de datos](../../study/decision-tables/01-data-processing.md) (DataBrew)

## ⚠️ Limpieza al terminar

- Los jobs de DataBrew, DQ y Clarify terminan solos. Revisa que ningún job de DataBrew haya quedado con *schedule*.

## Bitácora

- **Fecha:**
- **Tiempo real:** __ h de 2.25 h
- **Qué funcionó:**
- **Qué falló** (si se acabó la caja: qué falló → 20 min de documentación → seguir):
- **Lo que me llevo para el examen:**
- **Costo aproximado (USD):**
