import connect
def read_reg():
   conn = connect.connection_db()
   cursor = conn.cursor()

   sql_read = "SELECT * FROM clientes2"

   cursor.execute(sql_read)
   conn.commit()

   results = cursor.fetchall()
   print(results)