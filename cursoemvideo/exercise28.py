v = float(input("Qual a distancia da viagem? "))
if v <= 200:
    a = v * 0.50
    print("O custo da sua viagem é de {}" .format(a))
else:
    b = v * 0.45
    print("O custo da sua viagem é de {}" .format(b))