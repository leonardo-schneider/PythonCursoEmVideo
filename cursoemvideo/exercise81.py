lista = list()
listab= list()
listac= list()
while True:
    n = int(input("Digite seu número: "))
    lista.append(n)
    escolha = str(input("Voce quer continuar: S/N "))
    if n % 2 == 0:
        listab.append(n)
    else:
        listac.append(n)
    if escolha in "Nn":
        break

print(f"A sua lista é formada pelos seguintes números{lista}")
print(f"Os números pares da sua lista sao {listab}")
print(f"Os números impares da sua lista sao {listac}")