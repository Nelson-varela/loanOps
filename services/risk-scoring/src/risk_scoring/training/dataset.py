"""Preparación del dataset de riesgo para el XGBoost built-in de SageMaker."""

import pandas as pd

LABEL_COLUMN = "default_90d"

NUMERIC_FEATURES: tuple[str, ...] = (
    "age",
    "months_in_current_activity",
    "monthly_income",
    "monthly_expenses",
    "existing_debt",
    "requested_amount",
    "loan_term_months",
    "interest_rate",
    "previous_loans",
    "previous_defaults",
    "days_past_due_history",
    "debt_to_income_ratio",
    "has_collateral",
)

CATEGORICAL_FEATURES: tuple[str, ...] = (
    "department",
    "employment_type",
    "loan_purpose",
    "housing_status",
    "credit_type",
    "productive_subtype",
)

# Fuera a propósito: credit_id (identificador), application_date (no generaliza),
# record_type (constante), city y municipality_code (alta cardinalidad, redundantes con
# department) y sex (atributo protegido: se mide en Clarify, no se usa para decidir).

# Los créditos no productivos no tienen subtipo; el nulo es informativo, no un faltante.
NO_SUBTYPE = "none"


def build_features(dataset: pd.DataFrame) -> pd.DataFrame:
    """Devuelve una matriz numérica con la etiqueta en la primera columna (formato XGBoost)."""
    categorical = dataset[list(CATEGORICAL_FEATURES)].fillna({"productive_subtype": NO_SUBTYPE})
    encoded = pd.get_dummies(categorical, dtype=int)
    return pd.concat(
        [dataset[[LABEL_COLUMN]], dataset[list(NUMERIC_FEATURES)], encoded],
        axis=1,
    )


def stratified_split(
    features: pd.DataFrame,
    train_fraction: float = 0.70,
    validation_fraction: float = 0.15,
    seed: int = 42,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Parte en train/validation/test conservando la proporción de defaults en cada parte."""
    shuffled = features.sample(frac=1.0, random_state=seed)
    by_class = shuffled.groupby(LABEL_COLUMN)
    # Posición relativa (0..1) de cada fila dentro de su propia clase.
    position = by_class.cumcount() / by_class[LABEL_COLUMN].transform("size")

    validation_end = train_fraction + validation_fraction
    train = shuffled.loc[position < train_fraction]
    validation = shuffled.loc[(position >= train_fraction) & (position < validation_end)]
    test = shuffled.loc[position >= validation_end]
    return train, validation, test
