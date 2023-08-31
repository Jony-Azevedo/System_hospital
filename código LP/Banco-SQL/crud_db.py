from conta import Conta

def incluir_conta(conn, conta):
    query = "INSERT INTO conta (nome, saldo) VALUES (%s, %s);"
    cursor = conn.cursor()
    try:
        dados = [(conta.get_nome(), conta.get_saldo())]
        cursor.executemany(query, dados)
        conn.commit()
        print("Conta incluída")
    except Exception as ex:
        print(ex)
    finally:
        cursor.close()

def excluir_conta(conn, id):
    query = "DELETE FROM conta WHERE id_conta = %s;"
    cursor = conn.cursor()
    try:
        cursor.execute(query, [id])
        conn.commit()
        print("Conta excluída")
    except Exception as ex:
        print(ex)
    finally:
        cursor.close()

def alterar_conta(conn, conta):
    query = "UPDATE contas SET saldo = %s WHERE id_conta = %s;"
    cursor = conn.cursor()
    try:
        dados = [(conta.get_num(), conta.get_saldo())]
        cursor.execute(query, dados)
        conn.commit()
        print("Saldo alterado")
    except Exception as ex:
        print(ex)
    finally:
        cursor.close()

def existe_registro(conn):
    query = "SELECT COUNT(*) FROM conta;"
    cursor = conn.cursor()
    existe = False
    try:
        cursor.execute(query)
        records = cursor.fetchall()
        if records[0][0] > 0:
            existe = True
    except Exception as ex:
        print(ex)
    finally:
        cursor.close()
    return existe

def consultar_todos(conn):
    query = "SELECT * FROM conta;"
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        records = cursor.fetchall()
        contas = []
        for record in records:
            contas.append(Conta(record[0], record[1], record[2]))
    except Exception as ex:
        print(ex)
    finally:
        cursor.close()
    return contas

def consultar_conta(conn, id):
    query = "SELECT * FROM conta WHERE id_conta = %s;"
    cursor = conn.cursor()
    conta = None
    try:
        cursor.execute(query, [id])
        record = cursor.fetchall()
        if record:
            conta = Conta(record[0][0], record[0][1], record[0][2])
    except Exception as ex:
        print(ex)
    finally:
        cursor.close()
    return conta
