import os
import pandas as pd
import glob

def csv_to_df_dict(backup_directory):
    """
    Load each CSV in the backup directory into a DataFrame and store in a dictionary.

    Args:
    - backup_directory (str): Directory where CSVs are stored.

    Returns:
    - dict: Dictionary with CSV filenames (without extension) as keys and DataFrames as values.
    """
    df_dict = {}
    for csv_path in glob.glob(os.path.join(backup_directory, '**', '*.csv'), recursive=True):
        try:
            df = pd.read_csv(csv_path)
            csv_filename = os.path.splitext(os.path.basename(csv_path))[0]

            # Extract the last four characters from the containing folder (year)
            year_suffix = os.path.basename(os.path.dirname(csv_path))[-4:]
            
            # Ensure that the year_suffix is numeric
            if not year_suffix.isdigit():
                print(f"Warning: Expected a year suffix in the folder name for {csv_path}, but got {year_suffix}.")
            else:
                csv_filename += f"_{year_suffix}"
            
            df_dict[csv_filename] = df
        except Exception as e:
            print(f"Error processing {csv_path}: {e}")
            
    return df_dict
