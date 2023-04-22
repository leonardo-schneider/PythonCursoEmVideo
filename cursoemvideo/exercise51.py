from datetime import date
data = date.today().year
totmaior = 0
totmenor = 0
for p in range(1,8):
    ano = int(input("Em que ano a {} pessoa nasceu?".format(p)))
    idade = data - ano
    if idade >= 21:
        totmaior += + 1
    else:
        totmenor += + 1
print("O numero de pessoas maior de idade é {}".format(totmaior))
print("O numero de pessoas menor de idade é {}" .format(totmenor))




