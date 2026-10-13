"""Configuración central de AWS para LoanOps."""

import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv


@dataclass(frozen=True)
class Settings:
    """Representa la configuración compartida de LoanOps."""

    aws_region: str
    project_tag: str
    s3_bucket_raw: str
    s3_bucket_curated: str
    s3_bucket_docs: str
    aws_profile: str | None = None

    @property
    def raw_bucket_uri(self) -> str:
        """Devuelve la URI completa del bucket RAW."""
        return f"s3://{self.s3_bucket_raw}"

    @property
    def curated_bucket_uri(self) -> str:
        """Devuelve la URI completa del bucket CURATED."""
        return f"s3://{self.s3_bucket_curated}"

    @property
    def docs_bucket_uri(self) -> str:
        """Devuelve la URI completa del bucket de documentos."""
        return f"s3://{self.s3_bucket_docs}"


def require_environment_variable(variable_name: str) -> str:
    """Obtiene una variable obligatoria o detiene la ejecución."""

    value = os.getenv(variable_name)

    if value is None or not value.strip():
        raise RuntimeError(f"Required environment variable is missing: {variable_name}")

    return value.strip()


def load_settings(
    env_file: str | Path | None = None,
) -> Settings:
    """Carga y valida la configuración de LoanOps."""

    load_dotenv(
        dotenv_path=env_file,
        override=False,
    )

    return Settings(
        aws_profile=os.getenv("AWS_PROFILE"),
        aws_region=require_environment_variable("AWS_REGION"),
        project_tag=require_environment_variable("PROJECT_TAG"),
        s3_bucket_raw=require_environment_variable("S3_BUCKET_RAW"),
        s3_bucket_curated=require_environment_variable("S3_BUCKET_CURATED"),
        s3_bucket_docs=require_environment_variable("S3_BUCKET_DOCS"),
    )
