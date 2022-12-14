import psycopg2
# separate sql queries in another file
# import the sql queries below:
from sql_queries import *
from settings import cluster_user, cluster_password

print("try connect to postgresdb")

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



def main():
    """
    - Drops (if exists) and Creates the sparkify database.
    - Establishes connection with the sparkify database and gets
    cursor to it.
    - Drops all the tables.
    - Creates all tables needed.
    - Finally, closes the connection.
    """
    conn = psycopg2.connect(
        host="redshift-cluster-petclinic.cnrhltyzddie.us-east-1.redshift.amazonaws.com",
        port=5439,
        database="petclinic",
        user=cluster_user,
        password=cluster_password)        
    
    cur = conn.cursor()

    drop_tables(cur, conn)
    create_tables(cur, conn)
    loadinto_tables(cur, conn)

    conn.close()
    print("connection close")


if __name__ == "__main__":
    main()