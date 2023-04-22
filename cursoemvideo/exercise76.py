palavras = ("estudar", "experiencia", "jogar", "trabalhar", "viver", "praia",
            "ferias","receber", "ganhar", "beber", "comer", "chimarrao","Python",
            "programacao","campeao","futebol")
for p in palavras:
    print(f"\nNa palavra {p} aparecem", end=" ")
    for letra in p:
        if letra in "aeiou":
            print(f"{letra}", end="" )


