with open("arquivo.txt", "w", encoding="UTF-8") as arquivo:
    arquivo.write("Olá, mundo!\n")
    arquivo.write("Este é um arquivo de texto.\n")
    arquivo.write("Estamos aprendendo a manipular arquivos em Python.\n")

with open("arquivo.txt", "r", encoding="UTF-8") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

with open ("arquivo.txt", "r", encoding="UTF-8") as arquivo:
    while True:
        linha = arquivo.readline()
        if not linha:
            break
        print(linha)