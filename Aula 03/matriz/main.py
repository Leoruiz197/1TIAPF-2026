matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

novalinha = [10,11,12]
matriz.append(novalinha)

matriz[1].insert(1,100)

for linha in matriz:
    for elemento in linha:
        print(elemento, end= " ")
    print()

for x in range(3): # lista externa
    for y in range(3): #lista interna
        print(matriz[x][y])