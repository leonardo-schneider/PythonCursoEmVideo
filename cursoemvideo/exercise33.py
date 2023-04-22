print("Vamos ver se voce pode ser aprovado para o financiamento da casa")
valor = float(input("Digite o valor da casa: "))
salario = float(input("Digite o seu salário: "))
tempo = float(input("Digite em quantos anos voce quer pagar: "))
tempo = tempo * 12
b = salario * 0.30
a = valor / tempo
if a < b:
    print("""Voce foi aprovado porque para pagar uma casa de {} em {} meses,"
          voce vai ter uma prestaçao de {:.2f} """ .format(valor,tempo,a))
else:
    print("""voce foi recusado porque a casa de {} teria que ter prestaçoes de {:.2f} "
          para ser paga em {} meses""". format(valor,a,tempo))

