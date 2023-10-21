import os
import pandas as pd
import logging
import uuid
from txt_to_df import detect_encoding

logging.basicConfig(filename='etl_errors.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# ... Resto del código ...


def load_csv_to_dict(csv_path, backup_folder="backup_csv"):
    """
    Load all CSV files from the given path (either a folder or a single file) 
    into a dictionary of DataFrames. Also creates backup CSVs and maintains 
    a record of loaded CSVs.
    
    Args:
    - csv_path (str): Path to the folder containing CSV files or a single CSV file.

    Returns:
    - dict: Dictionary of DataFrames with unique identifiers as keys.
    """
    dfs = {}  # Dictionary to store DataFrames
    backup_data = []  # List to store meta information for backup
    
    # Ensure the backup folder and its subfolder exists
    backup_directory = os.path.join(backup_folder, "datos cargados")
    if not os.path.exists(backup_directory):
        os.makedirs(backup_directory)

    # Determine if the provided path is a directory or a file
    if os.path.isdir(csv_path):
        csv_files = [os.path.join(csv_path, file_name) for file_name in os.listdir(csv_path) if file_name.endswith('.csv')]
    elif os.path.isfile(csv_path) and csv_path.endswith('.csv'):
        csv_files = [csv_path]
    else:
        logging.error(f"Invalid path provided: {csv_path}. Expected a directory or a CSV file path.")
        return {}

    for full_path in csv_files:
        unique_id = f"{os.path.basename(full_path)}_{str(uuid.uuid4())[:4]}"
        encoding = detect_encoding(full_path)
        
        try:
            df = pd.read_csv(full_path, encoding=encoding)
            dfs[unique_id] = df

            # Backup the loaded CSV
            backup_path = os.path.join(backup_directory, f"{os.path.basename(full_path)}_{unique_id}.csv")
            df.to_csv(backup_path, index=False)
                
            backup_data.append({
                'Original_File': os.path.basename(full_path),
                'Document_Type': 'CSV',
                'Original_Folder': os.path.dirname(full_path),
                'Backup_Path': backup_path,
                'Unique_Identifier': unique_id
            })

        except Exception as e:
            logging.error(f"Error processing CSV files in {full_path}. Error: {e}")

    # Update the backup_info.csv
    backup_info_path = os.path.join(backup_folder, "backup_info.csv")
    if os.path.exists(backup_info_path):
        backup_info_df = pd.read_csv(backup_info_path)
        backup_info_df = backup_info_df.append(pd.DataFrame(backup_data), ignore_index=True)
    else:
        backup_info_df = pd.DataFrame(backup_data)
    backup_info_df.to_csv(backup_info_path, index=False)
    
    return dfs
