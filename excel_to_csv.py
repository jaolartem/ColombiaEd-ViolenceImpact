import pandas as pd
import os

def excel_to_csv(excel_path, backup_directory):
    """
    Convert sheets from an Excel file to CSV files. The CSV files are saved in a backup folder
    structure under "CSV's_backout" which mirrors the original directory structure.

    Args:
    - excel_path (str): The path to the Excel file to convert.
    - backup_directory (str): Directory where CSVs will be stored.
    """
    # Extract directory and filename from the provided path
    directory, filename = os.path.split(excel_path)
    base_filename = os.path.splitext(filename)[0]
    
    try:
        # Convert each sheet in the Excel file to a DataFrame and save as CSV
        df_dict = pd.read_excel(excel_path, sheet_name=None)
        for sheet_name, df in df_dict.items():
            csv_file_name = f"{base_filename}_{sheet_name}.csv"
            
            # Check if file already exists, if so add a version suffix
            version_suffix = 1
            original_csv_file_name = csv_file_name
            while os.path.exists(os.path.join(backup_directory, csv_file_name)):
                version_suffix += 1
                csv_file_name = f"{original_csv_file_name[:-4]}_V{version_suffix}.csv"
            
            # Save the DataFrame as a CSV file in the backup directory
            df.to_csv(os.path.join(backup_directory, csv_file_name), index=False, header=True)
    except Exception as e:
        print(f"Error processing file {excel_path}. Error: {e}")
    return backup_directory
