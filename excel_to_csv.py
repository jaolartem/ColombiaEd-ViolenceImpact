import pandas as pd

# Read the Excel file and return a dictionary of data frames
import pandas as pd
import os

def excel_to_csv(excel):
    """
    This function reads an Excel file and exports each sheet as a CSV file.
    The CSV file name is the same as the sheet name.
    Parameters:
        excel: a string with the Excel file name
    Return:
        None
    """
    # Read the Excel file as a dictionary of data frames
    df_dict = pd.read_excel(excel, sheet_name=None)
    
    # Loop through the dictionary and export each data frame to a CSV file
    for sheet_name, df in df_dict.items():
        # Use the os module to create the CSV file name with the correct path separator
        csv_file = os.path.join(sheet_name + ".csv")
        
        # Use a try-except block to handle any errors
        try:
            # Export the data frame to CSV
            df.to_csv(csv_file, index=False, header=True)
            print(f"Successfully exported {csv_file}")
        except Exception as e:
            print(f"Failed to export {csv_file}: {e}")

# Define a function that takes a folder name as an argument and converts all Excel files in that folder to CSV files
def convert_excel_to_csv(folder_name):
    # Create the full path of the folder
    folder_path = os.path.join(os.getcwd(), folder_name)

    # Get the list of the names of the Excel files in the folder
    excel_list = glob.glob(os.path.join(folder_path, "*.xlsx"))

    # Iterate over the list and apply the conversion function
    for file in excel_list:
        # Read the Excel file and return a dictionary of data frames
        df_dict = excel_to_csv(file)

# Call the function with the desired folder name

