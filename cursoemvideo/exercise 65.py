total = soma = 0
while True:
    n = int(input("Digite seu número: "))
    if n == 999:
        break
    total += 1
    soma += n
print(f"O total de numeros foi {total} e a soma foi {soma}")
