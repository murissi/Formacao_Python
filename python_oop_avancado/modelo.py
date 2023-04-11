class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def add_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        self._nome = value.title()


class Filme(Programa):
    # extensao ou sobrescrita
    def __init__(self, nome, ano, duracao):
        # chamando atributos e metodos da classe mae
        super().__init__(nome, ano)
        self.duracao = duracao


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas


vingadores = Filme('Vingadores', 2022, 150)
the_office = Serie('The office', 2007, 8)
print(the_office.temporadas)
