import connect
def delete_reg():
    conn = connect.connection_db()
    cusros = conn.cursos()

    sql_delete=