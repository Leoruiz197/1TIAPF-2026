from Produto import Produto

class Roupa(Produto):
    def __init__(self, codigo, nome, preco, descricao, marca, quantidade, tamanho, material, cor):
        super().__init__(codigo, nome, preco, descricao, marca, quantidade)
        self.tamanho = tamanho
        self.material = material
        self.cor = cor

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Tamanho: {self.tamanho}")
        print(f"Material: {self.material}")

    def definir_cor(self, nova_cor):
        self.cor = nova_cor
        print(f"A cor da roupa foi alterada para: {self.cor}") 