def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print("ERRO! Este numero nao é inteiro, tente novamente!")
        if ok:
            break
    return valor




#programa
n = leiaInt("Digite um número inteiro: ")
print(f"{n} é um numero inteiro")
