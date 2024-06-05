import requests
import os
import pandas as pd
import sqlite3
from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile

class Pipeline:
    def __init__(self):
        self.dataurl1 = 'https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/EDGAR/datasets/v61_AP/NMVOC/v61_AP_NMVOC_1970_2018b.zip'
        self.data_url2 = 'https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/GWA02/CSV/1.0/en'
        self.data_dir = 'data'

    def read_zip(self):   
        if not os.path.exists(self.data_dir):
                os.makedirs(self.data_dir)
                print(f"Directory '{self.data_dir}' created.")

        try:
            with urlopen(self.data_url1) as zipresp:
                with ZipFile(BytesIO(zipresp.read())) as zfile:
                    for file in zfile.namelist():
                        if not file.endswith('_readme.html'):
                            zfile.extract(member=file, path=self.data_dir)
                            os.rename(os.path.join(self.data_dir, file), os.path.join(self.data_dir, 'emissions.csv'))
                            print(f"File '{file}' extracted and renamed.")

            # with urlopen(self.data_url1) as zipresp:
            #     with ZipFile(BytesIO(zipresp.read())) as zfile:
            #         files_to_extract = [f for f in zfile.namelist() if not f.endswith('_readme.html')]
            #         # print("Files in the ZIP:")
            #         # print(zfile.namelist())
            #         zfile.extractall(self.data_dir, members=files_to_extract)
            print("Extraction successful.")
        except Exception as e:
            print("An error occurred:", e)

    def read_csv(self):
        try:
            df = pd.read_csv(f'{self.data_dir}/v61_AP_NMVOC_1970_2018b.csv')
            print("Dataframe created.")
            return df
        except Exception as e:
            print("An error occurred:", e)