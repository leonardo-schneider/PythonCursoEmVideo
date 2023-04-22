pessoa = dict()
pessoas = list()
escolha = 's'
mulher = media =0
while escolha not in "Nn":
    pessoa['nome'] = str(input("Digite o nome: "))
    pessoa['idade'] = int(input("Digite a idade: "))
    pessoa['sexo'] = str(input("Digite o sexo: ")).lower()
    pessoas.append(pessoa.copy())
    escolha = str(input("Voce quer continuar? [S/N]"))
print(pessoas)
print(f"O numero total de cadastrados foi {len(pessoas)}")
print(f"O número total de mulheres foi {mulher}")
print(media)
