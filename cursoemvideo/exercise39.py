print("Hoje vamos descobrir se suas 3 retas vao formar um triangulo")
a = float(input("Digite o primeiro valor: "))
b = float(input("Digite o segundo valor: "))
c = float(input("Digite o terceiro valor: "))

if a < b + c and b < a + c and c < a + b:
    if a == b and b == c and a == c:
        print("formam um triangulo Equilatero")
    elif a == b or a == c or b == c:
        print("formam um triangulo Isósceles")
    elif a != b != c:
        print("formam um triangulo Escalarte")
else:
    print("Esses numeros nao formam um triangulo")