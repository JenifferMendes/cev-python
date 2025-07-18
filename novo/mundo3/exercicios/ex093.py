"""
Crie um programa que gerencie o aproveitamento de um jogador de futebol.
o programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler
a quantidade de gols feitos em cada partida. No final, tudo isso será guardado
em um dicionário, incluindo o total de gols feitos durante o campeonato.
"""


jogador = {}
gols = []
n = "=-" * 30


jogador['nome']= input("Nome do jogador: ")
partidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))

total = 0

for p in range(0, partidas):
    qgol = int(input(f"quantos gols na partida {p + 1}: "))
    gols.append(qgol)
    total += qgol

jogador["gols"] = gols[:]
jogador["total"] = total

print(n)
print(jogador)
print(n)
for k,v in jogador.items():
    print(f"O campo {k} tem o valor {v}.")
print(n)
print(f"O jogador {jogador['nome']} jogou {partidas} partidas.")

for p, g in enumerate(gols):
    print(f"     => Na partida {p + 1}, fez {g} gols.")
print(f"Foi um total de {total} gols.")
