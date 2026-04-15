with open("meuarquivo.txt", "r", encoding="UTF-8") as arquivo:
    while True:
        linha = arquivo.readline()
        if not linha:
            break
        print(linha)