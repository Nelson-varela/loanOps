"""Lectura de datasets tabulares almacenados en Amazon S3."""

import io
import logging

import pandas as pd
from botocore.client import BaseClient
from botocore.exceptions import BotoCoreError, ClientError

logger = logging.getLogger(__name__)

PARQUET_SUFFIX = ".parquet"


def read_parquet_prefix(s3_client: BaseClient, bucket: str, prefix: str) -> pd.DataFrame:
    """Lee y concatena todos los .parquet bajo un prefijo (Glue escribe uno o varios part-files)."""
    try:
        paginator = s3_client.get_paginator("list_objects_v2")
        keys = [
            obj["Key"]
            for page in paginator.paginate(Bucket=bucket, Prefix=prefix)
            for obj in page.get("Contents", [])
            if obj["Key"].endswith(PARQUET_SUFFIX)
        ]
        if not keys:
            raise FileNotFoundError(f"No parquet files under s3://{bucket}/{prefix}")

        frames = []
        for key in sorted(keys):
            logger.info("Reading s3://%s/%s", bucket, key)
            body = s3_client.get_object(Bucket=bucket, Key=key)["Body"].read()
            frames.append(pd.read_parquet(io.BytesIO(body)))
    except (BotoCoreError, ClientError) as error:
        raise RuntimeError(f"Could not read s3://{bucket}/{prefix}: {error}") from error

    return pd.concat(frames, ignore_index=True)
