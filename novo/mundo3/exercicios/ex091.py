"""
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
guarde esses resultados em um dicionario. no final, coloque esse dicionario
em ordem, sabendo que o vencedor tirou o maior numero no dado.
"""


from random import randint
from time import sleep
from operator import itemgetter


jogadores = {}
ranking = {}

print("valores sorteados: ")

for c in range(1, 5):
    key = f"Jogador{c}"
    jogadores[key] = randint(1,6)
    print(f"O {key} tirou {jogadores[key]} no dado.")
    sleep(0.5)

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

print(ranking)
