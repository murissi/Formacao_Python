class Animal:
    def __init__(self, raca, tamanho):
        self._raca = raca
        self.tamanho = tamanho

    def barulho(self):
        pass


class Passaro(Animal):
    def __init__(self, raca, tamanho, cor):
        super().__init__(raca, tamanho)
        self._cor = cor

    # sobrescrita
    def barulho(self):
        return "Canta"


class Cachorro(Animal):
    def __init__(self, raca, tamanho, idade):
        super().__init__(raca, tamanho)
        self._idade = idade

    def barulho(self):
        return "Latido"


c1 = Cachorro('Vira_lata', 'medio', '5 anos')
p1 = Passaro('Pombo', 'pequeno', 'branca')

# polimorfismo
print(c1.barulho())
print(p1.barulho())
