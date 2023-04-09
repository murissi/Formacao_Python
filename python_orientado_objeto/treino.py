class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print(f"Construindo objeto..{self}")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.limite = limite

    def extrato(self):
        print(f"Saldo de {self.__saldo}\nTitular: {self.__titular}")

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        if valor < self.__saldo:
            self.__saldo -= valor
