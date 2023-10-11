import pandas as pd

def pivot_and_save_df(sheet_name, dataframe):
    """
    Transposes the given dataframe, splits it at the 'Total' column (if present), 
    and saves each part as a CSV file. The filename is derived from the sheet_name 
    and the title present in the cell (0,0) of the sub-dataframe.

    Args:
    - sheet_name (str): Name of the Excel sheet from which the dataframe is derived.
    - dataframe (pd.DataFrame): DataFrame to be transposed and saved.

    Returns:
    - dict: Dictionary containing the transformed dataframes.
    """
    df_pivoted = dataframe.transpose()
    transformed_dfs = {}
    
    if 'Total' in df_pivoted.columns:
        idx = df_pivoted.columns.get_loc('Total')
        dfs = [df_pivoted.iloc[:, :idx], df_pivoted.iloc[:, idx+1:]]
        
        for sub_dataframe in dfs:
            title = sub_dataframe.iloc[0,0]
            csv_file = sheet_name + "_" + title + ".csv"
            try:
                sub_dataframe.to_csv(csv_file, index=True, header=True)
                print(f"Successfully saved pivoted DataFrame as {csv_file}")
                transformed_dfs[title] = sub_dataframe
            except Exception as e:
                print(f"Failed to save {csv_file}: {e}")
                
    return transformed_dfs
