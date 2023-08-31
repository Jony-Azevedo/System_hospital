import pandas as pd
from sqlalchemy import create_engine, text
from conectar_db import ler_db_params

params = ler_db_params()
#engine = create_engine("mysql+pymysql://root:lpmaia@localhost/bd_tarde")
engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
                       .format(user=params.get("DB", "username"),
                               pw=params.get("DB", "password"),
                               host=params.get("DB", "host"),
                               db=params.get("DB", "database")))
conn = engine.connect()

df_contas = pd.DataFrame(columns=["id", "nome", "saldo"],
                         data=[[1, "Juli", 1000],
                               [2, "Bruno", 2000],
                               [3, "Leo", 3000]])
NOME_TABELA = "contas"
try:
    df_contas.to_sql(NOME_TABELA, conn, if_exists="replace", index=False)
    conn.execute(text("ALTER TABLE " + NOME_TABELA + " ADD PRIMARY KEY (id);"))
    print("Tabela gravada")
except Exception as ex:
    print(ex)