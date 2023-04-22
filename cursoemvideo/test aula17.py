#num = [5, 6, 8, 3]
#num[1] = 4
#num.sort(reverse=True)
#num.append(10)
#num.insert(0, 5)
#num.pop(2)
#num.sort()
#num.remove(8)
#if 6 in num:
#    num.remove(6)
#else:
 #   print("Nao é possivel remover o numero 6 porque ele nao exite")
#print(num)
#print(f"Essa lista tem {len(num)} elementos")

#lista = []
#lista.append(9)
#lista.append(3)
#lista.append(5)
#lista.append(8)
#lista.insert(0, 10)
lista = list()
for count in range(0,4):
    lista.append(int(input("Digite seu valor: ")))
for v in lista:
    print(f"O valor {v} está na sua lista")
for c, v in enumerate (lista):
    print(f"Na posiçao {c} da lista encontrei o valor {v}")
print("Final da lista")

a = [2,4,5,8]
b = a[:] #dessa maneira eu nao crio uma ligaçao entre elas e ai posso modificar os valores
b[2] = 3
print(f"Lista A: {a}")
print(f"Lista B: {b}")











