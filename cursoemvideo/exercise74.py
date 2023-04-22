numeros = (int(input("Digite, seus numeros: ")),
            int(input("Digite, seus numeros: ")),
            int(input("Digite, seus numeros: ")),
            int(input("Digite, seus numeros: ")))
print(f"O numero 9 aparece {numeros.count(9)} vezes")
if 3 in numeros:
    print(f"O número 3 está na posiçao {numeros.index(3) +1}")
else:
    print(f"O numéro 3 nao foi encontrado em nenhuma posiçao")
for n in numeros:
    if n % 2 == 0:
        print(f"O número {n} é par")
