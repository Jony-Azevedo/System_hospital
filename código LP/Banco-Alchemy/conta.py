from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()

class Conta(base):
    __tablename__ = "conta"
    id_conta = Column(Integer, primary_key=True)
    nome = Column(String)
    saldo = Column(Float)

    def __init__(self, num, nome, saldo):
        self.id_conta = num
        self.nome = nome
        self.saldo = saldo

    def set_num(self, num):
        self.id_conta = num

    def get_num(self):
        return self.id_conta

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
        return str(self.id_conta) + " " + self.nome + " " + str(self.saldo)
