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
    # Iterate over all Excel files in the specified folder and its subdirectories
    for excel_path in glob.glob(os.path.join(folder_path, '**', '*.xlsx'), recursive=True):
        # Convert each Excel file to CSV files (one per sheet)
        excel_to_csv(excel_path)

if __name__ == "__main__":
    # Sample execution
    path_to_folder = "/path/to/your/folder"
    folder_to_csv(path_to_folder)
