from Animal import Animal

class Gato(Animal):
    def __init__(self, nome, idade, peso, altura, tipo_alimentacao, tipo_pelo):
        super().__init__(nome, idade, peso, altura, tipo_alimentacao)
        self.tipo_pelo = tipo_pelo

    def emitir_som(self):
        return "Miau!"