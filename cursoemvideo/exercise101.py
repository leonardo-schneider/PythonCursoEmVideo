def fatorial(num=1, show=False):
    """

    :param num: o num é o que voce quer fatorar
    :param show: (opcional) mostra o calculo ou nao
    :return: retorna o valor de f
    """
    f = 1
    for c in range(num, 0 , -1):
        if show:
            print(f"{c}", end=" ")
            if c > 1:
                print("x", end=" ")
            else:
                print("=", end=" ")
        f *= c
    return f




print(fatorial(5))