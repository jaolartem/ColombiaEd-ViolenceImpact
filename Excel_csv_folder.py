import pandas as pd
import glob
import os
# Import the excel_to_csv function from the file where you defined it
import excel_to_csv 

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

# Define a main function that calls the convert_excel_to_csv function with the desired folder name
def main():
    # Call the convert_excel_to_csv function with the desired folder name
    convert_excel_to_csv("data")

# Check if the module is being run as the main program or being imported by another module
if __name__ == "__main__":
    # Execute the main function only when the module is run as the main program
    main()
