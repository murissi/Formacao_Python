import random


# jogo da forca

def numero_aleatorio():
    n = random.randrange(3)
    return n


palavras = ["capivara", "brasil", "portao"]
palavra = palavras[numero_aleatorio()]
forca = ["_" for i in palavra]
tentativa = 1

while tentativa <= 5:
    chute = input("Digite letra: ")
    if chute in palavra:
        for i, j in enumerate(palavra):
            if chute == j:
                forca[i] = chute
        print(forca)
    else:
        print(f"Tentativas: {tentativa}")
        tentativa += 1

    if tentativa == 5:
        print("Perdeu ")
        break
