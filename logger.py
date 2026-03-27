import logging

def get_logger():
    logger = logging.getLogger("ETL_Pipeline")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        file_handler = logging.FileHandler("pipeline.log")
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s -%(message)s"
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    return logger