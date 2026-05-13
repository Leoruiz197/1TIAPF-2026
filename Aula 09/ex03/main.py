from Funcionario import Funcionario
from Aluno import Aluno

def main():
    aluno1 = Aluno("João", 20, "Engenharia de Software", "2021001", 2)
    funcionario1 = Funcionario("Maria", 35, "Gerente de Projetos", 5000, "TI")

    print("Apresentação do Aluno:")
    aluno1.apresentar()
    print("\nApresentação do Funcionário:")
    funcionario1.apresentar()

    print("\nAdicionando falta para o aluno...")
    aluno1.adicionar_falta()

if __name__ == "__main__":
    main()