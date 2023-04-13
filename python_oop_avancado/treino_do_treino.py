class Lista:
    def __init__(self, nome, lista):
        self.nome = nome
        self._lista = lista

    def __getitem__(self, item):
        return self._lista[item]


lista_frutas = ['Banana', 'Maça', 'Pera']

p1 = Lista('lista frutas', lista_frutas)

for i in p1:
    print(i)
