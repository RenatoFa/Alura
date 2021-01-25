dinheiro = float(input("Digite o valor: "))

notas_de_100 = int(dinheiro // 100)
notas_de_50 = int((dinheiro - notas_de_100 * 100)//50)
notas_de_20 = int(((dinheiro - (notas_de_100 * 100) - (notas_de_50*50)))//20)
notas_de_10 = int(((dinheiro - (notas_de_100 * 100) -
                    (notas_de_50 * 50)-(notas_de_20 * 20)))//10)
notas_de_5 = int(((dinheiro - (notas_de_100 * 100) -
                   (notas_de_50 * 50)-(notas_de_20 * 20)) - (notas_de_10 * 10)) // 5)
notas_de_2 = int(((dinheiro - (notas_de_100 * 100) -
                   (notas_de_50 * 50)-(notas_de_20 * 20)) - (notas_de_10 * 10) - (notas_de_5)*5) // 2)

somatorio_notas = notas_de_100 * 100 + notas_de_50 * 50 + \
    notas_de_20 * 20 + notas_de_10 * 10 + notas_de_5 * 5 + notas_de_2 * 2

moedas_de_1 = float((dinheiro - somatorio_notas) // 1.00)
moedas_de_50 = float((dinheiro - somatorio_notas - moedas_de_1 * 1.00)//0.50)
moedas_de_25 = float((dinheiro - somatorio_notas -
                      moedas_de_1 * 1.00 - moedas_de_50 * 0.50)//0.25)
moedas_de_10 = float((dinheiro - somatorio_notas -
                      moedas_de_1 * 1.00 - moedas_de_50 * 0.50 - moedas_de_25 * 0.25)//0.10)
moedas_de_05 = float((dinheiro - somatorio_notas -
                      moedas_de_1 * 1.00 - moedas_de_50 * 0.50 - moedas_de_25 * 0.25 - moedas_de_10 * 0.10)//0.05)
moedas_de_01 = float((dinheiro - somatorio_notas -
                      moedas_de_1 * 1.00 - moedas_de_50 * 0.50 - moedas_de_25 * 0.25 - moedas_de_10 * 0.10 - moedas_de_05*0.05)//0.01)


if(dinheiro > 0 and dinheiro < 1000000.00):
    print("Valor valido")
    print("NOTAS:")
    print("{} notas(s) de R$ 100.00 ".format(notas_de_100))
    print("{} notas(s) de R$ 50.00 ".format(notas_de_50))
    print("{} notas(s) de R$ 20.00 ".format(notas_de_20))
    print("{} notas(s) de R$ 10.00 ".format(notas_de_10))
    print("{} notas(s) de R$ 5.00 ".format(notas_de_5))
    print("{} notas(s) de R$ 2.00 ".format(notas_de_2))
    print("MOEDAS:")
    print("{} moedas(s) de R$ 1.00".format(int(moedas_de_1)))
    print("{} moedas(s) de R$ 0.50".format(int(moedas_de_50)))
    print("{} moedas(s) de R$ 0.25".format(int(moedas_de_25)))
    print("{} moedas(s) de R$ 0.10".format(int(moedas_de_10)))
    print("{} moedas(s) de R$ 0.05".format(int(moedas_de_05)))
    print("{} moedas(s) de R$ 0.01".format(int(moedas_de_01)))
else:
    print("Valor inválido")
