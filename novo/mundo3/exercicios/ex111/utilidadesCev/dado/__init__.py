from ..moeda import moeda, dobrar, metade, aumentar, diminuir


def resumo(valor=0, taxaa=10, taxab=5):
    n = 35
    dash = "-" * n
    print(dash)
    print("RESUMO DO VALOR".center(30))
    print(dash)
    print(f"Preço analisado: \t{moeda(valor)}")
    print(f"Dobro do preço: \t{dobrar(valor, True)}")
    print(f"Metade do preço: \t{metade(valor, True)}")
    print(f"{taxaa}% de aumento: \t{aumentar(valor, taxaa, True)}")
    print(f"{taxab}% de redução: \t\t{diminuir(valor, taxab, True)}")
    print(dash)
