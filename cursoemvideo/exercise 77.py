lista = []
maior = menor = 0
for v in range(0,5):
    lista.append(int(input(f"Digite o numero da posiçao {v}: ")))
    if v == 0:
        maior = menor = lista[v]
    else:
        if lista[v] > maior:
            maior = lista[v]
        if lista[v] < menor:
            menor = lista[v]
print(f"Voce digitou os valores{lista}")
for c, v in enumerate(lista):
    if v == maior:
        print(f"O maior número da lista é o {maior} e está na posiçao {c}")
    if v == menor:
        print(f"O menor número da lista é o {menor} e está na posiçao {c}")
