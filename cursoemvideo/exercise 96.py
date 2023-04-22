def escreva(txt):
    for l in txt:
        print("-", end='')
    print()
    print(txt)
    for l in txt:
        print("-", end='')
    print()






frase = str(input("Digite sua primeira frase aqui: "))

a = str(input("Digite a segunda frase aqui: "))

b = str(input("Digite sua terceira frase aqui: "))

escreva(frase)
escreva(a)
escreva(b)

