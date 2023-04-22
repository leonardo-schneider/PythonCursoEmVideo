#def soma(a, b):
# print(f"A soma de {a} + {b}")
 #  s = a + b
 #   print(f"O resultado vai ser {s}")


#programa principal
#soma(b=6, a=8)
#soma(7, 8)
#soma(9, 9)
#soma(10, 12)

#def contador(*num):
 #   for v in num:
 #       print(v + 25)
 #   tam = len(num)
 #   print(tam)


#contador(8, 9, 6, 2, 1)
#contador(19, 3, 20)
#contador(0)
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos+= 1

def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f"A soma do {valores} é {s}!")


soma(3, 8, 5)
soma(4, 9, 17, 22)
soma(3, 2)
valores = [3, 8, 5, 19, 2]
dobra(valores)
print(valores)
