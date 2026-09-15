# Infra · Plataforma AWS compartida

**Sin IaC por ahora** ([ADR-0002](../docs/adr/0002-no-iac-for-now.md)): los recursos se crean por consola o CLI y aquí se versionan los artefactos declarativos.

## Cuenta y región (llenar el día 1)

| | Valor |
|---|---|
| Cuenta | ____ (usuario IAM sin root, con MFA) |
| **Región** | ____ (verificada: tiene Bedrock KB, S3 Vectors y AgentCore a la vez) |
| Acceso a modelos de Bedrock | Solicitado el ____ |
| Budget | Alertas en USD 50 y USD 100 |

## Convenciones

- Etiqueta `Project=LoanOps` en **todo**, para filtrar Cost Explorer por esa etiqueta.
- Nombres con el formato `loanops-<componente>`. Los recursos con nombre global (como los buckets) llevan `-<account-id>` al final.
- Instancias: `ml.m5.large` para entrenar y `ml.t3.medium` para notebooks. **Nunca GPU.**
- **Una sola región.** Los recursos huérfanos en otra región son como se pierden USD 200 sin darse cuenta.

## Carpetas

| Carpeta | Qué va | Cuándo |
|---|---|---|
| [auth/](auth/) | Cognito: user pool, app client y grupos ([ADR-0003](../docs/adr/0003-auth-cognito-jwt.md)) | Futuro |
| [iam/](iam/) | Políticas de menor privilegio (JSON) | Lab 11 |
| [security/](security/) | KMS en los buckets, CloudTrail, Macie | Tour 3, Lab 11 |
| [network/](network/) | VPC y VPC endpoints sin salida a internet | Lab 9 |
| [observability/](observability/) | Dashboards y alarmas de CloudWatch (JSON) | Lab 11 |
| [cost/](cost/) | Budgets | Día 1 |
| [iac/](iac/) | Reservado | Después del examen |

## ⚠️ Las tres trampas caras (plan §9)

1. **OpenSearch Serverless** cobra OCUs mínimas aunque no lo uses, y una colección olvidada un mes cuesta cientos de dólares. Para el Lab 7 usa S3 Vectors o pgvector.
2. **Los endpoints de SageMaker** se cobran por hora, estén en uso o no (`ml.m5.large` durante un mes ≈ USD 80). Bórralos al terminar cada sesión.
3. **Las apps de SageMaker Studio** siguen corriendo después de cerrar el navegador. Apágalas de forma explícita.

Presupuesto estimado: **USD 40–90** en las 7 semanas. Cada viernes → [limpieza](../scripts/cleanup/).
