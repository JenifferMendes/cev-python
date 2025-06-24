"""
Faça um programa que ajude um jogador da mega sena a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números
entre 1 a 60 para cada jogo, cadastrando tudo em uma lista composta.
"""


from random import randint
from time import sleep


jogos_megasena = []
jogo = []
c = 24
n = 49
dash_simples = "-" * n
dash = "\n" + dash_simples + "\n"

print(dash_simples)
print(f"{'JOGA NA MEGA SENA':^{n}}")
print(dash_simples)

quantidade_jogos = int(input("Quantos jogos você quer que eu sorteie? "))

print(f"{'SORTEANDO: 0':.>{c}}{quantidade_jogos}{' JOGOS':.<{c}}")

for c in range(0, quantidade_jogos):
    for num in range(0, 6):
        numero = randint(1, 60)
        jogo.append(numero)
    jogos_megasena.append(jogo[:])
    jogo.clear()

for posicao, num in enumerate(jogos_megasena, 1):
    num.sort()
    print(f"Jogo {posicao}: {num}")
    sleep(0.5) 

print(f"{' < BOA SORTE! > ':.^{n}}")
