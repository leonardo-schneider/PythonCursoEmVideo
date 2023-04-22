n = 0
cont = 0
for c in range(1 ,501, 2):
    if c % 3 == 0:
        print(c)
        cont += 1 # CONT= CONT+1
        n += c # N = N + C
print("A Soma de todos os {} valores é {}".format(cont,n))

