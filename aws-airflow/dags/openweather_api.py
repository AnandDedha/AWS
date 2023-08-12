from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.http_operator import SimpleHttpOperator
from airflow.sensors.http_sensor import HttpSensor
from airflow.models import Variable
from datetime import datetime, timedelta
import json

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 8, 12),
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG('openweather_api_dag', default_args=default_args, schedule_interval="@once",catchup=False)

 # Set your OpenWeather API endpoint and parameters
api_endpoint = "https://api.openweathermap.org/data/2.5/weather"
appid = Variable.get("api_key")
city_country = "Toronto,Canada"
api_params = {
        "q": "Toronto,Canada",
        "appid": Variable.get("api_key")
    }

def extract_openweather_data(**kwargs):

    response = SimpleHttpOperator(
        task_id='extract_data',
        http_conn_id='http_weatherapi',  # You'll need to set up an HTTP connection in Airflow
        endpoint=api_endpoint,
        method='GET',
        data=json.dumps(api_params),
        response_check=lambda response: True if response.status_code == 200 else False,
        dag=dag,
    )
    response.execute(kwargs)

def process_openweather_data(**kwargs):
    response = kwargs['task_instance'].xcom_pull(task_ids='extract_data')
    data = json.loads(response.text)
    # Process the data as needed
    print(data)

# Define the tasks
is_api_ready = HttpSensor(
    task_id='check_api_data',
    http_conn_id='http_weatherapi',
    endpoint= f'{api_endpoint}?q={city_country}&appid={appid}'
    response_check=lambda response: True if response.status_code == 200 else False,
    dag=dag,
)

extract_data_task = PythonOperator(
    task_id='process_data',
    python_callable=process_openweather_data,
    provide_context=True,
    dag=dag,
)

# Set task dependencies
is_api_ready >> extract_data_task >> upload_to_s3_task
