jogador = dict()
partidas = list()
atletas = list()
while True:
    jogador.clear()
    partidas.clear()
    jogador["nome"] = str(input("Nome do jogador: "))
    tot = int(input(f"Numero de jogos feito pelo {jogador['nome']}: "))
    for c in range(0 , tot):
        partidas.append(int(input(f"Quantos gols ele fez na partida {c}: ")))
    jogador['jogos'] = tot
    jogador['golspartida'] = partidas[:]
    jogador['total'] = sum(partidas)
    atletas.append(jogador.copy())
    while True:
        decisao = str(input("Voce quer continuar? [S/N]")) .upper()
        if decisao in "SsNn":
            break
        print("Voce errou, apenas S ou N")
    if decisao == "N":
        break
print("=-" * 20)
print("cod", end=" ")
for i in jogador.keys():
    print(f"{i:<15}", end="")
print()
for k, v in enumerate(atletas):
    print(f"{k:>3}", end=" ")
    for d in v.values():
        print(f"{str(d):<15}", end=" ")
    print()
print("=-" * 20)
while True:
    busca= int(input("Digite o codigo para buscar dados do jogador: (999 para parar)"))
    if busca == 999:
        break
    if busca > len(atletas):
        print("ERRO, Esse atleta nao existe, digite novamente")
    else:
        print(f"------- LEVANTAMENTO DO {atletas[busca]['nome'].upper()}-------")
        print(f"{atletas[busca]['nome'].upper()} fez {atletas[busca]['total']} gols em {tot} partidas sendo:")
    for i,g in enumerate (atletas[busca]['golspartida']):
        print(f"No jogo {i+1} fez {g} gols")
