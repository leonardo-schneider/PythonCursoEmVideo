num = [[], []]
total = 0
for c in range(1,8):
    total = int(input(f"Digite o {c} valor: "))
    if total % 2 == 0:
        num[0].append(total)
        num[0].sort()
    else:
        num[1].append(total)
        num[1].sort()
print(f"Os números pares sao {num[0]}")
print(f"Os números impares sao {num[1]}")
print(f"Os números sao {num}")