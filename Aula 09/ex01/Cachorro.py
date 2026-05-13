from Animal import Animal

class Cachorro(Animal):
    def __init__(self, nome, idade, peso, altura, tipo_alimentacao, raca):
        super().__init__(nome, idade, peso, altura, tipo_alimentacao)
        self.raca = raca

    def emitir_som(self):
        return "Au au!"