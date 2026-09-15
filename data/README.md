# Data

Espejo local de los buckets S3 del plan (§2). Los datos son **minúsculos a propósito**.

| Carpeta local | Bucket S3 | ¿Se versiona? | Contenido |
|---|---|---|---|
| `raw/` | `loanops-raw` | ❌ No (en `.gitignore`) | German Credit; Give Me Some Credit (opcional) |
| — | `loanops-curated` | — | Lo produce el Glue job del Lab 1 (Parquet particionado). No existe en local. |
| `docs/credit-policy/` | `loanops-docs` | ✅ Sí | Política de crédito generada con un LLM: criterios DTI y LTV, excepciones, matriz de aprobación (PDF de 10–15 páginas) |
| `docs/payslips/` | `loanops-docs` | ✅ Sí | 5–10 recibos de nómina sintéticos |
| `samples/` | — | ✅ Sí (< 1 MB) | Muestras pequeñas para tests y notebooks |

## Fuentes

| Dataset | Tamaño | Por qué |
|---|---|---|
| **German Credit** (UCI) | 1.000 filas | Los jobs corren en minutos y cuestan centavos. Trae atributos protegidos, así que los labs de sesgo salen solos. |
| **Give Me Some Credit** (Kaggle), opcional | 150k filas, ~7% de default | Desbalance realista |

## Reglas

- **Nunca PII real.** Todos los documentos de solicitantes son sintéticos.
- `raw/` no se versiona: revisa los términos de cada dataset antes de redistribuir cualquier cosa.
- Los scripts de descarga y de generación de sintéticos van en [scripts/setup/](../scripts/setup/).
- Los nombres de los buckets salen de `.env` / `loanops_core.config`, nunca escritos a mano.
