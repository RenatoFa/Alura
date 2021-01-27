def jogar():
    print("********************************")
    print("Bem vindo no jogo da Forca")
    print("********************************")
    print("Fim de jogo")

    palavra_secreta = "banana"

    enforcou = False
    acertou = False

    while(not enforcou and not acertou):

        # funcao .strip() = retira o espaço do input ou de uma string
        # funcao .upper() = passa a string para letras maiusculas
        chute = (input("Qual é a letra? ")).upper().strip()

        # find nao vai funcionar , pois existe letras repetidas
        # vamos implementar um for para pecorrer a palavra

        index = 0
        for letra in palavra_secreta:
            if chute == letra.upper():
                print("Encontrei a letra: {} na posição {}".format(
                    letra, index))
            index += 1

        print("jogando...")


if(__name__ == "__main__"):
    jogar()
