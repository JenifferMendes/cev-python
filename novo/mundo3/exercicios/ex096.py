"""
Faça um programa que tenha uma função chamada área(), que receba as dimensões de
um terreno retangular(largua e comprimento) e mostre a área do terreno.

"""


def area(l: float, c: float):
    terreno = l * c
    print(f"A área de um terreno {l}x{c} é de {terreno:.1f}m²")


largura = float(input())
comprimento = float(input())

area(largura, comprimento)
