# Orchestration

Capa transversal a las dos vías (Dominio 3). Se construye en el [Lab 11](../labs/lab-11-orchestration-monitoring-security/).

| Carpeta | Qué va |
|---|---|
| [step-functions/](step-functions/) | Definición ASL (JSON) del pipeline reentrenar → evaluar → registrar → desplegar |
| [eventbridge/](eventbridge/) | Reglas que disparan el pipeline |

- **Sin IaC** ([ADR-0002](../docs/adr/0002-no-iac-for-now.md)): se versiona el JSON exportado de la consola.
- **Nota del temario (plan §6):** EventBridge sigue vivo como *disparador* de orquestación (3.3). Lo que se eliminó es el ángulo de *monitoreo de infraestructura*.
- **Solo lectura, no se construye:** SageMaker Pipelines, MWAA y CodePipeline → [tabla 13](../study/decision-tables/13-orchestration.md).
