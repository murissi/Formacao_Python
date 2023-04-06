palavra = "capivara"
forca = []
for i in range(len(palavra)):
    forca.append("_")

while True:
    chute = input("Digite letra: ")
    for indice, letra in enumerate(palavra):
        if chute.lower() == letra:
            forca[indice] = chute
    print(forca)