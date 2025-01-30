import psycopg2

from bloc2_AkashaKaram.connect import connect


def update_reg():
    conn = connect.connection_db()
    cursos = conn.cursor()

    sql_update ='''
    UPDATE clientes
    SET teléfon_cliente=000000
    WHERE id_client = 1
    '''
    cursos.execute (sql_update)
    conn.commit()

    cursos.close()
    conn.close()

    resturn{"Update succesfully"}