import random
numero = random.randint(0,6)
print("Olá tente adivinhar o mesmo número do nosso robo, ele vai de 0 a 6")
a1 = int(input("Digite um número de 0 a 6: "))
if numero == a1:
    print("Parabéns voce acertou")
else:
    print("o número do robo foi {} e voce errou" .format(numero))