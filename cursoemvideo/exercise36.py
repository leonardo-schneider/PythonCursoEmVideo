from datetime import date
ano = int(input("Digite o seu ano de nascimento: "))
print("Vamos analisar se voce precisa se alistar")
data = date.today().year
calc = data - ano
idade = calc - 18
if calc > 18:
    print("""Quem nasceu em {} tem {} anos 
ja passaram {} anos que voce deveria ter se alistado""" . format(ano, calc, idade))
elif calc < 18:
    idade = idade * -1
    print("""Quem nasceu em {} tem {} anos
voce vai se alistar daqui {} anos""" .format(ano, calc, idade))
else:
    print("""Quem nasceu em {} tem {} anos
e precisa se alistar agora""" .format(ano, calc))
