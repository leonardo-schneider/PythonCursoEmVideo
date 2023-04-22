from random import randint
numeros = randint(0,10)
print("Hoje voce vai tentar acertar o numero do robo")
tentativas = 0
acertou = False
while not acertou:
    j1= int(input("seu palpite: "))
    tentativas += +1
    if j1 == numeros:
        acertou = True
        print("Parabéns voce acertou em {} tentativa".format(tentativas))
    else:
        if j1 < numeros:
           print("Mais... tente novamente:")
        else:
            print("Menos... tente novamente:")


