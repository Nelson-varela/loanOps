# ADR-0002 · Sin infraestructura como código por ahora

- **Estado:** Aceptado
- **Fecha:** 2026-09-15

## Contexto

- El plan (§3) dice explícitamente que **CloudFormation no se construye**: pasa a lectura y tabla.
- Los labs suman **23.0 h con cajas de tiempo duras**. Escribir IaC para cada recurso duplicaría el tiempo de cada lab.
- El objetivo es la certificación, no un despliegue reproducible (§2: "no va a quedar desplegado de forma estable").

## Decisión

- Los recursos se crean desde la **consola, el CLI o el SDK** (desde notebooks o scripts).
- Se **versionan los artefactos declarativos** que la consola exporta o que escribes a mano:

| Artefacto | Carpeta |
|---|---|
| Políticas IAM (JSON) | `infra/iam/` |
| Definiciones de Step Functions (ASL JSON) y reglas de EventBridge | `orchestration/` |
| Reglas de Glue Data Quality (DQDL) | `services/risk-scoring/src/risk_scoring/data_quality/` |
| Dashboards y alarmas de CloudWatch (JSON) | `infra/observability/` |
| Configuración de Guardrails y esquemas OpenAPI del agente | `services/credit-assistant/src/credit_assistant/` |
| Configuración de Cognito (sin secretos) | `infra/auth/` |

- `infra/iac/` queda **reservado**.

## Alternativas consideradas

- **AWS CDK (Python):** todo sería reproducible, pero cada lab tardaría más y chocaría con las cajas de tiempo.
- **Terraform:** agrega otro lenguaje (HCL) y no suma para el MLA-C02.

## Cuándo revisar esta decisión

Después del examen, si LoanOps pasa a ser portafolio. Candidato natural: **CDK en Python**, porque es el mismo lenguaje que el resto del repo.

## Consecuencias

- ✅ Todo el tiempo de lab se va a los servicios que evalúa el examen.
- ⚠️ No hay un "deploy con un comando". Los recursos creados a mano **se olvidan**, así que la etiqueta `Project=LoanOps` y la [limpieza de los viernes](../../scripts/cleanup/) son obligatorias.
