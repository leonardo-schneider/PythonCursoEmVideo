from datetime import date
n1 = int(input("Digite o ano de nascimento: "))
print("Vamos analisar que categoria ele vai competir")
data = date.today().year
idade = data - n1
if idade <= 9:
    print("Voce tem {} anos e sua categoria é a mirim" .format(idade))
elif idade <= 14:
    print("Voce tem {} anos e sua categoria é infantil" .format(idade))
elif idade <= 19:
    print("Voce tem {} anos e sua categoria é junior" .format(idade))
elif idade <= 20:
    print("voce tem {} anos e sua categoria é senior" .format(idade))
else:
    print("Voce ja tem mais de 20 anos e sua categoria é master")
