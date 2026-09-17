# LoanOps

Monorepo del proyecto **LoanOps**, el dispositivo mnemotécnico para la certificación **AWS Certified Machine Learning Engineer – Associate (MLA-C02 beta)**, a presentarse a finales de octubre de 2026.

Plan maestro: [docs/loanops-aws-mla-c02-v3.md](docs/loanops-aws-mla-c02-v3.md)

LoanOps es un banco que:

- **Vía A · Riesgo de default:** calcula la probabilidad de que un solicitante no pague, con explicabilidad, detección de sesgo y monitoreo. Vive en [services/risk-scoring/](services/risk-scoring/).
- **Vía B · Asistente de crédito:** le da al analista un asistente que responde sobre la política de crédito y los documentos del solicitante, con RAG, agente y guardrails. Vive en [services/credit-assistant/](services/credit-assistant/).

> LoanOps **no es una pieza de portafolio** (plan §2). Si hay que elegir entre certificación y pulir el repo, gana la certificación.

---

## Mapa del repo

| Carpeta | Qué hay | Cuándo la tocas |
|---|---|---|
| [study/](study/) | Tablas de decisión, checklist de skills, preguntas, compuertas, tarjetas | Todos los días (73% de las horas) |
| [labs/](labs/) | Bitácora de los 11 labs y el **único** lugar donde van los notebooks | En cada lab |
| [services/risk-scoring/](services/risk-scoring/) | Código de la Vía A | Labs 1, 2, 4, 5, 9, 11 |
| [services/credit-assistant/](services/credit-assistant/) | Código de la Vía B | Tour 3 y Labs 6, 7, 8, 10 |
| [packages/loanops-core/](packages/loanops-core/) | Configuración, etiquetas y clientes AWS compartidos | Desde el Lab 1 |
| [orchestration/](orchestration/) | Step Functions y EventBridge | Lab 11 |
| [infra/](infra/) | IAM, KMS, VPC, CloudWatch, Budgets y Cognito | Día 1 y Labs 9 y 11 |
| [data/](data/) | Espejo local de los buckets S3 | Labs 1, 3 y 7 |
| [scripts/](scripts/) | Setup y limpieza de los viernes | Día 1 y cada viernes |
| [apps/](apps/) | API y frontend del analista (futuro) | Después del examen |
| [docs/](docs/) | Plan, arquitectura y ADRs | Cuando tomes una decisión de arquitectura |

## Por dónde empezar

1. [study/README.md](study/README.md): cómo es una sesión de estudio.
2. [labs/README.md](labs/README.md): qué lab toca esta semana.
3. [study/skills-checklist.md](study/skills-checklist.md): el instrumento con el que mides tu avance.
4. [docs/architecture/overview.md](docs/architecture/overview.md): qué servicio AWS vive en qué carpeta.

## Reglas del repo

- Carpetas y código en **inglés**; notas y documentación en **español**.
- Todo recurso AWS lleva la etiqueta `Project=LoanOps`. Se usa **una sola región**, anotada en [infra/README.md](infra/README.md).
- Ningún secreto se versiona. Usa `.env`, copiado de [.env.example](.env.example).
- Los notebooks van **solo en `labs/`**, uno por lab ([ADR-0004](docs/adr/0004-notebooks-policy.md)).
- La lógica reutilizable va en `services/` o `packages/`, nunca en un notebook.
- Cada decisión de arquitectura queda en un ADR en [docs/adr/](docs/adr/).
- Los estándares de código están en [CLAUDE.md](CLAUDE.md) y `ruff` los aplica en cada commit. Antes de un push con código, pasa `/code-review`.

## Calendario

| Semana | Fechas | Foco | Labs | Hito |
|---|---|---|---|---|
| S1 | 15–21 sep | Diagnóstico + D1 Datos | 1, 2, Tour 3 | Diagnóstico el día 2 |
| S2 | 22–28 sep | D2A ML clásico | 4, 5 | 80 preguntas |
| S3 | 29 sep–5 oct | D2B FM, RAG y evals | 6, 7, 8 | |
| S4 | 6–12 oct | D3A Inferencia, red y FMs | 9 | **Compuerta 1 · 12 oct** |
| S5 | 13–19 oct | D3B Agentes y orquestación | 10 | **Compuerta 2 · 19 oct** |
| S6 | 20–26 oct | D4 + primer simulacro | 11 | Simulacro 1 |
| S7 | 27 oct–examen | Consolidación, sin construir nada | — | Simulacro 2 |
