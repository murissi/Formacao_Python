class Lista:
    def __init__(self, nome, lista):
        self.nome = nome
        self._lista = lista

    # com esse metodo podemos usar o for
    def __getitem__(self, item):
        return self._lista[item]

    # com esse metodo podemos usar a funcao len()
    def __len__(self):
        return len(self._lista)

lista_frutas = ['Banana', 'Maça', 'Pera']

p1 = Lista('lista frutas', lista_frutas)

print(f'Lista tem {len(lista_frutas)} itens')

for i in p1:
    print(i)

# Python Data Model
# Inicializacao __init__
# Representacao __str__, __repr__
# Container, sequencia __contains__, __iter__, __len__, __getitem__
# Numericos __add__, __sub__, __mul__, __mod__
