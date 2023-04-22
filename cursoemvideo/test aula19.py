#dados = dict()
#dados = {"nome": "Pedro", "sexo": "M", "idade": 25}
#dados["nome"] = "Leonardo"
#dados["Peso"] = 70
#dados["idade"] = 24
#dados["sexo"]= "M"
#del dados["sexo"]
#print(dados)
#for k, v in dados.items():
#        print(f"o {k} é {v}")
#brasil = []
#estado1 = {"uf": "Rio grande do sul", "sigla": "RS"}
#estado2 = {"uf": "Sao paulo", "sigla": "SP"}
#brasil.append(estado1)
#brasil.append(estado2)
#print(brasil[0]["sigla"])
brasil = list()
estado = dict()
for c in range (0,3):
        estado["uf"] = str(input("Unidade Federativa: "))
        estado["Sigla"] = str(input("Sigla: "))
        brasil.append(estado.copy())
for e in brasil:
        print(f"O estado é {e}")