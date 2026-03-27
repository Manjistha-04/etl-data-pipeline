import pandas as pd
from logger import get_logger
logger = get_logger()

def extract_data(file_path):
    try:
        logger.info("starting data extraction")
        df = pd.read_csv(file_path)

        logger.info("extraction successful")
        return df
    except Exception as e:
        logger.error(f"Error during extraction: {e}")
        return None