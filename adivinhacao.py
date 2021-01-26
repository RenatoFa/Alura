import random


def jogar():
    print("********************************")
    print("Bem vindo no jogo de Adivinhação")
    print("********************************")

    # funcao random  = esta entre 0.0 e 1.0
    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual nivel de dificuldade ?")
    print("(1) Fácil (2) Médio (3) Dificil")

    nivel = int(input("Define o nivel: "))

    if nivel == 1:
        total_de_tentativas = 20
        print("Facil")
    elif (nivel == 2):
        total_de_tentativas = 10
        print("Médio")
    else:
        total_de_tentativas = 5
        print("Dicil")

    # for rodado in range(1, 10):
    # print(rodado)

    # for rodado in range(1, 10, 2):  # range(inicio,final,step)
    # print(rodado)

    for rodada in range(1, total_de_tentativas+1):
        print("Tentativa {} de {}" .format(rodada, total_de_tentativas))
        chute = int(input("Digite o seu numero entre 1 e 100: "))
        print("Voce digitou: ", chute)

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(chute < 1 or chute > 100):
            print("Voce deve digitar um numero entre 1 e 100: ")
            continue

        if acertou:
            print("Voce acertou e fez {} pontos!".format(pontos))
            break  # sair do laço
        else:
            if(maior):
                print("Você errou! O seu chute foi maior do que o numero ")
                if (rodada == total_de_tentativas):
                    print("O numero secreto era {}. Voce fez {}".format(
                        numero_secreto, pontos))
            elif(menor):
                print("Você errou! O seu chute foi menor do que o numero ")
                if (rodada == total_de_tentativas):
                    print("O numero secreto era {}. Voce fez {}".format(
                        numero_secreto, pontos))

            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

        print("Tentativas: %s" % total_de_tentativas)

    print("Fim do Jogo")

    # Formatação
    """print("R$ {:07.2f} ".format(1.59))  # Float    
    print("R$ {:07d} ".format(46))  # inteiro1    
    print("Data {:02d}/{:02d} ".format(9, 4))    
    print("Data {:02d}/{:02d} ".format(19, 11))    
        
    # exemplo de f-string    
    nome = 92    
    print(f'Meu nome é {nome}')"""


if(__name__ == "__main__"):
    jogar()
