class Banco:
    def __init__(self, agencia, conta, saldo, nome_cliente):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
        self.nome_cliente = nome_cliente
    
    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor} realizado com sucesso.")
    
    def sacar(self, valor):
        pass

    def consultar_saldo(self):
        print(f"Saldo atual: R${self.saldo}")