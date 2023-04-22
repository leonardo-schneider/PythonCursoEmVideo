a = int(input("Digite seu primeiro valor:"))
b = int(input("Digite seu segundo valor:"))
c = int(input("Digite seu terceiro valor:"))
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
print("O menor numero é o {}" .format(menor))
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print("O maior numero é o {}" .format(maior))