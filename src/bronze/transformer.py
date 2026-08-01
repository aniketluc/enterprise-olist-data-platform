from pyspark.sql import DataFrame
from pyspark.sql.functions import current_timestamp, current_date, lit


def add_metadata_columns(
    df: DataFrame,
    source_file: str,
    batch_id: str
) -> DataFrame:
    """
    Add metadata columns required for the Bronze layer.
    """

    return (
        df
        .withColumn("ingestion_timestamp", current_timestamp())
        .withColumn("ingestion_date", current_date())
        .withColumn("source_file", lit(source_file))
        .withColumn("batch_id", lit(batch_id))
    )