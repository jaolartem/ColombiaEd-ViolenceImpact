import os
import glob
from file_detector import process_directory
from csv_to_df import load_csv_to_dict

ALL_DFS = {}

class Extraction:
    """
    Class responsible for data extraction.
    """

    def __init__(self):
        """
        Initialize the Extraction class.
        """
        self.dataframes = {}

    def extract_from_directory(self, directory_path):
        """
        Extracts data from a directory, processing all supported file formats.
        
        Args:
        - directory_path (str): Path to the directory.
        
        Updates:
        - self.dataframes: Dictionary containing extracted DataFrames.
        """
        self.dataframes = process_directory(directory_path)

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
            if "municipio del hecho" in df_name.lower():
                transformed_df = self.transform_and_save(df_name, df)
                ALL_DFS[df_name] = transformed_df  
        return ALL_DFS

if __name__ == "__main__":
    folder_name = '/path/to/your/folder'
    extractor = Extraction()
    extractor.extract_from_directory(folder_name)
    transformer = Transformation()
    dfs_dict = transformer.Violence_pivot()
    print(dfs_dict)
