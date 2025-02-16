import connect
def read_reg():
   conn = connect.connection_db()
   cursor = conn.cursor()

   sql_read = "SELECT * FROM Clientes"

   cursor.execute(sql_read)
   conn.commit()

   results = cursor.fetchall()
   print(results)
   print(results[4],[5])
