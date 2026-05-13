from Pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, salario, departamento):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.salario = salario
        self.departamento = departamento

    def apresentar(self):
        super().apresentar()
        print(f"Eu trabalho como {self.cargo}.")
        print(f"Meu salário é {self.salario} e trabalho no departamento {self.departamento}.")