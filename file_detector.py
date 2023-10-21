import os
import glob
import logging
from txt_to_df import process_txt_to_dict_and_backup
from csv_to_df import load_csv_to_dict
from excel_to_csv import load_excel_to_dict

# Basic logging configuration to capture errors into a log file
logging.basicConfig(filename='file_detector_errors.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def process_directory(directory_path: str) -> dict:
    """
    Processes a directory and its subdirectories to detect and process files.
    
    Args:
    - directory_path (str): Path to the directory.

    Returns:
    - dict: A dictionary containing processed DataFrames.
    """
    dfsf = {}  # Dictionary to store the DataFrames
    processed_files = []  # To track which files have been processed

    # Detect and process .txt files
    txt_files = glob.glob(os.path.join(directory_path, '**', '*.txt'), recursive=True)
    for txt_file in txt_files:
        try:
            dfs = process_txt_to_dict_and_backup(txt_file)
            dfsf.update(dfs)
            processed_files.append(txt_file)
        except Exception as e:
            logging.error(f"Error processing the TXT file {txt_file}. Error message: {e}")

    # Detect and process .csv files, but exclude those that have already been processed
    csv_files = [f for f in glob.glob(os.path.join(directory_path, '**', '*.csv'), recursive=True) if f not in processed_files]
    for csv_file in csv_files:
        try:
            dfs = load_csv_to_dict(csv_file)
            dfsf.update(dfs)
            processed_files.append(csv_file)
        except Exception as e:
            logging.error(f"Error processing the CSV file {csv_file}. Error message: {e}")

    # Detect and process .xls and .xlsx files, but exclude those that have already been processed
    excel_files = [f for f in glob.glob(os.path.join(directory_path, '**', '*.xls*'), recursive=True) if f not in processed_files]
    for excel_file in excel_files:
        try:
            dfs = load_excel_to_dict(excel_file)
            dfsf.update(dfs)
            processed_files.append(excel_file)
        except Exception as e:
            logging.error(f"Error processing the Excel file {excel_file}. Error message: {e}")

    return dfsf
