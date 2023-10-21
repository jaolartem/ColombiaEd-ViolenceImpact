import pandas as pd
import os
import glob
import uuid
import logging
import chardet

# Constants
LINES_FOR_DETECTION = 5
DEFAULT_ENCODING = 'utf-8'
SECONDARY_ENCODING = 'ISO-8859-1'  # A frequent encoding for various data files

# Logging Configuration
logging.basicConfig(filename='etl_errors.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def detect_encoding(file_path: str) -> str:
    """
    Detect the file's encoding.
    
    Parameters:
    - file_path (str): Path to the file.
    
    Returns:
    - str: Detected encoding of the file.
    """
    try:
        with open(file_path, 'r', encoding=DEFAULT_ENCODING) as file:
            file.read()
        return DEFAULT_ENCODING
    except UnicodeDecodeError:
        try:
            with open(file_path, 'r', encoding=SECONDARY_ENCODING) as file:
                file.read()
            return SECONDARY_ENCODING
        except UnicodeDecodeError:
            with open(file_path, 'rb') as file:
                result = chardet.detect(file.read(10000))  # Check first 10KB for performance
            return result['encoding']

def detect_separator(file_path: str, encoding: str) -> str:
    """
    Detect the file's delimiter.
    
    Parameters:
    - file_path (str): Path to the file.
    - encoding (str): Encoding of the file.
    
    Returns:
    - str: Detected delimiter of the file.
    """
    with open(file_path, 'r', encoding=encoding) as file:
        lines = [file.readline().strip() for _ in range(LINES_FOR_DETECTION)]
    
    sep_counts = {sep: sum(line.count(sep) for line in lines) for sep in [',', '\\t', ';', '|', '\t', '¬']}
    likely_sep = max(sep_counts, key=sep_counts.get)
    return likely_sep if sep_counts[likely_sep] > 0 else None

def read_file_line_by_line(file_path: str, separator: str) -> pd.DataFrame:
    """
    Read problematic files line by line to circumvent issues like DtypeWarnings.
    
    Parameters:
    - file_path (str): Path to the file.
    - separator (str): Delimiter used in the file.
    
    Returns:
    - DataFrame: Parsed data.
    """
    with open(file_path, 'r') as f:
        lines = f.readlines()
    header = lines[0].split(separator)
    data = [line.split(separator) for line in lines[1:]]
    return pd.DataFrame(data, columns=header)

def process_txt_to_dict_and_backup(txt_path: str, backup_folder: str = "backup_csv/datos cargados") -> dict:
    """
    Process and back up the given TXT files.
    
    Parameters:
    - txt_path (str): Path to the TXT file or directory containing TXT files.
    - backup_folder (str, optional): Destination folder for backups. Defaults to "backup_csv/datos cargados".
    
    Returns:
    - dict: Dictionary containing DataFrames with the processed data.
    """
    os.makedirs(backup_folder, exist_ok=True)
    backup_data = []

    txt_files = [txt_path] if os.path.isfile(txt_path) else glob.glob(os.path.join(txt_path, '**', '*.txt'), recursive=True)
    dfs = {}

    for full_path in txt_files:
        encoding = detect_encoding(full_path)
        separator = detect_separator(full_path, encoding)
        if separator is None:
            separator = input(f"Unable to detect the separator for {full_path}. Please specify manually (e.g., ',', '\\t', ';'): ")
               
        engine_to_use = 'python' 
        
        try:
            df = pd.read_csv(full_path, sep=separator, encoding=encoding, warn_bad_lines=True, engine=engine_to_use, dtype='object')
        except (pd.errors.ParserError, UnicodeDecodeError):
            df = read_file_line_by_line(full_path, separator)
                

        base_filename = os.path.basename(full_path).split('.')[0]
        dfs[base_filename] = df

        unique_id = f"{base_filename}_{str(uuid.uuid4())[:4]}"
        backup_file = os.path.join(backup_folder, f"{base_filename}_{unique_id}.csv")
        df.to_csv(backup_file, index=False)

        backup_data.append({
            'Original_File': base_filename,
            'Document_Type': 'TXT',
            'Original_Folder': os.path.dirname(full_path),
            'Backup_Path': backup_file,
            'Unique_Identifier': unique_id
        })

    backup_info_path = os.path.join("backup_csv", "backup_info.csv")
    if os.path.exists(backup_info_path):
        backup_info_df = pd.read_csv(backup_info_path)
        backup_info_df = backup_info_df.append(pd.DataFrame(backup_data), ignore_index=True)
    else:
        backup_info_df = pd.DataFrame(backup_data)
    backup_info_df.to_csv(backup_info_path, index=False)

    return dfs
