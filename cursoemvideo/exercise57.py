import random
numero = random.randint(0,10)
tentativa = 1
print("Olá tente adivinhar o mesmo número do nosso robo, ele vai de 0 a 10")
a1 = int(input("Digite um número de 0 a 10: "))
while numero != a1:
    a1 = int(input("Voce errou, tente novamente: "))
    tentativa += +1
    if numero == a1:
        print("Voce acertou, seu numero foi {} e do robo {}, voce conseguiu em {} tentativas".format(a1,numero,tentativa))
