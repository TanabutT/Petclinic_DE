# DROP TABLES
# actualy cascade no need to use if drop sql queries order is correct
pets_table_drop = "DROP TABLE IF EXISTS pets;"
owners_table_drop = "DROP TABLE IF EXISTS owners CASCADE;"
phistory_table_drop = "DROP TABLE IF EXISTS phistory CASCADE;"
pdetail_table_drop = "DROP TABLE IF EXISTS pdetail CASCADE;"


# CREATE TABLES
owners_table_create = """CREATE TABLE IF NOT EXISTS owners( 
     OwnerID text 
    ,Name text
    ,Surname text
    ,StreetAddress text
    ,City text
    ,State text
    ,StateFull text
    ,ZipCode text      
);
"""

phistory_table_create = """CREATE TABLE IF NOT EXISTS phistory 
 (
    PetID text
    ,Date text
    ,ProcedureType text
    ,ProcedureSubcode 
    --PRIMARY KEY (PetID)
    
);
"""

pdetail_table_create = """CREATE TABLE IF NOT EXISTS pdetail 
 (
    ProcedureType text
    ,ProcedureSubcode text
    ,Description text
    ,Price text 
    --PRIMARY KEY (ProcedureType)
);
"""

pets_table_create = """CREATE TABLE IF NOT EXISTS pets
 (
    --id INT NOT NULL AUTO_INCREMENT,
    PetID text 
    ,Kind text
    ,Gender text
    ,Age text
    ,OwnerID text    
    --PRIMARY KEY (PetID),
    --CONSTRAINT FK_petowner FOREIGN KEY (OwnerID) REFERENCES owners(OwnerID),
    --CONSTRAINT FK_petprocedure KEY (PetID) REFERENCES phistory(PetID),
    --CONSTRAINT FK_payload_push_event FOREIGN KEY (payload_push_id) REFERENCES dim_payload_push(push_id),
    --CONSTRAINT FK_org_event FOREIGN KEY (org_id) REFERENCES dim_org(org_id)
);

 """




# INSERT RECORDS
# COPY s3 to Redshift

load_owners = """COPY owners FROM 's3://petclinic13/cleaned_zone_parquet/owners.parquet'
	ACCESS_KEY_ID %s
	SECRET_ACCESS_KEY %s
	SESSION_TOKEN %s
	FORMAT AS PARQUET""" % 
    (to_table, fn, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY,delim,quote,gzip)

load_phistory = """COPY owners FROM 's3://petclinic13/cleaned_zone_parquet/phistory.parquet'
	ACCESS_KEY_ID 'ASIAWFHJWX4C3O7Q3XUN'
	SECRET_ACCESS_KEY 'LHZZoi1t0LJoaZi63AuI8M5QOH1W7iIA91fUYMVJ'
	SESSION_TOKEN 'FwoGZXIvYXdzEIf//////////wEaDG1vwZ1r98xuxNWgPCLHAXdjUF71mhOaSvNdw/EzrQ1w4ycoeSJfZc+RxYz3PVs+x3WweTxohAwTye4mke8jaVeK4g5uqYLiZlvoLCZjD1bhxUG21ELgedKHf9rQm8qKtxNE7+9dRhfltsbpCV9flZqUKJkvke/pAbHcOfltjWeWD1QTatqZiumG0KiV2Zo+vlqlAHmbZ/r2onyTG1sx5j4iW6eYTd4TS716vUkGgYuV3l8NJqskMe/oXgvYp/tEQoa+R7sVvEkgF5pSQ5gaks7yyZ34Wzgo8oHbnAYyLYQai0cuwdE2SMvXcPGFfjtlSHFjuyWqPzfruZGgiiWR9jkX4Ro76IQbYeqY8Q=='
	FORMAT AS PARQUET"""

load_pdetail = """COPY owners FROM 's3://petclinic13/cleaned_zone_parquet/pdetail.parquet'
	ACCESS_KEY_ID 'ASIAWFHJWX4C3O7Q3XUN'
	SECRET_ACCESS_KEY 'LHZZoi1t0LJoaZi63AuI8M5QOH1W7iIA91fUYMVJ'
	SESSION_TOKEN 'FwoGZXIvYXdzEIf//////////wEaDG1vwZ1r98xuxNWgPCLHAXdjUF71mhOaSvNdw/EzrQ1w4ycoeSJfZc+RxYz3PVs+x3WweTxohAwTye4mke8jaVeK4g5uqYLiZlvoLCZjD1bhxUG21ELgedKHf9rQm8qKtxNE7+9dRhfltsbpCV9flZqUKJkvke/pAbHcOfltjWeWD1QTatqZiumG0KiV2Zo+vlqlAHmbZ/r2onyTG1sx5j4iW6eYTd4TS716vUkGgYuV3l8NJqskMe/oXgvYp/tEQoa+R7sVvEkgF5pSQ5gaks7yyZ34Wzgo8oHbnAYyLYQai0cuwdE2SMvXcPGFfjtlSHFjuyWqPzfruZGgiiWR9jkX4Ro76IQbYeqY8Q=='
	FORMAT AS PARQUET"""

load_pets = """COPY owners FROM 's3://petclinic13/cleaned_zone_parquet/pets.parquet'
	ACCESS_KEY_ID 'ASIAWFHJWX4C3O7Q3XUN'
	SECRET_ACCESS_KEY 'LHZZoi1t0LJoaZi63AuI8M5QOH1W7iIA91fUYMVJ'
	SESSION_TOKEN 'FwoGZXIvYXdzEIf//////////wEaDG1vwZ1r98xuxNWgPCLHAXdjUF71mhOaSvNdw/EzrQ1w4ycoeSJfZc+RxYz3PVs+x3WweTxohAwTye4mke8jaVeK4g5uqYLiZlvoLCZjD1bhxUG21ELgedKHf9rQm8qKtxNE7+9dRhfltsbpCV9flZqUKJkvke/pAbHcOfltjWeWD1QTatqZiumG0KiV2Zo+vlqlAHmbZ/r2onyTG1sx5j4iW6eYTd4TS716vUkGgYuV3l8NJqskMe/oXgvYp/tEQoa+R7sVvEkgF5pSQ5gaks7yyZ34Wzgo8oHbnAYyLYQai0cuwdE2SMvXcPGFfjtlSHFjuyWqPzfruZGgiiWR9jkX4Ro76IQbYeqY8Q=='
	FORMAT AS PARQUET"""

# QUERY LISTS

create_table_queries = [     
    owners_table_create
    ,phistory_table_create
    ,pdetail_table_create
    ,pets_table_create
    ]
    # order in drop table should drop fact first all constrain will free and no need to use casecade
drop_table_queries = [
    pets_table_drop
    ,owners_table_drop
    ,phistory_table_drop 
    ,pdetail_table_drop    
    ]
