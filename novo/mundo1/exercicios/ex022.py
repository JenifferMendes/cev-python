"""
Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiusculas
- O nome com todas as minusculas
- Quantas letras ao total(sem considerar espaços)
- Quantas letras tem o primeiro nome
"""


nome_completo = input("Qual é o seu nome completo? ")

nome_completo_upper = nome_completo.upper()
nome_completo_lower = nome_completo.lower()
nome_completo_split = nome_completo.split()
nome_completo_join = "".join(nome_completo_split)
nome_completo_len = len(nome_completo_join)
primeiro_nome_len = len(nome_completo_split[0])

print(
    f"O seu nome é {nome_completo}.\n" 
    f"Seu nome em maiusculo fica: {nome_completo_upper}.\n"
    f"Em minusculo fica: {nome_completo_lower}.\n"
    f"Seu nome completo tem {nome_completo_len} caracteres.\n"
    f"E o primeiro tem {primeiro_nome_len} caracteres.\n"
)
