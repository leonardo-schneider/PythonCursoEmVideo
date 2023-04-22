from random import randint
v = 0
while True:
    print("VAMOS JOGAR PAR OU IMPAR")
    numero = int(input("Voce quer escolher qual numero:"))
    robo = randint(0, 20)
    soma = numero + robo
    escolha = " "
    while escolha not in "IP":
        escolha = str(input("Voce quer par ou impar? [P/I]")).upper().strip()
    if escolha == "I":
        if soma % 2 == 0:
            print(f"Voce perdeu porque {numero} + {robo} é {soma} que é par")
            break
        else:
            print(f"Voce ganhou porque {numero} + {robo} é {soma} e é impar")
            v += 1

    if escolha == "P":
        if soma % 2 == 0:
            print(f"Voce ganhou porque {numero} + {robo} é {soma} e é par")
            v += 1
        else:
            print(f"Voce perdeu porque {numero} + {robo} é {soma} que é impar")
            break

print(f"Voce ganhou um total de {v} consecutivas")
print("Game over")