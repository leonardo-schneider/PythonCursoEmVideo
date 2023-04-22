jogador = dict()
partidas = list()
jogador["nome"] = str(input("Nome do jogador: "))
tot = int(input(f"Numero de jogos feito pelo {jogador['nome']}: "))
for c in range(0 , tot):
    partidas.append(int(input(f"Quantos gols ele fez na partida {c}: ")))
jogador['jogos'] = tot
jogador['golspartida'] = partidas[:]
jogador['total'] = sum(partidas)
print("=-" * 20)
print(jogador)
print("=-" * 20)
for k, v in jogador.items():
    print(f"{k} é igual a {v}")
print("=-" * 20)
print(f"O jogador {jogador['nome']} jogou {len(jogador['golspartida'])} partidas e fez {jogador['total']} gols")
for i, v in enumerate(jogador['golspartida']):
    print(f"O jogador {jogador['nome']} na partida {i} fez {v} gols")


