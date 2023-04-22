from ex115.lib.interface import *
from ex115.lib.arquivo import *

arq = 'Cursoemvideo.txt'
if arquivoExiste(arq):
    print("Arquivo encontrado com sucesso")
else:
    print("Arquivo nao encontrado")
    criarArquivo(arq)

while True:
    resposta = menu(['Cadastrar Pessoa', 'Mostrar lista de pessoas no sistema', 'Sair do Programa'])
    if resposta == 1:
        cabeçalho("NOVO CADASTRO")
        nome = str(input("Nome: "))
        idade = leiaInt("Idade: ")
        cadastrar(arq,nome,idade)
    elif resposta == 2:
        lerArquivo(arq)
    elif resposta == 3:
        print("SAINDO DO SISTEMA. OBRIGADO")
        break
    else:
        print("OPÇAO INVALIDA. Tente novamente")





