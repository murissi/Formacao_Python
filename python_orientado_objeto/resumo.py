class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.__titular = titular
        self.__numero = numero
        self.__saldo = saldo
        self.__limite = limite

    # atributo estatico
    PI = 3.14

    # static method
    @staticmethod
    def conta_banco():
        return "001"

    # getter
    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, value):
        self.__limite = value

    # getter
    @property
    def titular(self):
        return self.__titular

    # setter
    @titular.setter
    def titular(self, value):
        self.__titular = value

    # methods
    def extrato(self):
        text = f"{self.__titular}\nR${self.__saldo}"
        return text

    def deposita(self, value):
        self.__saldo += value

    def __pode_sacar(self, value):
        total = self.__saldo + self.__limite
        return value < total

    def saca(self, value):
        if self.__pode_sacar(value):
            self.__saldo -= value

print(Conta.conta_banco())
c1 = Conta(111, 'Lucas', 50.0, 1000.0)
c1.limite = 200
print(c1.limite)
c1.saca(25)
c1.deposita(100)
print(c1.extrato())
print(Conta.PI)