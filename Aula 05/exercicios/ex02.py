arq1 = input("Digite o nome do primeiro arquivo: ")
arq2 = input("Digite o nome do segundo arquivo: ")
arq3 = input("Digite o nome do terceiro arquivo: ")

conteudo1 = ""
conteudo2 = ""

with open(arq1, "r", encoding="UTF-8") as arquivo1:
    conteudo1 = arquivo1.read()
with open(arq2, "r", encoding="UTF-8") as arquivo2:
    conteudo2 = arquivo2.read()

with open(arq3, "w", encoding="UTF-8") as arquivo3:
    arquivo3.write(conteudo1)
    arquivo3.write("\n")
    arquivo3.write(conteudo2)   

print(f"Os arquivos {arq1} e {arq2} foram combinados no arquivo {arq3}.")
