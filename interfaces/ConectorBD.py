# Importar el módulo de mysql.connector
import mysql.connector
# Establecer la conexión con la base de datos
conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="helpme"
)

# Obtener el cursor de la conexión
cursor = conn.cursor()