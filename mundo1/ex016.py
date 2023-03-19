"""Crie um programa que leia um número Real qualquer pelo teclado e 
mostre na tela a sua porção Inteira"""


from math import floor


numero = float(input('Digite um número: '))

numero_inteiro1 = floor(numero)
numero_inteiro2 = numero // 1
numero_inteiro3 = int(numero)

print(f'O número é {numero}, a parte inteira é {numero_inteiro1}')
print(f'O número é {numero}, a parte inteira é {numero_inteiro2}')
print(f'O número é {numero}, a parte inteira é {numero_inteiro3}')
