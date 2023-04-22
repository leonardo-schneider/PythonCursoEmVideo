totidade = 0
mediaidade = 0
maioridade = 0
idadevelho = 0
idademulher = 0
for stats in range (1,5):
    nome = str(input("digite o nome da {} pessoa: ".format(stats)))
    idade = int(input("digite a idade da {} pessoa: ".format(stats)))
    sexo = str(input("digite o sexo da {} pessoa [M/F]: ".format(stats))).lower()
    totidade += idade
    mediaidade = totidade / 4
    if stats == 1 and sexo == "m":
        maioridade = nome
        idadevelho = idade
    if idade > idadevelho:
        maioridade = nome
        idadevelho = idade
    if sexo == "f":
        if idade <= 20:
            idademulher += +1
print("O homem mais velho é o {} e a idade é {}" .format(maioridade,idadevelho))
print("A media de idade do grupo é {}" .format(mediaidade))
print("No grupo tem {} mulheres menores de idade" .format(idademulher))
