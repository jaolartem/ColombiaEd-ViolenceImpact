
import pandas as pd
import os
import glob
import uuid

def process_txt_to_dict_and_backup(txt_path, backup_folder="backup_txt"):
    """
    Processes TXT files by detecting their separator, loading them as DataFrames, and 
    then backing them up as CSV files in a specified folder. Also returns a dictionary
    with the DataFrames.
    
    Args:
    - txt_path (str): Path to the TXT file or directory containing multiple TXT files.
    - backup_folder (str, optional): Name of the folder to backup CSV files. Defaults to "backup_txt".
    
    Returns:
    - dict: Dictionary with keys as the base filenames and values as the DataFrames.
    """
    
    # Function to detect separator in a TXT file
    def detect_separator(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = [file.readline().strip() for _ in range(5)]
        sep_counts = {
            ',': sum(line.count(',') for line in lines),
            '\\t': sum(line.count('\\t') for line in lines),
            ';': sum(line.count(';') for line in lines)
        }
        likely_sep = max(sep_counts, key=sep_counts.get)
        if sep_counts[likely_sep] == 0:
            return None
        return likely_sep

    # Ensure the backup folder exists
    if not os.path.exists(backup_folder):
        os.mkdir(backup_folder)

    # Get list of TXT files
    txt_files = [txt_path] if os.path.isfile(txt_path) else glob.glob(os.path.join(txt_path, '**', '*.txt'), recursive=True)

    dfs = {}
    for full_path in txt_files:
        separator = detect_separator(full_path)
        if separator is None:
            print(f"Unable to detect the separator for the file: {full_path}. Please specify the separator manually.")
            separator = input("Enter the separator (e.g., ',', '\\t', ';'): ")

        df = pd.read_csv(full_path, sep=separator)

        # Get the base filename for the current TXT file (without extension)
        base_filename = os.path.basename(full_path).split('.')[0]
        dfs[base_filename] = df

        # Save a backup copy as CSV
        backup_file = os.path.join(backup_folder, base_filename + ".csv")
        df.to_csv(backup_file, index=False)
    
    return dfs

