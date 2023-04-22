from random import randint


def sorteia(lista):
    for v in range (0,5):
        n= randint(1,100)
        lista.append(n)
        print(f"{n}", end=" ")


def somapar(lista):
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma += n
    print(f"A soma dos números pares {lista} é {soma}")





numeros = list()
sorteia(numeros)
somapar(numeros)

