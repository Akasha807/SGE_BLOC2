import psycopg2

def send_data_to_db(pos, data):
    print(data)
    conn = psycopg2.connect(
        database ="The_bear",
        password="admin",
        user="admin",
        hosts="localhost"
        port="5432"
    )

    cur = conn.cursor()
    sql = "INSERT INTO Clientes (nombre_cliente, dirección_cliente, teléfono_cliente, correo_electrónico_cliente, fecha_cumpleaños")VALUES (%s, %s, %s, %s, %s);"

    values = (data["Nombre_Clientes"][pos],[data],["Dirreción_Clientes"][pos], data["Teléfon_Cliente"][pos], data[Correo_Electrónico_Cliente][pos], data["fecha_Cumpleaños"][pos])

    cur.execute(sql, value)
    conn.commit()

    cur.close()
    conn.close()

    return{"Messatge:"Data inserted"}
