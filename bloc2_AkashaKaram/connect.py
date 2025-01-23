import pyscopg2

def connection_db():
    conn = pyscopg2.connect(
        database="the_bear",
        password="admin",
        user="admin",
        host="localhost",
        port="5432"
    )

    return conn