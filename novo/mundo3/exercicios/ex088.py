"""
Faça um programa que ajude um jogador da mega sena a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números
entre 1 a 60 para cada jogo, cadastrando tudo em uma lista composta.
"""


from random import sample
from time import sleep


jogos_megasena = []
n = 49
dash_simples = "-" * n
dash = "\n" + dash_simples + "\n"

print(dash_simples)
print(f"{'JOGA NA MEGA SENA':^{n}}")
print(dash_simples)

quantidade_jogos = int(input("Quantos jogos você quer que eu sorteie? "))

print(f"{f'SORTEANDO: 0 {quantidade_jogos} JOGOS':.^{n}}")

for c in range(0, quantidade_jogos):
    numero = sample(range(1, 61), 6)
    jogos_megasena.append(numero)

for posicao, jogo in enumerate(jogos_megasena, 1):
    jogo.sort()
    print(f"Jogo {posicao}: {jogo}")
    sleep(0.5)

print(f"{' < BOA SORTE! > ':.^{n}}")
