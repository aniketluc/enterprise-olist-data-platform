from pathlib import Path
from pyspark.sql import DataFrame


def validate_file_exists(file_path: Path) -> None:
    """
    Validate that the source file exists.
    """

    if not file_path.exists():
        raise FileNotFoundError(
            f"Source file not found: {file_path}"
        )


def validate_dataframe_not_empty(df: DataFrame) -> None:
    """
    Validate that the DataFrame contains data.
    """

    if df.rdd.isEmpty():
        raise ValueError(
            "The DataFrame is empty."
        )


def validate_required_columns(
    df: DataFrame,
    required_columns: list[str]
) -> None:
    """
    Validate that all required columns exist.
    """

    missing_columns = [
        column
        for column in required_columns
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )