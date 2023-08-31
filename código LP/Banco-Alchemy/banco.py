from crud import *
from menu import *
from conectar_db import *

FIM = 0
conn =  connect()
if not conn:
    print("Erro de conexão ao banco")
    exit()
opcao = entrar_opcao()
while (opcao != FIM):
    match (opcao):
        case 1: 
            incluir(conn)
        case 2: 
            alterar(conn)
        case 3: 
            excluir(conn)
        case 4: 
            listar(conn)
        case other: 
            print("Erro: opção inválida")
    opcao = entrar_opcao()