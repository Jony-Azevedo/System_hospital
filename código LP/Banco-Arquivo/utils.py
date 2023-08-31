def entrar_inteiro(msg):
    ok = False
    while (not ok):
        try:
            num = int(input(msg))
            ok = True
        except:
            print("Erro: número inválido")
    return num

def entrar_nome():
    ok = False
    while (not ok):
        nome = input("Entre com o nome do cliente: ")
        if (len(nome) < 2):
            print("Erro: nome inválido")
        else:
            ok = True
    return nome

def entrar_real(msg):
    ok = False
    while (not ok):
        try:
            num = float(input(msg))
            ok = True
        except:
            print("Erro: número inválido")
    return num    

def entrar_saldo():
    ok = False
    while (not ok):
        saldo = entrar_real("Entre com o saldo: ")
        if (saldo > 0):
            ok = True
        else:
            print("Erro: saldo inválido")
    return saldo

def pesquisar_conta(num, contas):
    pos = -1
    for conta in range(len(contas)):
        if (contas[conta].get_num() == num):
            pos = conta
            break
    return pos

def entrar_operacao():
    ok = False
    while not ok:
        operacao = input("Emtre com o tipo de operação [C]rédito ou [D]ébito: ")
        operacao = operacao.upper()
        if operacao == "C" or operacao == "D":
            ok = True
        else:
            print("Erro: operação inválida")
    return operacao

def entrar_valor():
    ok = False
    while (not ok):
        valor = entrar_real("Entre com o valor: ")
        if (valor > 0):
            ok = True
        else:
            print("Erro: valor inválido")
    return valor

def alterar_saldo(conta):
    operacao = entrar_operacao()
    valor = entrar_valor()
    if operacao == "C":
        conta.creditar_saldo(valor)
    else:
        conta.debitar_saldo(valor)

def listar_todas(contas):
    print("Listagem de contas")
    for conta in contas:
        print(conta)

def listar_conta(contas):
    num = entrar_inteiro("Entre com o número da conta: ")
    pos = pesquisar_conta(num, contas)
    if (pos == -1):
        print("Erro: conta não existe")
        return
    print(contas[pos])
