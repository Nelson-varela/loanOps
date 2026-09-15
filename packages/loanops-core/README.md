# loanops-core

Código compartido por `services/`, `apps/api` y los notebooks de `labs/`. **Si algo se usa en dos lugares, vive aquí.**

| Módulo | Responsabilidad |
|---|---|
| [config/](src/loanops_core/config/) | Única fuente de región, perfil, nombres de buckets y ARNs. Lee `.env`. |
| [tagging/](src/loanops_core/tagging/) | Pone `Project=LoanOps` en todo recurso que se cree por SDK. |
| [aws/](src/loanops_core/aws/) | Fábrica de clientes `boto3` con la región y el perfil de `config`. |

Se crea en el **Lab 1** ([ADR-0001](../../docs/adr/0001-monorepo-structure.md)).

## Reglas

- **Sin lógica de negocio**: eso va en `services/`.
- **No depende de `services/` ni de `apps/`**: la dependencia va en un solo sentido.
