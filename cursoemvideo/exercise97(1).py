from time import sleep


def contador(i, f, c):
    print("--" * 18)
    print(f'vamos contar de {i} ate {f} de {c} em {c}')
    print("--" * 18)
    if c < 0:
        c *= -1

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=" ")
            cont += c
            sleep(0.5)
        print()
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end= " ")
            cont -= c
            sleep(0.5)
        print()




contador(1,10,1)
contador(10, 0, 2)
print("Agora é sua vez de personalizar a contagem!")
inic = int(input("Digite o seu primeiro número: "))
fim = int(input("Digite o seu ultimo número: "))
conta = int(input("Digite de quanto em quanto voce quer contar: "))
contador(inic,fim, conta)