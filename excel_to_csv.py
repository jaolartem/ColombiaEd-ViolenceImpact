import os
import pandas as pd
import logging
import hashlib

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
        excel_files = [os.path.join(path, f) for f in os.listdir(path) if f.endswith(('.xlsx', '.xls'))]
    else:
        excel_files = [path] if path.endswith(('.xlsx', '.xls')) else []

    try:
        for full_path in excel_files:
            df_dict = pd.read_excel(full_path, sheet_name=None)
            for sheet_name, df in df_dict.items():
                unique_id = hashlib.md5(sheet_name.encode()).hexdigest()[:3]
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
            backup_info_df = backup_info_df.append(pd.DataFrame(backup_data), ignore_index=True)
        else:
            backup_info_df = pd.DataFrame(backup_data)
        backup_info_df.to_csv(backup_info_path, index=False)
        
    except Exception as e:
        logging.error(f"Error processing Excel files in {path}. Error: {e}")
    
    return dfs


