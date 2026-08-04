from pyspark.sql import DataFrame


def validate_dataframe(df: DataFrame, primary_key: str):
    """
    Validate Silver DataFrame.
    """

    total_rows = df.count()

    duplicate_rows = (
        total_rows -
        df.select(primary_key).distinct().count()
    )

    null_values = (
        df.filter(df[primary_key].isNull()).count()
    )

    print(f"Rows          : {total_rows}")
    print(f"Duplicates    : {duplicate_rows}")
    print(f"Null {primary_key}: {null_values}")

    return {
        "rows": total_rows,
        "duplicates": duplicate_rows,
        "nulls": null_values,
    }