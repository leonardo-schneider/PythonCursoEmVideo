n = 0
total = soma = maior = menor = media = quant = 0
escolha = "Y"
while escolha == "Y":
        n = int(input("Digite seu número inteiro: "))
        escolha = str(input("Voce quer continuar? [Y/N] ")).upper()
        total += 1
        soma += n
        quant += 1
        if quant == 1:
                maior = n
                menor = n
        else:
                if n > maior:
                        maior = n
                if n < menor:
                        menor = n
        media = soma / total
        if escolha == "N":
            print("O total de números foi {} e a soma {} resultando em uma media {:.2f}".format(total, soma, media))
            print("O maior numero é {} e o menor numero é {}" .format(maior,menor))




