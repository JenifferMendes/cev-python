def aumentar(valor=0, aumento=0, format=False):
    aumento_total = valor * (1 + aumento/100)
    return aumento_total if format is False else moeda(aumento_total)


def diminuir(valor=0, diminuir=0, format=False):
    diminuir_total = valor * (1 - diminuir/100)
    return diminuir_total if format is False else moeda(diminuir_total)


def dobrar(valor=0, format=False):
    dobro = valor * 2
    return dobro if not format else moeda(dobro)


def metade(valor=0, format=False):
    a_metade = valor / 2
    return a_metade if not format else moeda(a_metade)


def moeda(valor = 0, moeda = "R$"):
    return f"{moeda}{valor:>.2f}".replace(".",",")


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
