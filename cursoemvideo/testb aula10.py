n1 = float(input("Digite sua primeira nota: "))
n2 = float(input("Digite sua segunda nota: "))
n3 = float(input("Digite sua terceira nota: "))
nota = (n1+n2+n3) /3

print("Parabens voce passou" if nota >= 6.0 else "voce reprovou")