from utils import *

def entrar_opcao():
    while (True):
        exibir_menu()
        opcao = entrar_inteiro("Entre com a opção: ")
        if ((opcao < 0) or (opcao > 4)):
            print("Erro: opção inválida")
        else:
            break
    return opcao

def exibir_menu():
    print("[1] - Incluir")
    print("[2] - Alterar")
    print("[3] - Excluir")
    print("[4] - Listar")
    print("[0] - Sair")
