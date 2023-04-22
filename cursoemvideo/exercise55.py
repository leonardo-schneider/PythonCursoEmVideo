sexo = " "
while sexo != "M" or "F":
    sexo = str(input("Digite o sexo da pessoa [M/F]: "))
    if sexo == "M":
        print("Voce é do sexo masculino")
        break
    elif sexo == "F":
        print("Voce é do sexo feminino")
        break
    else:
        print("Voce digitou errado, tente novamente")