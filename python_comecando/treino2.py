palavra = "Paixao"
lista = []

for i, j in enumerate(palavra):
    lista.append("_")

# while True:
#     chute = input("Digite letra: ").lower()
#     for i, letra in enumerate(palavra):
#         if chute == letra.lower():
#             lista[i] = chute
#     print(lista)

# Tuplas
ponto = (3, 5)
p1 = (3, 5)
p2 = (4, 6)
p3 = (5, 7)
line = [p1, p2, p3]
print(line)

p1 = ("Nico", 39)
p2 = ("Flavio", 37)
instrutores = [p1, p2]
print(instrutores)

print(instrutores[0][0])
print(instrutores[0][1])

palavra = []
palavra.append("capivara")
palavra.append("abacaxi")
nova = tuple(palavra)

print(nova)

outra = list(nova)
print(outra)
