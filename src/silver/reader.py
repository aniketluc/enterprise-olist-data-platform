from pathlib import Path

from pyspark.sql import DataFrame, SparkSession
from delta import configure_spark_with_delta_pip


def get_spark_session(app_name: str = "SilverTransformation") -> SparkSession:
    builder = (
        SparkSession.builder
        .appName(app_name)
        .master("local[*]")
        .config(
            "spark.sql.extensions",
            "io.delta.sql.DeltaSparkSessionExtension",
        )
        .config(
            "spark.sql.catalog.spark_catalog",
            "org.apache.spark.sql.delta.catalog.DeltaCatalog",
        )
    )

    return configure_spark_with_delta_pip(builder).getOrCreate()


def read_delta(
    spark: SparkSession,
    path: Path,
) -> DataFrame:

    return (
        spark.read
        .format("delta")
        .load(str(path))
    )