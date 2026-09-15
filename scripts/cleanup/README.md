# Viernes de limpieza (10 min, sin excepción · plan §9)

## 1. Lista lo que está cobrando

```bash
bash scripts/cleanup/friday-cleanup.sh
```

**Solo lista, no borra nada.** Usa la región y el perfil del `.env` y termina con los recursos que tienen la etiqueta `Project=LoanOps`.

## 2. Borra lo que no vas a usar la próxima semana

- [ ] **Endpoints de SageMaker:** `aws sagemaker delete-endpoint --endpoint-name <nombre>` (redesplegar toma ~6 min)
- [ ] **Apps de SageMaker Studio** (JupyterLab, Code Editor): detenlas desde Studio
- [ ] **Notebook instances:** detenlas
- [ ] **Monitoring schedules** de Model Monitor (Lab 11)
- [ ] **Tracking server de MLflow** (Lab 5)
- [ ] **Colecciones de OpenSearch Serverless** (no deberías tener ninguna)
- [ ] **RDS pgvector** (Lab 7): detenla o bórrala. Una RDS detenida se vuelve a encender sola a los 7 días.
- [ ] **VPC interface endpoints** (Lab 9)
- [ ] **Provisioned Throughput de Bedrock** (no deberías tener ninguno)
- [ ] **Regla de EventBridge** del Lab 11: desactívala
- [ ] **Macie** (Tour 3): suspéndelo si ya no lo usas

## 3. Revisa el gasto

- [ ] Cost Explorer filtrado por `Project=LoanOps`
- [ ] El Budget (alertas en USD 50 y USD 100)
- [ ] Que no haya recursos en otra región

## Registro

| Fecha | Qué borré | Gasto acumulado (USD) |
|---|---|---|
| | | |
