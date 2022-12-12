# DROP TABLES
# actualy cascade no need to use if drop sql queries order is correct
pets_table_drop = "DROP TABLE IF EXISTS pets;"
owners_table_drop = "DROP TABLE IF EXISTS owners CASCADE;"
phistory_table_drop = "DROP TABLE IF EXISTS phistory CASCADE;"
pdetail_table_drop = "DROP TABLE IF EXISTS pdetail CASCADE;"


# CREATE TABLES

owners_table_create = ("""CREATE TABLE IF NOT EXISTS owners 
 (
    OwnerID text 
    ,Name text
    ,Surname text
    ,StreetAddress text
    ,City text
    ,State text
    ,StateFull text
    ,ZipCode text
    PRIMARY KEY (OwnerID)
    
);
""")

phistory_table_create = ("""CREATE TABLE IF NOT EXISTS phistory 
 (
    PetID text
    ,Date text
    ,ProcedureType text
    ,ProcedureSubcode 
    PRIMARY KEY (PetID)
    
);
""")

pdetail_table_create = ("""CREATE TABLE IF NOT EXISTS pdetail 
 (
    ProcedureType text
    ,ProcedureSubcode text
    ,Description text
    ,Price text 
    PRIMARY KEY (ProcedureType)
);
""")

pets_table_create = ("""CREATE TABLE IF NOT EXISTS pets
 (
    --id INT NOT NULL AUTO_INCREMENT,
    PetID text 
    ,Kind text
    ,Gender text
    ,Age text
    ,OwnerID text    
    PRIMARY KEY (PetID),
    --CONSTRAINT FK_petowner FOREIGN KEY (OwnerID) REFERENCES owners(OwnerID),
    --CONSTRAINT FK_petprocedure KEY (PetID) REFERENCES phistory(PetID),
    --CONSTRAINT FK_payload_push_event FOREIGN KEY (payload_push_id) REFERENCES dim_payload_push(push_id),
    --CONSTRAINT FK_org_event FOREIGN KEY (org_id) REFERENCES dim_org(org_id)
);

 """)




# INSERT RECORDS
# COPY s3 to Redshift

dim_actor_table_insert = ("""INSERT INTO dim_actor
 ( actor_id ,actor_login , actor_display_login , actor_gravatar_id , actor_url ,actor_avatar_url )
 VALUES (%s, %s, %s, %s, %s, %s)
 ON CONFLICT (actor_id) DO NOTHING;
""")

dim_repo_table_insert = ("""INSERT INTO dim_repo
 ( repo_id ,repo_name , repo_url )
 VALUES (%s, %s, %s)
 ON CONFLICT (repo_id) DO NOTHING;
""")


dim_payload_push_table_insert = ("""INSERT INTO dim_payload_push 
 (  push_id ,    size,     distinct_size ,    ref ,    head ,  before_code ,    commits  )
 VALUES (%s, %s, %s, %s, %s, %s, %s)
 ON CONFLICT (push_id) DO NOTHING;
""")

dim_org_table_insert = ("""INSERT INTO dim_org 
 (    org_id ,    org_login ,    org_gravatar_id ,    org_url ,    org_avatar_url     )
 VALUES (%s, %s, %s, %s, %s)
 ON CONFLICT (org_id) DO NOTHING;
""")

fact_event_table_insert = ("""INSERT INTO fact_event
 (event_id , event_type, actor_id,  repo_id,   payload_action, payload_push_id,  pulic,  create_at,   org_id,  event_time )
 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
 ON CONFLICT (event_id) DO NOTHING;
 """)




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
    ,pdetail_push_table_drop    
    ]
