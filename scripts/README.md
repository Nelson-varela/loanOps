# Scripts

| Carpeta | Qué va |
|---|---|
| [setup/](setup/) | Descarga de datasets a `data/raw/`, generación de documentos sintéticos y, en el futuro, alta de usuarios en Cognito |
| [cleanup/](cleanup/) | Limpieza de los viernes: checklist y un script que **lista** los recursos que cobran |

## Reglas

- Los scripts se pueden correr varias veces sin romper nada (idempotentes).
- Leen la región y el perfil del `.env`.
- **Nunca borran nada sin confirmación explícita.**
