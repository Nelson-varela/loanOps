# web · Consola del analista (futuro)

> **Estado:** futuro. El stack se decide en un ADR cuando empiece el desarrollo.

## Alcance

- Login con la Hosted UI de Cognito.
- Score de riesgo de un solicitante con su explicación SHAP (*"por qué se negó este préstamo"*).
- Chat con el asistente de crédito.

## Estructura (feature-first)

| Carpeta | Qué va | Rutas de la API |
|---|---|---|
| [src/auth/](src/auth/) | Login, manejo del token, rutas protegidas | — |
| [src/features/risk-score/](src/features/risk-score/) | Vista del score con SHAP | `/score`, `/explain` |
| [src/features/assistant-chat/](src/features/assistant-chat/) | Chat con el asistente | `/assistant/chat` |

Cada funcionalidad nueva es una carpeta nueva en `src/features/`.

## Reglas

- **Nunca pongas credenciales AWS en el frontend.** Todo pasa por [apps/api](../api/).
- La configuración pública (user pool id, client id, URL de la API) llega por variables de entorno del build, nunca escrita en el código.
