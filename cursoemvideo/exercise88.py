lista = list()
decisao = "s"
while decisao not in "Nn":
    nom = str(input("Digite seu nome: ")).title()
    n1= float(input("Digite sua primeira nota: "))
    n2 = float(input("Digite sua segunda nota: "))
    decisao = str(input("Voce quer continuar? "))
    m1 = (n1 + n2) / 2
    lista.append([nom,[n1, n2], m1])
print(f"{'N':<4} {'NOME':<10} {'MEDIA':>8}")
print("--" *12)
for i, a in enumerate(lista):
    print(f"{i:<4}{a[0]:<10} {a[2]:>8.1f}")
print("--"*12)
while True:
    opc = int(input("Qual notas de aluno voce quer ver? (999 para interromper)"))
    if opc == 999:
        print("Finalizando")
        break
    if opc <= len(lista)-1:
        print(f"notas de {lista[opc][0]} sao {lista[opc][1]}")


