
"""
etl_module: Contains the main ETL functionalities for processing different file types.

This module is responsible for orchestrating the extraction, transformation, and loading
of data from various sources, including Excel, CSV, and TXT files. The processed data is
then stored in appropriate data structures for further analysis.
"""
import os
import glob
import logging
from excel_to_csv import load_excel_to_dict
from csv_to_df import load_csv_to_dict
from txt_to_df import load_txt_to_dict

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define the global dictionary
ALL_DFS = {}

class Extract:
    """
    Class responsible for data extraction.
    """

    def __init__(self):
        """
        Initialize the ETL class with default settings.
        """
        self.converted_files = []

    def from_excel(self, path):
        """
        Extracts data from Excel and converts it to DataFrames stored in ALL_DFS.
        
        Args:
        - path (str): Path to the Excel file or directory containing multiple Excel files.
        """
        global ALL_DFS
        
        try:
            dfs_dict = load_excel_to_dict(path)
            ALL_DFS.update(dfs_dict)
        except FileNotFoundError:
            logger.error(f"File not found: {path}")
        except Exception as e:
            logger.error(f"Error in extraction process from Excel. Error: {e}")

    def from_csv(self, csv_path):
        """
        Extracts data from CSVs and loads them into DataFrames stored in ALL_DFS.
        
        Args:
        - csv_path (str): Path to the CSV file or directory containing multiple CSV files.
        """
        global ALL_DFS
        try:
            loaded_data = load_csv_to_dict(csv_path)
            ALL_DFS.update(loaded_data)
        except FileNotFoundError:
            logger.error(f"File not found: {csv_path}")
        except Exception as e:
            logger.error(f"Error in extraction process from CSV. Error: {e}")

    def from_txt(self, txt_path):
        """
        Extracts data from TXT files and loads them into DataFrames stored in ALL_DFS.
        
        Args:
        - txt_path (str): Path to the TXT file or directory containing multiple TXT files.
        """
        global ALL_DFS        
        try:
            extracted_dfs = load_txt_to_dict(txt_path)
            ALL_DFS.update(extracted_dfs)
        except FileNotFoundError:
            logger.error(f"File not found: {txt_path}")
        except Exception as e:
            logger.error(f"Error in extraction process from TXT. Error: {e}")

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
    extractor = Extract()
    extractor.from_excel(folder_name)
    extractor.from_csv(folder_name)
    transformer = Transformation()
    dfs_dict = transformer.Violence_pivot()
    print(dfs_dict)
