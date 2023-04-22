def notas(*nota, sit=False):
    """
    :param nota: Notas que vao mostrar a maior,menor,quantidade de notas e a medias delas
    :param sit: mostra se pode ser aprovado/reprovado(opcional)
    :return: aluno e suas notas
    """
    aluno = dict()
    aluno['maior'] = max(nota)
    aluno['menor'] = min(nota)
    aluno['quantidade'] = len(nota)
    aluno['media'] = sum(nota) / len(nota)
    if sit:
        if aluno['media'] > 8:
            print("Parabéns voce esta muito bem")
        if aluno['media'] < 8 and aluno['media'] > 6:
            print("Voce precisa melhorar")
        if aluno['media'] < 6:
            print("Voce vai reprovar desse jeito")
    return aluno




resp = notas(7.5, 10, 7, sit=True)
print(resp)