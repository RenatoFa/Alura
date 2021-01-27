def jogar():
    print("********************************")
    print("Bem vindo no jogo da Forca")
    print("********************************")

    palavra_secreta = "banana"
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]

    enforcou = False
    acertou = False

    while(not enforcou and not acertou):

        # funcao .strip() = retira o espaço do input ou de uma string
        # funcao .upper() = passa a string para letras maiusculas
        chute = (input("Qual é a letra? ")).strip().upper()

        # find nao vai funcionar , pois existe letras repetidas
        # vamos implementar um for para pecorrer a palavra

        index = 0
        for letra in palavra_secreta:
            if chute == letra.upper():
                letras_acertadas[index] = letra
            index += 1
        print(letras_acertadas)

        print("jogando...")


if(__name__ == "__main__"):
    jogar()
