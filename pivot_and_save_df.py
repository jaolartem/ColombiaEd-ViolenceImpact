import os
import pandas as pd

"""
    Pivots the DataFrame and saves it as a CSV file.
    
    Parameters:
    - df_name (str): The name for the DataFrame (to be used in the CSV file name).
    - df (DataFrame): The DataFrame to pivot and save.
    
    Returns:
    - DataFrame: The pivoted DataFrame.
"""

def pivot_and_save_df(sheet_name, dataframe):
    df_pivoted = dataframe.transpose()
    if 'Total' in df_pivoted.columns:
        idx = df_pivoted.columns.get_loc('Total')
        dfs = [df_pivoted.iloc[:, :idx], df_pivoted.iloc[:, idx+1:]]
        
        for sub_dataframe in dfs:
            title = sub_dataframe.iloc[0,0]
            csv_file = sheet_name + "_" + title + ".csv"
            try:
                sub_dataframe.to_csv(csv_file, index=True, header=True)
                print(f"Successfully saved pivoted DataFrame as {csv_file}")
            except Exception as e:
                print(f"Failed to save {csv_file}: {e}")

def main(sheet_name, dataframe):
    # Call the convert_excel_to_csv function with the desired folder name
    pivot_and_save_df(sheet_name, dataframe)

# Check if the module is being run as the main program or being imported by another module
if __name__ == "__main__":
    # Execute the main function only when the module is run as the main program
    main()
