
# Capstone Project Data Engineer

## Getting Started linux
ENV is name of virtual environment can name up to user 
example CUTECAT then 
source CUTECAT/bin/active
```sh
python -m venv ENV
source ENV/bin/activate
pip install -r requirements.txt
```

### create AWS S3

* go to aws console - S3 
* create bucket
  - make sure - [x] **Block all public access** 
  - keep - [x] Disable for Bucket Versioning
  - create bucket

### connect  AWS S3 with boto3
การที่เราจะเชื่อมต่อไปยัง Amazon S3 เราจำเป็นต้องมี AWS Access Key ID และ AWS Secret Access Key ก่อน และถ้าเป็นการเชื่อมต่อแบบ temporary เราจะต้องใช้ AWS Session Token อีกค่าหนึ่งด้วย

การที่เราจะได้มาทั้ง 3 ค่านั้น สามารถทำได้โดยไปที่ AWS Learner Lab ของคอร์สนี้ และที่ Terminal ให้เราพิมพ์คำสั่ง 
```sh 
cat ~/.aws/credentials
```
 ลงไป เราจะได้ค่าทั้ง 3 ค่าที่เราต้องการมา 
 * cuation! ค่า สามค่านี้ เปลี่ยนทุกๆ กี่ชั่วโมงไม่ทราบแน่ชัดเช็คจาก AWS cli เมื่อ connect ไม่ได้ 

### upload csv files to bucket
* create directory in bucket for csv files in "Petclinic_landing" directory 
  - Pets
  - Owners
  - ProcedureDetails
  - ProcedureHistory

### Use Spark to transform csv to data and write (save) to new transfromed file
* cd เข้าไปที่ folder resource ก่อน
* EDA if use gitpod run this command to allow permission to create file in workspace
    เพื่อให้เราสามารถสร้างไฟล์ได้จาก Jupyter Lab ให้รันคำสั่งด้านล่างนี้

    ```sh
    sudo chmod 777 .
    ```
    แล้วค่อยรัน

```sh
docker-compose up
```
เข้าไปดู การ transformation data in ipynb notebook ที่ ไฟล์ [Petcliniccleaning](./resource/Petcliniccleaning.ipynb)
ใน pipeline ทั้งหมดจะไปทำใน ไฟล์ [s3_transform_with_spark.py](./s3_transform_with_spark.py) แทน

ก่อนทำการ read_csv การใช้ path ชี้ไปที่ s3 ต้องใช้ แบบนี้ มีตัว "a" หลัง s3  เช่น "s3a://petclinic13/PetClinic_landing/P9-Pets.csv"
* Join table or just clean ค่อยใช้ dbt ครอบแล้วjoin sql เอาจะได้เห็น lineage graph
* get rid some field (column)
* save to .parquet file in S3 in "Petclinic_cleaned" directory
* use with Redshift or dbt later

note: Airflow from upload csv to s3, read csv and transform with spark-save new file to s3, redshift มาดึงไปไงดี?  แล้วเอา dbt ครอบตรงการทำ analytic จากโจทย์ เก็บ พวก sql querry









## create Redshift cluster
ใช้ boto3.client('redshift').create_cluster(**kwargs) สร้าง Redshift cluster
ดูได้ที่ ไฟล์ [create_Reshift.py](./create_Redshift.py)  

* หาค่า VpcSecurityGroupIds=["sg-0451e739676e3d587"] ได้ที่  
หา VPC security groups โดยไปที่ aws console at https://console.aws.amazon.com/redshift/.
ไปที่หน้า create cluster ลงมาที่ Additional configurations เข้าไปเปิดดู Network and security และดูที่ ค่า  VPC security groups แล้วนำมาใส่
* หาค่า ClusterParameterGroupName='default.redshift-1.0' ได้ที่  
ไปที่ aws console at https://console.aws.amazon.com/redshift/.
On the navigation menu, choose Configurations, then choose Workload management to display the Workload management page. ดูชื่อ Parameter group ที่ต้องการใช้ ถ้าไม่มีก็สร้างใหม่
* หาค่า ClusterSubnetGroupName='default' ได้ที่  
ไปที่ aws console at https://console.aws.amazon.com/redshift/.
On the navigation menu, choose Configurations, then choose subnet groups to display the Cluster subnet groups. ดูชื่อ Cluster subnet groups ที่ต้องการใช้ 


## create table in Redshift
full sql_query in [sql_qureires](./sql_queries.py)  

example
drop table 
```sh
drop table owners cascade;
```
Create table owners
```sh
CREATE TABLE IF NOT EXISTS owners (
  OwnerID text primary key
  ,Name text
  ,Surname text
  ,StreetAddress text
  ,City text
  ,State text
  ,StateFull text
  ,ZipCode text
  )
```
load owner table with COPY command in aws via boto3 connect using pycopg2 or redshift_connector? csv file
```sh
COPY owners FROM 's3://v/P9-Owners.csv'
	ACCESS_KEY_ID ''
	SECRET_ACCESS_KEY ''
	SESSION_TOKEN ''
	CSV
	REGION ''
```

load owner table with COPY command in aws via boto3 connect using pycopg2 or redshift_connector? parquet file
```sh
COPY owners FROM 's3://v/owners.parquet'
	ACCESS_KEY_ID ''
	SECRET_ACCESS_KEY ''
	SESSION_TOKEN ''
	FORMAT AS PARQUET
```





![AWS Redshift query console](resource/redshift_jsonpaht0.jpg)

## insert data from json with json_path

```sh
copy github_event
from 's3://tanabruce-bucket06092022/github_events_01.json'
iam_role 'arn:aws:iam::423544405765:role/LabRole' 
json 's3://tanabruce-bucket06092022/events_json_path.json';
```

To show data in table github_event:

```sh
select * from github_event
```
see the result in 
[github_event_query_result.csv](github_event_query_result.csv)

example result
| event_id	  |   event_type      |actor_login  |	repo_name	                    | created_at           |
| :---        |   :---            |:---:        |:---:                          | ---:                 |
|23487929637  |	IssueCommentEvent	|  sukhada	  |350org/ak_intl_v3	            | 2022-08-17T15:51:05Z |
|23487929676	|PushEvent	        |  yousabu	  |yousabu/ansible_rhce	          | 2022-08-17T15:51:05Z |
|23487929674	|PushEvent	        |  MathisGD	  |morpho-dao/morpho-utils        |	2022-08-17T15:51:05Z |
|23487929661	|PushEvent	        |  BR-Junior	|BR-Junior/crud-com-vue-e-quasar|2022-08-17T15:51:05Z  |

To close all service
- S3 empty bucket
- Delete S3 bucket
- Delete Redshift cluster** with out keeping snapshot** - [ ] snap shot 





## watch cost explorer

![cost](resource/redshift_cost1.jpg)