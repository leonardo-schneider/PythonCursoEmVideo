from time import sleep


def contador(inic, fim, passo):
    print("CONTANDO DE 1 ATE 10 DE 1 EM 1")
    while inic < 10:
        inic += 1
        print(f"{inic}", end=" ")
        sleep(1)
    print()
    print("CONTANDO DE 10 ATE 0 DE 2 EM 2")
    while fim > 1:
        fim -= 2
        print(f"{fim}", end=" ")
        sleep(1)
    print()
    print("AGORA É SUA HORA DE PERSONALIZAR")
    while passo < 40:
        passo += 4
        print(f"{passo}", end=" ")
        sleep(1)
    print()





a = 0
b = 12
c = 0
contador(a, b, c)
