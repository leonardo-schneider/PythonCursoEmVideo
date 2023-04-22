lista = ("Pao", 1,
         "Manteiga", 4,
         "Arroz", 3,
         "Erva-mate",10,
         "Cuia", 35,
         "Atum", 4.50,
         "Caderno", 7,
         "Livro", 40,
         "Bola", 120,
         "Queijo", 5.50)
print("Listagem de preço")
print("---" * 12)
for p in range(0,18):
    if p % 2 == 0:
        print(f"{lista[p]:.<30}", end="")
    else:
        print(f"R${lista[p]:5.2f}")
