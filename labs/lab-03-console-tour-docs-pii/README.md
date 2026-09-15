# Lab 03 · Tour de consola: documentos y PII

| Caja | Semana | Skills que compra |
|---|---|---|
| **0.75 h** | S1 · 15–21 sep | 1.1.8 · 1.2.8 |

## Objetivo (plan §3)

*No es un lab.* Textract sobre un recibo → Comprehend PII → una pasada de Macie. Mira las salidas y no construyas ningún pipeline.

> **El skill real se compra escribiendo la [tabla 03](../../study/decision-tables/03-data-security.md), no haciendo clic.**

## Sin notebook

Es un tour de consola, así que no lleva notebook. Si en el futuro la ingesta se automatiza, el código va en [services/credit-assistant/src/credit_assistant/ingestion/](../../services/credit-assistant/src/credit_assistant/ingestion/).

## Insumos

- Un recibo sintético de [data/docs/payslips/](../../data/docs/payslips/)

## Tablas relacionadas

- [03 · Seguridad de datos](../../study/decision-tables/03-data-security.md)
- [17 · Servicios de IA gestionados](../../study/decision-tables/17-managed-ai-services.md)

## ⚠️ Limpieza al terminar

- **Macie:** si no lo vas a volver a usar, suspéndelo o desactívalo. Cobra por bucket monitoreado y por datos analizados.

## Bitácora

- **Fecha:**
- **Tiempo real:** __ h de 0.75 h
- **Qué vi en cada salida (Textract, Comprehend PII, Macie):**
- **Lo que me llevo para el examen:**
- **Costo aproximado (USD):**
