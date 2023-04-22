def fatorial(num=1):
    f = 1
    for c in range(num, 0 , -1):
        f *= c
    return f


r1 = fatorial(4)
r2 = fatorial(6)
r3 = fatorial(2)

print(f"O resultado dos fatoriais sao {r1}, {r2}, {r3}")
