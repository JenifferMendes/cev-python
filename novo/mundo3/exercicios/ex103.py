"""
Faça um programa que tenha um função chamada ficha(), que receba dois parâmetros
opcionais: o nome de um jogador e quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado 
nao tenha sido informado.
"""


def ficha(name='<desconhecido>', gols=0):
    print(f"O jogador {name} fez {gols} gol(s) no campeonato.")


nome = input("Nome do Jogador: ")
gol = input("Número de Gols: ")
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if nome.strip() == '':
    ficha(gols=gol)
else:
    ficha(nome, gol)
