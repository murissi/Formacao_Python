class Filme:
    def __init__(self, titulo, diretor):
        self.titulo = titulo
        self.diretor = diretor

    def __str__(self):
        return f'{self.titulo} - {self.diretor}'

    def __eq__(self, other):
        return self.titulo == other.titulo

coringa = Filme('Joker', 2019)
batman = Filme('Joker', 2020)

# mostra que o titulo é igual
print(coringa == batman)
print(coringa != batman)
# Rich Comparison
# __eq__() ==
# __ne__() !=
# __gt__() >
# __lt__() <
# __ge__() >=
# __le__() <=
