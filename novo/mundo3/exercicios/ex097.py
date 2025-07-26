"""
Faça um programa que tenha uma função chamada escreve(), que receba um texto
qualquer como parametro e mostre uma mensagem com tamanho adaptavel.
"""


def escreva(msg: str):
    tam = len(msg)
    c = tam + 2
    dash = "~" * c
    print(dash)
    print(f"{msg:^{c}}")
    print(dash)


escreva("Olá, Mundo!")
