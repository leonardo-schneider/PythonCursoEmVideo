print("Gerador de PA")
primeiro = int(input("Digite o primeiro termo da sua PA: "))
razao = int(input("Digite a razao da sua PA:"))
termo = primeiro
count = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while count <= total:
        print(termo)
        termo += razao
        count += 1
    print("PAUSE")
    mais = int(input("Digite mais quantos termos voce quer ver? "))
print("O programa acabou com {} termos formados" .format(total))









