from pathlib import Path
import pandas as pd
import uuid
import logging
import chardet

# Configure logging
logging.basicConfig(filename='etl_errors.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def detect_encoding(file_path: Path) -> str:
    """
    Detects the encoding of a given file by reading the first 10KB and analyzing the byte patterns.
    If the encoding cannot be detected, it defaults to 'utf-8'.

    Parameters:
    - file_path (Path): The path to the file whose encoding needs to be detected.

    Returns:
    - str: The detected encoding, or 'utf-8' if the detection fails.
    """
    try:
        with file_path.open('rb') as file:
            result = chardet.detect(file.read(10000))  # Check first 10KB for performance.
        return result['encoding'] if result['encoding'] else 'utf-8'
    except Exception as e:
        logging.error(f"Failed to detect encoding for file {file_path}: {e}", exc_info=True)
        return 'utf-8'  # Default to utf-8 if an error occurs.

def detect_separator(file_path: Path, encoding: str) -> str:
    """
    Detects the column separator used in a text file by checking the first 15 lines and identifying
    the most common delimiter character from a set of common delimiters.

    Parameters:
    - file_path (Path): The path to the file whose separator needs to be detected.
    - encoding (str): The encoding of the file.

    Returns:
    - str: The detected separator, or ',' if the detection fails.
    """
    try:
        with file_path.open('r', encoding=encoding) as file:
            lines = [file.readline().strip() for _ in range(15)]  # Read the first 15 lines
        separators = [',', '\t', ';', '|', '¬']
        sep_counts = {sep: sum(line.count(sep) for line in lines) for sep in separators}
        return max(sep_counts, key=sep_counts.get, default=',')
    except Exception as e:
        logging.error(f"Failed to detect separator for file {file_path}: {e}", exc_info=True)
        return ','  # Default to comma if an error occurs.

def process_txt_to_dict_and_backup(txt_path: Path, backup_folder: Path = Path("backup_csv")) -> dict:
    """
    Processes text files into pandas DataFrames and backs them up as CSV files. The function also
    logs the details of the backup for each processed file.

    Parameters:
    - txt_path (Path): The path to the directory containing text files or a single text file.
    - backup_folder (Path): The path to the directory where backup CSVs will be stored.

    Returns:
    - dict: A dictionary mapping unique identifiers to DataFrames of the processed text files.

    Raises:
    - FileNotFoundError: If the txt_path is invalid or does not exist.
    - Exception: For any other exception that occurs during file processing.
    """
    if not txt_path.exists():
        error_msg = f"Provided path does not exist: {txt_path}"
        logging.error(error_msg)
        raise FileNotFoundError(error_msg)

    backup_txt_folder = backup_folder / "Datos_cargados"
    backup_txt_folder.mkdir(parents=True, exist_ok=True)

    if txt_path.is_dir():
        txt_files = list(txt_path.rglob('*.txt'))+list(txt_path.rglob('*.csv'))
    elif txt_path.is_file() and txt_path.suffix == ['.txt', '.csv']:
        txt_files = [txt_path]
    else:
        error_msg = f"Invalid path provided: {txt_path}. Expected a directory or a TXT file path."
        logging.error(error_msg)
        raise ValueError(error_msg)

    dfs = {}
    backup_data = []

    for full_path in txt_files:
        try:
            encoding = detect_encoding(full_path)
            separator = detect_separator(full_path, encoding)
            df = pd.read_csv(full_path, sep=separator, encoding=encoding, dtype=str)
            unique_id = f"{full_path.stem}_{uuid.uuid4().hex[:4]}"
            dfs[unique_id] = df

            backup_file = backup_txt_folder / f"{unique_id}.csv"
            df.to_csv(backup_file, index=False)

            backup_data.append({
                'Original_File': full_path.name,
                'Document_Type': 'TXT',
                'Original_Folder': full_path.parent.as_posix(),
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
