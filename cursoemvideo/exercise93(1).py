galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa["nome"] = str(input("Digite o nome: "))
    while True:
        pessoa["sexo"] = str(input("Digite o sexo [F/M]: "))
        if pessoa["sexo"] in "FfMm":
            break
        print("Erro, digite M ou F")
    pessoa["idade"] = int(input("Digite a idade: "))
    soma += pessoa["idade"]
    galera.append(pessoa.copy())
    while True:
        decisao = str(input("Voce quer continuar? [S/N]")) .upper()[0]
        if decisao in "SsNn":
            break
        print("Erro, digite S ou N")
    if decisao == 'N':
        break
print(f"Ao todo temos {len(galera)} pessoas")
media = soma / len(galera)
print(f"A media de idade das pessoas é {media:.2f}")
print(f"As mulheres cadastradas foram", end=" ")
for p in galera:
    if p['sexo'] in "Ff":
        print(f"{p['nome']}", end=" ")
print()
print("As pessoas acima da media sao: ")
for p in galera:
    if p['idade'] >= media:
        print("     ", end=" ")
        for k, v in p.items():
            print(f"{k} = {v};", end=" ")
print()
print("------ENCERRADO------")


