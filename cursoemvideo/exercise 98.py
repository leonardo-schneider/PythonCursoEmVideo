def maior(*num):
    cont = maior = 0
    print("\n Analisando os valores...")
    for valor in num:
        print(f"{valor}", end=" ")

        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f"\nForam informados {cont} valores e o maior valor é o {maior}")




maior(1,7,8,10,2,5)
maior(1,9,6,5)
maior()
maior(20,40,1,4)