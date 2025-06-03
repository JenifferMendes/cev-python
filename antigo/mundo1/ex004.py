"""
Faça um programa que leia algo pelo teclado e mostre na telao seu tipo primitivo
e todas as informações possíveis sobre ela.
"""

n1 = input('Digite algo: ')
print(type(n1))
print(f'Ele é um alfa-númerico: {n1.isalnum()}')
print(f'Ele só tem letras: {n1.isalpha()}')
print(f'Ele é um ascii: {n1.isascii()}')
print(f'Ele é um decimal: {n1.isdecimal()}')
print(f'Ele é um digito: {n1.isdigit()}')
print(f'Ele é um identifier: {n1.isidentifier()}')
print(f'Ele tá em minusculo: {n1.islower()}')
print(f'Ele é um número: {n1.isnumeric()}')
print(f'Ele tem espaço: {n1.isspace()}')
print(f'Ele é um titulo: {n1.istitle()}')
print(f'Ele ta em maisculo: {n1.isupper()}')