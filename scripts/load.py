import sqlite3
from logger import get_logger

logger = get_logger()

def load_data(df, output_path, db_name, table_name):
    try:
        logger.info("Starting data loading")

        # Save to CSV
        df.to_csv(output_path, index=False)
        logger.info(f"Data saved to CSV at {output_path}")

        # Save to SQLite database
        conn = sqlite3.connect(db_name)
        df.to_sql(table_name, conn, if_exists='replace', index=False)
        conn.close()

        logger.info(f"Data loaded into database table: {table_name}")

        logger.info("Data loading successful")

    except Exception as e:
        logger.error(f"Error during loading: {e}")