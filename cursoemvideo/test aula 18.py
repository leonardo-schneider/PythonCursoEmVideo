galera = [["Joao", 25],["leonardo", 24],["mateus", 32],["catarina", 28]]
#for p in galera:
#    print(f"Essa lista tem {p[0]} e sua idades é {p[1]}")
pessoal = list()
dados = list()
for c in range(0,2):
    dados.append(str(input("Qual o seu nome?")))
    dados.append(int(input("Qual a sua idade?")))
    pessoal.append(dados[:])
    dados.clear()
for p in pessoal:
    if p[1] >= 21:
        print(f"{p[0]} é de maior")
print(pessoal)