# Lab 07 · Knowledge Base

| Caja | Semana | Skills que compra |
|---|---|---|
| **2 h** | S3 · 29 sep–5 oct | 1.1.7 · 1.2.5 · 1.2.7 · 3.1.8 · 3.2.7 · 3.2.8 · 3.3.11 |

## Objetivo (plan §3)

Bedrock KB sobre la política de crédito usando **S3 Vectors o RDS pgvector**. Prueba dos estrategias de chunking, agrega filtros por metadatos y haz una sincronización incremental.

## Dónde va el código

- [services/credit-assistant/src/credit_assistant/knowledge_base/](../../services/credit-assistant/src/credit_assistant/knowledge_base/): configuración de chunking, metadatos y sync
- Insumo: [data/docs/credit-policy/](../../data/docs/credit-policy/) → `s3://loanops-docs`

## Notebook

[lab-07-knowledge-base.ipynb](lab-07-knowledge-base.ipynb) es el único notebook de este lab. Solo importa y llama ([reglas](../README.md#reglas-de-notebooks)).

## Tablas relacionadas

- [08 · Almacén vectorial](../../study/decision-tables/08-vector-stores.md)
- [07 · RAG vs. fine-tuning vs. prompt engineering](../../study/decision-tables/07-rag-vs-finetuning-vs-prompting.md)

## ⚠️ Limpieza al terminar

- **Nunca uses OpenSearch Serverless**: cobra OCUs mínimas aunque no lo uses y una colección olvidada un mes cuesta cientos de dólares (plan §9).
- Si usaste RDS `db.t3.micro`, detenla o bórrala. Una RDS detenida **se vuelve a encender sola a los 7 días**.

## Bitácora

- **Fecha:**
- **Tiempo real:** __ h de 2 h
- **Almacén elegido y por qué:**
- **Chunking A vs. B (qué cambió en las respuestas):**
- **Qué falló** (si se acabó la caja: qué falló → 20 min de documentación → seguir):
- **Lo que me llevo para el examen:**
- **Costo aproximado (USD):**
