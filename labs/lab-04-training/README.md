# Lab 04 · Entrenamiento

| Caja | Semana | Skills que compra |
|---|---|---|
| **2.5 h** | S2 · 22–28 sep | 1.3.5 · 2.2.1 · 2.2.3 · 2.2.4 · 2.2.7 · 2.3.6 |

## Objetivo (plan §3)

XGBoost built-in sobre German Credit. Entrena dos veces, con y sin corrección de desbalance. Compara accuracy contra AUC-PR y entiende por qué accuracy miente. Después, AMT bayesiano con 10 jobs y early stopping.

## Dónde va el código

- [services/risk-scoring/src/risk_scoring/training/](../../services/risk-scoring/src/risk_scoring/training/): entrenamiento y configuración de AMT

## Notebook

[lab-04-training.ipynb](lab-04-training.ipynb) es el único notebook de este lab. Solo importa y llama ([reglas](../README.md#reglas-de-notebooks)).

## Tablas relacionadas

- [05 · Métricas de clasificación](../../study/decision-tables/05-classification-metrics.md)
- [06 · Algoritmos built-in](../../study/decision-tables/06-sagemaker-builtin-algorithms.md)

## ⚠️ Limpieza al terminar

- Los training jobs y los tuning jobs terminan solos. Usa `ml.m5.large` y **nunca GPU**.

## Bitácora

- **Fecha:**
- **Tiempo real:** __ h de 2.5 h
- **Accuracy vs. AUC-PR (sin corrección / con corrección):**
- **Mejor job de AMT:**
- **Qué falló** (si se acabó la caja: qué falló → 20 min de documentación → seguir):
- **Lo que me llevo para el examen:**
- **Costo aproximado (USD):**
