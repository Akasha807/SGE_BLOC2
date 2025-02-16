import connect


#Funció per crear un registre a la DB amb una consulta preparada
def create_reg():


   #Crear la connexió i guardar-la a la variable conn
   conn = connect.connection_db()


   #Crear un cursor amb la connexió guardada a la variable conn
   cursor = conn.cursor()


   #Consulta preparada amb %s
   sql_create = "INSERT INTO Clientes (name, address, phone, email, birthdate) VALUES (%s, %s, %s, %s, %s);"


   #Valors a afegir, en ordre, als %s de VALUES de la consulta preparada
   values = ('Roger', 'carrer el que sigui', '678113452', 'correu@correu.com', '1999-09-12')


   #Enviar la consulta preparada amb els valors utilitzant el cursor
   cursor.execute(sql_create, values)
   #Fer les modificacions a la DB segons execute()
   conn.commit()


   #Tancar connexió
   conn.close()
   cursor.close()
