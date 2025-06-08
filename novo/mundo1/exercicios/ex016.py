"""
Crie um programa que leia um número Real qualquer pelo teclado e mostre
na tela a sua porção inteira.
"""


from math import trunc


num = float(input("Digite um número: "))

num_inteiro = trunc(num)

print(f"O número {num} tem a parte inteira {num_inteiro}")
