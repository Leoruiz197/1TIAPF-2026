matriz = [
    [1,2],
    [3,4],
]

matriz2 = [
    [5,6],
    [7,8]
]

matriz3 = []

for i in range(len(matriz)):
    linha = []
    for j in range(len(matriz[i])):
        sub = matriz[i][j] - matriz2[i][j]
        linha.append(sub)
    matriz3.append(linha)

for linha in matriz3:
    print(linha)