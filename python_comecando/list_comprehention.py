# List Comprehensions

# sem list comprehensions
lista = []
for item in range(10):
    lista.append(item ** 2)

print(lista)

# com list comprehensions
lista = [item ** 2 for item in range(10)]
print(lista)

nomes = ['Lucas', 'Marcos', 'Joao', 'Paulo']
maiuscula = [str(item).upper() for item in nomes]

print(maiuscula)

forca = ["_" for i in range(10) if i == 6]
print(forca)

frutas = ['maçã', 'banana', 'laranja', 'melancia']
frutas = [item.upper() for item in frutas]
print(frutas)

inteiros = [1, 3, 4, 5, 7, 8]
inteiros = [i * 2 for i in inteiros]
print(inteiros)

par = [i for i in range(11) if i % 2 == 0]
print(par)