matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0],]
somapar = maior = somacoluna = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f"Digite um valor para {l}, {c}: "))
for l in range(0,3):
    for c in range(0,3):
        print(f"{matriz[l][c]}", end=" ")
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
    print()
print("--" * 20)
print(f"A soma dos valores pares é {somapar}")
for l in range(0,3):
    somacoluna += matriz[l][2]
print(f"A soma da terceira coluna é {somacoluna}")
for c in range(0,3):
    if matriz[1][c] == 0:
        maior = matriz[1][c]
    else:
        if matriz[1][c] > maior:
            maior = matriz[1][c]
print(f"O maior numéro da linha dois é {maior}")


