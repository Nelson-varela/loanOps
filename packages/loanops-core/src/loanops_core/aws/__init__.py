"""Clientes AWS compartidos por LoanOps."""

from loanops_core.aws.clients import (
    create_aws_session,
    create_s3_client,
)
from loanops_core.aws.s3_io import read_parquet_prefix

__all__ = [
    "create_aws_session",
    "create_s3_client",
    "read_parquet_prefix",
]
