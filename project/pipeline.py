import os
import pandas as pd
import sqlite3
from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile
import sqlite3

class Pipeline:
    def __init__(self,url,data_name, data_dir):
        self.url = url
        self.data_name =data_name
        self.data_dir = data_dir
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
            print(f"Directory '{data_dir}' created.")

    def open_zip_xlsx(self):
        df_xls=None
        with urlopen(self.url) as zipresp:
            with ZipFile(BytesIO(zipresp.read())) as zfile:
                for file in zfile.namelist():
                    if not file.endswith('_readme.html'):
                        with zfile.open(file) as excel_file_content:
                            df_xls = pd.read_excel(excel_file_content,skiprows=9)
                    
        print('Zip file imported and created draframe from xlsx file')
        return df_xls
    
    def open_csv(self):
        self._df = pd.read_csv(self.url)
        return self._df
    
    def clean_data(self,df, columns_toDrop=None, rename_columns=None):
        if rename_columns:
            df = df.rename(columns=rename_columns)
        if columns_toDrop:
            df = df.drop(columns=columns_toDrop)
        df.dropna(inplace=True)
        print("Data cleaned successfully. Tasks carried out: drop columns, rename columns, drop na")
        return df

    def create_sqldb(self,df):
        db_full_path = os.path.join(self.data_dir, self.data_name)
        db_con = sqlite3.connect(db_full_path)
        df.reset_index(inplace=True)
        df.to_sql('treatment', db_con, if_exists='replace', index=False)
        db_con.close()
        print("Database created successfully. Dataframe saved to sqlite database")

class DownloadData:

    def __init__(self):
        self.data_url1 = 'https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/EDGAR/datasets/v61_AP/NMVOC/v61_AP_NMVOC_1970_2018b.zip'
        self.data_name1 = 'emissions'
        self.data_url2 = 'https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/GWA02/CSV/1.0/en'
        self.data_name2 = 'treat_waste'
        self.data_url3 = 'https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/GWA01/CSV/1.0/en'
        self.data_name3 = 'generate_waste'
        self.data_dir = 'data'

    def download_data1(self):
        data_p = Pipeline(self.data_url1, self.data_name1, self.data_dir)
        df = data_p.open_zip_xlsx()
        columns_to_keep = ['Emission Sector'] + [f'Y_{year}' for year in range(2004, 2019)]
        columns_to_drop = ['Name','IPCC_annex', 'C_group_IM24_sh', 'Country_code_A3', 'ipcc_code_2006_for_standard_report', 'Substance', 'fossil_bio']
        columns_to_rename = {'ipcc_code_2006_for_standard_report_name': 'Emission Sector'}
        df = df.loc[df['Name'] == 'Ireland']
        df = data_p.clean_data(df,columns_to_drop,columns_to_rename)
        df = df[columns_to_keep]
        data_p.create_sqldb(df)

    def download_data2(self):
        data_p = Pipeline(self.data_url2, self.data_name2, self.data_dir)
        df = data_p.open_csv()
        columns_to_drop = ['STATISTIC', 'Statistic Label', 'TLIST(A1)', 'C04253V05027', 'C04251V05025','C04252V05026','UNIT']
        df = data_p.clean_data(df, columns_to_drop)
        df = df[df['Waste Category'] != 'Total waste']
        data_p.create_sqldb(df)
               

    def download_data3(self):
        data_p = Pipeline(self.data_url3, self.data_name3, self.data_dir)
        df = data_p.open_csv()
        columns_to_drop = ['STATISTIC', 'Statistic Label', 'TLIST(A1)', 'C014259V05033', 'C04253V05027','C04251V05025','UNIT']
        df = data_p.clean_data(df, columns_to_drop)
        df = df[df['Waste Category'] != 'Total waste']
        data_p.create_sqldb(df)

# Create an instance of DownloadData
download_data_instance = DownloadData()

# Download and process each dataset
download_data_instance.download_data1()
download_data_instance.download_data2()
download_data_instance.download_data3()
