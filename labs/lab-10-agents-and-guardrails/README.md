# Lab 10 · Agentes y guardarraíles

| Caja | Semana | Skills que compra |
|---|---|---|
| **2.5 h** | S5 · 13–19 oct | 3.1.6 · 3.2.9 · 3.3.8 · 4.3.9 |

> Si la [compuerta 1](../../study/gates/gate-1-2026-10-12.md) dio **< 24/32**, este lab se recorta a la mitad.

## Objetivo (plan §3)

Agente de Bedrock de pre-underwriting con un action group que invoque el endpoint de scoring. Agrega Guardrails: bloqueo de PII y un tema denegado (asesoría financiera). Crea una versión y un alias.

**El endpoint de scoring tiene que estar vivo.** Redesplegarlo toma unos 6 minutos, y ese tiempo ya está dentro de la caja.

## Dónde va el código

- [services/credit-assistant/src/credit_assistant/agent/action_groups/](../../services/credit-assistant/src/credit_assistant/agent/action_groups/): esquema OpenAPI y Lambda que llama al endpoint de [risk-scoring](../../services/risk-scoring/) con permisos IAM
- [services/credit-assistant/src/credit_assistant/guardrails/](../../services/credit-assistant/src/credit_assistant/guardrails/): configuración de los guardrails

## Notebook

[lab-10-agents-and-guardrails.ipynb](lab-10-agents-and-guardrails.ipynb) es el único notebook de este lab. Solo importa y llama ([reglas](../README.md#reglas-de-notebooks)).

## Tablas relacionadas

- [14 · Agentes](../../study/decision-tables/14-agents.md)
- [03 · Seguridad de datos](../../study/decision-tables/03-data-security.md) (Guardrails)

## ⚠️ Limpieza al terminar

- **Borra el endpoint de scoring.**

## Bitácora

- **Fecha:**
- **Tiempo real:** __ h de 2.5 h
- **Qué bloqueó cada guardrail:**
- **Versión y alias creados:**
- **Qué falló** (si se acabó la caja: qué falló → 20 min de documentación → seguir):
- **Lo que me llevo para el examen:**
- **Costo aproximado (USD):**
