import os
import glob
from excel_to_csv import excel_to_csv
from Excel_csv_folder import folder_to_csv
from pivot_and_save_df import pivot_and_save_df

# Define the global dictionary
ALL_DFS = {}

class Extract:
    """
    Class responsible for data extraction from Excel files.
    """
    def __init__(self):
        self.converted_files = []

    def from_excel(self, path):
        """
        Extracts data from Excel and converts it to DataFrames stored in ALL_DFS.
        
        Args:
        - path (str): Path to the Excel file or directory containing multiple Excel files.
        
        Updates:
        - ALL_DFS: Global dictionary containing sheet names as keys and corresponding DataFrames as values.
        
        """
        global ALL_DFS
        
        # Check if the given path is a directory or single file
        if os.path.isdir(path):
            dfs_dict = folder_to_csv(path)  # This function should handle the directory, not the excel_to_csv function
            for excel_path in glob.glob(os.path.join(path, "*.xlsx")):
                self.converted_files.append(excel_path)
            ALL_DFS.update(dfs_dict)
        else:
            # If it's a single file
            dfs_dict = {os.path.basename(path): excel_to_csv(path)}
            self.converted_files.append(path)
            ALL_DFS.update(dfs_dict)
class Transformation:
    """
    Class responsible for data transformation.
    """

    def transform_and_save(self, sheet_name, dataframe):
        """
        Logic to transform and save the dataframe.
        Can be extended in the future for more complex transformations.
        
        Args:
        - sheet_name (str): Name of the DataFrame/sheet.
        - dataframe (pd.DataFrame): DataFrame to be transformed.
        
        Returns:
        - pd.DataFrame: Transformed DataFrame.
        """
        # Current logic is a placeholder. Actual transformation logic should replace this.
        return dataframe

    def Violence_pivot(self):
        """
        Transforms DataFrames that match certain conditions.
        
        Updates:
        - ALL_DFS: Global dictionary containing transformed DataFrames.
        
        Returns:
        - dict: Dictionary containing transformed DataFrames.
        """
        global ALL_DFS
        for df_name, df in list(ALL_DFS.items()):
            if "municipio del hecho" in df_name.lower():  # Case-insensitive check
                transformed_df = self.transform_and_save(df_name, df)
                ALL_DFS[df_name] = transformed_df  
        return ALL_DFS
    
if __name__ == "__main__":
    folder_name = '/path/to/your/folder'
    extractor = Extract()
    extractor.from_excel(folder_name)
    transformer = Transformation()
    dfs_dict = transformer.Violence_pivot()
    print(dfs_dict)
