from conta import Conta 
from arquivo import *
from crud import *
from menu import *

FIM = 0
contas = ler_contas()
opcao = entrar_opcao()
while (opcao != FIM):
    match (opcao):
        case 1: 
            incluir(contas)
        case 2: 
            alterar(contas)
        case 3: 
            excluir(contas)
        case 4: 
            listar(contas)
        case other: 
            print("Erro: opção inválida")
    opcao = entrar_opcao()
gravar_contas(contas)