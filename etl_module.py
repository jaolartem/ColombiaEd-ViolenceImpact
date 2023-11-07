import os
import glob
from file_detector import process_directory

# Global variable to hold all DataFrames
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
        print("DataFrames after processing directory:", self.dataframes.keys())  # Debugging print statement
        ALL_DFS.update(self.dataframes) 

class Transformation:
    """
    Class responsible for data transformation.
    """

    def __init__(self):
        # Work with a local copy of the DataFrames for transformations
        self.local_dfs = ALL_DFS.copy()

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

    def violence_pivot(self):
        """
        Transforms DataFrames that match certain conditions.
        """
        for df_name, df in list(self.local_dfs.items()):
            if "municipio del hecho" in df_name.lower():
                transformed_df = self.transform_and_save(df_name, df)
                self.local_dfs[df_name] = transformed_df  
        return self.local_dfs

if __name__ == "__main__":
    folder_name = '/path/to/your/folder'  # Update with the actual path
    extractor = Extraction()
    extractor.extract_from_directory(folder_name)

    # Create a Transformation object and perform transformations
    transformer = Transformation()
    transformed_dfs = transformer.violence_pivot()
    print(transformed_dfs)
