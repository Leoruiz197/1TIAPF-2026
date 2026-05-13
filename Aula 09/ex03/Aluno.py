from Pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, matricula, faltas):
        super().__init__(nome, idade)
        self.curso = curso
        self.matricula = matricula
        self.faltas = faltas

    def apresentar(self):
        super().apresentar()
        print(f"Eu sou um aluno do curso de {self.curso}.")
        print(f"Minha matrícula é {self.matricula}.")
        print(f"Tenho {self.faltas} faltas.")

    def adicionar_falta(self):
        self.faltas += 1
        print(f"Falta adicionada. Total de faltas: {self.faltas}")