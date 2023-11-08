from pathlib import Path
import pandas as pd
import logging
import uuid
from txt_to_df import detect_separator  # Ensure this function is correctly defined before using

def load_csv_to_dict(csv_path: Path, backup_folder: Path = Path("backup_csv")) -> dict:
    """
    Reads all CSV files from a specified path into a dictionary of pandas DataFrames. Each CSV file
    is read using a dynamically detected separator and encoding to ensure proper parsing. Additionally,
    the function backs up the loaded CSV files into a specified backup folder and logs the backup details.

    The function returns a dictionary where each key is a unique identifier composed of the original
    file's stem and a UUID, and the corresponding value is the DataFrame created from the CSV file.

    Parameters:
    - csv_path (Path): A Path object pointing to a single CSV file or a directory containing CSV files.
    - backup_folder (Path): A Path object pointing to the directory where backups of the CSVs will be stored.
                            Defaults to a subdirectory named "backup_csv" in the current working directory.

    Returns:
    - dict: A dictionary with unique identifiers as keys and corresponding DataFrames as values.

    Raises:
    - Logs an error if the provided csv_path is neither a directory nor a CSV file.
    - Logs an error if an exception occurs during CSV file processing.
    - Logs an error if there's an issue updating the backup information file.
    """

    dfs = {}  # Dictionary to store DataFrames keyed by unique identifiers
    backup_data = []  # List to keep track of backup details

    # Check if the provided csv_path is a directory containing CSV files or a single CSV file
    if csv_path.is_dir():
        csv_files = list(csv_path.rglob('*.csv'))  # Search for all CSV files in the directory
    elif csv_path.is_file() and csv_path.suffix == '.csv':
        csv_files = [csv_path]  # Single CSV file provided
    else:
        logging.error(f"Invalid path provided: {csv_path}. Expected a directory or a CSV file path.")
        return {}  # Return an empty dictionary if the path is invalid

    # Process each CSV file
    for file_path in csv_files:
        try:
            separator, encoding = detect_separator(file_path)  # Detect separator and encoding
            df = pd.read_csv(file_path, sep=separator, encoding=encoding)  # Read CSV into DataFrame
            unique_id = f"{file_path.stem}_{uuid.uuid4().hex}"  # Generate a unique identifier
            dfs[unique_id] = df  # Add DataFrame to the dictionary

            # Create a backup of the CSV file
            backup_file = backup_folder / "datos_cargados" / f"{unique_id}.csv"
            backup_folder.mkdir(parents=True, exist_ok=True)  # Ensure the backup directory exists
            df.to_csv(backup_file, index=False)  # Write the DataFrame to a CSV file for backup
            
            # Record backup details for later reference
            backup_data.append({
                'Original_File': file_path.name,
                'Document_Type': 'CSV',
                'Backup_Path': str(backup_file),
                'Unique_Identifier': unique_id
            })
        except Exception as e:
            logging.error(f"Error processing CSV file {file_path}: {e}", exc_info=True)  # Log any exceptions that occur

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
