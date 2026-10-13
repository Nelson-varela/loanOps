"""Tests del contrato del dataset de riesgo."""

import pandas as pd
import pytest
from risk_scoring.data_prep import (
    DatasetValidationError,
    validate_dataset,
)


@pytest.fixture
def valid_dataset() -> pd.DataFrame:
    """Construye un dataset mínimo que satisface el contrato."""

    return pd.DataFrame(
        {
            "credit_id": [
                "CR-001",
                "CR-002",
            ],
            "application_date": [
                "2024-10-15",
                "2025-02-10",
            ],
            "age": [
                32,
                45,
            ],
            "sex": [
                "male",
                "female",
            ],
            "department": [
                "Antioquia",
                "Cundinamarca",
            ],
            "city": [
                "Medellín",
                "Bogotá",
            ],
            "municipality_code": [
                "05001",
                "11001",
            ],
            "employment_type": [
                "employee",
                "self_employed",
            ],
            "months_in_current_activity": [
                48,
                72,
            ],
            "monthly_income": [
                5_000_000,
                8_000_000,
            ],
            "monthly_expenses": [
                2_000_000,
                3_500_000,
            ],
            "existing_debt": [
                3_000_000,
                5_000_000,
            ],
            "requested_amount": [
                10_000_000,
                20_000_000,
            ],
            "loan_term_months": [
                24,
                36,
            ],
            "interest_rate": [
                18.5,
                20.0,
            ],
            "loan_purpose": [
                "personal",
                "business",
            ],
            "housing_status": [
                "rent",
                "owned",
            ],
            "previous_loans": [
                1,
                3,
            ],
            "previous_defaults": [
                0,
                1,
            ],
            "days_past_due_history": [
                0,
                30,
            ],
            "debt_to_income_ratio": [
                0.35,
                0.50,
            ],
            "credit_type": [
                "consumer",
                "productive",
            ],
            "productive_subtype": [
                None,
                "productive_urban",
            ],
            "has_collateral": [
                0,
                1,
            ],
            "default_90d": [
                0,
                1,
            ],
            "record_type": [
                "synthetic_calibrated",
                "synthetic_calibrated",
            ],
        }
    )


def test_valid_dataset_passes(
    valid_dataset: pd.DataFrame,
) -> None:
    validate_dataset(valid_dataset)


def test_missing_column_is_rejected(
    valid_dataset: pd.DataFrame,
) -> None:
    invalid_dataset = valid_dataset.drop(columns=["city"])

    with pytest.raises(
        DatasetValidationError,
        match="Missing required columns",
    ):
        validate_dataset(invalid_dataset)


def test_duplicated_credit_id_is_rejected(
    valid_dataset: pd.DataFrame,
) -> None:
    invalid_dataset = valid_dataset.copy()
    invalid_dataset.loc[1, "credit_id"] = "CR-001"

    with pytest.raises(
        DatasetValidationError,
        match="Duplicated credit_id values",
    ):
        validate_dataset(invalid_dataset)


def test_invalid_municipality_code_is_rejected(
    valid_dataset: pd.DataFrame,
) -> None:
    invalid_dataset = valid_dataset.copy()
    invalid_dataset.loc[0, "municipality_code"] = "5001"

    with pytest.raises(
        DatasetValidationError,
        match="exactly five digits",
    ):
        validate_dataset(invalid_dataset)


def test_productive_credit_requires_subtype(
    valid_dataset: pd.DataFrame,
) -> None:
    invalid_dataset = valid_dataset.copy()
    invalid_dataset.loc[1, "productive_subtype"] = None

    with pytest.raises(
        DatasetValidationError,
        match="Productive credits without productive_subtype",
    ):
        validate_dataset(invalid_dataset)


def test_non_productive_credit_rejects_subtype(
    valid_dataset: pd.DataFrame,
) -> None:
    invalid_dataset = valid_dataset.copy()
    invalid_dataset.loc[
        0,
        "productive_subtype",
    ] = "productive_urban"

    with pytest.raises(
        DatasetValidationError,
        match="Non-productive credits with productive_subtype",
    ):
        validate_dataset(invalid_dataset)
