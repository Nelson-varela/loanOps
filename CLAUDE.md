# LoanOps · Estándares del repo

Proyecto de estudio para la certificación AWS MLA-C02 (plan en [docs/loanops-aws-mla-c02-v3.md](docs/loanops-aws-mla-c02-v3.md)). Dos vías: `services/risk-scoring` (riesgo de default) y `services/credit-assistant` (asistente RAG con agente).

**El tiempo del examen manda.** Prefiere la solución simple y directa sobre la elegante. Si algo no compra un skill del examen ni evita un error caro, no va.

## Estructura

- El código reutilizable vive en `services/` o `packages/`, organizado **por dominio, no por lab**.
- Los **notebooks van solo en `labs/`**, uno por lab. Solo importan y llaman: si una función se usa dos veces, se mueve a `services/` o `packages/`. Detalle en [ADR-0004](docs/adr/0004-notebooks-policy.md).
- `packages/loanops-core` no depende de `services/` ni de `apps/`. La dependencia va en un solo sentido.
- Decisión de arquitectura nueva → un ADR en [docs/adr/](docs/adr/).

## Python

- Python 3.12, formateado y revisado con `ruff` (config en [ruff.toml](ruff.toml)).
- **Nombres de variables, funciones y archivos en inglés; comentarios y docstrings en español.**
- Type hints en las firmas públicas. Docstring de una línea cuando el nombre no basta.
- Tests con `pytest`, en el `tests/` de cada servicio.
- Nada de `print` para diagnóstico en código de servicio: usa `logging`.

## AWS

- **Ningún nombre de recurso escrito a mano.** Región, buckets y ARNs salen de `loanops_core.config`, que lee el `.env`.
- Todo recurso creado por SDK lleva la etiqueta `Project=LoanOps`.
- Nunca credenciales ni secretos en el código ni en los notebooks. Van en `.env`, que está en `.gitignore`.
- Nunca PII real: los documentos de solicitantes son sintéticos.
- Instancias: `ml.m5.large` para entrenar, `ml.t3.medium` para notebooks. **Nunca GPU.**
- Almacén vectorial: S3 Vectors o RDS pgvector. **Nunca OpenSearch Serverless** (cobra aunque no se use).
- Lo que se cobra por hora (endpoints, apps de Studio, VPC interface endpoints, RDS) se borra al terminar la sesión.

## Qué señalar en una revisión

1. Credenciales, secretos o ARNs escritos a mano en el código.
2. Recursos que quedan encendidos y cobran, o sin la etiqueta `Project=LoanOps`.
3. Lógica reutilizable atrapada en un notebook, o código duplicado entre notebook y servicio.
4. Errores de correctitud: fugas de datos entre train y test, métricas mal elegidas con clases desbalanceadas, manejo de fallos ausente en llamadas a AWS.
5. Complejidad que no hace falta: abstracciones para un solo uso, configuración que nadie lee.

## Como responderme a mi? 

1. siempre se especifico con lo que hagas, y trata de explicarme el codigo que generes, especialmente  las partes mas relevantes. 