import mysql.connector
#import configparser
#import pathlib

db_config = {
    "host":"localhost",
    "user":"root",
    "password":"1234",
    "database":"at_pb"
}
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# teste consulta
query = "SELECT * FROM medico"
cursor.execute(query)

# Recupera os resultados da consulta
result = cursor.fetchall()

# Mostra os resultados
for row in result:
    print(row)

cursor.close()
conn.close()