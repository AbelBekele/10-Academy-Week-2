from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
import pandas as pd

class DatabaseConnection:
    def __init__(self):
        # Load environment variables from the .env file
        load_dotenv()

        # Fetch database credentials from environment variables
        self.username = os.getenv("DB_USERNAME")
        self.password = os.getenv("DB_PASSWORD")
        self.host = os.getenv("DB_HOST")
        self.port = os.getenv("DB_PORT")
        self.database = os.getenv("DB_DATABASE")

        # Check if any credentials are missing
        if None in (self.username, self.password, self.host, self.port, self.database):
            raise ValueError("One or more database credentials are missing.")

        self.connection_url = f"postgresql+psycopg2://{self.username}:{self.password}@{self.host}:{self.port}/{self.database}"
        self.engine = None
        self.connection = None

    def connect(self):
        try:
            self.engine = create_engine(self.connection_url)
            self.connection = self.engine.connect()
            print("Connected to the database.")
        except Exception as e:
            print(f"Error connecting to the database: {str(e)}")

    def execute_query(self, query):
        try:
            df = pd.read_sql_query(query, self.connection)
            return df
        except Exception as e:
            print(f"Error executing query: {str(e)}")
            
    def execute_update_query(self, query):
        try:
            self.connection.execute(query)
            print("Query executed successfully.")
        except Exception as e:
            print(f"Error executing query: {str(e)}")

    def close_connection(self):
        try:
            self.connection.close()
            print("Connection closed.")
        except Exception as e:
            print(f"Error closing connection: {str(e)}")
