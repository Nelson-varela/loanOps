"""Carga del dataset de riesgo desde la zona curated de S3."""

import pandas as pd
from loanops_core.aws import create_s3_client, read_parquet_prefix
from loanops_core.config import Settings

from risk_scoring.data_prep.schema import validate_dataset

# Prefijo donde el job de Glue deja el dataset limpio (el nombre del part-file cambia por corrida).
CURATED_DATASET_PREFIX = "creditColombia/"


def load_curated_dataset(settings: Settings) -> pd.DataFrame:
    """Lee el dataset curated de S3 y valida su contrato antes de devolverlo."""
    dataset = read_parquet_prefix(
        create_s3_client(settings),
        bucket=settings.s3_bucket_curated,
        prefix=CURATED_DATASET_PREFIX,
    )
    validate_dataset(dataset)
    return dataset
