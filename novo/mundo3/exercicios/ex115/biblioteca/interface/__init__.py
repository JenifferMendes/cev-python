def dash(tamanho = 40):
    return "-" * tamanho


def titulo(texto):
    print(dash())
    print(texto.center(40))
    print(dash())


def menu(lista):
    titulo("MENU PRINCIPAL")
    for p,l in enumerate(lista):
        print(p + 1,l)
    print(dash())
