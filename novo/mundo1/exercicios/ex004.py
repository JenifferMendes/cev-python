"""
Faça um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo
e todas as informaçoes possiveis sobre ela.
"""


something = input("Digite algo: ")

print(
    f"{type(something)}\n"
    f"Ele é uma alfa-númerico: {something.isalnum()}\n"
    f"Ele só tem letras: {something.isalpha()}\n"
    f"Ele é um ascii: {something.isascii()}\n"
    f"Ele é um decimal:{something.isdecimal()}\n"
    f"Ele é um digito: {something.isdigit()}\n"
    f"Ele é um identifier: {something.isidentifier()}\n"
    f"Ele tá em minusculo: {something.islower()}\n"
    f"Ele é um número: {something.isnumeric()}\n"
    f"Ele tem espaço: {something.isspace()}\n"
    f"Ele é um titulo: {something.istitle()}\n"
    f"Ele ta em maiusculo: {something.isupper()}\n"
)
