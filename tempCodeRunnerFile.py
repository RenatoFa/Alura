<<<<<<< HEAD
# -*- coding: utf-8 -*-
=======

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

>>>>>>> ab222570db11d95bc0a5db265c366d43a151cefe
