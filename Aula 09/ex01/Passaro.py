from Animal import Animal

class Passaro(Animal):
    def __init__(self, nome, idade, peso, altura, tipo_alimentacao, especie):
        super().__init__(nome, idade, peso, altura, tipo_alimentacao)
        self.especie = especie

    def emitir_som(self):
        return "Piu piu!"