from pathlib import Path
import pandas as pd
import logging
import uuid

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
    return dfs
