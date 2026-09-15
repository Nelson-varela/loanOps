#!/usr/bin/env bash
# Viernes de limpieza (plan §9): LISTA los recursos que cobran por hora. No borra nada.
# Uso: bash scripts/cleanup/friday-cleanup.sh
# Lee AWS_REGION y AWS_PROFILE del entorno o, si no están, del .env de la raíz del repo.
set -uo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"

read_env() {
  [[ -f "$ROOT/.env" ]] || return 0
  grep -E "^$1=" "$ROOT/.env" | tail -n 1 | cut -d= -f2- | tr -d '\r'
}

REGION="${AWS_REGION:-$(read_env AWS_REGION)}"
PROFILE="${AWS_PROFILE:-$(read_env AWS_PROFILE)}"

if [[ -z "$REGION" ]]; then
  echo "Falta AWS_REGION: defínela en .env (ver .env.example)." >&2
  exit 1
fi
[[ -n "$PROFILE" ]] && export AWS_PROFILE="$PROFILE"

run() {
  aws --region "$REGION" "$@" || echo "  (no se pudo consultar: revisa permisos o si el servicio existe en la región)"
}

section() { printf '\n=== %s ===\n' "$1"; }

echo "Región: $REGION · Perfil: ${AWS_PROFILE:-default}"

section "SageMaker: endpoints (se cobran por hora)"
run sagemaker list-endpoints --query 'Endpoints[].[EndpointName,EndpointStatus]' --output table

section "SageMaker Studio: apps en servicio"
run sagemaker list-apps --query "Apps[?Status=='InService'].[DomainId,UserProfileName,SpaceName,AppType,AppName]" --output table

section "SageMaker: notebook instances en servicio"
run sagemaker list-notebook-instances --status-equals InService --query 'NotebookInstances[].[NotebookInstanceName,InstanceType]' --output table

section "SageMaker: monitoring schedules activos"
run sagemaker list-monitoring-schedules --status-equals Scheduled --query 'MonitoringScheduleSummaries[].[MonitoringScheduleName,EndpointName]' --output table

section "SageMaker: tracking servers de MLflow"
run sagemaker list-mlflow-tracking-servers --query 'TrackingServerSummaries[].[TrackingServerName,TrackingServerStatus]' --output table

section "OpenSearch Serverless: colecciones (OCUs mínimas aunque no se usen)"
run opensearchserverless list-collections --query 'collectionSummaries[].[name,status]' --output table

section "RDS: instancias"
run rds describe-db-instances --query 'DBInstances[].[DBInstanceIdentifier,DBInstanceStatus,DBInstanceClass]' --output table

section "Bedrock: Provisioned Throughput"
run bedrock list-provisioned-model-throughputs --query 'provisionedModelSummaries[].[provisionedModelName,status]' --output table

section "EC2: VPC interface endpoints (se cobran por hora)"
run ec2 describe-vpc-endpoints --filters Name=vpc-endpoint-type,Values=Interface --query 'VpcEndpoints[].[VpcEndpointId,ServiceName,State]' --output table

section "EC2: NAT gateways disponibles"
run ec2 describe-nat-gateways --filter Name=state,Values=available --query 'NatGateways[].[NatGatewayId,VpcId]' --output table

section "Todo lo etiquetado Project=LoanOps"
run resourcegroupstaggingapi get-resources --tag-filters Key=Project,Values=LoanOps --query 'ResourceTagMappingList[].ResourceARN' --output text

printf '\nSiguiente paso: borra lo que no uses la próxima semana (checklist en scripts/cleanup/README.md).\n'
