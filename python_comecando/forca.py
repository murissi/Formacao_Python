def jogo_forca():
    print("*" * 17)
    print("Jogo da Forca")
    print("*" * 17)

    palavra_secreta = "capivara"
    letras_acertadas = ["_","_","_","_","_","_","_","_"]

    enforcou = acertou = False
    index = 0

    print(letras_acertadas)

    while not enforcou and not acertou:
        chute = input("Qual letra? ")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if chute.upper() == letra.upper():
                letras_acertadas[index] = letra
            index += 1
        print(letras_acertadas)

if __name__ == "__main__":
    jogo_forca()
