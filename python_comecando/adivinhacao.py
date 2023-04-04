import random


def jogo_adivinhacao():
    print("*" * 36)
    print("Bem vindos aos jogos de adivinhação!")
    print("*" * 36)
    print()

    numero_secreto = round(random.randrange(1, 100))
    tentativas = 0
    pontos = 1000

    print("Nivel |1 facil |2 medio |3 dificil ")
    dificuldade = int(input())

    match dificuldade:
        case 1:
            tentativas = 20
        case 2:
            tentativas = 10
        case 3:
            tentativas = 5
        case _:
            print("Nivel invalido")
            tentativas = 0

    while tentativas >= 1:

        chute = int(input("Digite um numero 1 a 100: "))
        if 1 <= chute <= 100:

            if chute == numero_secreto:
                print(f"Parabens, você acertou! {numero_secreto}")
                break
            else:
                if chute < numero_secreto:
                    print(f"Você chutou {chute} muito baixo!")
                else:
                    print(f"Você chutou {chute} muito alta!")
        else:
            print("Digite Numero permitido")
        tentativas -= 1
        pontos_perdidos = abs(numero_secreto - chute)
        pontos -= pontos_perdidos
        print()
        print("Tentativas: ", tentativas)

    print(f"Pontos {pontos}")
    print("FIM DO PROGRAMA")


if __name__ == "__main__":
    jogo_adivinhacao()
