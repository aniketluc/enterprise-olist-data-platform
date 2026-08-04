from pathlib import Path

from pyspark.sql import DataFrame


def write_silver(
    df: DataFrame,
    output_path: Path,
    mode: str = "overwrite",
) -> None:
    """
    Write DataFrame to the Silver layer in Delta format.
    """

    output_path.mkdir(parents=True, exist_ok=True)

    (
        df.write
        .format("delta")
        .mode(mode)
        .save(str(output_path))
    )