from pathlib import Path
import logging
import sys
import pandas as pd
from typing import Dict
from txt_to_df import process_txt_to_dict_and_backup
from csv_to_df import load_csv_to_dict
from excel_to_csv import load_excel_to_dict

def setup_logging(log_file: str = 'etl_errors.log') -> None:
    """
    Sets up the logging configuration for the application.
    """
    logging.basicConfig(filename=log_file, level=logging.ERROR,
                        format='%(asctime)s - %(levelname)s - %(message)s')

   
def process_directory(directory_path: Path) -> Dict[str, pd.DataFrame]:
    """
    Processes a directory and its subdirectories to detect and process files.

    Args:
        directory_path (Path): The Path object of the directory to be processed.

    Returns:
        Dict[str, pd.DataFrame]: A dictionary with file names as keys and corresponding DataFrames as values.
    """
    # Ensure directory_path is a Path object
    directory_path = Path(directory_path) if not isinstance(directory_path, Path) else directory_path

    dfs = {}  # Dictionary to store the DataFrames keyed by file names
    all_files = list(directory_path.rglob('*.*'))  # Get all files in the directory

    for file_path in all_files:
        try:
            if file_path.suffix in ['.txt', '.csv']:
                dfs.update(process_txt_to_dict_and_backup(file_path))
            elif file_path.suffix in ['.xls', '.xlsx']:
                dfs.update(load_excel_to_dict(file_path))
        except FileNotFoundError as e:
            logging.error(f"File not found: {file_path}", exc_info=True)
        except pd.errors.ParserError as e:
            logging.error(f"Parsing error in file: {file_path}", exc_info=True)
        except Exception as e:
            logging.error(f"Error processing file {file_path}: {e}", exc_info=True)

    return dfs

if __name__ == "__main__":
    setup_logging()  # Setup logging

    if len(sys.argv) > 1:
        directory_to_process = Path(sys.argv[1])
        if not directory_to_process.exists():
            logging.error(f"The provided directory does not exist: {directory_to_process}")
            sys.exit(1)

        processed_data = process_directory(directory_to_process)

        # Here, you might want to do something with the processed data.
        # For example, you could write it to a file, or pass it to another function for further processing.
    else:
        logging.error("No directory path provided as argument to the script.")
        sys.exit(1)
