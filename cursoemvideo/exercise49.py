a = int(input("Digite o seu numero inteiro: "))
tot = 0
for c in range(1, a+1):
    if a % c == 0:
        print("\33[31m", end= " ")
        tot += 1
    else:
        print("\033[34m", end= " ")
    print("{}".format(c), end= " ")
print("\nO número {} foi divisivel {} vezes".format(a, tot))
if tot == 2:
    print("E por isso é um numero primo")
else:
    print("E por isso nao é um numero primo")


