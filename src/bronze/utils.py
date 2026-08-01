import logging
from pathlib import Path


def get_logger(name: str) -> logging.Logger:
    """
    Create and return a logger.
    """

    log_dir = Path("logs/ingestion")
    log_dir.mkdir(parents=True, exist_ok=True)

    logger = logging.getLogger(name)

    if logger.hasHandlers():
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    file_handler = logging.FileHandler(
        log_dir / "bronze_ingestion.log"
    )

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger