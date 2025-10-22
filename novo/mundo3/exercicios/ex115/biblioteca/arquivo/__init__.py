from biblioteca.interface import *


def arquivoExiste(nomedoarquivo):
    try: 
        a = open(nomedoarquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nomedoarquivo):
    try:
        a = open(nomedoarquivo, 'wt+')
        a.close()
    except:
        print("Houve um ERRO na criação do arquivo!")
    else:
        print(f"Arquivo {nomedoarquivo} criado com sucesso!")


def lerArquivo(nome):
    try:
        a = open(nome, "rt")
    except:
        print("Erro ao ler o arquivo")
    else:
        titulo("PESSOAS CADASTRADAS?")
        print(a.read())