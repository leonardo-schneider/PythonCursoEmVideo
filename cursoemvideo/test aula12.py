nome = str(input("qual é o seu nome? "))
if nome == "leonardo":
    print("Que nome bonito")
elif nome in "Ana  Claudia Josiane":
    print("que belo nome feminino")
else:
    print("Seu nome é bem comum")
print("Tenha um ótimo dia {}" .format(nome))
