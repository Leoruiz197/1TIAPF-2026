class Produto:
    def __init__(self, codigo, nome, preco, descricao, marca, quantidade):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco
        self.descricao = descricao
        self.marca = marca
        self.quantidade = quantidade

    def calcular_valor_total(self):
        return self.preco * self.quantidade
    
    def exibir_informacoes(self):
        print(f"Código: {self.codigo}")
        print(f"Nome: {self.nome}")
        print(f"Preço: R${self.preco:.2f}")
        print(f"Descrição: {self.descricao}")
        print(f"Marca: {self.marca}")
        print(f"Quantidade: {self.quantidade}")