import psycopg2
import boto3
# separate sql queries in another file
# import the sql queries below:
from sql_queries import *
from settings_dags import cluster_user, cluster_password

def _create_tables_process(**context):

    # print("try connect to postgresdb")

    def drop_tables(cur, conn) -> None:
        """
        Drops each table using the queries in `drop_table_queries` list.
        """
        for query in drop_table_queries:
            cur.execute(query)
            conn.commit()


    def create_tables(cur, conn) -> None:
        """
        Creates each table using the queries in `create_table_queries` list.
        """
        for query in create_table_queries:
            cur.execute(query)
            conn.commit()


    def loadinto_tables(cur, conn) -> None:
        """
        Creates each table using the queries in `create_table_queries` list.
        """
        for query in loadinto_table_queries:
            cur.execute(query)
            conn.commit()



    # def main():
        """
        - Drops (if exists) and Creates the sparkify database.
        - Establishes connection with the sparkify database and gets
        cursor to it.
        - Drops all the tables.
        - Creates all tables needed.
        - Finally, closes the connection.
        """
    redshift = boto3.client('redshift',

                        region_name='us-east-1',
                        aws_access_key_id=aws_access_key_id,
                        aws_secret_access_key=aws_secret_access_key,
                        aws_session_token=aws_session_token)
    
    ti = context["ti"]
    # Get list of files from filepath
    ClusterEndpoint = ti.xcom_pull(task_ids="describe_cluster", key="return_value")
    print("ClusterEndpoint to  fill in response: ", ClusterEndpoint)
    """ClusterEndpoint will return "endpoint" after cluster was created"""
    
    conn = psycopg2.connect(
        # host="redshift-cluster-petclinic.cnrhltyzddie.us-east-1.redshift.amazonaws.com",
        host=ClusterEndpoint,
        port=5439,
        database="petclinic",
        user=cluster_user,
        password=cluster_password)        
    
    cur = conn.cursor()

    drop_tables(cur, conn)
    create_tables(cur, conn)
    # loadinto_tables(cur, conn)

    conn.close()
    print("connection close")


# if __name__ == "__main__":
#     main()