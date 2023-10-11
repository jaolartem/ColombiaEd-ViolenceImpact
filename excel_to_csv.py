import pandas as pd


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
    def excel_to_csv(excel):
        df_dict = pd.read_excel(excel, sheet_name=None)
        dfs_list = []
        for sheet_name, df in df_dict.items():
            csv_file = os.path.join(sheet_name + ".csv")
            try:
                df.to_csv(csv_file, index=False, header=True)
                print(f"Successfully exported {csv_file}")
            except Exception as e:
                print(f"Failed to export {csv_file}: {e}")
            dfs_list.append((sheet_name, df))
        return dfs_list

def main():
    # Call the convert_excel_to_csv function with the desired folder name
    excel_to_csv(excel)

# Check if the module is being run as the main program or being imported by another module
if __name__ == "__main__":
    # Execute the main function only when the module is run as the main program
    main()
