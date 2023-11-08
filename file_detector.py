from pathlib import Path
import logging
from txt_to_df import process_txt_to_dict_and_backup
from csv_to_df import load_csv_to_dict
from excel_to_csv import load_excel_to_dict

def process_directory(directory_path: Path) -> dict:
    """
    Scans a given directory and all its subdirectories for files with specific extensions
    (.txt, .csv, .xls, .xlsx) and processes each file according to its type. The function 
    aggregates all processed files into a single dictionary of DataFrames.

    Parameters:
    - directory_path (Path): The Path object of the directory to be processed.

    Returns:
    - dict: A dictionary with unique identifiers as keys and corresponding DataFrames as values.

    Raises:
    - Logs an error if any exception occurs during the processing of individual files.
    """

    dfs = {}  # Dictionary to store the DataFrames keyed by unique identifiers
    all_files = list(directory_path.rglob('*.*'))  # Get all files in the directory and subdirectories

    # Iterate over each file and process according to file type
    for file_path in all_files:
        try:
            if file_path.suffix == '.txt':
                # Process .txt files and update the dictionary with the returned DataFrames
                dfs.update(process_txt_to_dict_and_backup(file_path))
            elif file_path.suffix == '.csv':
                # Process .csv files and update the dictionary with the returned DataFrames
                dfs.update(load_csv_to_dict(file_path))
            elif file_path.suffix in ['.xls', '.xlsx']:
                # Process Excel files and update the dictionary with the returned DataFrames
                dfs.update(load_excel_to_dict(file_path))
        except Exception as e:
            # Log any exceptions with detailed information
            logging.error(f"Error processing file {file_path}: {e}", exc_info=True)

    return dfs  # Return the aggregated dictionary containing DataFrames

# The code below should only be executed when this script is the main program.
if __name__ == "__main__":
    # Configure logging to write errors to a log file with a specific format
    logging.basicConfig(filename='file_detector_errors.log', level=logging.ERROR,
                        format='%(asctime)s - %(levelname)s - %(message)s')


    # Define the directory to be processed
    directory_to_process = Path('/path/to/directory')

    # Process the directory and capture the returned dictionary of DataFrames
    processed_data = process_directory(directory_to_process)
