# -SGE_BLOC2
# Introducción
Este documento guía la configuración de un entorno de desarrollo con Docker, PyCharm y PostgreSQL, permitiendo gestionar bases de datos de manera eficiente. Se explican los pasos para instalar Docker, configurar PyCharm con el plugin de Docker, ejecutar un docker-compose.yml con PostgreSQL y pgAdmin, conectar Python con la base de datos mediante psycopg2, trabajar con archivos CSV para insertar datos y realizar operaciones CRUD (create, read, update, delete).

Antes de empezar, debemos elegir qué sistema operativo vamos a usar, ya que cada uno requiere una versión diferente de Docker.
- En Windows, se utiliza Docker Desktop, el cual debe activarse cada vez que le damos uso.
- En Linux, se usa Docker Engine.

Podemos descargar Docker desde su página oficial. Nos será útil, ya que nos permite crear y gestionar contenedores, que son entornos aislados donde podemos ejecutar aplicaciones sin preocuparnos por las diferencias entre sistemas operativos.

![image](https://github.com/user-attachments/assets/734634e7-3f77-4dd4-89ad-bb05a68cab20)

Una vez que Docker está instalado y funcionando, procedemos a instalar PyCharm, un entorno de desarrollo integrado (IDE) para Python.

![image](https://github.com/user-attachments/assets/ed72d987-5dd8-49db-b556-6cff646cd1cd)

Después de instalar PyCharm, lo primero que debemos comprobar es que tengamos la versión 13.10. En caso de que tengamos otra versión, podemos cambiarla desde la configuración.

![image](https://github.com/user-attachments/assets/0bfcec37-f4cb-49b2-b5d8-12cdbc45ab8a)

Luego, desde allí mismo nos instalamos el plugin de Docker, que nos permitirá conectarnos a Docker desde PyCharm y gestionar contenedores.

![image](https://github.com/user-attachments/assets/1a4bccac-2f06-46e6-bc07-7451d4e2c7f3)

El archivo `docker-compose.yml` contiene lo siguiente:

![3](https://github.com/user-attachments/assets/578f07d1-cafa-4f48-a94f-e512670b7b76)

- **db**: Un contenedor que ejecuta PostgreSQL con un usuario, una contraseña y una base de datos preconfigurados.
- **pgAdmin**: Una interfaz web para gestionar PostgreSQL, accesible desde el navegador en el puerto 80.

En PyCharm, ejecutamos el archivo `docker-compose.yml`, asegurándonos de que Docker Desktop está activo. Para ello, utilizamos el siguiente comando en la terminal:

![1](https://github.com/user-attachments/assets/f14eb01c-8277-49af-af65-74e99a6b7ebc)

Luego, en la terminal, accedemos a http://localhost:80 en el navegador y nos registramos con el usuario y la contraseña por defecto, que están en el archivo `docker-compose.yml`, para ingresar a pgAdmin 4.

![image](https://github.com/user-attachments/assets/2a0716a7-3082-4fe8-b896-828ccb30551c)

Allí creamos un servicio de base de datos con un nombre personalizado.

![image](https://github.com/user-attachments/assets/3962075c-99b9-49f1-81cd-cfad964a1fe4)

En la sección **Connection**, ingresamos los siguientes datos:

![image](https://github.com/user-attachments/assets/a9330aab-ef11-40ba-af9a-6b5bd0f830fe)

Con esto, el contenedor se llama `db_erp` y utiliza el usuario `admin` y la contraseña `admin` para entrar en el servidor.

Creamos la carpeta `bloc2_NOMALUMNX` en PyCharm Community. Dentro de esta carpeta, creamos otra carpeta llamada `postgresql_python`. Dentro de esta carpeta, creamos los siguientes archivos:

### **connect.py**

![image](https://github.com/user-attachments/assets/8384095b-4b2c-496e-bdca-489abf41b1b6)

Este código sirve para establecer la conexión con la base de datos y poder realizar las operaciones CRUD (Create, Read, Update y Delete) en una tabla de PostgreSQL.

Los datos que se utilizan en la conexión:
- **Base de datos**: the_bear
- **Usuario**: admin
- **Contraseña**: admin
- **Host**: localhost
- **Puerto**: 5432

Estos datos se extraen del archivo `docker-compose.yml` creado en la configuración de Docker. Además, imprime el objeto de conexión indicando que está abierta (`closed: 0`), luego la cierra con `connect.close()` y vuelve a imprimir el objeto, ahora indicando que está cerrada (`closed: 1`).

Luego, en PyCharm, instalamos los plugins. `psycopg2` es una librería para conectar Python con PostgreSQL, y `pandas` nos permite trabajar con datos en formato de tabla. Además, descargamos el archivo de clientes en formato `.csv` y lo añadimos en una carpeta con el nombre `send_data_to_db` que estará dentro de la carpeta `bloc2`.

Dentro de `send_data_to_db` creamos los siguientes archivos:

### **create_table_to_db.py**

![image](https://github.com/user-attachments/assets/ebae9996-4abf-494d-90e7-3bb6d4a324ec)

Se encargará de leer el archivo `.csv` para determinar los nombres y tipos de columnas y luego crear una tabla en la base de datos PostgreSQL con esos campos.

### **csv_to_dict.py**

![image](https://github.com/user-attachments/assets/05362e47-38b4-4b28-86e0-86e6a6715db4)

Transformará el archivo `.csv` en una lista de diccionarios. Cada fila será un diccionario donde las claves son los nombres de las columnas y los valores los datos correspondientes.

### **dict_to_db.py**

![image](https://github.com/user-attachments/assets/dad241b0-7611-42aa-9eed-f9c0291912e8)

### **create_register.py**

![image](https://github.com/user-attachments/assets/4135f0b1-f0d4-464d-bcc8-547f7cdde8e7)

### **main.py**

![image](https://github.com/user-attachments/assets/5710dbbe-f56f-4579-a287-22562a08ceb2)

Para comprobar que los datos se han añadido, debemos ir a **pgAdmin4**, refrescar la tabla de clientes y ejecutarla para que se muestren los datos introducidos.

![image](https://github.com/user-attachments/assets/23373626-0c1e-457e-9d6a-55800ff1e907)

Visualizamos en pantalla los detalles de cada cliente, incluyendo su nombre, dirección, teléfono, correo electrónico y fecha de nacimiento.

![totoCliente](https://github.com/user-attachments/assets/58559825-6f11-461d-a3e4-aa788e69eeaa)


Finalmente, debemos agregar los últimos códigos a los archivos:

### **read_registre.py**

![read_registre.py](https://github.com/user-attachments/assets/9dd46f56-ea2d-47d5-8f7f-7b266f8362f3)

Este script se conecta a la base de datos y recupera todos los registros de la tabla clientes. De hecho, se pueden ver todos los datos de la lista imprimiendo la variable en la que se guardan los resultados.

Si imprimimos la variable que almacena los resultados, veremos una lista con todas las filas de la tabla clientes:

![image](https://github.com/user-attachments/assets/0fd195da-7b8a-441d-b67a-c4d784996ae5)

Para visualizar los datos, es necesario usar un print(results). Si lo hacemos, obtendremos el siguiente:

![resultado](https://github.com/user-attachments/assets/cb143fbf-ba93-4c46-84fb-04a1b90ad807)

### **Extracción de un registro específico**

Después de haber obtenido y mostrado todos los resultados de la consulta, el siguiente paso es extraer un registro concreto de la lista.Imaginemos que queremos obtener el registro donde id_cliente = 5 y mostrar todos sus datos. Para ello, debemos recorrer la lista de resultados y buscar el registro que tenga el identificador deseado.

Añadimos el siguiente código justo debajo del print(results), que filtra los registros y obtiene únicamente el que tiene id_cliente = 5:

![image](https://github.com/user-attachments/assets/f41bd3e5-0dda-4ffe-a036-fc709eae4678)

Una vez almacenado el registro filtrado, podemos imprimirlo para verificar que se ha extraído correctamente:

![print cliente 5](https://github.com/user-attachments/assets/79aedb99-be70-4441-a9d0-93925881db64)

Si queremos obtener solo un dato específico del cliente filtrado (por ejemplo, su número de teléfono o su dirección), podemos acceder a la posición exacta en la lista de datos del registro:

![image](https://github.com/user-attachments/assets/a7134436-2770-4b77-b549-c79043131249)

Si solo necesitamos el número de cliente sin más información, podemos imprimir únicamente ese valor:

![solo numero del cliente n 05](https://github.com/user-attachments/assets/34509025-85ba-4a24-b7f6-928cbbee2075)

### **Ejercicos con registro**

1. Los datos de Andreu
   
![1](https://github.com/user-attachments/assets/af458fda-3b5e-4ee2-b5f2-43956d6fc4bc)

2 El correo de Andreu

![2](https://github.com/user-attachments/assets/86c910e8-489a-41d9-bb6e-61b595d6b54d)

3 Les dades de la Vivian

![3](https://github.com/user-attachments/assets/c85fb092-dd08-487c-8e77-e9934b7b71e5)

4 La direcció de la Vivian

![4](https://github.com/user-attachments/assets/b5f155ba-4740-4fdf-a683-e3bf40989cf9)

5 Les dades de l’Albert

![5](https://github.com/user-attachments/assets/deedab59-db69-4311-8565-1e20d2141c86)

6 La data de cumpleanys de l’Albert

![6](https://github.com/user-attachments/assets/a7f4a93a-6203-4295-b9b8-bd0c4296c575)

### **update_registre.py**

Para modificar los datos de un cliente, hemos utilizado la función update_reg(), llamándola desde main.py para visualizar los cambios y asegurarme de que la actualización se ha realizado correctamente en la base de datos.

![update_registre.py](https://github.com/user-attachments/assets/38be6ed6-03c9-4d0d-a623-c215b8ff60bc)

En la consulta SQL, he cambiado los valores de telefono_cliente y Nombre_Cliente, repitiendo el procedimiento tres veces para comprobar cómo se actualizaban los datos de diferentes clientes.

![ak (1)](https://github.com/user-attachments/assets/b88f19d1-e45e-489c-a10e-044e9bb102a9)

### **delete_registre.py**

Para eliminar registros de la base de datos, hemos implementado la función delete_reg(), encargada de gestionar la eliminación de clientes según su Nombre_Cliente.

Desde main.py, he llamado a delete_reg(), de manera similar a update_reg(), para comprobar cómo se eliminan clientes específicos de la base de datos.

![delete_registre.py](https://github.com/user-attachments/assets/9d241fc2-731c-495e-b3b0-0c42d04d9fcb)

Para verificar el funcionamiento del proceso, eliminaremos tres clientes creados previamente.

![ak 1](https://github.com/user-attachments/assets/21cb657e-4741-4ac7-a32a-5f42834da074)

**Fallos**
Fallos
- No podia añadir datos a la tabla  ya que los datos de pgadmin4 y los archivos dict_to_db.py no coindiean y lo teniena que ser exactos
- Hay aliniar todo bien para que o detecte
- Copié los archivos anteriores y tenía dos contenedores con el mismo nombre en Docker, por lo que tuve que eliminar uno, ya que causaba errores al iniciar Docker.

**Conclusión**

Podemos configurar un entorno de desarrollo con Docker, PyCharm y PostgreSQL para gestionar bases de datos de forma sencilla. Aprendimos a instalar Docker, configurar PyCharm, usar docker-compose.yml y conectar Python con PostgreSQL usando psycopg2. También trabajamos con archivos CSV e hicimos operaciones CRUD. Ahora tenemos una base sólida para manejar bases de datos de manera práctica y eficiente.









