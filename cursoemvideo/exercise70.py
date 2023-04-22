saque = int(input("Qual vai ser o valor do saque?"))
valor = saque
cedulas = 50
totcedulas = 0
while True:
    if valor >= cedulas:
        valor -= cedulas
        totcedulas += 1
    else:
        if totcedulas > 0:
            print(f"O total de {totcedulas} de {cedulas} R$ ")
        if cedulas == 50:
            cedulas = 20
        elif cedulas == 20:
            cedulas = 10
        elif cedulas == 10:
            cedulas = 1
        totcedulas = 0
        if valor == 0:
            break




