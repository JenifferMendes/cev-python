"""
Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
o primeiro que indique o número a calcular e o outro chamado show, que será
um valor lógico(opcional) indicando se será mostrado ou não na tela o processo
de cálculo do fatorial.
"""


def fatorial(num, show=0):
    """
    -> Calcula o Fatorial de um número.
    :param num: O número a ser calculado.
    :param show:(opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número num.
    """
    fatorial = 1
    print("-" * 30)
    for c in range(num, 0, -1):
        fatorial *= c
        if show != 0:
            print(f"{c} x ", end="")
    if show != 0:
        print(f"= {fatorial}")
    return fatorial


numero = int(input())
show = int(input())
print(fatorial(numero, show))
