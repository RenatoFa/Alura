
numero_advinhacao = 30
chute = int(input("Digite um numero: "))

acertou = numero_advinhacao == chute
maior = numero_advinhacao < chute
menor = numero_advinhacao > chute

if (acertou):
    print("Voce acertou!!!")
elif(maior):
    print("Você errou! O seu chute foi maior que o numero de advinhacao ")
elif(menor):
    print("Você errou! O seu chute foi menor que o numero de advinhacao ")
27
