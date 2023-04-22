continuar = "S"
maioridade = homens = mulher = 0
while continuar == "S":
    idade = int(input("Qual a idade? "))
    sexo = " "
    while sexo not in "MmFf":
        sexo = str(input("Qual o sexo [F/M]? ")).upper().strip()
    continuar = str(input("Voce quer continuar[S/N]? ")).upper()
    print("-" * 12)
    if idade >= 18:
        maioridade += 1
    if sexo == "M":
        homens += 1
    elif sexo == "F" and idade <= 20:
        mulher += 1
    while continuar not in "SsNn":
        continuar = str(input("Voce quer continuar[S/N]? ")).upper()
    if continuar == "N":
        break
    print("-" * 12)
print(f"Tem {maioridade} pessoas maiores de 18 anos.")
print(f"{homens} homens foram cadastrados.")
print(f"{mulher} mulheres com menos de 20 anos foram cadastradas.")



