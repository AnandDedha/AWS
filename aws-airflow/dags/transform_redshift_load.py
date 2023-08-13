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

dag = DAG('s3_to_redshift_dag', default_args=default_args, schedule_interval=timedelta(hours=1))


# Define the Glue Job
transform_task = GlueJobOperator(
    task_id='transform_task',
    job_name='your_glue_job_name',
    script_location='s3://datatech-glue-scripts/your-glue-script.py',
    aws_conn_id='AWS_CONN',  # You'll need to set up an AWS connection in Airflow
    region_name='your_aws_region',
    num_of_dpus=2,
    dag=dag,
)

# Define the S3 to Redshift transfer
s3_to_redshift_task = S3ToRedshiftOperator(
    task_id='s3_to_redshift',
    schema='public',
    table='your_redshift_table_name',
    copy_options=["CSV"],
    schema_mapping=["column_name_1:VARCHAR", "column_name_2:INTEGER"],  # Define column mapping
    s3_bucket='your_s3_bucket',
    s3_key='your_s3_key',
    aws_conn_id='AWS_CONN',  # You'll need to set up an AWS connection in Airflow
    redshift_conn_id='redshift_default',  # You'll need to set up a Redshift connection in Airflow
    dag=dag,
)



# Set task dependencies
transform_task >> s3_to_redshift_task 
