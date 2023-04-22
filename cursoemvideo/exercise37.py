print("Vamos calcular sua média para ver se voce foi aprovado, esta de recuperaçao ou foi reprovado")
n1 = float(input("Digite sua primeira nota: "))
n2 = float(input("Digite sua segunda nota: "))
media = (n1 + n2) / 2
if media >= 7.0:
    print("Parabéns sua media foi {:.2f} e voce esta aprovado" .format(media))
elif media <= 5.0:
    print("Sua média foi {:.2f} e voce esta reprovado" . format(media))
elif media >= 5 and media <= 6.9:
    print("Sua média foi {:.2f} e voce esta de recuperaçao" .format(media))