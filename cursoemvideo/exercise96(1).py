def escreva(txt):
    tam = len(txt) + 4
    print("-" * tam)
    print(f"  {txt}")
    print("-" * tam)



a = str(input("Digite sua primeira frase:"))
b = str(input("Digite sua segunda frase: "))
c = str(input("Digite sua terceira frase: "))
escreva(a)
escreva(b)
escreva(c)