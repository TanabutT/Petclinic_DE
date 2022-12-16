from typing import List
import os
import glob
import json
# from sql_queries import *
from _get_files import _get_files
from _con_upload_to_s3 import _con_upload_to_s3
from _s3_transform_with_spark import _s3_transform_with_spark

from airflow import DAG
from airflow.utils import timezone
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook

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
  
    con_upload_to_s3 = PythonOperator(
        task_id="con_upload_to_s3",
        python_callable=_con_upload_to_s3,
    )

    s3_transform_with_spark = PythonOperator(
        task_id="s3_transform_with_spark",
        python_callable=_s3_transform_with_spark,
    ) 

     #create_Redshift first 
    get_files >> con_upload_to_s3 >> _s3_transform_with_spark

    #create_Redshift >> sleep for 5 min >> create_table 