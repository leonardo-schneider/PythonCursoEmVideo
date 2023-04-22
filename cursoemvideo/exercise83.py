lista = list()
principal = list()
listagem = maior = menor = 0
decisao = "S"
while decisao not in "Nn":
    a1 = str(input("Digite o nome:"))
    lista.append(a1)
    listagem += 1
    a2= float(input("Digite o peso:"))
    lista.append(a2)
    if len(principal) == 0:
        maior = menor = lista[1]
    else:
        if maior < lista[1]:
            maior = lista[1]
        if menor > lista[1]:
            menor = lista[1]
    principal.append(lista[:])
    lista.clear()
    decisao = str(input("Voce quer continuar? [S/N]"))
print(f"{listagem} pessoas se cadastraram")
print(f"A mais pesada é {maior} e sao os pesos de",end=" ")
for p in principal:
    if p[1] == maior:
        print(f"{p[0]}", end=" ")
print(f"A mais leve é {menor}, peso de", end=" ")
for p in principal:
    if p[1] == menor:
        print(f"{p[0]}", end= " ")
print()

