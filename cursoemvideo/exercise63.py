total = 0
soma = 0
n = int(input("Digite seu número inteiro:(999 para parar)"))
while n != 999:
    total += 1
    soma += n
    n = int(input("Digite seu número inteiro:(999 para parar)"))
print("O total de números foi {} e a soma deles {}" .format(total,soma))
