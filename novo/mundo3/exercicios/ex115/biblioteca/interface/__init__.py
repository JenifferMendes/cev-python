def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("ERRO: por favor, digite um número inteiro válido")
            continue
        except (KeyboardInterrupt):
            print("Entrada de dados interrompida pelo usuário")
            return 0
        else: 
            return n


def dash(tamanho = 40):
    return "-" * tamanho


def titulo(texto):
    print(dash())
    print(texto.center(40))
    print(dash())


def menu(lista):
    titulo("MENU PRINCIPAL")
    for p,l in enumerate(lista):
        print(p + 1," - ",(l))
    print(dash())
    opcao = leiaInt("Sua Opção: ")
    return opcao
