aluno = dict()
alunos = list()
aluno["nome"] = str(input("Nome do aluno: "))
aluno["media"] = float(input("Média do aluno: "))
alunos.append(aluno.copy())
for p in alunos:
    for k, v in p.items():
        print(f"{k} é {v}")
    if aluno['media'] >= 6:
        print(f"{aluno['nome']} foi aprovado")
    else:
        print(f"{aluno['nome']} foi reprovado")