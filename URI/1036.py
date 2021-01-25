# formula de Bhaskara


from math import sqrt


a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))


x_positivo = ((-b + sqrt((b ** 2) - 4 * a * c)) / (2 * a))
x_negativo = ((-b - sqrt((b ** 2) - 4 * a * c)) / (2 * a))

print("R1 = {:.5f} ".format(x_positivo))
print("R2 = {:.5f} ".format(x_negativo))
