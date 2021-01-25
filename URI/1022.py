A = int(input("Digite o numero A: "))
B = int(input("Digite o numero B: "))
C = int(input("Digite o numero C: "))
D = int(input("Digite o numero D: "))

B_maior_C = B > C
D_maior_A = D > A


soma_C_D = C + D
soma_A_B = A + B

C_e_D_positivo = C > 0 and D > 0 and A % 2 == 0


if (B_maior_C and D_maior_A):
    if(soma_C_D > soma_A_B):
        if(C_e_D_positivo == True):
            print("Valores aceitos")
else:
    print("Valores não aceitos")
