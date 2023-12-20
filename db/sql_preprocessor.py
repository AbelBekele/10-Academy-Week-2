import pandas as pd
import numpy as np
import sqlite3

class DBFilter:
    def __init__(self, dataframe):
        self.df = dataframe

    def filter_numeric_columns(self, threshold=0):
        numeric_columns = self.df.select_dtypes(include=[np.number]).columns
        filtered_df = self.df[numeric_columns].apply(lambda x: x[x > threshold])

        return filtered_df
    
    def load_data_from_db(self, db_path, sql_query):
        connection = sqlite3.connect(db_path)
        df = pd.read_sql_query(sql_query, connection)
        connection.close()
        return df

    def get_unique_values(self, column):
        unique_values = self.df[column].unique()
        return unique_values
    
    def most_repeated_value(self, column):
        return self.df[column].mode().values[0]

    def calculate_average(self, column):
        return self.df[column].mean()

    def close_connection(self):
        # No connection to close for a DataFrame-based implementation
        pass
