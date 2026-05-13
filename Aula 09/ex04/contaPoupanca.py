from Banco import Banco

class contaPoupanca(Banco):
    def __init__(self, agencia, conta, saldo, nome_cliente, rendimento):
        super().__init__(agencia, conta, saldo, nome_cliente)
        self.rendimento = rendimento
    
    def calcular_rendimento(self):
        rendimento_calculado = self.saldo * self.rendimento
        print(f"Rendimento calculado: R${rendimento_calculado}")