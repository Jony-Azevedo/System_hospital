from conta import Conta
from utils import *
from crud_db import *

def incluir(conn):
    nome = entrar_nome() 
    saldo = entrar_saldo()
    conta = Conta(0, nome,saldo)
    incluir_conta(conn, conta)

def alterar(conn):
    if not existe_registro(conn):
        print("Não há contas cadastradas")
        return
    num = entrar_inteiro("Entre com o número da conta: ")
    conta = consultar_conta(conn, num)
    if not conta:
        print("Erro: conta não existe")
        return
    else:
        alterar_saldo(conta)
        alterar_conta(conn, conta)
        print("Conta alterada")

def excluir(conn):
    if not existe_registro(conn):
        print("Não há contas cadastradas")
        return
    num = entrar_inteiro("Entre com o número da conta: ")
    conta = consultar_conta(conn, num)
    if not conta:
        print("Erro: conta inexistente")
        return
    if conta.get_saldo() != 0:
        print("Erro: saldo não está zerado")
        return
    excluir_conta(conn, num)

def listar(conn):
    if not existe_registro(conn):
        print("Não há contas cadastradas")
        return
    opcao = entrar_inteiro("[1] - Listar todas as contas\n[2] - Listar uma conta: ")
    if (opcao == 1):
        listar_todas(conn)
    elif (opcao == 2):
        listar_conta(conn)
    else:
        print("Erro: opção inválida")
    print()

def listar_todas(conn):
    print("Listagem de contas")
    contas = consultar_todos(conn)
    for conta in contas:
        print(conta)

def listar_conta(conn):
    num = entrar_inteiro("Entre com o número da conta: ")
    conta = consultar_conta(conn, num)
    if (conta):
        print(conta)
    else:
        print("Erro: conta não existe")
