class Game:

    def __init__(self, nome, vezes_jogadas):
        self.__nome = nome
        self.__vezes_jogadas = vezes_jogadas

    def get_nome(self):
        return self.__nome

    def get_vezes_jogadas(self):
        return self.__vezes_jogadas
