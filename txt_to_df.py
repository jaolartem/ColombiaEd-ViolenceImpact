import pandas as pd
import os
import glob
import uuid
import logging

# Basic logging configuration to capture errors
logging.basicConfig(level=logging.ERROR)

def process_txt_to_dict_and_backup(txt_path: str, backup_folder: str = "backup_txt") -> dict:
    """
    Extracts data from TXT files by detecting their delimiter, converts them into DataFrames, 
    and then backs them up as CSV files in a specified directory.
    
    Parameters:
    - txt_path (str): Absolute or relative path pointing to the TXT file or a directory containing multiple TXT files.
    - backup_folder (str, optional): Name or path of the directory to store the backup CSV files. Defaults to "backup_txt".
    
    Returns:
    - dict: A dictionary mapping base filenames (without extensions) to their respective DataFrames.
    """
    
    omitted_lines = []

    def detect_separator(file_path: str) -> str:
        """
        Detect the delimiter used in a TXT file.
        
        Parameters:
        - file_path (str): Path to the target TXT file.
        
        Returns:
        - str or None: Detected delimiter as a string or None if unable to detect.
        """
        codifications = ['utf-8', 'ISO-8859-1', 'latin1']
        for cod in codifications:
            try:
                # Attempt to read the file using various encodings
                with open(file_path, 'r', encoding=cod) as file:
                    lines = [file.readline().strip() for _ in range(5)]
                
                # Count occurrences of potential delimiters
                sep_counts = {
                    ',': sum(line.count(',') for line in lines),
                    '\\t': sum(line.count('\\t') for line in lines),
                    ';': sum(line.count(';') for line in lines),
                    '|': sum(line.count('|') for line in lines),
                    '\t': sum(line.count('\t') for line in lines)
                }
                likely_sep = max(sep_counts, key=sep_counts.get)
                if sep_counts[likely_sep] == 0:
                    return None
                return likely_sep
            except UnicodeDecodeError:
                continue

        # If none of the encodings work, log the error and return None
        logging.error(f"Failed to decode file {file_path} using common encodings.")
        return None

    backup_directory = os.path.join(backup_folder, "backup_data")
    if not os.path.exists(backup_directory):
        os.makedirs(backup_directory)

    txt_files = [txt_path] if os.path.isfile(txt_path) else glob.glob(os.path.join(txt_path, '**', '*.txt'), recursive=True)
    dfs = {}

    for full_path in txt_files:
        separator = detect_separator(full_path)
        if separator is None:
            separator = input(f"Unable to detect the separator for the file: {full_path}. Please specify the separator manually (e.g., ',', '\\t', ';'): ")

        try:
            df = pd.read_csv(full_path, sep=separator, error_bad_lines=False, warn_bad_lines=True)
            base_filename = os.path.basename(full_path).split('.')[0]
            dfs[base_filename] = df

            # Backup the DataFrame as a CSV
            backup_file = os.path.join(backup_folder, base_filename + ".csv")
            df.to_csv(backup_file, index=False)
            
        except Exception as e:
            logging.error(f"Error processing the file {full_path}. Error message: {e}")

    # If there are omitted lines, save them in a specified directory
    omitted_folder = "Lost_Data"
    if not os.path.exists(omitted_folder):
        os.makedirs(omitted_folder)

    if omitted_lines:
        omitted_file_path = os.path.join(omitted_folder, "omitted_lines.csv")
        with open(omitted_file_path, 'w') as f:
            for line in omitted_lines:
                f.write(line + '\n')

    return dfs
