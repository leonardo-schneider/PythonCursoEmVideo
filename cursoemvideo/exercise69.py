total = maisdemil = barato = cont = menor = 0

while True:
    nome = str(input("Qual o nome do produto? "))
    preco = float(input("Qual o valor do produto?"))
    cont += 1
    total += preco
    if preco >= 1000:
        maisdemil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = nome


    escolha = str(input("Voce quer continuar? [S/N] ")).upper()
    if escolha == "N":
        break
print(f"O valor total foi de {total}")
print(f"Tem {maisdemil} produtos custando mais de 1000")
print(f"O produto mais barato é {menor} e se chama {barato}")
