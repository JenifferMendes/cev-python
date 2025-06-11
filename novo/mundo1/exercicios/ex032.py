"""
Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
"""


ano = int(input("Digite um ano: "))

if ano % 4 != 0:
    print("Não é bissexto")
elif ano % 100 != 0:
    print("é bissexto")
elif ano % 400 == 0:
    print("é bissexto")
else:
    print("Não é bissexto")
