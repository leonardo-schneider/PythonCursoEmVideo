lista = list()
while True:
    n = int(input("Digite seu número: "))
    lista.append(n)
    escolha = str(input("Voce quer continuar: S/N "))
    if escolha in "Nn":
        break
print(f"A sua lista contém os respectivos números {lista}")
print(f"A sua lista tem {len(lista)} numeros")
lista.sort(reverse=True)
print(f"A lista de valores decrescente é {lista}")
if 5 in lista:
    print(f"O número 5 esta na lista")
else:
    print(f"O numero 5 nao esta na lista")