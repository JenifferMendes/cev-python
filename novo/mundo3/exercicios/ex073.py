"""
Crie uma tupla preenchida com 20 primeiros colocados da tabela do campeonato
brasileiro de futebol, na ordem de colocação. Depois mostre:
a) Apenas os 5 primeiros colocados.
b) Os últimos 4 colocados da tabela.
c) Uma lista com os times em ordem alfabética.
d) Em que posição na tabela está o time da Chapecoense.
"""


dash = "\n" * 2 + "=" * 100 + "\n" 

times = (
    "Flamengo", "Cruzeiro", "Bragantino","Palmeiras", "Bahia", "Fluminense",
    "Atlético-MG","Botafogo","Mirassol", "Corinthians", "Grêmio", "Ceará SC",
    "Vasco da Gama", "São Paulo", "Santos", "EC Vitória", "Internacional",
    "Fortaleza", "Juventude", "Sport Recife",
)

print(dash)

for time in times[:5]:
    print(f"{time} ➜ ", end="")
print("Os 5 primeiros colocados.", dash)

for time in times[-4:]:
    print(f"{time} ➜ ", end="")
print("Os 4 últimos colocados.", dash)

for time in sorted(times):
    print(f"{time} ➜ ", end="")
print("times em ordem alfabética.\n", dash)

time = input(
    "Digite o nome do time que você quer saber a posição: \n"
).strip().title()

if time in times:
    print(f"O time {time} está em {times.index(time) + 1}º no campeonato.")
else:
    print("Seu time não está no campeonato ou você digitou o nome errado.")
print("Fim")
