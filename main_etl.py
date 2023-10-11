from Excel_csv_folder import convert_excel_to_csv
from pivot_and_save_df import pivot_and_save_df

def main_etl_process():
    folder_name = input("Enter the name of the folder containing Excel files: ")
    dfs_list = convert_excel_to_csv(folder_name)
    
    for sheet_name, df in dfs_list:
        if sheet_name == "MUNICIPIO DEL HECHO":
            pivot_and_save_df(sheet_name, df)
            dfs_list[idx] = (sheet_name, pivoted_df)

if __name__ == "__main__":
    main_etl_process()