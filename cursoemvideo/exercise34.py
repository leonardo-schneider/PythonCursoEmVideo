num = int(input("Digite seu numero inteiro: "))
print("""
     Digite 1 se voce quer transformar esse numero em binário\n
     Digite 2 se voce quer transformar esse numero em octal\n
     Digite 3 se voce quer transformar esse numero em hexadecimal\n""")
a = int(input("digite sua opçao: "))
if a == 1:
    print("Seu número {} convertido para binário é {}" . format(num, bin(num)[2:]))
elif a == 2:
    print("Seu número {} convertido para octal é {}" .format(num, oct(num)[2:]))
elif a == 3:
    print("Seu número {} convertido para hexadecimal é {}" .format(num, hex(num)[2:]))
else:
    print("seu valor está errado")

