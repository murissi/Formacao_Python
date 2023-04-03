print("*" * 36)
print("Bem vindos aos jogos de adivinhação!")
print("*" * 36)
print()

numero_secreto = 42
chute = int(input("Digite um numero: "))
tentativas = 3
while tentativas >= 1:

    if chute == numero_secreto:
        print("Parabens, você acertou! {}".format(numero_secreto))
        break
    else:
        if chute < numero_secreto:
            print("Você chutou {} muito baixo!".format(chute))
        else:
            print("Você chutou {} muito alta!".format(chute))
    tentativas -= 1
    print()
    print("Tentativas: ", tentativas)
    chute = int(input("Digite outro numero: "))


print("FIM DO PROGRAMA")
