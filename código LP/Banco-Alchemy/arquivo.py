import pathlib
from conta import Conta

CUR_DIR = pathlib.Path(__file__).parent.resolve()
NOME_ARQ = "\contas.csv"
ARQ = str(CUR_DIR) + NOME_ARQ

def gravar_contas(contas):
    with open(ARQ, "w") as arquivo:
        for conta in contas:
            arquivo.write(str(conta.get_num()) + "," +
                          conta.get_nome() + "," +
                          str(conta.get_saldo()) + "\n")
            
def ler_contas():
    contas = []
    try:
        with open(ARQ, "r") as arquivo:
            linha = arquivo.readline()
            while (linha != ""):
                linha = linha.strip("\n")
                campos = linha.split(",")
                num, nome, saldo = int(campos[0]), campos[1], float(campos[2])
                contas.append(Conta(num, nome, saldo))
                linha = arquivo.readline()
    except Exception as ex:
        print(ex)
    return contas