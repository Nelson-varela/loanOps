# ADR-0003 · Autenticación con JWT emitidos por Cognito

- **Estado:** Aceptado
- **Fecha:** 2026-09-15

## Contexto

- El frontend del analista ([apps/web](../../apps/web/)) y su API ([apps/api](../../apps/api/)) llegarán en el futuro y necesitan autenticación básica con JWT.
- **No debe consumir tiempo del plan de certificación.**
- Es un banco regulado: guardar contraseñas propias es un riesgo que no hace falta asumir.

## Decisión

**Amazon Cognito User Pool** emite los JWT y el **JWT authorizer de API Gateway (HTTP API)** los valida antes de que el request llegue a la Lambda.

| Pieza | Carpeta | Esfuerzo estimado |
|---|---|---|
| User pool, app client público (sin secreto), grupos `analyst` y `admin`, un usuario de prueba | [infra/auth/](../../infra/auth/) | ~30 min de consola |
| JWT authorizer en el HTTP API: *issuer* `https://cognito-idp.<region>.amazonaws.com/<userPoolId>`, *audience* = app client id | [infra/auth/README.md](../../infra/auth/README.md) | ~15 min, sin código |
| Chequeo de rol por ruta: leer `cognito:groups` de `event.requestContext.authorizer.jwt.claims` | [apps/api/src/loanops_api/auth/](../../apps/api/src/loanops_api/auth/) | Una función corta |
| Login con la Hosted UI de Cognito, guardado del token y rutas protegidas | [apps/web/src/auth/](../../apps/web/src/auth/) | Al construir el frontend |

**Total: unas 1–1.5 h cuando llegue el frontend. Ahora: 0 h.**

### Regla de fronteras

- **Los JWT son solo para personas** (web → api).
- **Entre servicios se usan roles IAM** (agente → endpoint de SageMaker, Step Functions → SageMaker, api → endpoint o agente). Nunca un JWT.

## Alternativas consideradas

- **JWT propios** (PyJWT, tabla de usuarios, hash de contraseñas, endpoint de login, rotación de la clave de firma): hay más código, más horas y hay que custodiar contraseñas. Se descarta.

## Consecuencias

- ✅ No hay que escribir código para emitir tokens, guardar contraseñas ni verificar firmas.
- ✅ Es el patrón de "mínimo esfuerzo operativo" que el examen premia (plan §11).
- ⚠️ Queda acoplado al formato de claims de Cognito.
- ⚠️ Verifícalo al implementar: en los HTTP API, los claims que son listas (como `cognito:groups`) pueden llegar serializados como string, por ejemplo `"[analyst admin]"`. Parsea con cuidado.
