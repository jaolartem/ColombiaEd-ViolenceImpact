from pathlib import Path
import pandas as pd
import logging
import uuid
from txt_to_df import detect_separator  # Ensure this function is correctly defined before using

logging.basicConfig(filename='etl_errors.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def load_csv_to_dict(csv_path: Path, backup_folder: Path = Path("backup_csv")) -> dict:
    """
    Reads CSV files from a specified path into a dictionary of DataFrames, backing up the files.

    The function dynamically detects the separator and encoding for each CSV file to ensure proper parsing. 
    It generates a unique identifier for each DataFrame and stores backups in a specified folder.

    Parameters:
        csv_path (Path): Path to a directory of CSV files or a single CSV file.
        backup_folder (Path): Path to the directory where backups will be stored.

    Returns:
        dict: A dictionary mapping unique identifiers to DataFrames.

    Raises:
        FileNotFoundError: If the path is not a directory or a CSV file.
        Exception: For any other errors during CSV processing or backup.
    """
    if not csv_path.exists():
        error_msg = f"Provided path does not exist: {csv_path}"
        logging.error(error_msg)
        raise FileNotFoundError(error_msg)

    # Prepare backup folder
    backup_csv_folder = backup_folder / "Datos_cargados"
    backup_csv_folder.mkdir(parents=True, exist_ok=True)

    # Find CSV files
    if csv_path.is_dir():
        csv_files = list(csv_path.rglob('*.csv'))
    elif csv_path.is_file() and csv_path.suffix == '.csv':
        csv_files = [csv_path]
    else:
        error_msg = f"Invalid path provided: {csv_path}. Expected a directory or a CSV file path."
        logging.error(error_msg)
        raise FileNotFoundError(error_msg)

    dfs = {}
    backup_data = []

    for file_path in csv_files:
        try:
            separator, encoding = detect_separator(file_path)
            df = pd.read_csv(file_path, sep=separator, encoding=encoding)
            unique_id = f"{file_path.stem}_{uuid.uuid4().hex}"
            dfs[unique_id] = df
            backup_file = backup_csv_folder / f"{unique_id}.csv"
            df.to_csv(backup_file, index=False)

            backup_data.append({
                'Original_File': file_path.name,
                'Document_Type': 'CSV',
                'Backup_Path': str(backup_file),
                'Unique_Identifier': unique_id
            })
        except Exception as e:
            logging.error(f"Error processing CSV file {file_path}: {e}", exc_info=True)

    # Update backup information
    backup_info_path = backup_folder / "backup_info.csv"
    try:
        backup_info_df = pd.DataFrame(backup_data)
        if backup_info_path.exists():
            existing_info_df = pd.read_csv(backup_info_path)
            backup_info_df = pd.concat([existing_info_df, backup_info_df], ignore_index=True)
        backup_info_df.to_csv(backup_info_path, index=False)
    except Exception as e:
        logging.error(f"Failed to update backup info: {e}", exc_info=True)

    return dfs
