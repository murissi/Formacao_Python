import adivinhacao
import forca

print("*" * 17)
print("Escolha seu jogo:")
print("*" * 17)

print("(1) Forca (2) Adivinhação ")
jogo = int(input("Jogo: "))

match jogo:
    case 1:
        forca.jogo_forca()
    case 2:
        adivinhacao.jogo_adivinhacao()
    case _:
        print("INVALIDO")
