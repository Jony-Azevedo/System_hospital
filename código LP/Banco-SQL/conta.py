class Conta:
    def __init__(self, num, nome, saldo):
        self.num = num
        self.nome = nome
        self.saldo = saldo

    def set_num(self, num):
        self.num = num

    def get_num(self):
        return self.num

    def set_nome(self, nome):
        self.nome = nome

    def get_nome(self):
        return self.nome
    
    def set_saldo(self, saldo):
        self.saldo = saldo

    def get_saldo(self):
        return self.saldo

    def creditar_saldo(self, valor):
        self.saldo += valor

    def debitar_saldo(self, valor):
        self.saldo -= valor

    def __str__(self):
        return str(self.num) + " " + self.nome + " " + str(self.saldo)