arquivo = input("Digite o nome do arquivo: ")

with open(arquivo, "r", encoding="UTF-8") as file:
    conteudo = file.read()
    palavras = conteudo.split()
    print(f"O arquivo '{arquivo}' contém {len(palavras)} palavras.")

