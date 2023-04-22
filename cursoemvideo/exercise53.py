menor = 0
totidade = 0
mediaidade = 0
maioridadehomem = 0
velho = ' '
for stats in range(1,5):
    nome = str(input("Digite o nome da {} pessoa: ".format(stats)))
    idade = int(input("Digite a idade da {} pessoa: ".format(stats)))
    sexo = str(input("Digite o sexo da {} pessoa [M/F]: ".format(stats))).upper()
    totidade += idade
    mediaidade = totidade / 4
    if sexo == "F":
        if idade <= 20:
            menor += +1

    if stats == 1 and sexo == "M":
        maioridadehomem = idade
        velho = nome
    else:
        if idade > maioridadehomem:
            maioridadehomem = idade
            velho = nome


print("O homem mais velho tem {} e é o {}" .format(maioridadehomem, velho))
print("A media de idade é {} " .format(mediaidade))
print("Tem {} mulheres menor de 20 anos".format(menor))




