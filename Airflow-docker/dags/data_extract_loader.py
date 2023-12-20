import os
import sys
from datetime import datetime
from datetime import timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

cwd=os.getcwd()
sys.path.append(f'../utils/')
sys.path.append(f'../db/')
sys.path.append(f'../temp/')
sys.path.insert(0,os.path.abspath(os.path.dirname(__file__)))

from extractor import DataExtractor
import sql_preprocessor

data_extractor=DataExtractor()

# def separate_data(ti):
#     data_extractor.separate(file_name='20181024_d1_0830_0900.csv',number=5)

def extract_data(ti):

    loaded_df_name=data_extractor.extract_data(file_name='20181024_d1_0830_0900.csv',return_json=True)
    traffic_file_name,automobile_file_name=loaded_df_name
   
    ti.xcom_push(key="traffic",value=traffic_file_name)
    ti.xcom_push(key="automobile",value=automobile_file_name)

def create_table():
    db_util.create_table()

def populate__automobiles_table(ti):
    traffic_file_name = ti.xcom_pull(key="traffic",task_ids='extract_from_file')
    # automobile_file_name = ti.xcom_pull(key="automobile",task_ids='extract_from_file')
    # traffic_data,automobile_data=combined_df['traffic'], combined_df['automobile']
    db_util.insert_to_table(traffic_file_name, 'trajectories',from_file=True)
    # db_util.insert_to_table(automobile_file_name, 'automobiles',from_file=True)

def populate_traffic_table(ti):
    # traffic_file_name = ti.xcom_pull(key="traffic",task_ids='extract_from_file')
    automobile_file_name = ti.xcom_pull(key="automobile",task_ids='extract_from_file')
    # traffic_data,automobile_data=combined_df['traffic'], combined_df['automobile']
    # db_util.insert_to_table(traffic_file_name, 'trajectories',from_file=True)
    db_util.insert_to_table(automobile_file_name, 'automobiles',from_file=True)

def clear_memory_automobile(ti):
    traffic_file_name = ti.xcom_pull(key="traffic",task_ids='extract_from_file')
    # automobile_file_name = ti.xcom_pull(key="automobile",task_ids='extract_from_file')

    os.remove(f'../temp_storage/{traffic_file_name}')
    # os.remove(f'../temp_storage/{automobile_file_name}')

def clear_memory_traffic(ti):
    # traffic_file_name = ti.xcom_pull(key="traffic",task_ids='extract_from_file')
    automobile_file_name = ti.xcom_pull(key="automobile",task_ids='extract_from_file')

    # os.remove(f'../temp_storage/{traffic_file_name}')
    os.remove(f'../temp_storage/{automobile_file_name}')

# Specifing the default_args
default_args = {
    'owner': 'Natnael',
    'depends_on_past': False,
    'email': ['natnaelmasresha@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0
}

with DAG(
    dag_id='extractor_loader_pg',
    default_args=default_args,
    description='this loads our data to the database',
    start_date=datetime(2022,9,20,3),
    schedule_interval='@daily',
    catchup=False
) as dag:
    
    read_data = PythonOperator(
        task_id='extract_from_file',
        python_callable = extract_data,
    ) 
    
    create_tables = PythonOperator(
        task_id='create_table',
        python_callable = create_table
    )
    
    populate_automobiles = PythonOperator(
        task_id='load_automobile_data',
        python_callable = populate__automobiles_table
    )
    
    populate_traffic = PythonOperator(
        task_id='load_traffic_data',
        python_callable = populate_traffic_table
    ) 

    clear_temp_automobile_data = PythonOperator(
        task_id='delete_temp_automobile_files',
        python_callable = clear_memory_automobile
    )
    clear_temp_traffic_data = PythonOperator(
        task_id='delete_temp_traffic_files',
        python_callable = clear_memory_traffic
    )

    [read_data,create_tables]>>populate_automobiles>>clear_temp_automobile_data,populate_automobiles>>populate_traffic>>clear_temp_traffic_data
    
