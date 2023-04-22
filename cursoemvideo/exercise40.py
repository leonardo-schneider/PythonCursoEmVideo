
print("Ola hoje vamos medir seu IMC")
peso = float(input("Comece colocando seu peso: "))
altura = float(input("Agora coloque sua altura"))
print ("Estamos calculando...")
altura = altura * altura
imc = peso / altura
if imc <= 18.5:
    print("Seu imc é {:.2f} e voce esta abaixo do peso" .format(imc))
elif imc <= 25:
    print("Seu imc é {:.2f} voce esta no peso ideal" .format(imc))
elif imc <= 30:
    print("Seu imc é {:.2f} e voce esta sobrepeso" .format(imc))
elif imc <= 40:
    print("Seu imc é {:.2f} e voce esta obeso". format(imc))
else:
    print("seu imc é {:.2f} e voce esta com obesidade morbida" .format(imc))
