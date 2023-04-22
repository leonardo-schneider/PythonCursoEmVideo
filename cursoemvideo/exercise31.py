sal = float(input("digite o seu salário: "))
if sal > 1250.00:
    a = sal * 0.10 + sal
    print("Voce recebeu um aumento de 10% e o seu salario agora é {}".format(a))
else:
    b = sal * 0.15 + sal
    print("Voce recebeu um aumento de 15% e o seu salario agora é {}" .format(b))