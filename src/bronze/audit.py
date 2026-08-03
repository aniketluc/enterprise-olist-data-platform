from datetime import datetime


def create_audit_record(
    pipeline_name: str,
    source_table: str,
    records_read: int,
    records_written: int,
    status: str,
    batch_id: str,
):
    """
    Create an audit record for the ingestion pipeline.
    """

    return {
        "pipeline_name": pipeline_name,
        "source_table": source_table,
        "records_read": records_read,
        "records_written": records_written,
        "status": status,
        "batch_id": batch_id,
        "execution_timestamp": datetime.utcnow().isoformat(),
    }