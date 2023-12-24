import unittest
import pandas as pd
from datetime import datetime
from data_extractor import DataExtractor

class TestDataExtractor(unittest.TestCase):

    def setUp(self):
        self.data_extractor = DataExtractor()

    def test_get_columns_and_rows(self):
        file_path = 'sample_data.txt'
        columns, data = self.data_extractor.get_columns_and_rows(file_path)
        self.assertIsInstance(columns, list)
        self.assertIsInstance(data, list)

    def test_chunk_list(self):
        input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        chunked_list = self.data_extractor.chunk_list(input_list, 3, default_first_val=0)
        self.assertIsInstance(chunked_list, list)

    def test_prepare_data_for_pandas(self):
        columns = ['col1', 'col2', 'col3']
        all_data = [['1', '2', '3'], ['4', '5', '6']]
        id_prefix = 'prefix'
        traffic_data, automobile_data = self.data_extractor.prepare_data_for_pandas(columns, all_data, id_prefix)
        self.assertIsInstance(traffic_data, tuple)
        self.assertIsInstance(automobile_data, tuple)

    def test_prepare_data_frame(self):
        traffic_data = (['col1', 'col2'], [['1', '2'], ['3', '4']])
        timed_automobile_data = (['col3', 'col4'], [['5', '6'], ['7', '8']])
        traffic_df, automobile_df = self.data_extractor.prepare_data_frame(traffic_data, timed_automobile_data)
        self.assertIsInstance(traffic_df, pd.DataFrame)
        self.assertIsInstance(automobile_df, pd.DataFrame)

    def test_extract_data(self):
        file_name = 'sample_data.txt'
        tr_file, vh_file = self.data_extractor.extract_data(file_name, return_json=False)
        self.assertIsInstance(tr_file, str)
        self.assertIsInstance(vh_file, str)

    def test_separate_data(self):
        file_name = 'sample_data.txt'
        chunk_size = 100
        result = self.data_extractor.separate_data(file_name, chunk_size)
        self.assertIsNone(result)  # Add assertions based on the expected behavior

if __name__ == '__main__':
    unittest.main()
