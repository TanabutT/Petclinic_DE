
# Capstone Project Data Engineer

## Getting Started

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
* EDA if use gitpod run this command to allow permission to create file in workspace
    เพื่อให้เราสามารถสร้างไฟล์ได้จาก Jupyter Lab ให้รันคำสั่งด้านล่างนี้

    ```sh
    sudo chmod 777 .
    ```
    แล้วค่อยรัน

```sh
docker-compose up
```
ก่อนทำการ read_csv การใช้ path ชี้ไปที่ s3 ต้องใช้ แบบนี้ มีตัว "a" หลัง s3  เช่น "s3a://petclinic13/PetClinic_landing/P9-Pets.csv"
* Join table or just clean ค่อยใช้ dbt ครอบแล้วjoin sql เอาจะได้เห็น lineage graph
* get rid some field (column)
* save to .parquet file in S3 in "Petclinic_cleaned" directory
* use with Redshift or dbt later

note: Airflow from upload csv to s3, read csv and transform with spark-save new file to s3, redshift มาดึงไปไงดี?  แล้วเอา dbt ครอบตรงการทำ analytic จากโจทย์ เก็บ พวก sql querry




## create table in Redshift
```sh
drop table owners cascade;
```

```sh
CREATE TABLE IF NOT EXISTS owners (
  OwnerID text primary
  ,Name text
  ,Surname text
  ,StreetAddress text
  ,City text
  ,State text
  ,StateFull text
  ,ZipCode text
  )
```

```sh
COPY owners FROM 's3://v/P9-Owners.csv'
	ACCESS_KEY_ID ''
	SECRET_ACCESS_KEY ''
	SESSION_TOKEN ''
	CSV
	REGION ''
```

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