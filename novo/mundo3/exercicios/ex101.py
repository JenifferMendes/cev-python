"""
Crie um programa que tenha uma função chamada voto() que vai receber como
parâmetro o ano de nascimento de uma pessoa, retornando um valor literal
indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.
"""


from datetime import date


def voto(ano):
    idade = date.today().year - ano
    if idade < 16:
        valor = 'NEGADO'
    elif 18 > idade >= 16 or idade > 70:
        valor = 'VOTO OPCIONAL'
    else:
        valor = 'VOTO OBRIGATÓRIO'
    print(f"Com {idade} anos: ", end="")
    return valor


ano = int(input("Em que ano você nasceu? "))
print(f"{voto(ano)}.")
