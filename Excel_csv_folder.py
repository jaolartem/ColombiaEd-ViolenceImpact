import glob
import os
import shutil
from excel_to_csv import excel_to_csv 

def move_csv_to_subfolder(folder_path):
    """Move all .csv files in the specified directory to a subfolder named 'CSV'."""
    csv_files = glob.glob(os.path.join(folder_path, "*.csv"))
    
    # Create 'CSV' subdirectory if it doesn't exist
    csv_subfolder = os.path.join(folder_path, 'CSV')
    if not os.path.exists(csv_subfolder):
        os.makedirs(csv_subfolder)
        
    # Move all .csv files to the 'CSV' subdirectory
    for csv_file in csv_files:
        shutil.move(csv_file, csv_subfolder)
    print(f"Moved all CSV files to {csv_subfolder}")

def convert_excel_to_csv(folder_name):
    all_dfs = {}
    
    # Create the full path of the folder
    folder_path = os.path.join(os.getcwd(), folder_name)

    # Get the list of the names of the Excel files in the folder
    excel_list = glob.glob(os.path.join(folder_path, "*.xlsx"))

    # Iterate over the list and apply the conversion function
    for file in excel_list:
        df_dict = excel_to_csv(file)
        all_dfs.update(df_dict)
        
    # Move all .csv files to 'CSV' subfolder
    move_csv_to_subfolder(folder_path)
    
    return all_dfs

def main():
    # Call the convert_excel_to_csv function with the desired folder name
    convert_excel_to_csv("data")

if __name__ == "__main__":
    main()
