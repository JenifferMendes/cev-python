"""
Escreva um programa que leia dois números inteiros e compare-os
mostrando na tela uma mensagem:
- o primeiro valor é maior
- o segundo valor é maior
- não existe valor maior. os dois são iguais.
"""


numero_um = int(input("Digite o número um: "))
numero_dois = int(input("Digite o número dois: "))

if numero_um > numero_dois:
    print(f"O primeiro valor é o maior")
elif numero_um < numero_dois:
    print(f"O segundo valor é maior")
elif numero_um == numero_dois:
    print(f"não existe valor maior. Os dois são iguais.")
