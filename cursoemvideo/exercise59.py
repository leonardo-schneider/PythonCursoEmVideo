n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
menu = 0
while menu != 5:
    menu = int(input(""" O que voce gostaria de fazer com os seguintes numeros
[1] somar
[2] multiplicar
[3] maior
[4] solicitar novos numeros
[5] sair do programa
Digite para uma das opçoes: """))
    if menu == 1:
        soma = n1 + n2
        print("A soma dos números é {}".format(soma))

    elif menu == 2:
        multiplica = n1 * n2
        print("A multiplicaçao dos numeros é {}".format(multiplica))

    elif  menu == 3:
        if n1 > n2:
            print("O maior número é o {}".format(n1))

        else:
            print("O maior número é o {}".format(n2))
    elif menu == 4:
        print("Digite os novos números")
        n1 = int(input("Digite o primero número: "))
        n2 = int(input("Digite o segundo número: "))
    else:
        print("Voce informou um valor nao correspondente, tente novamente")

print("O programa acabou")



