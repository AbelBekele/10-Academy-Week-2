from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

# Define default_args
default_args = {
    'owner': 'your_username',
    'start_date': datetime(2023, 12, 23),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Instantiate a DAG
dag = DAG(
    'dbt_traffic_dag',
    default_args=default_args,
    description='A simple DAG to run dbt from specified folder',
    schedule_interval=timedelta(days=1),  # Set your desired schedule
)

# Task to run dbt
run_dbt_task = BashOperator(
    task_id='run_dbt_task',
    bash_command='cd ../dbt_traffic/dbt_traffic && dbt run',
    dag=dag,
)

# Set task dependencies
run_dbt_task

if __name__ == "__main__":
    dag.cli()
