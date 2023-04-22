sexo = str(input("Digite o seu sexo [M/F]: ")).strip().upper()
while sexo not in "MF":
    sexo = str(input("Combinaçao invalida, tente novamente: ")).strip() .upper()
print("Registro do sexo {} concluido com sucesso" .format(sexo))