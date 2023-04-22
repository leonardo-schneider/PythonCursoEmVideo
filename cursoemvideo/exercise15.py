from math import sqrt
oposto = float(input("Digite o numero do cateto oposto: "))
adj = float(input("Digite o numero do cateto adjacente: "))
hyp = (sqrt (oposto ** 2 + adj ** 2))
print("A hipotenusa do triangulo retangulo é {:.2f}" . format(hyp))