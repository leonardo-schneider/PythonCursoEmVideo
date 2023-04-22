def ficha(nome="desconhecido", gols=0):
    print(f"O {nome} fez {gols} gols")




n = str(input("Nome do Jogador: "))
g = str(input("Gols do jogador: "))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n,g)
