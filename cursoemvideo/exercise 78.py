lista = list()
while True:
    num = int(input("Digite seu valor:  "))
    if num not in lista:
        lista.append(num)
        print("Número adicionado com sucesso")
    else:
        print("Esse número é repetido e nao vou adicionar a lista")

    decisao = str(input("Voce quer continuar[S/N]? "))
    if decisao in "Nn":
        lista.sort()
        print(lista)
        break



