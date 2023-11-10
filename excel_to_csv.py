<<<<<<< HEAD
import os
import glob
=======
from pathlib import Path
>>>>>>> transformation
import pandas as pd
import logging
import uuid

<<<<<<< HEAD
logging.basicConfig(filename='etl_errors.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def load_excel_to_dict(path, backup_folder="backup_csv"):
    """
    Load all Excel files from the given folder or a single file into a dictionary of DataFrames.
    Also creates backup CSVs and maintains a record of loaded CSVs.
    
    Args:
    - path (str): Path to the Excel file or directory containing multiple Excel files.

    Returns:
    - dict: Dictionary of DataFrames with unique identifiers as keys.
    """
    dfs = {}  # Dictionary to store DataFrames
    backup_data = []  # List to store meta information for backup
    
    # Ensure the backup folder and its subfolder exists
    backup_directory = os.path.join(backup_folder, "datos cargados")
    if not os.path.exists(backup_directory):
        os.makedirs(backup_directory)
    
    # Get list of Excel files
    if os.path.isdir(path):
        excel_files = [f for ext in ['*.xlsx', '*.xls'] for f in glob.glob(os.path.join(path, '**', ext), recursive=True)]
    else:
        excel_files = [path] if path.endswith(('.xlsx', '.xls')) else []

    for full_path in excel_files:
        try:
            df_dict = pd.read_excel(full_path, sheet_name=None)
            for sheet_name, df in df_dict.items():
                file_name = os.path.basename(full_path)
                unique_id = f"{os.path.basename(file_name)}_{sheet_name}_{str(uuid.uuid4())[:4]}"
                dfs[unique_id] = df

                # Backup the loaded excel
                backup_file_name = f"{sheet_name}_{unique_id}.csv"
                backup_path = os.path.join(backup_directory, backup_file_name)
                df.to_csv(backup_path, index=False)
                
                backup_data.append({
                    'Original_File': os.path.basename(full_path),
                    'Document_Type': 'excel',
                    'Original_Folder': os.path.dirname(full_path),
                    'Backup_Path': backup_path,
                    'Unique_Identifier': unique_id
                })

            # Update the backup_info.csv
            backup_info_path = os.path.join(backup_folder, "backup_info.csv")
            if os.path.exists(backup_info_path):
                backup_info_df = pd.read_csv(backup_info_path)
                backup_info_df = backup_info_df.append(pd.DataFrame(backup_data)).drop_duplicates().reset_index(drop=True)
            else:
                backup_info_df = pd.DataFrame(backup_data)
            backup_info_df.to_csv(backup_info_path, index=False)
        
        except Exception as e:
            logging.error(f"Error processing Excel files in {full_path}. Error: {e}")
    
=======
# Configure logging to report errors.
logging.basicConfig(filename='etl_errors.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def load_excel_to_dict(excel_path: Path, backup_folder: Path = Path("backup_csv")) -> dict:
    """
    Loads data from Excel files into a dictionary of DataFrames and creates backups in CSV format.
    
    This function processes each Excel file in the specified directory or a single Excel file,
    creating a backup CSV for each sheet. It also compiles a log of these actions into a CSV file.
    
    Parameters:
        excel_path (Path): A directory containing Excel files or a path to a single Excel file.
        backup_folder (Path): The root folder where backup CSV files and the log will be stored.
        
    Returns:
        dict: A dictionary mapping unique identifiers to DataFrames extracted from the Excel files.
    
    Raises:
        FileNotFoundError: If the path provided does not exist or is not as expected.
        Exception: For any unexpected errors during processing.
    """
    dfs = {}
    backup_data = []
    
    # Create a subdirectory within the backup folder for storing the CSV backups.
    backup_csv_folder = backup_folder / "Datos_cargados"
    backup_csv_folder.mkdir(parents=True, exist_ok=True)
    
    # Determine if the provided path is a directory or a single file.
    if excel_path.is_dir():
        excel_files = list(excel_path.rglob('*.xlsx')) + list(excel_path.rglob('*.xls'))
    elif excel_path.is_file() and excel_path.suffix in ['.xlsx', '.xls']:
        excel_files = [excel_path]
    else:
        error_msg = f"Invalid path provided: {excel_path}. Expected a directory or an Excel file path."
        logging.error(error_msg)
        raise FileNotFoundError(error_msg)

    for file_path in excel_files:
        try:
            df_dict = pd.read_excel(file_path, sheet_name=None)
            for sheet_name, df in df_dict.items():
                unique_id = f"{file_path.stem}_{sheet_name}_{uuid.uuid4().hex[:4]}"
                dfs[unique_id] = df

                backup_file_name = f"{unique_id}.csv"
                backup_path = backup_csv_folder / backup_file_name
                df.to_csv(backup_path, index=False)

                # Checking if the file exists right after creation might be redundant.
                # It may be more reliable to handle I/O errors during the to_csv operation.
                backup_data.append({
                    'Original_File': file_path.name,
                    'Document_Type': 'Excel',
                    'Original_Folder': file_path.parent.as_posix(),
                    'Backup_Path': backup_path.as_posix(),
                    'Unique_Identifier': unique_id
                })
        except pd.errors.EmptyDataError:
            logging.warning(f"No data in file {file_path}. Skipping.")
        except Exception as e:
            logging.error(f"Unexpected error processing Excel file {file_path}: {e}")

    backup_info_path = backup_folder / "backup_info.csv"
    try:
        backup_info_df = pd.read_csv(backup_info_path) if backup_info_path.is_file() else pd.DataFrame()
        new_backup_info_df = pd.DataFrame(backup_data)
        backup_info_df = pd.concat([backup_info_df, new_backup_info_df], ignore_index=True)
        backup_info_df.to_csv(backup_info_path, index=False)
    except Exception as e:
        logging.error(f"Failed to update backup info: {e}")

    logging.info(f"Processed {len(dfs)} Excel files successfully.")
>>>>>>> transformation
    return dfs
