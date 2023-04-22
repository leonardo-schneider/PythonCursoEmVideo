n = int(input("Quantos termos da sequencia de Fibonacci voce quer ver?"))
t1 = 0
t2 = 1
count = 3
print( "{} - {}" .format(t1,t2), end= " ")
while count <= n:
    t3 = t2 + t1
    count += 1
    t1 = t2
    t2 = t3
    print("- {}" .format(t3), end=" ")
print("FIM")