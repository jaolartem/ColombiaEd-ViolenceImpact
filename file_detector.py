
import os
import glob
from txt_to_df import load_txt_to_dict
from csv_to_df import load_csv_to_dict
from excel_to_csv import convert_excel_to_csv

def process_directory(directory_path):
    """Process a directory and its subdirectories to detect and process files.
    
    Args:
    - directory_path (str): Path to the directory.
    
    Returns:
    - dict: A dictionary containing processed DataFrames.
    """
    global ALL_DFS

    # Detect .txt files and process them
    txt_files = glob.glob(os.path.join(directory_path, '**', '*.txt'), recursive=True)
    for txt_file in txt_files:
        loaded_data = load_txt_to_dict(txt_file)
        ALL_DFS.update(loaded_data)

    # Detect .csv files and process them
    csv_files = glob.glob(os.path.join(directory_path, '**', '*.csv'), recursive=True)
    for csv_file in csv_files:
        loaded_data = load_csv_to_dict(csv_file)
        ALL_DFS.update(loaded_data)

    # Detect .xls and .xlsx files and process them
    excel_files = [os.path.join(dirpath, f) 
                   for dirpath, dirnames, filenames in os.walk(directory_path) 
                   for f in filenames if f.endswith(('.xlsx', '.xls'))]
    for excel_file in excel_files:
        csv_path = convert_excel_to_csv(excel_file)
        loaded_data = load_csv_to_dict(csv_path)
        ALL_DFS.update(loaded_data)

    return ALL_DFS
