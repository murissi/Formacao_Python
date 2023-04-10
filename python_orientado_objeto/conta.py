class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto...")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f"Saldo: {self.__saldo} do Titular {self.__titular}")

    def deposito(self, valor):
        self.__saldo += valor

    # Metodo privado
    def __pode_sacar(self, value):
        valor_disponivel = (self.__saldo + self.__limite)
        return value <= valor_disponivel

    def saca(self, valor):
        if valor < self.__saldo:
            if self.__pode_sacar(valor):
                self.__saldo -= valor

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposito(valor)

    # Static method
    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def condigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco':'237'}


p1 = Conta(111, 'Nico', 55.5, 1000.0)
p1.saca(10)
print(p1.extrato())
print(Conta.codigo_banco())