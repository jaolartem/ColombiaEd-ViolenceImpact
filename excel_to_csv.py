import pandas as pd


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


def main():
    # Call the convert_excel_to_csv function with the desired folder name
    excel_to_csv(excel)

# Check if the module is being run as the main program or being imported by another module
if __name__ == "__main__":
    # Execute the main function only when the module is run as the main program
    main()
