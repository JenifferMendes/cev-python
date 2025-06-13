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
sexo = int(input( 
    "Qual é o seu sexo?\n"
    "[1] Mulher\n" 
    "[2] Homem\n"
))

if sexo == 2:
    idade = ano - nascimento
    if idade == 18:
        print("Está na hora de se alistar.")
    elif idade > 18:
        tempo = idade - 18
        alistar = ano - tempo
        print(
            f"Você tem {idade} anos, já passou {tempo} anos. "
            f"Você deveria se alistar em {alistar}."
        )
    else:
        tempo = 18 - idade
        alistar = nascimento + 18
        print(
            f"Você tem {idade} anos, ainda não está na idade para servir, "
            f"falta {tempo} anos. "
            f"Você deverá se alistar em {alistar}."
        )
elif sexo == 1:
    print("Você é mulher e não precisa se alistar.")
