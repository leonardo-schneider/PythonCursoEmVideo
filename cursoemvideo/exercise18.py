from random import shuffle
n1 = str(input("primeiro aluno:"))
n2 = str (input("segundo aluno:"))
n3 = str (input("terceiro aluno:"))
n4 = str (input ("quarto aluno:"))
listad = [n1,n2,n3,n4]
shuffle(listad)
print("a ordem é:")
print(listad)