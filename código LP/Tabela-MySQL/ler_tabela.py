# pip install mysql-connector-python
# pip install pandas

import pandas as pd
from conectar_db import *

SQL = "SELECT * FROM alunos"

conn = connect()
if (conn == None):
    exit
try:
    df = pd.read_sql_query(SQL, conn)
    print(df)
except:
    print("Erro: execução SQL")    
desconnect(conn)