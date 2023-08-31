from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import configparser
import pathlib

CUR_DIR = pathlib.Path(__file__).parent.resolve()
ENV = str(CUR_DIR) + "\local.env"

def ler_db_params():
    params = configparser.ConfigParser()
    params.read(ENV)
    return params

def connect():
    session = None
    try:
        params = ler_db_params()
        engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
                       .format(user=params.get("DB", "username"),
                               pw=params.get("DB", "password"),
                               host=params.get("DB", "host"),
                               db=params.get("DB", "database")))
        engine.connect()
        Session = sessionmaker(bind=engine)
        session = Session()
        print("Banco conectado")
    except Exception as ex:
        print(ex)
    return session
