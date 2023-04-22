numeros = ("Zero", "Um", "Dois", "Tres", "Quatro", "Cinco",
            "Seis", "Sete", "Oito", "Nove", "Dez", "Onze",
           "Doze", "Treze", "Quatorze", "Quinze",
           "Dezesseis", "Dezessete", "Dezoito", "Dezenove", "Vinte")
while True:
    num = int(input("Digite seu número entre 0 e 20: "))
    if 0 <= num <= 20:
        print(f"O seu valor é {numeros[num]}")
        break
    print("Tente novamente")


