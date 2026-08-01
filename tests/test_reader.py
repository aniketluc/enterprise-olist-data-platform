from src.bronze.config import RAW_DATA_PATH, TABLES
from src.bronze.reader import get_spark_session, read_csv

spark = get_spark_session()

customers = read_csv(
    spark,
    RAW_DATA_PATH / TABLES["customers"]
)

customers.printSchema()
customers.show(5)