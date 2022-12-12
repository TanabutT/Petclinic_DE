import redshift_connector
# separate sql queries in another file
# import the sql queries below:
from sql_queries import *
from settings import cluster_user, cluster_password

conn = redshift_connector.connect(
        host="redshift-cluster-petclinic.cnrhltyzddie.us-east-1.redshift.amazonaws.com",
        port=5439,
        database="petclinic",
        user=cluster_user,
        password=cluster_password)    

sql="""CREATE TABLE IF NOT EXISTS owners12345
( 
     OwnerID text primary key
    ,Name text    
);
"""

sql1 = "select * from phistory limit 10;"

cur = conn.cursor()
cur.execute(sql1)
result: tuple = cur.fetchall()
print(result)
conn.close() 

# cur = conn.cursor()
# cur.execute(sql)
# conn.commit()


