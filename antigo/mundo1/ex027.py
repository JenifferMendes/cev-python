"""Faça um programa que leia o nome completo de uma pessoa, mostrando em 
seguida o primeiro e último nome separadamente."""


nome = input('digite seu nome completo: ').strip()

nome_completo = nome.split()
primeiro_nome = nome_completo[0]
ultimo_nome = nome_completo[-1]

print(f'O nome completo é {nome_completo}')
print(f'O primeiro nome é {primeiro_nome}')
print(f'O ultimo nome é {ultimo_nome}')
