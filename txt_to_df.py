from pathlib import Path
import pandas as pd
import uuid
import logging
import chardet

def detect_encoding(file_path: Path) -> str:
    """
    Detect the file's encoding by reading the first 10KB of the file and using the chardet library to
    infer the encoding. If no encoding is detected, defaults to 'utf-8'.

    Parameters:
    - file_path (Path): The file path object to check.

    Returns:
    - str: The detected file encoding.
    """
    with file_path.open('rb') as file:
        result = chardet.detect(file.read(10000))  # Check first 10KB for performance.
    return result['encoding'] if result['encoding'] else 'utf-8'  # Fallback to utf-8 if detection fails.

def detect_separator(file_path: Path, encoding: str) -> str:
    """
    Detect the file's delimiter by analyzing the first 15 lines and identifying the most consistent
    character that could act as a delimiter from a set of common delimiters. Defaults to ',' if no
    clear delimiter is found.

    Parameters:
    - file_path (Path): The file path object to check.
    - encoding (str): The file encoding to use when opening the file.

    Returns:
    - str: The detected delimiter.
    """
    with file_path.open('r', encoding=encoding) as file:
        lines = [file.readline().strip() for _ in range(15)]  # Read the first 15 lines

    separators = [',', '\t', ';', '|', '¬']
    sep_counts = {sep: sum(line.count(sep) for line in lines) for sep in separators}
    return max(sep_counts, key=sep_counts.get, default=',')  # Return the most common separator or ',' as default

def process_txt_to_dict_and_backup(txt_path: Path, backup_folder: Path = Path("backup_csv")) -> dict:
    """
    Reads all TXT files from the specified path into a dictionary of pandas DataFrames, using dynamically
    detected separators and encodings. Backs up the loaded TXT files into CSV format in the specified
    backup folder and logs the backup details.

    Parameters:
    - txt_path (Path): A Path object pointing to a single TXT file or a directory containing TXT files.
    - backup_folder (Path): A Path object pointing to the directory where backups will be stored.
                            Defaults to a subdirectory named "backup_csv" in the current working directory.

    Returns:
    - dict: A dictionary with unique identifiers as keys and corresponding DataFrames as values.

    Raises:
    - Logs an error if the provided txt_path is neither a directory nor a TXT file.
    - Logs an error if an exception occurs during TXT file processing.
    - Logs an error if there's an issue updating the backup information file.
    """

    dfs = {}  # Dictionary to store DataFrames keyed by unique identifiers
    backup_data = []  # List to keep track of backup details

    # Check if the provided txt_path is a directory containing TXT files or a single TXT file
    if txt_path.is_file():
        txt_files = [txt_path]
    elif txt_path.is_dir():
        txt_files = list(txt_path.rglob('*.txt'))  # Search for all TXT files in the directory
    else:
        logging.error(f"Invalid path provided: {txt_path}. Expected a directory or a TXT file path.")
        return {}  # Return an empty dictionary if the path is invalid

    # Process each TXT file
    for full_path in txt_files:
        try:
            encoding = detect_encoding(full_path)  # Detect file encoding
            separator = detect_separator(full_path, encoding)  # Detect file separator
            df = pd.read_csv(full_path, sep=separator, encoding=encoding)  # Read TXT into DataFrame
            unique_id = f"{full_path.stem}_{uuid.uuid4().hex}"  # Generate a unique identifier
            dfs[unique_id] = df  # Add DataFrame to the dictionary

            # Create a backup of the TXT file in CSV format
            backup_file = backup_folder / "datos_cargados" / f"{unique_id}.csv"
            backup_folder.mkdir(parents=True, exist_ok=True)  # Ensure the backup directory exists
            df.to_csv(backup_file, index=False)  # Write the DataFrame to a CSV file for backup
            
            # Record backup details for later reference
            backup_data.append({
                'Original_File': full_path.name,
                'Document_Type': 'TXT',
                'Backup_Path': str(backup_file),
                'Unique_Identifier': unique_id
            })
        except Exception as e:
            logging.error(f"Error processing TXT file {full_path}: {e}", exc_info=True)  # Log any exceptions that occur

    # Update or create the backup information file
    backup_info_path = backup_folder / "backup_info.csv"
    try:
        # Combine new backup data with existing info, if available
        backup_info_df = pd.DataFrame(backup_data)
        if backup_info_path.exists():
            backup_info_df = pd.concat([pd.read_csv(backup_info_path), backup_info_df], ignore_index=True)
        backup_info_df.to_csv(backup_info_path, index=False)  # Save the updated backup information
    except Exception as e:
        logging.error(f"Failed to update backup info: {e}", exc_info=True)  # Log any exceptions that occur

    return dfs  # Return the dictionary containing DataFrames
