import pandas as pd
import os

def excel_to_csv(excel):
    """
    This function reads an Excel file and exports each sheet as a CSV file.
    The CSV file name is the same as the sheet name.
    
    Parameters:
        excel: a string with the Excel file name
    
    Return:
         - dict: A dictionary where keys are sheet names and values are corresponding dataframes.
    """
    # Read the Excel file as a dictionary of data frames
    df_dict = pd.read_excel(excel, sheet_name=None)
    
    # Get the directory path of the Excel file
    dir_path = os.path.dirname(excel)
    
    for sheet_name, df in df_dict.items():
        # Create a full path for the CSV file to save in the same directory as the Excel file
        csv_file = os.path.join(dir_path, sheet_name + ".csv")
        try:
            df.to_csv(csv_file, index=False, header=True)
            print(f"Successfully exported {csv_file}")
        except Exception as e:
            print(f"Failed to export {csv_file}: {e}")
            
    return df_dict
