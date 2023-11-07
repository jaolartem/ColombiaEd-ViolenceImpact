from pathlib import Path
import logging
from txt_to_df import process_txt_to_dict_and_backup
from csv_to_df import load_csv_to_dict
from excel_to_csv import load_excel_to_dict

# Basic logging configuration to capture errors into a log file
logging.basicConfig(filename='file_detector_errors.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def process_directory(directory_path: Path) -> dict:
    """
    Processes a directory and its subdirectories to detect and process files.
    
    Args:
    - directory_path (Path): Path to the directory.

    Returns:
    - dict: A dictionary containing processed DataFrames.
    """
    dfs = {}  # Dictionary to store the DataFrames

    # Get all files in the directory and its subdirectories
    all_files = list(directory_path.rglob('*.*'))

    for file_path in all_files:
        try:
            if file_path.suffix == '.txt':
                dfs.update(process_txt_to_dict_and_backup(file_path))
            elif file_path.suffix == '.csv':
                dfs.update(load_csv_to_dict(file_path))
            elif file_path.suffix in ['.xls', '.xlsx']:
                dfs.update(load_excel_to_dict(file_path))
        except Exception as e:
            logging.error(f"Error processing file {file_path}: {e}")

    return dfs

# Example usage:
# processed_data = process_directory(Path('/path/to/directory'))
