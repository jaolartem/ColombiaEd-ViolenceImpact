from pathlib import Path
import pandas as pd
import logging
import uuid

# Configure logging to report errors.
logging.basicConfig(filename='etl_errors.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def load_excel_to_dict(excel_path: Path, backup_folder: Path = Path("backup_csv/datos cargados")) -> dict:
    """
    Load all Excel files from the given folder or a single file into a dictionary of DataFrames.
    Also creates backup CSVs and maintains a record of loaded Excel files.
    
    Args:
    - excel_path (Path): Path to the Excel file or directory containing multiple Excel files.

    Returns:
    - dict: Dictionary of DataFrames with unique identifiers as keys.
    """
    dfs = {}
    backup_data = []
    
    backup_folder.mkdir(parents=True, exist_ok=True)
    
    if excel_path.is_dir():
        excel_files = list(excel_path.rglob('*.xlsx')) + list(excel_path.rglob('*.xls'))
    elif excel_path.is_file() and excel_path.suffix in ['.xlsx', '.xls']:
        excel_files = [excel_path]
    else:
        logging.error(f"Invalid path provided: {excel_path}. Expected a directory or an Excel file path.")
        return {}

    for file_path in excel_files:
        try:
            df_dict = pd.read_excel(file_path, sheet_name=None)
            for sheet_name, df in df_dict.items():
                unique_id = f"{file_path.stem}_{sheet_name}_{uuid.uuid4().hex[:4]}"
                dfs[unique_id] = df

                backup_file_name = f"{sheet_name}_{unique_id}.csv"
                backup_path = backup_folder / backup_file_name
                df.to_csv(backup_path, index=False)
                if not backup_path.is_file():
                    raise FileNotFoundError(f"Backup file was not created: {backup_path}")

                backup_data.append({
                    'Original_File': file_path.name,
                    'Document_Type': 'Excel',
                    'Original_Folder': file_path.parent.as_posix(),
                    'Backup_Path': backup_path.as_posix(),
                    'Unique_Identifier': unique_id
                })

        except pd.errors.EmptyDataError:
            logging.warning(f"No data in file {file_path}. Skipping.")
        except FileNotFoundError as fnfe:
            logging.error(fnfe)
        except Exception as e:
            logging.error(f"Unexpected error processing Excel file {file_path}: {e}")

    backup_info_path = backup_folder / "backup_info.csv"
    try:
        backup_info_df = pd.concat([
            pd.read_csv(backup_info_path) if backup_info_path.exists() else pd.DataFrame(),
            pd.DataFrame(backup_data)
        ], ignore_index=True)
        backup_info_df.to_csv(backup_info_path, index=False)
    except Exception as e:
        logging.error(f"Failed to update backup info: {e}")

    logging.info(f"Processed {len(dfs)} Excel files successfully.")
    return dfs
