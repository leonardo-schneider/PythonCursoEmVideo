lista = list()
pares = list()
impares = list()
for n in range(1,8):
    lista.append(int(input(f"digite o {n} numero: ")))
    for numero in lista:
        if numero % 2 == 0:
            pares.append(lista[:])
            pares.sort()
        else:
            impares.append(lista[:])
            impares.sort()
        lista.clear()

print(f"Os números pares sao {pares}")
print(f"Os números impares sao{impares}")
