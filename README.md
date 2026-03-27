ETL Data Pipeline Project
 Overview

This project implements a modular ETL (Extract, Transform, Load) pipeline using Python.
The pipeline extracts raw data from a source file, performs data cleaning and transformation, and loads the processed data into a structured format for further analysis.

This project focuses on building a clean, scalable, and production-like pipeline structure, similar to real-world data engineering workflows.

 Tech Stack
Python
Pandas
NumPy
Logging
File handling (CSV)
  Pipeline Workflow
Extract
Reads raw data from CSV files
Validates input data
Transform
Handles missing values
Removes duplicates
Applies basic data cleaning and formatting
Load
Saves processed data into a clean output file
Prepares data for analysis or downstream tasks
📁 Project Structure
etl-data-pipeline/
│
├── scripts/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│
├── pipeline/
│   ├── main_pipeline.py
│
├── data/
│   ├── raw/
│   ├── processed/
│
├── requirements.txt
├── README.md
├── .gitignore
 How to Run
Clone the repository:
git clone https://github.com/Manjistha-04/etl-data-pipeline.git
cd etl-data-pipeline
Install dependencies:
pip install -r requirements.txt
Run the pipeline:
python pipeline/main_pipeline.py
 Example
Input: Raw dataset (CSV file with missing/unclean data)
Output: Cleaned and structured dataset ready for analysis
 Features
Modular ETL architecture (separate extract, transform, load)
Clean and readable code structure
Scalable design for future extensions
Basic data cleaning pipeline
Ready for integration with databases or automation tools
 Learning Outcomes
Understood ETL pipeline design and workflow
Learned how to structure real-world data engineering projects
Practiced data preprocessing using Pandas
Improved code modularity and project organization
 Future Improvements
Integrate with PostgreSQL / MySQL
Add Apache Airflow for scheduling
Implement logging and monitoring system
Handle large-scale data processing
Add API-based data extraction

 Author

Manjistha Chakraborty
