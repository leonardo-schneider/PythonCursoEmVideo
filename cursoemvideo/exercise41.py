preco = float(input("Digite aqui o valor do seu produto: "))
print(""" Digite qual sua forma de pagamento:
1. Pagamento em dinheiro/ cheque a vista
2. Pagamento no cartao a vista
3. Pagamento no cartao em 2x
4. Pagamento no cartao 3x""")
a = int(input("Qual é a opçao?"))
if a == 1:
    dinheiro = preco - preco * 0.10
    print("Sua compra de {} vai custar {:.2f}" .format(preco,dinheiro))
elif a == 2:
    cartao = preco - (preco * 0.05)
    print("Sua compra de {} vai custar {:.2f}" .format(preco, cartao))
elif a == 3:
    v = preco / 2
    print("Sua compra de {} vai custar em 2x de {:.2f}" .format(preco,v ))
elif a == 4:
    parcela = int(input("Em quantas vezes voce vai querer parcelar? "))
    a = (preco * 0.20) + preco
    parcelado = a / parcela
    print("Sua compra de {} vai custar {:.2f} em {} vezes com juros ficando um total de {:.2f}" .format(preco, parcelado, parcela, a))
else:
    print("Nenhuma das opcoes foi selecionada, tente novamente")