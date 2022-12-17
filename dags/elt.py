from typing import List
import os
import glob
import json
# from sql_queries import *
from _get_files import _get_files
from _con_upload_to_s3 import _con_upload_to_s3
from _s3_transform_with_spark import _s3_transform_with_spark
from _create_Redshift import _create_Redshift
from _create_tables import _create_tables_process
from _read_bucket_landing_transform_to_cleaned_parquet import _read_bucket_landing_transform_to_cleaned_parquet

from airflow import DAG
from airflow.utils import timezone
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.providers.amazon.aws.sensors.redshift_cluster import RedshiftClusterSensor

with DAG (
    "elt",
    start_date=timezone.datetime(2022, 12, 16),
    schedule="@daily", # use cron " * * * * *"
    tags=["workshop"],
    catchup=False,
) as dag:

    get_files = PythonOperator(
        task_id="get_files",
        python_callable=_get_files,
        op_kwargs={
            "filepath" : "/opt/airflow/dags/data",
        }
    )

    create_Redshift = PythonOperator(
        task_id="create_Redshift",
        python_callable=_create_Redshift,
        
    )
  
    con_upload_to_s3 = PythonOperator(
        task_id="con_upload_to_s3",
        python_callable=_con_upload_to_s3,
    )

    read_transform_parquet = PythonOperator(
        task_id="read_bucket_landing_transform_to_cleaned_parquet",
        python_callable=_read_bucket_landing_transform_to_cleaned_parquet,
    )

    # s3_transform_with_spark = PythonOperator(
    #     task_id="s3_transform_with_spark",
    #     python_callable=_s3_transform_with_spark,
    #     op_kwargs={
    #         "filepath" : "/opt/airflow/dags/data",
    #     }
    # ) 
    cluster_sensor = RedshiftClusterSensor(
        task_id='wait_for_cluster',
        cluster_identifier='redshift-cluster-petclinic',
        target_status='available',
        aws_conn_id='redshift_petclinic' # input connections at admin section in airflow ui and put here
    )

    process_table = PythonOperator(
        task_id="process_table",
        python_callable=_create_tables_process,
       
    )

    
    

    # get_files >> con_upload_to_s3 >> create_Redshift >> cluster_sensor >> process_table
    # get_files >> con_upload_to_s3 >> cluster_sensor


    #xcom respond cluster to cluster_sensor and process_table to use endpoint and clustername
    # create_Redshift >> get_files >> con_upload_to_s3 >> read_transform_parquet >> cluster_sensor >> process_table
    
    create_Redshift >> cluster_sensor >> process_table
    get_files >> con_upload_to_s3 >> read_transform_parquet >> cluster_sensor >> process_table