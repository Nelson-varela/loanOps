# ADR-0001 · Estructura de monorepo

- **Estado:** Aceptado
- **Fecha:** 2026-09-15

## Contexto

LoanOps tiene:

- dos vías de producto: la A (riesgo de default con ML clásico) y la B (asistente con RAG, agente y guardrails);
- una capa transversal de orquestación, monitoreo y seguridad;
- 11 labs con time-box, que son experiencias de aprendizaje y no módulos de código;
- un track de estudio que se lleva el 73% de las 84 horas;
- una API y un frontend para el analista, en el futuro.

Todo tiene que vivir en **un solo repositorio** que se pueda leer rápido y extender sin reorganizar.

## Decisión

Monorepo con el patrón **apps / services / packages**, más carpetas transversales:

| Carpeta | Rol |
|---|---|
| `services/` | Un dominio de negocio por carpeta: `risk-scoring` (Vía A) y `credit-assistant` (Vía B). **El código se organiza por dominio, no por lab.** |
| `packages/` | Código compartido (`loanops-core`: configuración, etiquetas, clientes AWS). |
| `apps/` | Interfaces: `api` (BFF) y `web` (frontend). Futuro. |
| `orchestration/`, `infra/` | Transversales a las dos vías. |
| `labs/` | Bitácora de labs y único lugar de notebooks ([ADR-0004](0004-notebooks-policy.md)). |
| `study/` | Material de certificación. |
| `docs/` | Plan, arquitectura y ADRs. |
| `data/` | Espejo local de los buckets S3. |

Convenciones:

- Carpetas y código en **inglés**; contenido en **español**.
- Carpetas de servicio con guion (`risk-scoring`) y paquetes Python con guion bajo (`risk_scoring`), dentro de `src/`.
- **Tooling de Python:** un workspace de `uv` con miembros `packages/*`, `services/*` y `apps/api`. Se configura en el **Lab 1**, cuando exista el primer código, junto con `pre-commit install` y `nbdime config-git --enable`. No se crean `pyproject.toml` vacíos antes de tiempo.

## Alternativas consideradas

- **Organizar por lab** (`lab-01/`, `lab-02/`, … con su código dentro): se descartó porque el código de un lab se reutiliza en otros (el endpoint del Lab 9 se usa en el Lab 10, y la configuración en todos). Organizar así termina en copias.
- **Varios repos** (uno por vía y uno para estudio): se descartó porque multiplica el setup y rompe los links entre labs, código y tablas.

## Consecuencias

- ✅ Un servicio o una app nueva se agrega como carpeta hermana, sin tocar lo existente.
- ✅ Los labs apuntan al código y el código no depende de los labs.
- ✅ `study/` se puede extraer si LoanOps se vuelve portafolio.
- ⚠️ Al inicio hay muchas carpetas vacías con `.gitkeep`.
- ⚠️ Hace falta disciplina para no dejar lógica en los notebooks ([ADR-0004](0004-notebooks-policy.md)).
