"""Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas letras maiusculas
O nome com todas minusculas
Quantas letras ao todo(sem considerar espaços)
Quantas letras tem o primeiro nome"""


nome = input('Qual é o seu nome completo?').strip()

nome_maiusculo = nome.upper()
nome_minusculo = nome.lower()
nome_total = nome.split()
nome_letras_total = len(''.join(nome_total))
nome_letras_primeiro = len(nome_total[0])

print(f'O nome em maiusculo fica {nome_maiusculo}')
print(f'O nome em minusculo fica {nome_minusculo}')
print(f'o total de letras do nome completo é {nome_letras_total} ')
print(f'o total de letras no primeiro nome é {nome_letras_primeiro} ')
