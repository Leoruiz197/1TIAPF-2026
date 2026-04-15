alunos = []

aluno = []

aluno.append(1)
aluno.append("Joao")
aluno.append(5)
aluno.append(8.5)
aluno.append('M')

alunos.append(aluno)

aluno = []

aluno.append(2)
aluno.append("Lucas")
aluno.append(8)
aluno.append(7)
aluno.append('M')

alunos.append(aluno)

aluno = []

aluno.append(3)
aluno.append("Maria")
aluno.append(4)
aluno.append(9.5)
aluno.append('F')

alunos.insert(1,aluno)

print(aluno)
print(alunos)

print(alunos[1][1])
alunos[1].pop(0)
alunos[1].insert(0,2)
print(alunos)


alunos[2].pop(0)
alunos[2].insert(0,3)
print(alunos)

for x in range(len(alunos)):
    for y in range(len(alunos[x])):
        print(alunos[x][y], end= " ")
    print()

for linha in alunos:
    for elemento in linha:
        print(elemento)