
import os
import glob
from txt_to_df import process_txt_to_dict_and_backup
from csv_to_df import load_csv_to_dict
from excel_to_csv import load_excel_to_dict

def process_directory(directory_path):
    """Process a directory and its subdirectories to detect and process files.
    
    Args:
    - directory_path (str): Path to the directory.
    
    Returns:
    - dict: A dictionary containing processed DataFrames.
    """
    dfs = {}

    # Detect .txt files and process them
    txt_files = glob.glob(os.path.join(directory_path, '**', '*.txt'), recursive=True)
    for txt_file in txt_files:
        loaded_data = process_txt_to_dict_and_backup(txt_file)
        dfs.update(loaded_data)

    # Detect .csv files and process them
    csv_files = glob.glob(os.path.join(directory_path, '**', '*.csv'), recursive=True)
    for csv_file in csv_files:
        loaded_data = load_csv_to_dict(csv_file)
        dfs.update(loaded_data)

    # Detect .xls and .xlsx files and process them
    excel_files = []
    for ext in ['*.xlsx', '*.xls']:
        excel_files.extend(glob.glob(os.path.join(directory_path, '**', ext), recursive=True))

    for excel_file in excel_files:
        loaded_data = load_excel_to_dict(excel_file)
        dfs.update(loaded_data)

    return dfs
