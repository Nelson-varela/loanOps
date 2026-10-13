"""Contrato del dataset de riesgo: columnas requeridas y reglas de integridad."""

from __future__ import annotations

from collections.abc import Iterable

import pandas as pd

# Orden de columnas tal como las produce la generación del dataset sintético.
REQUIRED_COLUMNS: tuple[str, ...] = (
    "credit_id",
    "application_date",
    "age",
    "sex",
    "department",
    "city",
    "municipality_code",
    "employment_type",
    "months_in_current_activity",
    "monthly_income",
    "monthly_expenses",
    "existing_debt",
    "requested_amount",
    "loan_term_months",
    "interest_rate",
    "loan_purpose",
    "housing_status",
    "previous_loans",
    "previous_defaults",
    "days_past_due_history",
    "debt_to_income_ratio",
    "credit_type",
    "productive_subtype",
    "has_collateral",
    "default_90d",
    "record_type",
)

PRODUCTIVE_CREDIT_TYPE = "productive"

# Código DANE de municipio: dos dígitos de departamento + tres de municipio.
MUNICIPALITY_CODE_PATTERN = r"\d{5}"


class DatasetValidationError(ValueError):
    """El dataset no cumple el contrato esperado."""


def validate_dataset(dataset: pd.DataFrame) -> None:
    """Valida el contrato del dataset y falla en el primer incumplimiento."""
    missing_columns = [column for column in REQUIRED_COLUMNS if column not in dataset.columns]
    if missing_columns:
        raise DatasetValidationError(f"Missing required columns: {', '.join(missing_columns)}")

    duplicated_ids = dataset.loc[dataset["credit_id"].duplicated(), "credit_id"]
    if not duplicated_ids.empty:
        raise DatasetValidationError(
            f"Duplicated credit_id values: {_as_list(duplicated_ids.unique())}"
        )

    codes = dataset["municipality_code"].astype("string")
    valid_codes = codes.str.fullmatch(MUNICIPALITY_CODE_PATTERN).fillna(False).astype(bool)
    invalid_codes = dataset.loc[~valid_codes, "credit_id"]
    if not invalid_codes.empty:
        raise DatasetValidationError(
            f"municipality_code must be exactly five digits: {_as_list(invalid_codes)}"
        )

    is_productive = dataset["credit_type"] == PRODUCTIVE_CREDIT_TYPE
    has_subtype = dataset["productive_subtype"].notna()

    missing_subtype = dataset.loc[is_productive & ~has_subtype, "credit_id"]
    if not missing_subtype.empty:
        raise DatasetValidationError(
            f"Productive credits without productive_subtype: {_as_list(missing_subtype)}"
        )

    unexpected_subtype = dataset.loc[~is_productive & has_subtype, "credit_id"]
    if not unexpected_subtype.empty:
        raise DatasetValidationError(
            f"Non-productive credits with productive_subtype: {_as_list(unexpected_subtype)}"
        )


def _as_list(values: Iterable[object]) -> str:
    return ", ".join(str(value) for value in values)
