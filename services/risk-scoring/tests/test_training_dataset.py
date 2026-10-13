"""Tests de la preparación del dataset para XGBoost."""

import pandas as pd
import pytest
from risk_scoring.training import LABEL_COLUMN, build_features, stratified_split


@pytest.fixture
def raw_dataset() -> pd.DataFrame:
    """Dataset de 100 filas con 20 % de defaults y las columnas que usa build_features."""
    rows = 100
    is_productive = [i % 5 == 0 for i in range(rows)]
    return pd.DataFrame(
        {
            "credit_id": [f"CO-{i:06d}" for i in range(rows)],
            "sex": ["female", "male"] * (rows // 2),
            "age": range(18, 18 + rows),
            "months_in_current_activity": 12,
            "monthly_income": 3_000_000,
            "monthly_expenses": 1_000_000,
            "existing_debt": 0,
            "requested_amount": 5_000_000,
            "loan_term_months": 24,
            "interest_rate": 20.5,
            "previous_loans": 1,
            "previous_defaults": 0,
            "days_past_due_history": 0,
            "debt_to_income_ratio": 0.3,
            "has_collateral": 0,
            "department": ["Antioquia", "Bogotá D.C."] * (rows // 2),
            "employment_type": "salaried",
            "loan_purpose": "consumption",
            "housing_status": "rent",
            "credit_type": ["productive" if p else "consumer" for p in is_productive],
            "productive_subtype": ["productive_urban" if p else None for p in is_productive],
            LABEL_COLUMN: [1 if i % 5 == 1 else 0 for i in range(rows)],
        }
    )


def test_features_are_numeric_with_label_first(raw_dataset: pd.DataFrame) -> None:
    features = build_features(raw_dataset)

    assert features.columns[0] == LABEL_COLUMN
    assert all(pd.api.types.is_numeric_dtype(dtype) for dtype in features.dtypes)
    assert not features.isna().any().any()


def test_excludes_identifier_and_protected_attribute(raw_dataset: pd.DataFrame) -> None:
    columns = build_features(raw_dataset).columns

    assert "credit_id" not in columns
    assert not any(column.startswith("sex") for column in columns)


def test_missing_subtype_becomes_its_own_category(raw_dataset: pd.DataFrame) -> None:
    features = build_features(raw_dataset)

    assert features["productive_subtype_none"].sum() == 80


def test_split_keeps_default_rate_and_does_not_overlap(raw_dataset: pd.DataFrame) -> None:
    train, validation, test = stratified_split(build_features(raw_dataset))

    assert (len(train), len(validation), len(test)) == (70, 15, 15)
    for part in (train, validation, test):
        assert part[LABEL_COLUMN].mean() == pytest.approx(0.20)
    assert set(train.index).isdisjoint(validation.index)
    assert set(train.index).isdisjoint(test.index)
    assert set(validation.index).isdisjoint(test.index)
