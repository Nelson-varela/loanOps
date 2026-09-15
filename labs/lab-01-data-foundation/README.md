# Lab 01 · Fundación de datos

| Caja | Semana | Skills que compra |
|---|---|---|
| **2 h** | S1 · 15–21 sep | 1.1.1 · 1.1.2 · 1.1.5 · 1.1.6 · 1.2.1 · 1.3.7 |

## Objetivo (plan §3)

3 buckets S3 (raw, curated y docs) → Glue Crawler → Glue job (limpieza, imputación, deduplicación, CSV → Parquet particionado) → consulta en Athena.

## Setup del repo (una sola vez, ~15 min)

Este es el primer lab con código, así que aquí se activa el tooling ([ADR-0001](../../docs/adr/0001-monorepo-structure.md)):

- [ ] Workspace de `uv` y `packages/loanops-core` con `config/` (región y buckets desde `.env`)
- [ ] `pre-commit install` (activa `nbstripout`)
- [ ] `nbdime config-git --enable` (diffs legibles de notebooks)

## Dónde va el código

- [services/risk-scoring/src/risk_scoring/data_prep/](../../services/risk-scoring/src/risk_scoring/data_prep/): script del Glue job
- [packages/loanops-core/](../../packages/loanops-core/): configuración y etiquetas
- Datos: [data/raw/](../../data/) → `s3://loanops-raw`

## Notebook

[lab-01-data-foundation.ipynb](lab-01-data-foundation.ipynb) es el único notebook de este lab. Solo importa y llama ([reglas](../README.md#reglas-de-notebooks)).

## Tablas relacionadas

- [01 · Procesamiento de datos](../../study/decision-tables/01-data-processing.md)

## ⚠️ Limpieza al terminar

- Revisa que el Glue Crawler no haya quedado con un *schedule* activo.
- Etiqueta `Project=LoanOps` en los buckets, el crawler y el job.

## Bitácora

- **Fecha:**
- **Tiempo real:** __ h de 2 h
- **Qué funcionó:**
- **Qué falló** (si se acabó la caja: qué falló → 20 min de documentación → seguir):
- **Lo que me llevo para el examen:**
- **Costo aproximado (USD):**
