from airflow import DAG
from airflow.providers.amazon.aws.transfers.s3_to_redshift import S3ToRedshiftOperator
from airflow.providers.amazon.aws.transfers.gluejob import GlueJobOperator
from airflow.providers.postgres.transfers.s3_to_postgres import S3ToPostgresOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 8, 12),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG('transform_redshift_dag', default_args=default_args, schedule_interval="@once",catchup=False)


# Define the Glue Job
transform_task = GlueJobOperator(
    task_id='transform_task',
    job_name='glue_transform_task',
    script_location='s3://DatatechGlueScripts/transform.py',
    aws_conn_id='AWS_CONN',  # You'll need to set up an AWS connection in Airflow
    region_name="us-east-1",
    iam_role_name='GlueS3',
    num_of_dpus=4,
    dag=dag,
)

# Define the S3 to Redshift transfer
s3_to_redshift_task = S3ToRedshiftOperator(
    task_id='s3_to_redshift',
    schema='public',
    table='weather_data',
    copy_options=["CSV"],
    s3_bucket='s3://airflowoutputtos3bucket',
    s3_key='transformed/run-1691970615954-part-r-00000',
    aws_conn_id='AWS_CONN',  # You'll need to set up an AWS connection in Airflow
    redshift_conn_id='redshift_default',  # You'll need to set up a Redshift connection in Airflow
    dag=dag,
)



# Set task dependencies
transform_task >> s3_to_redshift_task 
