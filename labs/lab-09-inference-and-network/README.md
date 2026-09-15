# Lab 09 · Inferencia y red

| Caja | Semana | Skills que compra |
|---|---|---|
| **2.5 h** | S4 · 6–12 oct | 3.1.3 · 3.2.4 · 3.2.5 · 4.3.6 |

## Objetivo (plan §3)

Despliega el endpoint real-time y corre Batch Transform sobre la cartera completa. Compara costo y latencia con tus propios ojos. Después, redespliega el endpoint dentro de una VPC con VPC endpoints y sin salida a internet.

## Dónde va el código

- [services/risk-scoring/src/risk_scoring/inference/](../../services/risk-scoring/src/risk_scoring/inference/): despliegue real-time y Batch Transform
- [infra/network/](../../infra/network/): VPC, subredes y VPC endpoints

## Notebook

[lab-09-inference-and-network.ipynb](lab-09-inference-and-network.ipynb) es el único notebook de este lab. Solo importa y llama ([reglas](../README.md#reglas-de-notebooks)).

## Tablas relacionadas

- [10 · Los 4 tipos de inferencia ⭐](../../study/decision-tables/10-inference-types.md)
- [11 · Estrategias de despliegue](../../study/decision-tables/11-deployment-strategies.md)

## ⚠️ Limpieza al terminar

- **Borra el endpoint.** Se cobra por hora aunque no reciba tráfico: `ml.m5.large` durante un mes cuesta unos USD 80.
- Borra los **VPC interface endpoints**, que también se cobran por hora.

## Bitácora

- **Fecha:**
- **Tiempo real:** __ h de 2.5 h

| | Real-time | Batch Transform |
|---|---|---|
| Latencia | | |
| Costo | | |

- **Qué falló** (si se acabó la caja: qué falló → 20 min de documentación → seguir):
- **Lo que me llevo para el examen:**
- **Costo aproximado (USD):**
