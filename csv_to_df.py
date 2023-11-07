from pathlib import Path
import pandas as pd
import logging
import uuid
from txt_to_df import detect_separator  # Assuming this function detects both separator and encoding

# Configure logging to report errors.
logging.basicConfig(filename='etl_errors.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def load_csv_to_dict(csv_path: Path, backup_folder: Path = Path("backup_csv/datos cargados")) -> dict:
    """
    Load all CSV files from the given path into a dictionary of DataFrames.
    Also creates backup CSVs and maintains a record of loaded CSVs.

    Args:
    - csv_path (Path): Path to the folder containing CSV files or a single CSV file.

    Returns:
    - dict: Dictionary of DataFrames with filenames as keys.
    """
    backup_folder.mkdir(parents=True, exist_ok=True)

    dfs = {}
    backup_data = []

    if csv_path.is_file():
        csv_files = [csv_path]
    elif csv_path.is_dir():
        csv_files = list(csv_path.rglob('*.csv'))
    else:
        logging.error(f"Invalid path provided: {csv_path}. Expected a directory or a CSV file path.")
        return {}

    for file_path in csv_files:
        unique_id = f"{file_path.stem}_{uuid.uuid4().hex[:4]}"
        separator, encoding = detect_separator(file_path)  # Assuming this function returns a tuple (separator, encoding)
        
        try:
            df = pd.read_csv(file_path, sep=separator, encoding=encoding)
            dfs[unique_id] = df

            backup_path = backup_folder / f"{file_path.stem}_{unique_id}.csv"
            df.to_csv(backup_path, index=False)
            if not backup_path.is_file():
                raise FileNotFoundError(f"Backup file was not created: {backup_path}")
            
            backup_data.append({
                'Original_File': file_path.name,
                'Document_Type': 'CSV',
                'Original_Folder': file_path.parent.as_posix(),
                'Backup_Path': backup_path.as_posix(),
                'Unique_Identifier': unique_id
            })

        except pd.errors.EmptyDataError:
            logging.warning(f"No data in file {file_path}. Skipping.")
        except pd.errors.ParserError as pe:
            logging.error(f"Parser error in file {file_path}: {pe}")
        except FileNotFoundError as fnfe:
            logging.error(fnfe)
        except Exception as e:
            logging.error(f"Unexpected error processing CSV file {file_path}: {e}")

    backup_info_path = backup_folder / "backup_info.csv"
    try:
        backup_info_df = pd.concat([
            pd.read_csv(backup_info_path) if backup_info_path.exists() else pd.DataFrame(),
            pd.DataFrame(backup_data)
        ], ignore_index=True)
        backup_info_df.to_csv(backup_info_path, index=False)
    except Exception as e:
        logging.error(f"Failed to update backup info: {e}")

    logging.info(f"Processed {len(dfs)} CSV files successfully.")
    return dfs
