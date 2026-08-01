import uuid

from config import (
    RAW_DATA_PATH,
    BRONZE_DATA_PATH,
    TABLES,
    BRONZE_TABLES,
)

from reader import (
    get_spark_session,
    read_csv,
)

from validator import (
    validate_file_exists,
    validate_dataframe_not_empty,
)

from transformer import (
    add_metadata_columns,
)

from writer import (
    write_bronze,
)

from utils import get_logger

def main():

    spark = get_spark_session()
    
    logger = get_logger("bronze_ingestion")

    batch_id = str(uuid.uuid4())

    for table_name, file_name in TABLES.items():

        logger.info(f"Processing {table_name}")

        file_path = RAW_DATA_PATH / file_name

        validate_file_exists(file_path)

        df = read_csv(
            spark=spark,
            file_path=file_path,
        )

        validate_dataframe_not_empty(df)

        df = add_metadata_columns(
            df=df,
            source_file=file_name,
            batch_id=batch_id,
        )

        output_path = BRONZE_DATA_PATH / BRONZE_TABLES[table_name]

        write_bronze(
            df=df,
            output_path=output_path,
        )

        logger.info(f"{table_name} completed successfully.")

    spark.stop()


if __name__ == "__main__":
    main()