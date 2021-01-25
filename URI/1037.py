valor = float(input("Digite um valor: "))

if(valor < 0):
    print("Fora de intervalo")
if(0 < valor and valor < 0.25):
    print("Intervalo 0 e 0.25")
if(valor > 0.25 and valor < 25.00):
    print("Intervalo 0.25 e 25.00")
if(valor > 25.000001 and valor < 50.0000000):
    print("Valor entre 25 e 50")
if(valor > 50.0000001 and valor < 75.0):
    print("Valor entre 50 e 75")
if(valor > 75.0000001 and valor < 100):
    print("Valor entre 75 e 100")
