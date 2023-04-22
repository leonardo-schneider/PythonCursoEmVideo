soma = 0
count = 0
for c in range(1,7):
    s = int(input("Digite seu número {} :" .format(c)))
    if s % 2 == 0:
        soma += s
        count += 1
print("A soma dos numeros pares é {} e {} valores foram selecionados" .format(soma,count))