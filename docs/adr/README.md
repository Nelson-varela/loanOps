# Architecture Decision Records (ADR)

Un ADR guarda **una** decisión de arquitectura: el contexto en que se tomó, qué se decidió y qué consecuencias trae. Sirve para que en tres meses sepas *por qué* el repo es como es.

## Cómo crear uno

1. Copia [0000-template.md](0000-template.md) como `NNNN-titulo-corto.md`, usando el siguiente número libre.
2. Llénalo y déjalo en estado **Propuesto**. Cuando lo decidas, pásalo a **Aceptado**.
3. Un ADR aceptado **no se edita**. Si cambias de opinión, escribe uno nuevo que lo reemplace y marca el viejo como **Reemplazado por ADR-XXXX**.

## Índice

| # | Decisión | Estado |
|---|---|---|
| [0001](0001-monorepo-structure.md) | Estructura de monorepo | Aceptado |
| [0002](0002-no-iac-for-now.md) | Sin IaC por ahora | Aceptado |
| [0003](0003-auth-cognito-jwt.md) | Autenticación con JWT de Cognito | Aceptado |
| [0004](0004-notebooks-policy.md) | Política de notebooks sin duplicados | Aceptado |
