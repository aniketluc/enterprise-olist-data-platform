from pathlib import Path
from pyspark.sql import SparkSession, DataFrame


def get_spark_session(app_name: str = "BronzeIngestion") -> SparkSession:
    """
    Create and return a Spark session.
    """
    return (
        SparkSession.builder
        .appName(app_name)
        .getOrCreate()
    )


def read_csv(
    spark: SparkSession,
    file_path: Path,
    infer_schema: bool = True,
    header: bool = True
) -> DataFrame:
    """
    Read a CSV file into a Spark DataFrame.
    """

    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    return (
        spark.read
        .option("header", header)
        .option("inferSchema", infer_schema)
        .csv(str(file_path))
    )