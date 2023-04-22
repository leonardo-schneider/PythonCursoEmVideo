from random import randint
from time import sleep
from operator import itemgetter
jogadores = {
"jogador 1": randint(1,6),
"jogador 2": randint(1,6),
"jogador 3": randint(1,6),
"jogador 4": randint(1,6)}
print("=-"*20)
print("          VALORES SORTEADOS               ")
for k, v in jogadores.items():
    print(f"{k} tirou {v} no dado", end=" ")
    sleep(1)
    print()
ranking = sorted(jogadores.items(), key=itemgetter(1),reverse=True)
print("=-" *20)
print("           RANKING DOS JOGADORES               ")
for k, v in enumerate (ranking):
    print(f"{k+1} lugar: {v[0]} com o número {v[1]}")
    sleep(1)
print("--FIM--")




