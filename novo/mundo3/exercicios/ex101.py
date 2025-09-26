"""
Crie um programa que tenha uma função chamada voto() que vai receber como
parâmetro o ano de nascimento de uma pessoa, retornando um valor literal
indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.
"""


from datetime import date



ano = int(input("Em que ano você nasceu? "))
idade = date.today().year - ano

def voto(ano):
    if idade < 16:
        valor = 'NEGADO'
    elif 18 > idade >= 16 or idade > 70:
        valor = 'VOTO OPCIONAL'
    else:
        valor = 'VOTO OBRIGATÓRIO'
    return valor


resultado = voto(ano)
print(f"Com {idade} anos: {resultado}")
