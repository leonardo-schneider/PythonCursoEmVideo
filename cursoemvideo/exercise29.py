ano = int(input("Coloque o ano para descobrir se ele é bissexto: "))
a = ano % 4
if a == 0:
    print("O ano {} é bissexto" .format(ano))
else:
    print("o ano nao é bissexto")