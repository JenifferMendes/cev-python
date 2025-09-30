def aumentar(valor, aumento):
    aumento_total = valor * (1 + aumento/100)
    return aumento_total


def diminuir(valor, diminuir):
    diminuir_total = valor * (1 - diminuir/100)
    return diminuir_total


def dobrar(valor):
    dobro = valor * 2
    return dobro


def metade(valor):
    a_metade = valor / 2
    return a_metade
