
def voto(a):
    from datetime import datetime
    idade = datetime.now().year - a
    if idade < 16:
        return f"Voce ainda nao pode votar porque voce tem {idade} anos"
    elif idade < 18 or idade > 65:
        return f"O seu voto é opcional porque voce tem {idade} anos"
    else:
        return f"O seu voto é obrigatorio porque voce tem {idade} anos"




#programa
print(voto(int(input("Digite o seu ano de nascimento: "))))

