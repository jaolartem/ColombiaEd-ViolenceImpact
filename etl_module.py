import os
import glob
from excel_to_csv import excel_to_csv
from Excel_csv_folder import convert_excel_to_csv
from pivot_and_save_df import pivot_and_save_df

# Define the global dictionary
ALL_DFS = {}

class Extract:
    """
    Class responsible for data extraction.
    """
    def __init__(self):
        self.converted_files = []

    def extract_from_excel(self, path):
        """
        Extracts data from Excel and converts it to DataFrames stored in ALL_DFS.
        
        Args:
        - path (str): Path to the Excel file or directory containing multiple Excel files.
        
        """
        global ALL_DFS
        
        # Check if the given path is a directory or single file
        if os.path.isdir(path):
            dfs_dict = convert_excel_to_csv(path)
            for excel_path in glob.glob(os.path.join(path, "*.xlsx")):
                self.converted_files.append(excel_path)
            ALL_DFS.update(dfs_dict)
        else:
            # If it's a single file
            dfs_dict = {os.path.basename(path): excel_to_csv(path)}
            self.converted_files.append(path)
            ALL_DFS.update(dfs_dict)

class Transformation:
    """Class responsible for data transformation."""

    def transform_and_save(self, sheet_name, dataframe):
        """
        Transforms and saves the DataFrame based on certain conditions.
        Returns the transformed DataFrame.
        """
        if sheet_name == "MUNICIPIO DEL HECHO":
            transformed_df = pivot_and_save_df(sheet_name, dataframe)
            return transformed_df
        return dataframe  # If the condition is not met, simply return the original DataFrame

    def process(self):
        """Processes all DataFrames in global_dfs_dict based on transformation conditions."""
        global global_dfs_dict
        
        # Iterate over the global dictionary and transform the data frames in place
        for df_name, df in list(global_dfs_dict.items()):
            global_dfs_dict[df_name] = self.transform_and_save(df_name, df)

if __name__ == "__main__":
    folder_name = '/path/to/your/folder'
    processor = Transformation()
    dfs_dict = processor.process(folder_name)
    print(dfs_dict)
