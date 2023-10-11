import os
import glob
from excel_to_csv import excel_to_csv

def folder_to_csv(folder_path):
    """
    Convert all Excel files within a specified folder (and its subdirectories) 
    to CSV format. The CSV files are saved in a backup folder structure 
    under "CSV's_backout" which mirrors the original directory structure.

    Args:
    - folder_path (str): The path to the folder containing Excel files to convert.
    """
    backup_directory = os.path.join(os.path.dirname(folder_path), "CSV's_backout")
    
    # Ensure the backup directory exists
    if not os.path.exists(backup_directory):
        os.makedirs(backup_directory)
    
    # Iterate over all Excel files in the specified folder and its subdirectories
    for excel_path in glob.glob(os.path.join(folder_path, '**', '*.xlsx' or '*.xls'), recursive=True):
        try:
            # Determine the relative sub-directory for the current Excel file
            relative_subdir = os.path.relpath(os.path.dirname(excel_path), start=folder_path)
            
            # Convert each Excel file to CSV files (one per sheet)
            excel_to_csv(excel_path, os.path.join(backup_directory, relative_subdir))
        except Exception as e:
            print(f"Error processing file {excel_path}. Error: {e}")
    return backup_directory