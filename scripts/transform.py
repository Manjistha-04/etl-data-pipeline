import pandas as pd
from logger import get_logger

logger = get_logger()

def transform_data(df):
    try:
        logger.info("Starting data transformation")

        # Remove duplicate rows
        df = df.drop_duplicates()
        logger.info("Duplicates removed")

        # Handle missing values for Age
        if "Age" in df.columns:
            df["Age"] = df["Age"].fillna(df["Age"].mean())
            logger.info("Missing Age values filled with mean")

        # Feature Engineering: Create FamilySize
        if "SibSp" in df.columns and "Parch" in df.columns:
            df["FamilySize"] = df["SibSp"] + df["Parch"]
            logger.info("FamilySize column created")

        # Feature Engineering: Create FarePerPerson
        if "Fare" in df.columns and "FamilySize" in df.columns:
            df["FarePerPerson"] = df["Fare"] / (df["FamilySize"] + 1)
            logger.info("FarePerPerson column created")

        logger.info("Data transformation successful")
        return df

    except Exception as e:
        logger.error(f"Error during transformation: {e}")
        return None