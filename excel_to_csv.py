import pandas as pd
import os

def excel_to_csv(excel_path):
    """
    Convert sheets from an Excel file to CSV files. The CSV files are saved in a backup folder
    structure under "CSV's_backout" which mirrors the original directory structure.

    Args:
    - excel_path (str): The path to the Excel file to convert.

    Returns:
    - dict: A dictionary where keys are CSV filenames (without '.csv' extension) 
            and values are corresponding dataframes.
    """
    # Extract directory and filename from the provided path
    directory, filename = os.path.split(excel_path)
    base_filename = os.path.splitext(filename)[0]
    
    # Define backup directory for CSVs
    backup_directory = os.path.join(directory, "CSV's_backout", base_filename)
    if not os.path.exists(backup_directory):
        os.makedirs(backup_directory)
    
    # Convert each sheet in the Excel file to a DataFrame and save as CSV
    df_dict = pd.read_excel(excel_path, sheet_name=None)
    for sheet_name, df in df_dict.items():
        csv_file_name = f"{base_filename}_{sheet_name}.csv"
        version_suffix = 1
        original_csv_file_name = csv_file_name
        
        # Check if file already exists, if so add a version suffix
        while os.path.exists(os.path.join(backup_directory, csv_file_name)):
            version_suffix += 1
            csv_file_name = f"{original_csv_file_name[:-4]}_V{version_suffix}.csv"
        
        # Save the DataFrame as a CSV file in the backup directory
        df.to_csv(os.path.join(backup_directory, csv_file_name), index=False, header=True)
        
        # Update dictionary key to match the CSV filename
        df_dict[csv_file_name[:-4]] = df_dict.pop(sheet_name)

    return df_dict

if __name__ == "__main__":
    # Sample execution
    path_to_excel = "sample.xlsx"
    dfs = excel_to_csv(path_to_excel)
