from pathlib import Path
import pandas as pd
import uuid
import logging
import chardet

# Constants
LINES_FOR_DETECTION = 20  # Use more lines for a better heuristic in delimiter detection.
DEFAULT_ENCODING = 'utf-8'
SECONDARY_ENCODING = 'ISO-8859-1'  # A common alternative encoding for various data files.
BACKUP_INFO_FILE = "backup_info.csv"  # Centralized backup info file name.

# Configure logging to report errors and info messages.
logging.basicConfig(filename='etl_errors.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def detect_encoding(file_path: Path) -> str:
    """
    Detect the file's encoding by trying different encodings.

    Args:
    file_path (Path): The file path object to check.

    Returns:
    str: The detected file encoding.
    """
    try:
        with file_path.open('r', encoding=DEFAULT_ENCODING) as file:
            file.read()
        return DEFAULT_ENCODING
    except UnicodeDecodeError:
        try:
            with file_path.open('r', encoding=SECONDARY_ENCODING) as file:
                file.read()
            return SECONDARY_ENCODING
        except UnicodeDecodeError:
            with file_path.open('rb') as file:
                result = chardet.detect(file.read(10000))  # Check first 10KB for performance.
            return result['encoding'] if result['encoding'] else 'utf-8'  # Fallback to utf-8.

def detect_separator(file_path: Path, encoding: str) -> str:
    """
    Detect the file's delimiter using a heuristic based on the first 20 lines.

    Args:
    file_path (Path): The file path object to check.
    encoding (str): The file encoding to use when opening the file.

    Returns:
    str: The detected delimiter or None if no consistent delimiter is found.
    """
    with file_path.open('r', encoding=encoding) as file:
        lines = [file.readline().strip() for _ in range(LINES_FOR_DETECTION)]

    # Define possible separators and count their occurrences in each line.

    separators = [',', '\t', ';', '|', '¬',':','\\', ':', '-', '_', '/', '.']
    sep_counts = {sep: [line.count(sep) for line in lines] for sep in separators}

    # Find the separator that has a consistent count across the most lines.
    consistent_separators = {sep: counts for sep, counts in sep_counts.items() if len(set(counts)) == 1}
    
    # Return the consistent separator with the highest count, or None if none found.
    if consistent_separators:
        return max(consistent_separators, key=lambda sep: consistent_separators[sep][0])
    
    return max(sep_counts, key=lambda sep: sum(sep_counts[sep]) / len(sep_counts[sep])) if sep_counts else None

def process_txt_to_dict_and_backup(txt_path: str, backup_folder: str = "backup_csv/datos cargados") -> dict:
    """
    Process and back up TXT files found at the given path, and store the processed data in a dictionary.

    Args:
    txt_path (str): Path to the TXT file or directory containing TXT files.
    backup_folder (str): Destination folder for backups. Defaults to "backup_csv/datos cargados".

    Returns:
    dict: A dictionary with the base filenames as keys and the corresponding DataFrames as values.
    """
    backup_folder_path = Path(backup_folder)
    backup_folder_path.mkdir(parents=True, exist_ok=True)  # Ensure backup directory exists.
    backup_data = []

    txt_files = [Path(txt_path)] if Path(txt_path).is_file() else list(Path(txt_path).rglob('*.txt'))
    dfs = {}

    for full_path in txt_files:
        if not full_path.is_file():
            logging.warning(f"File not found or not accessible: {full_path}")
            continue  # Skip non-existent or inaccessible files.

        encoding = detect_encoding(full_path)
        separator = detect_separator(full_path, encoding)
        
        if separator is None:
            logging.error(f"Unable to detect the separator for {full_path}.")
            continue  # Skip to the next file if separator cannot be determined.

        try:
            df = pd.read_csv(full_path, sep=separator, encoding=encoding, warn_bad_lines=True, engine='python', dtype='object')
            if df.empty:
                logging.warning(f"No data in file: {full_path}")
                continue  # Skip empty files.

            dfs[full_path.stem] = df  # Store DataFrame in dictionary with the base filename as key.
        except pd.errors.ParserError as pe:
            logging.error(f"Parser error in file {full_path}: {pe}")
            continue
        except UnicodeDecodeError as ude:
            logging.error(f"Encoding error in file {full_path}: {ude}")
            continue
        except Exception as e:
            logging.error(f"Unexpected error in file {full_path}: {e}")
            continue

        base_filename = full_path.stem
        unique_id = f"{base_filename}_{str(uuid.uuid4())[:4]}"
        backup_file = backup_folder_path / f"{unique_id}.csv"
        df.to_csv(backup_file, index=False)
        if not backup_file.is_file():
            logging.error(f"Failed to write backup file: {backup_file}")
            continue  # Skip if backup file wasn't written.

        backup_data.append({
            'Original_File': base_filename,
            'Document_Type': 'TXT',
            'Original_Folder': str(full_path.parent),
            'Backup_Path': str(backup_file),
            'Unique_Identifier': unique_id
        })

    backup_info_path = backup_folder_path / BACKUP_INFO_FILE
    try:
        # Append new backup info or create file if it doesn't exist.
        backup_info_df = pd.read_csv(backup_info_path) if backup_info_path.exists() else pd.DataFrame()
        new_backup_info_df = pd.DataFrame(backup_data)
        backup_info_df = pd.concat([backup_info_df, new_backup_info_df], ignore_index=True)
        backup_info_df.to_csv(backup_info_path, index=False, mode='w')
    except Exception as e:
        logging.error(f"Failed to update backup info file: {e}")

    logging.info("TXT processing and backup completed successfully.")
    return dfs
