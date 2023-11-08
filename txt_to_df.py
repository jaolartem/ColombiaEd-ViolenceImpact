from pathlib import Path
import pandas as pd
import uuid
import logging
import chardet

logging.basicConfig(filename='etl_errors.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def detect_encoding(file_path: Path) -> str:
    try:
        with file_path.open('rb') as file:
            result = chardet.detect(file.read(10000))  # Check first 10KB for performance.
        return result['encoding'] if result['encoding'] else 'utf-8'  # Fallback to utf-8 if detection fails.
    except Exception as e:
        logging.error(f"Failed to detect encoding for file {file_path}: {e}", exc_info=True)
        return 'utf-8'  # Default to utf-8 if there's an error

def detect_separator(file_path: Path, encoding: str) -> str:
    try:
        with file_path.open('r', encoding=encoding) as file:
            lines = [file.readline().strip() for _ in range(15)]  # Read the first 15 lines
        separators = [',', '\t', ';', '|', '¬']
        sep_counts = {sep: sum(line.count(sep) for line in lines) for sep in separators}
        return max(sep_counts, key=sep_counts.get, default=',')  # Return the most common separator or ',' as default
    except Exception as e:
        logging.error(f"Failed to detect separator for file {file_path}: {e}", exc_info=True)
        return ','  # Default to comma if there's an error

def process_txt_to_dict_and_backup(txt_path: Path, backup_folder: Path = Path("backup_csv")) -> dict:
    if not txt_path.exists():
        error_msg = f"Provided path does not exist: {txt_path}"
        logging.error(error_msg)
        raise FileNotFoundError(error_msg)

    # Prepare backup folder
    backup_txt_folder = backup_folder / "datos_cargados"
    backup_txt_folder.mkdir(parents=True, exist_ok=True)

    # Find TXT files
    if txt_path.is_dir():
        txt_files = list(txt_path.rglob('*.txt'))
    elif txt_path.is_file() and txt_path.suffix == '.txt':
        txt_files = [txt_path]
    else:
        error_msg = f"Invalid path provided: {txt_path}. Expected a directory or a TXT file path."
        logging.error(error_msg)
        raise FileNotFoundError(error_msg)

    dfs = {}
    backup_data = []

    for full_path in txt_files:
        try:
            encoding = detect_encoding(full_path)
            separator = detect_separator(full_path, encoding)
            df = pd.read_csv(full_path, sep=separator, encoding=encoding)
            unique_id = f"{full_path.stem}_{uuid.uuid4().hex}"
            dfs[unique_id] = df

            backup_file = backup_txt_folder / f"{unique_id}.csv"
            df.to_csv(backup_file, index=False)

            backup_data.append({
                'Original_File': full_path.name,
                'Document_Type': 'TXT',
                'Backup_Path': str(backup_file),
                'Unique_Identifier': unique_id
            })
        except Exception as e:
            logging.error(f"Error processing TXT file {full_path}: {e}", exc_info=True)

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
