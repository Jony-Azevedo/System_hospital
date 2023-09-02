import mysql.connector

db_config = {
    "host":"localhost",
    "user":"root",
    "password":"1234",
    "database":"at_pb"
}
# Função para obter uma conexão com o banco de dados
def obter_conexao():
    return mysql.connector.connect(**db_config)
