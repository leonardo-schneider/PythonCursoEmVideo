print("Hoje vamos descobrir se suas 3 retas vao formar um triangulo")
a = float(input("Digite o primeiro valor: "))
b = float(input("Digite o segundo valor: "))
c = float(input("Digite o terceiro valor: "))

if a < b + c and b < a + c and c < a + b:
    print("formam um triangulo")
else:
    print("Nao formam um triangulo")
