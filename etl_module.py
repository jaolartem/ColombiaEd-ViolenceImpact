import os
import glob
from excel_to_csv import excel_to_csv
from Excel_csv_folder import convert_excel_to_csv
from pivot_and_save_df import pivot_and_save_df


class Converters:
    def __init__(self):
        pass

class FileConverter(Converters):
    def __init__(self):
        super().__init__()
        self.converted_files = []

    def convert_excel(self, path):
        if os.path.isdir(path):
            dfs_list = convert_excel_to_csv(path)
            for excel_path in glob.glob(os.path.join(path, "*.xlsx")):
                self.converted_files.append(excel_path)
            return dfs_list
        else:
            dfs_list = {os.path.basename(path): excel_to_csv(path)}
            self.converted_files.append(path)
            return dfs_list
       

class DataFrameTransformation:
    def __init__(self):
        self.transformed_dfs = []

    def transform_and_save(self, df_name, df):
        df_pivoted = pivot_and_save_df(df_name, df)
        self.transformed_dfs.append(df_name)
        return df_pivoted

class ETLProcessor:
    def __init__(self, path):
        self.path = path
        self.file_converter = FileConverter()
        self.df_transformer = DataFrameTransformation()

    def process(self):
        dfs_list = self.file_converter.convert_excel(self.path)
        for df_name, df in dfs_list.items():
            if df_name == "MUNICIPIO DEL HECHO":
                self.df_transformer.transform_and_save(df_name, df)

    def get_converted_files(self):
        return self.file_converter.converted_files

    def get_transformed_dfs(self):
        return self.df_transformer.transformed_dfs

if __name__ == "__main__":
    path = input("Enter the path (file or folder) containing Excel files: ")
    processor = ETLProcessor(path)
    processor.process()
    print(f"Converted Files: {processor.get_converted_files()}")
    print(f"Transformed DataFrames: {processor.get_transformed_dfs()}")
