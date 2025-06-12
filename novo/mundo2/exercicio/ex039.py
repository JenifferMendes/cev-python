"""
Faça um programa que leia o ano de nascimento de um jovem e informe de acordo
com sua idade:
- se ele ainda vai se alistar ao serviço militar.
- seé hora de se alistar.
- se ja passou do tempo do alistamento.

O seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""


from datetime import date


ano = date.today().year

nascimento = int(input("Digite o ano de nascimento: "))

idade = ano - nascimento

if idade == 18:
    print("Está na hora de servir o exercito.")
elif idade > 18:
    print(f"Você tem {idade} anos, já passou {idade - 18} anos.")
elif idade < 19:
    print(f"Você ainda não está na idade para servir, falta {18 - idade} anos")
