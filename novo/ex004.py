""""
Faça um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo 
e todas as informaçoes possiveis sobre ela.
"""

something = input('Digite algo: ')
print(type(something))
print(f'Ele é uma alfa-númerico: {something.isalnum()}')
print(f'Ele só tem letras: {something.isalpha()}')
print(f'Ele é um ascii: {something.isascii()}')
print(f'Ele é um decimal:{something.isdecimal()}')
print(f'Ele é um digito: {something.isdigit()}')
print(f'Ele é um identifier: {something.isidentifier()}')
print(f'Ele tá em minusculo: {something.islower()}')
print(f'Ele é um número: {something.isnumeric()}')
print(f'Ele tem espaço: {something.isspace()}')
print(f'Ele é um titulo: {something.istitle()}')
print(f'Ele ta em maiusculo: {something.isupper()}')
