import os
import pandas as pd
import logging
import hashlib

logging.basicConfig(filename='etl_errors.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def load_csv_to_dict(csv_folder, backup_folder="backup_csv"):
    """
    Load all CSV files from the given folder into a dictionary of DataFrames.
    Also creates backup CSVs and maintains a record of loaded CSVs.
    
    Args:
    - csv_folder (str): Path to the folder containing CSV files.

    Returns:
    - dict: Dictionary of DataFrames with unique identifiers as keys.
    """
    dfs = {}  # Dictionary to store DataFrames
    backup_data = []  # List to store meta information for backup
    
    # Ensure the backup folder and its subfolder exists
    backup_directory = os.path.join(backup_folder, "datos cargados")
    if not os.path.exists(backup_directory):
        os.makedirs(backup_directory)

    try:
        for file_name in os.listdir(csv_folder):
            if file_name.endswith('.csv'):
                unique_id = hashlib.md5(file_name.encode()).hexdigest()[:3]
                full_path = os.path.join(csv_folder, file_name)
                df = pd.read_csv(full_path)
                dfs[unique_id] = df

                # Backup the loaded CSV
                backup_path = os.path.join(backup_directory, f"{file_name}_{unique_id}.csv")
                df.to_csv(backup_path, index=False)
                
                backup_data.append({
                    'Original_File': file_name,
                    'Document_Type': 'CSV',
                    'Original_Folder': csv_folder,
                    'Backup_Path': backup_path,
                    'Unique_Identifier': unique_id
                })

        # Update the backup_info.csv
        backup_info_path = os.path.join(backup_folder, "backup_info.csv")
        if os.path.exists(backup_info_path):
            backup_info_df = pd.read_csv(backup_info_path)
            backup_info_df = backup_info_df.append(pd.DataFrame(backup_data), ignore_index=True)
        else:
            backup_info_df = pd.DataFrame(backup_data)
        backup_info_df.to_csv(backup_info_path, index=False)
        
    except Exception as e:
        logging.error(f"Error processing CSV files in {csv_folder}. Error: {e}")
    
    return dfs
