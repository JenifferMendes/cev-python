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
    finally:
        a.close()


def cadastrarPessoa(nomearquivo,nome = "Desconhecido",idade = 0):
    try:
        a = open(nomearquivo, "at")
    except:
        print("Houve um ERRO ao abrir o arquivo")
    else:
        try:
            a.write(f"{nome};{idade}\n")
        except:
            print("Houve um ERRO na hora de escrever os dados!")
        else:
            print(f"Novo registro de {nome} adicionado.")
            a.close()