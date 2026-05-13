from Eletronico import Eletronico
from Roupa import Roupa

def  main():
    tv = Eletronico(123,"TV smart 50`` ", 1500.00,"Tv samsung 50 polegadas smart", "Samsung", 2, 110, 150.0)
    camisa = Roupa(456,"Camisa", 50.00, "Camisa sport", "Nike", 1, "M", "Algodão", "Azul")

    tv.exibir_informacoes()
    tv.calcular_consumo_mensal(4)
    print(" - " * 20)
    camisa.exibir_informacoes()
    camisa.definir_cor("Vermelho")

if __name__ == "__main__":
    main()