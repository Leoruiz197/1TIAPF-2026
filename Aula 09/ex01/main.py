from Cachorro import Cachorro
from Gato import Gato
from Passaro import Passaro

def main():
    cachorro = Cachorro("Rex", 5, 20.0, 0.5, "Carnívoro", "Labrador")
    gato = Gato("Mia", 3, 4.0, 0.3, "Carnívoro", "Curto")
    passaro = Passaro("Piu", 1, 0.5, 0.2, "Onívoro", "Canário")

    print(f"{cachorro.nome} diz: {cachorro.emitir_som()}")
    print(f"{gato.nome} diz: {gato.emitir_som()}")
    print(f"{passaro.nome} diz: {passaro.emitir_som()}")

if __name__ == "__main__":
    main()