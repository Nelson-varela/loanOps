# ADR-0004 · Política de notebooks sin duplicados

- **Estado:** Aceptado
- **Fecha:** 2026-09-15

## Contexto

Los notebooks son la herramienta natural de los labs, pero generan duplicados de cuatro formas:

1. **Código repetido:** una función se copia de un notebook a otro, o del notebook a `services/`, y las copias se desincronizan.
2. **Constantes repetidas:** nombres de buckets, región y ARNs pegados en cada notebook.
3. **Archivos repetidos:** `Untitled1.ipynb`, `lab-04-Copy1.ipynb`, `lab (1).ipynb`, subidas manuales a SageMaker Studio y `.ipynb_checkpoints/`.
4. **Outputs versionados:** tablas y gráficas embebidas que inflan cada commit y ensucian los diffs.

## Decisión

| Problema | Regla o mecanismo |
|---|---|
| Código repetido | **Los notebooks solo importan y llaman; no definen lógica reutilizable.** Si una función se usa dos veces, se mueve a `services/` o a `packages/`. |
| Constantes repetidas | Hay **una sola fuente**: `loanops_core.config`. Ningún notebook escribe nombres de recursos a mano. |
| Archivos repetidos | **Un notebook por lab**, con el mismo nombre que su carpeta (`labs/lab-04-training/lab-04-training.ipynb`). Los notebooks viven **solo** en `labs/`. El `.gitignore` bloquea `Untitled*.ipynb`, `*-Copy*.ipynb`, `*(N).ipynb` y `.ipynb_checkpoints/`. |
| Subidas manuales a Studio | En SageMaker Studio se **clona el repo con git** y se trabaja sobre el clon. Nunca se sube ni se descarga un `.ipynb` a mano. |
| Outputs versionados | `nbstripout` corre en `pre-commit` y quita los outputs antes de cada commit. Los resultados que importan se escriben en el README del lab, en la sección de bitácora. |
| Archivos generados | Las salidas locales van a `labs/**/outputs/` (ignorada por git) o a S3. |

La plantilla está en [labs/_template/lab.ipynb](../../labs/_template/lab.ipynb). Los notebooks de los labs ya están creados con el nombre correcto, así que no hace falta crear uno nuevo.

## Consecuencias

- ✅ Un notebook corresponde a un lab y a un archivo en git; no hay copias huérfanas.
- ✅ La lógica queda en módulos con tests, reutilizable en el Lab 10, el Lab 11 y `apps/api`.
- ⚠️ Hay que activar `pre-commit` en el Lab 1. Mientras no esté activo, limpia los outputs a mano antes de hacer commit (*Kernel → Restart & Clear Output*).
- ⚠️ Importar desde `services/` exige tener instalado el workspace (`uv sync`, Lab 1).
