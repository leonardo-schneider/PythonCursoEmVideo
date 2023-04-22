
while True:
    n = int(input("Digite o número que voce quer a tabuada: "))
    print("->" * 10)
    if n < 0:
        break
    for c in range(1,11):
        multiplica = n * c
        print(f"{n} X {c} = {multiplica}")
print("O seu programa acabou")







