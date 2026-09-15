# Auth · Cognito (futuro)

> **Ahora: 0 h.** Unos 45 minutos de consola cuando llegue el frontend. Detalle y porqué en [ADR-0003](../../docs/adr/0003-auth-cognito-jwt.md).

## Pasos

1. **User pool** con inicio de sesión por email.
2. **App client** público (sin secreto), para la SPA. Anota el client id en `COGNITO_APP_CLIENT_ID` del `.env`.
3. **Grupos** `analyst` y `admin`.
4. **Usuario de prueba**, agregado al grupo `analyst`.
5. **Hosted UI / managed login:** el dominio de Cognito y la callback URL del frontend.
6. **JWT authorizer** en el HTTP API de [apps/api](../../apps/api/):
   - Issuer: `https://cognito-idp.<region>.amazonaws.com/<userPoolId>`
   - Audience: `<app client id>`
   - Identity source: `$request.header.Authorization`
7. Exporta a esta carpeta la configuración **sin secretos** (por ejemplo, `user-pool.json`).

Pon la etiqueta `Project=LoanOps` en el user pool.

## Regla de fronteras

- **JWT:** solo para personas (web → api).
- **Entre servicios:** roles IAM, nunca JWT.
