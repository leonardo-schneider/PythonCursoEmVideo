from datetime import datetime
pessoa = dict()
pessoa["nome"] = str(input("Digite seu nome: "))
pessoa["idade"] = datetime.now().year - int(input("Digite o seu ano de nascimento: "))
pessoa["CTPS"] = int(input("Digite o numero da sua carteira de trabalho(0 se nao tiver): "))
if pessoa["CTPS"] != 0:
    pessoa["primeiro emprego"] = int(input("Ano do primeiro emprego: "))
    pessoa["salario"] = int(input("Digite o seu salário: R$ "))
    pessoa["aposentadoria"] = 35 - (datetime.now().year - pessoa["primeiro emprego"])
    pessoa["idade de aposentar"] = pessoa['idade'] + pessoa['aposentadoria']
    if pessoa["aposentadoria"] > 35:
        print("Voce pode se aposentar")
    else:
        print(f"Faltam {pessoa['aposentadoria']} anos para voce se aposentar")
for k,v in pessoa.items():
    print(f"{k} tem o valor {v}")
else:
    print("FIM")
