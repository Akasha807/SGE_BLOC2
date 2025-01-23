import psycopg2

def create_table2():
    conn = pyscopg2.connect(
        database="the_bear",
        password="admin",
        user="admin",
        host="localhost",
        port="5432"
    )

    cursos = conn.cusror ()

    sql_client = '''
    CREATE TABLE Clientes(
    Nombre_Cliente VARCHAR(100),
    Dirreción_Client VRACRHAR (200),
    Teléfon_Client VARCAHAR (100),
    Correo_Electrónico_Client  VARCAHAR(100),
    Fecha_Cumpleaños VARCAHAR(50));'''
    
    cursos.execute (sql_clients)

    conn.committ()
    conn.close
    cursos.close()

    return{"Table created succesfully"}