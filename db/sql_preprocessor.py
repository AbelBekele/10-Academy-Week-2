import pandas as pd
import numpy as np
import sqlite3
import DatabaseConnection from connection

DatabaseConnection.connect()

AUTOMOBILE_SCHEMA = "automobile_data_schema.sql"
TRAFFIC_SCHEMA = "traffic_schema.sql"

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

def create_table():
    try:
        with engine.connect() as conn:
            for name in [TRAJECTORIES_SCHEMA,VEHICLE_SCHEMA]:
                
                with open(f'/opt/pgsql/{name}', "r") as file:
                    query = text(file.read())
                    conn.execute(query)
        print("Successfull")
    except Exception as e:
        print("Error creating table",e)
        sys.exit(e)


# create_table()

def insert_to_table(json_stream :str, table_name: str,from_file=False ):
    try:
        if not from_file:
            df = pd.read_json(json_stream)
        else:
            # df = pd.read_json(f'../temp/{json_stream}')
            with open(f'../temp_storage/{json_stream}','r') as file:
                data=file.readlines()
            dt=data[0]

            df=pd.DataFrame.from_dict(json.loads(dt))
            df.columns=df.columns.str.replace(' ','')

            # TODO: This(the following line) shall be fixed when using cloud services
            # due to local memory (resource) shortage, I minimized the df to be loaded 
            # df=df.loc[:np.floor(df.shape[0]/10),:] 
            df.dropna(inplace=True)
        with engine.connect() as conn:
            df.to_sql(name=table_name, con=conn, if_exists='append', index=False)

    except Exception as e:
        print(f"error while inserting to table: {e}")  
        sys.exit(e)