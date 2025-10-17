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
