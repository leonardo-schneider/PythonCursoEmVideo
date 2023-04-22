from random import choice
pri = str(input("primeiro aluno:"))
seg = str(input("segundo aluno:"))
ter = str(input("terceiro aluno:"))
qua = str(input("quarto aluno:"))
lista = [pri,seg,ter,qua]
escolhido = choice(lista)
print("o escolhido foi: {}" .format(escolhido))

