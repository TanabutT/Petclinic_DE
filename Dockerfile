FROM apache/airflow:2.4.1

RUN pip install s3fs
# use  $ docker build . --tag extending_airflow 