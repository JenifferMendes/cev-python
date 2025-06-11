"""
Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
"""


from datetime import date


ano = int(input("Digite um ano. Coloque 0 para analisar o ano atual: "))

if ano == 0:
    ano = date.today().year
if ano % 4 != 0:
    print(f"o ano {ano} não é bissexto")
elif ano % 100 != 0:
    print(f"o ano {ano} é bissexto")
elif ano % 400 == 0:
    print(f"o ano {ano} é bissexto")
else:
    print(f"o ano {ano} não é bissexto")
