"""Creación centralizada de sesiones y clientes AWS."""

import boto3
from botocore.client import BaseClient

from loanops_core.config import Settings


def create_aws_session(
    settings: Settings,
) -> boto3.Session:
    """Crea una sesión AWS usando la configuración de LoanOps."""

    return boto3.Session(
        profile_name=settings.aws_profile,
        region_name=settings.aws_region,
    )


def create_s3_client(
    settings: Settings,
) -> BaseClient:
    """Crea un cliente de Amazon S3."""

    session = create_aws_session(settings)

    return session.client("s3")
