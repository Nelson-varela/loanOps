# api · BFF del analista (futuro)

> **Estado:** no se construye durante el plan de certificación. Empieza después del examen.

## Por qué existe

El navegador no puede llamar a SageMaker ni a Bedrock con credenciales AWS. Esta API es lo **único** que toca el frontend: valida la identidad y llama a los modelos con un rol IAM de menor privilegio.

```
apps/web ──HTTPS + JWT──▶ API Gateway (HTTP API + JWT authorizer) ──▶ Lambda (esta app)
                                                                        │ IAM
                                                  ┌─────────────────────┴─────────────────────┐
                                        endpoint de risk-scoring                  agente de credit-assistant
```

## Estructura

| Carpeta | Qué va |
|---|---|
| [src/loanops_api/auth/](src/loanops_api/auth/) | Chequeo de rol por ruta: lee `cognito:groups` de los claims que **API Gateway ya validó**. No verifica firmas. |
| [src/loanops_api/routes/](src/loanops_api/routes/) | `/score` y `/explain` (analyst), `/assistant/chat` (analyst), `/admin/*` (admin) |
| [src/loanops_api/clients/](src/loanops_api/clients/) | SageMaker Runtime (`invoke_endpoint`) y Bedrock Agent Runtime (`invoke_agent`) |
| [tests/](tests/) | Tests de la API |

## Autenticación

[ADR-0003](../../docs/adr/0003-auth-cognito-jwt.md): los JWT de Cognito se usan para personas; hacia los modelos se usa IAM. La configuración de Cognito vive en [infra/auth/](../../infra/auth/).

## Reglas

- No importa código de entrenamiento: habla con los modelos **ya desplegados**.
- La configuración viene de `loanops_core.config`.
