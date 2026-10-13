"""Tests de la lectura de Parquet desde S3, con un cliente falso (sin llamar a AWS)."""

import io

import pandas as pd
import pytest
from botocore.exceptions import ClientError
from loanops_core.aws import read_parquet_prefix


def _parquet_bytes(frame: pd.DataFrame) -> bytes:
    buffer = io.BytesIO()
    frame.to_parquet(buffer)
    return buffer.getvalue()


class FakeS3Client:
    """Imita list_objects_v2 paginado y get_object sobre un diccionario key -> bytes."""

    def __init__(self, objects: dict[str, bytes], fail_on_get: bool = False) -> None:
        self.objects = objects
        self.fail_on_get = fail_on_get

    def get_paginator(self, operation_name: str) -> "FakeS3Client":
        return self

    def paginate(self, Bucket: str, Prefix: str) -> list[dict]:
        keys = [key for key in self.objects if key.startswith(Prefix)]
        return [{"Contents": [{"Key": key} for key in keys]}]

    def get_object(self, Bucket: str, Key: str) -> dict:
        if self.fail_on_get:
            raise ClientError({"Error": {"Code": "AccessDenied", "Message": "denied"}}, "GetObject")
        return {"Body": io.BytesIO(self.objects[Key])}


def test_concatenates_all_part_files_and_skips_non_parquet() -> None:
    client = FakeS3Client(
        {
            "creditColombia/": b"",
            "creditColombia/part-0.parquet": _parquet_bytes(pd.DataFrame({"id": [1, 2]})),
            "creditColombia/part-1.parquet": _parquet_bytes(pd.DataFrame({"id": [3]})),
            "creditColombia/_SUCCESS": b"",
        }
    )

    dataset = read_parquet_prefix(client, bucket="curated", prefix="creditColombia/")

    assert dataset["id"].tolist() == [1, 2, 3]


def test_empty_prefix_raises_clear_error() -> None:
    with pytest.raises(FileNotFoundError, match="No parquet files"):
        read_parquet_prefix(FakeS3Client({}), bucket="curated", prefix="creditColombia/")


def test_aws_error_is_wrapped_with_location() -> None:
    client = FakeS3Client(
        {"creditColombia/part-0.parquet": b"irrelevant"},
        fail_on_get=True,
    )

    with pytest.raises(RuntimeError, match="s3://curated/creditColombia/"):
        read_parquet_prefix(client, bucket="curated", prefix="creditColombia/")
