from numpy import NAN
from pipeline import Pipeline
from unittest.mock import patch
import unittest
import pytest
import sqlite3
import pandas as pd
import numpy as np
import os
import pandas.testing as assert_frame_equal



class TestPipeline(unittest.TestCase):
# https://docs.python.org/3/library/unittest.html

    def setUp(self):
        self.data_url1 = 'https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/EDGAR/datasets/v61_AP/NMVOC/v61_AP_NMVOC_1970_2018b.zip'
        self.data_name1 = 'emissions'
        self.data_url2 = 'https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/GWA02/CSV/1.0/en'
        self.data_name2 = 'treat_waste'
        self.data_url3 = 'https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/GWA01/CSV/1.0/en'
        self.data_name3 = 'generate_waste'
        self.data_dir = 'data'
        data = {
            'integers': [1, 2, np.nan, 4, 5],
            'floats': [0.1, np.nan, 0.3, 0.4, 0.5],
            'strings': ['a', 'b', 'c', 'd', None],
            'bools': [True, False, True, None, False]
        }
        self.sample_df = pd.DataFrame(data)

    def test_open_zip_xlsx(self):
        pipeline = Pipeline(url=self.data_url1)
        df = pipeline.open_zip_xlsx()
        # checks if the dataframe is not empty
        self.assertIsNotNone(df, "Dataframe is empty")

    def test_open_csv(self):
        pl = Pipeline(url=self.data_url2)
        df = pl.open_csv()
        # checks if the dataframe is not empty
        self.assertIsNotNone(df, "Dataframe is empty")

    def test_clean_data(self):
        pl = Pipeline()
        pl.set_df(self.sample_df)
        columns_toDrop = ['floats', 'bools']
        rename_columns = {'integers': 'Numbers', 'strings': 'Letters'}
        df_clean = pl.clean_data(rename_columns=rename_columns, columns_toDrop=columns_toDrop, drop_na=True)
        # checks if the dataframe is not empty
        self.assertIsNotNone(df_clean, "Dataframe is empty")
        # checks if the columns are dropped
        self.assertNotIn('floats', df_clean.columns, "Column not dropped")
        self.assertNotIn('bools', df_clean.columns, "Column not dropped")
        # checks if the columns are renamed
        self.assertIn('Numbers', df_clean.columns, "Column not renamed")
        self.assertIn('Letters', df_clean.columns, "Column not renamed")

    def test_create_sqlite(self):
        pl = Pipeline(data_name='test', data_dir='data')
        pl.set_df(self.sample_df)
        pl.create_sqlite()

if __name__ == '__main__':
    unittest.main(exit=False)
