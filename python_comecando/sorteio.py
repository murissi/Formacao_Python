import random
random.seed(100)
numero_sorteado = random.randrange(1, 101)
print(numero_sorteado)

match numero_sorteado:
    case 1:
        print("Paulo")
    case 2:
        print("Juliana")
    case _:
        print("Tamires")
