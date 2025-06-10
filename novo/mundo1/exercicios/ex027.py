"""
Faça um programa que leia o nome completo de uma pessoa, mostrando
em seguida o primeiro e o ultimo nome separadamente.
"""


name = input("Digite seu nome inteiro:  ")

name_separado = name.split()
name_primeiro = name_separado[0]
name_tamanho = len(name_separado)
name_ultimo = name_separado[name_tamanho - 1 ]

print(
    f"O nome completo é {name},\n"
    f"O primeiro é = {name_primeiro}\n" 
    f"O último é = {name_ultimo}."
)
