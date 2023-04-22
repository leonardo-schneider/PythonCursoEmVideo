def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print("Voce digitou incorretamente, tente novamente um numero inteiro")
            continue
        except(KeyboardInterrupt):
            print("Sequencia interrompida pelo usuario")
            return 0
        else:
            return n

def leiaFloat(msg):
    valor = 0
    while True:
        try:
            n = float(input(msg))
        except(TypeError, ValueError):
            print("Voce digitou errado, tente um numero real novamente")
            continue
        else:
            return n




#programa
n1 = leiaInt("Digite um número inteiro: ")
n2 = leiaFloat("Digite um número real: ")
print(f"{n1} é um numero inteiro")
print(f"{n2} é um número real")