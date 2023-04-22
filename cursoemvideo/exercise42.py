from random import randint
from time import sleep
itens = ("pedra", "papel", "tesoura")
computador = randint(0,2)
print("Hoje vamos jogar jokenpo")
print("Voce tem 3 opçoes, pedra, papel e tesoura")
print("""0. Pedra
1. Papel
2. tesoura""")
jogador = int(input("Escolha com qual voce vai jogar: "))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO")
sleep(1)
print("--"* 25)
print("O jogador jogou {} e o computador {} ".format(itens[jogador],itens[computador]))
print("--" * 25)
if computador == 0:# computador jogou pedra
    if jogador == 0:
        print("Voces empataram")
    elif jogador == 1:
        print("Parabens voce embrulhou a pedra")
    elif jogador == 2:
        print("Voce perdeu e sua tesoura foi quebrada")
    else:
        print("Jogada invalida")

elif computador == 1: # computador jogou papel
    if jogador == 0:
        print("Voce perdeu e foi embrulhado pelo papel do computador")
    elif jogador == 1:
        print("Voces empataram")
    elif jogador == 2:
        print("Voce ganhou e cortou o papel")
    else:
        print("Combiancao invalida, tente novamente")
elif computador == 2: # computador jogou tesoura
    if jogador == 0:
        print("Parabéns voce ganhou e quebrou a tesoura do computador")
    elif jogador == 1:
        print("Voce perdeu e foi cortado pela tesoura do computador")
    elif jogador == 2:
        print("Voces empataram")
    else:
        print("Combinacao invalida, tente novamente")
else:
    print("combinaçao invalida, tente novamente")


