from scripts.extract import extract_data
from scripts.transform import transform_data
from scripts.load import load_data

def main():
    # File paths
    input_path = "data/raw.csv"
    output_path = "data/processed.csv"
    db_name = "data.db"
    table_name = "titanic_data"

    # Step 1: Extract
    df = extract_data(input_path)

    if df is None:
        print("Extraction failed")
        return

    # Step 2: Transform
    df = transform_data(df)

    if df is None:
        print("Transformation failed")
        return

    # Step 3: Load
    load_data(df, output_path, db_name, table_name)

    print("ETL Pipeline executed successfully")

if __name__ == "__main__":
    main()