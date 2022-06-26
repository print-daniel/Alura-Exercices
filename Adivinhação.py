import random

def jogar():

    print("_________________________________")
    print("Bem vindo ao jogo de Adivinhação!")
    print("_________________________________")

    numero_da_sorte = round(random.random() * 30)
    tentativas = 3
    pontos = 300
    print("Selecione o nivel de dificuldade")
    print("(1) Facil, (2) Médio, (3) Difícil")

    nivel = int(input("Defina o nivel:"))

    if(
            nivel == 1
    ):
        tentativas = 10

    elif(
            nivel == 2
    ):
        tentativas = 5

    else:
        tentativas = 3

    while (tentativas > 0):
        chute_str = input("Digite o seu número:")
        print("Seu chute foi:", chute_str)
        chute = int(chute_str)
        if (chute < 1):
            print("Escreva um número entre 1 e 30")
            continue
        acertou = chute == numero_da_sorte
        maior = chute > numero_da_sorte
        menor = chute < numero_da_sorte

        if (
                acertou
        ):

              print("Você acertou e fez {}!".format(pontos))
              break
        else:
              if(
                maior
              ):
                    print("Você Errou, seu número foi maior que o esperado")
              elif(
                menor
              ):
                    print("Você errou, seu número foi menor que o esperado")

              print(
                  "Tentativas Restantes: {}".format(tentativas)
              )
              pontos_perdidos = abs(numero_da_sorte - chute)
              pontos = pontos - pontos_perdidos

        tentativas = tentativas - 1

    print("Fim do Jogo")

if(__name__ == "__main__"):
    jogar()