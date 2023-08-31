from conta import Conta
from utils import *

def incluir(contas):
    num = entrar_inteiro("Entre com o número da conta: ")
    if (pesquisar_conta(num, contas) != -1):
        print("Erro: conta já existe")
        return
    nome = entrar_nome() 
    saldo = entrar_saldo()
    contas.append(Conta(num, nome,saldo))
    print("Conta incluída")

def alterar(contas):
    num = entrar_inteiro("Entre com o número da conta: ")
    pos = pesquisar_conta(num, contas)
    if (pos == -1):
        print("Erro: conta não existe")
        return
    else:
        alterar_saldo(contas[pos])
    print("Conta alterada")

def excluir(contas):
    if not contas:
        print("Não há contas cadastradas")
        return
    num = entrar_inteiro("Entre com o número da conta: ")
    pos = pesquisar_conta(num, contas)
    if (pos == -1):
        print("Erro: conta não existe")
        return
    if contas[pos].get_saldo() != 0:
        print("Erro: saldo não está zerado")
        return
    else:
        del contas[pos]
    print("Conta excluída")

def listar(contas):
    if (not contas):
        print("Não há contas cadastradas")
        return
    opcao = entrar_inteiro("[1] - Listar todas as contas\n[2] - Listar uma conta: ")
    if (opcao == 1):
        listar_todas(contas)
    elif (opcao == 2):
        listar_conta(contas)
    else:
        print("Erro: opção inválida")
    print()     
    