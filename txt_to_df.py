
import pandas as pd
import os
import glob
import uuid

def detect_separator(file_path):
    # (This is the detect_separator function)
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = [file.readline().strip() for _ in range(5)]
    sep_counts = {
        ',': sum(line.count(',') for line in lines),
        '\t': sum(line.count('\t') for line in lines),
        ';': sum(line.count(';') for line in lines)
    }
    likely_sep = max(sep_counts, key=sep_counts.get)
    if sep_counts[likely_sep] == 0:
        return None
    return likely_sep

def load_txt_to_dict(txt_path, backup_folder="backup_txt"):
    # Ensure the backup folder exists
    if not os.path.exists(backup_folder):
        os.mkdir(backup_folder)

    # Get list of TXT files
    txt_files = [txt_path] if os.path.isfile(txt_path) else glob.glob(os.path.join(txt_path, '**', '*.txt'), recursive=True)


    dfs = {}
    for full_path in txt_files:
        separator = detect_separator(full_path)
        if separator is None:
            print(f"Unable to detect the separator for the file: {full_path}. Please specify the separator manually.")
            separator = input("Enter the separator (e.g., ',', '\t', ';'): ")

        df = pd.read_csv(full_path, sep=separator)

        # Assign a unique ID for this DataFrame
        unique_id = f"{os.path.basename(full_path)}_{str(uuid.uuid4())[:4]}"
        dfs[unique_id] = df

        # Save a backup copy as CSV
        backup_file = os.path.join(backup_folder, unique_id + ".csv")
        df.to_csv(backup_file, index=False)
    
    return dfs
