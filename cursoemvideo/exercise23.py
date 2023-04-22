frase = str(input("digite uma frase:")).lower().strip()
print("Analizando frase")
print("O numero de vezes encontrando a letra a é {}".format(frase.count("a")))
print("A primeira vez que ela aparece é na posiçao {}" .format(frase.find("a")+1))
print("A ultima vez que ela aparece é na posiçao {}" .format(frase.rfind("a")+1))

