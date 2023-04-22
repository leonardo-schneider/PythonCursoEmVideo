from random import randint
from time import sleep
lista = list()
palpites = list()
decisao = int(input("Quantos jogos voce quer sortear?" ))
totaljogos = 0
while totaljogos < decisao:
    cont = 0
    while True:
        numeros = randint(1,60)
        if numeros not in lista:
            lista.append(numeros)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    palpites.append(lista[:])
    lista.clear()
    totaljogos += 1
print(f"Sorteando {decisao} jogos")
print("=-" * 15)
for i,v in enumerate(palpites):
    print(f"jogo {i+1}, {v}")
    sleep(1)
print("        BOA SORTE       ")





