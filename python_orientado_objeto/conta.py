class Conta:
    # funcao construtora
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto...")
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print(f"Saldo: {self.saldo} do Titular {self.titular}")

    def deposito(self, valor):
        self.saldo += valor

    def saca(self, valor):
        if valor < self.saldo:
            self.saldo -= valor
