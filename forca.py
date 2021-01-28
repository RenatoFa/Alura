import random


def imprime_abertura():
    print("********************************")
    print("Bem vindo no jogo da Forca")
    print("********************************")


def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))

    palavra_secreta = palavras[numero].upper()

    return palavra_secreta


def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]


def jogar():

    imprime_abertura()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):

        # funcao .strip() = retira o espaço do input ou de uma string
        # funcao .upper() = passa a string para letras maiusculas
        chute = (input("Qual é a letra? ")).strip().upper()
        # find nao vai funcionar , pois existe letras repetidas
        # vamos implementar um for para pecorrer a palavra
        # A tupla é uma sequecia tambem ( igual a lista) , so que ela é imutavel.

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra.upper()):
                    letras_acertadas[index] = letra
                index += 1

        else:
            erros += 1
            print("Ops, você errou! Faltam {} tentativa.".format(6-erros))

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

        if(acertou):
            print("Você ganhou!!")
        else:
            print("Tem que ganhar pow!!! Tenta mais uma vez ai.... ")


if(__name__ == "__main__"):
    jogar()
