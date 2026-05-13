from contaCorrente import ContaCorrente
from contaPoupanca import contaPoupanca

def main():
    conta_corrente = ContaCorrente("001", "12345-6", 1000.0, "João Silva", 500.0)
    conta_poupanca = contaPoupanca("001", "54321-0", 2000.0, "Maria Oliveira", 0.05)

    print("=== Conta Corrente ===")
    conta_corrente.consultar_saldo()
    conta_corrente.consultar_limite()
    conta_corrente.sacar(1200.0)
    conta_corrente.consultar_saldo()

    print("\n=== Conta Poupança ===")
    conta_poupanca.consultar_saldo()
    conta_poupanca.calcular_rendimento()

if __name__ == "__main__":
    main()