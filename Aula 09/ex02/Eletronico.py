from Produto import Produto

class Eletronico(Produto):
    def __init__(self, codigo, nome, preco, descricao, marca, quantidade, voltagem, consumo_energia):
        super().__init__(codigo, nome, preco, descricao, marca, quantidade)
        self.voltagem = voltagem
        self.consumo_energia = consumo_energia

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Voltagem: {self.voltagem}")
        print(f"Consumo de Energia: {self.consumo_energia}")
    
    def calcular_consumo_mensal(self, horas_uso_diario):
        consumo_diario = self.consumo_energia * horas_uso_diario
        consumo_mensal = consumo_diario * 30  # Considerando 30 dias no mês
        print(f"Consumo mensal: {consumo_mensal}")