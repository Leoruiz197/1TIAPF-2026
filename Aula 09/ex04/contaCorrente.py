from Banco import Banco

class ContaCorrente(Banco):
    def __init__(self, agencia, conta, saldo, nome_cliente, limite):
        super().__init__(agencia, conta, saldo, nome_cliente)
        self.limite = limite
    
    def sacar(self, valor):
        if valor <= self.saldo + self.limite:
            self.saldo -= valor
            print(f"Saque de R${valor} realizado com sucesso.")
        else:
            print("Saldo insuficiente para realizar o saque.")

    def consultar_limite(self):
        print(f"Limite disponível: R${self.limite}")
    
    def consultar_saldo(self):
        super().consultar_saldo()
        print(f"Limite disponível: R${self.limite}")