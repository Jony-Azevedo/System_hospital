from conta import Conta

def incluir_conta(conn, conta):
    try:
        conn.add(conta)
        conn.commit()
        print("Conta incluída")
    except Exception as ex:
        print(ex)

def excluir_conta(conn, conta):
    try:
        conn.delete(conta)
        conn.commit()
        print("Conta excluída")
    except Exception as ex:
        print(ex)

def alterar_conta(conn):
    conta = None
    try:
        conn.query(Conta).first()
        print("Saldo alterado")
    except Exception as ex:
        print(ex)

def existe_registro(conn):
    query = "SELECT COUNT(*) FROM conta;"
    cursor = conn.cursor()
    existe = False
    try:
        cursor.execute(query)
        records = cursor.fetchall()
        if len(records) > 0:
            existe = True
    except Exception as ex:
        print(ex)
    finally:
        cursor.close()
    return existe

def consultar_todos(conn):
    contas = []
    try:
        contas = conn.query(Conta).all()
    except Exception as ex:
        print(ex)
    return contas

def consultar_conta(conn, id):
    conta = None
    try:
        conta = conn.query(Conta).get(id)
    except Exception as ex:
        print(ex)
    return conta
