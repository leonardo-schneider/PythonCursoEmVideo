c = ('\033[m', # 0 - branco
     '\033[0;30;41m',# 1 - vermelho
     '\033[0;30;42m',#2 - verde
     '\033[0;30;43m',#3 - amarelo
     '\033[0;30;44m',#4 -azul
     '\033[0;30;45m',#5 -roxo
     '')

def ajuda(com):
    titulo(f'Acessando o manual do comando\'{com}\'', 4)
    print(c[5], end="")
    help(com)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end="")
    print("˜" * tam)
    print(f"  {msg}")
    print("˜" * tam)
    print(c[0], end="")



#programaprincipal
comando = ''
while True:
    titulo("SISTEMA DE AJUDA PyHELP", 2)
    comando = str(input("Digite a funçao: "))
    if comando.upper() == "FIM":
        break
    else:
        ajuda(comando)
titulo("ATE LOGO!", 1)
