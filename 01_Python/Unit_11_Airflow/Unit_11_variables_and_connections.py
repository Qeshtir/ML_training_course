from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta


def get_variable():
    from airflow.models import Variable
    """
    Gets totalTestResultsIncrease field from Covid API for given state and return value
    """
    is_prod = Variable.get("is_prod")  # необходимо передать имя, заданное при создании Variable
    return is_prod
    # теперь в is_prod лежит значение Variable

def get_connection():
    from airflow.hooks.base import BaseHook

    connection = BaseHook.get_connection("conn_name")
    conn_password = connection.password
    conn_login = connection.login
    return conn_password, conn_login

# Default settings applied to all tasks
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    'connections_and_variables',
    start_date=datetime(2021, 1, 1),
    max_active_runs=2,
    schedule_interval=timedelta(minutes=30),
    default_args=default_args,
    catchup=False
) as dag:
    t1 = PythonOperator(
        task_id = 'example_variable',
        python_callable=get_variable,
    )
    t2 = PythonOperator(
        task_id = 'example connection',
        python_callable=get_connection,
    )

    t1 >> t2