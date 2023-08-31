import mysql.connector
import configparser
import pathlib

CUR_DIR = pathlib.Path(__file__).parent.resolve()
ENV = str(CUR_DIR) + "\local.env"

def ler_db_params():
    params = configparser.ConfigParser()
    params.read(ENV)
    return params

def connect():
    conn = None
    try:
        params = ler_db_params()
        conn = mysql.connector.connect(
            user=params.get("DB", "username"),
            password=params.get("DB", "password"),
            host=params.get("DB", "host"),
            port=params.get("DB", "port"),
            database=params.get("DB", "database")
        )
        print("Banco conectado")
    except Exception as ex:
        print(ex)
    return conn
    
def disconnect(conn):
    if (conn is not None):
        conn.close()
        print("Banco desconectado")
