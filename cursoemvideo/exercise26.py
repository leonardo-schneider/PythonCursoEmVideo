vel = int(input("Qual a velocidade do carro?"))
if vel>=80:
    print("Voce foi multado por que sua velocidade é {} e o limite é 80" .format(vel))
    print("a multa vai custar R$ 7,00 reais por cada km que voce passou dos 80")
    multa = (vel - 80) * 7
    print("Sua multa é: {}" .format(multa))
else:
    print("tenha uma otima viagem")