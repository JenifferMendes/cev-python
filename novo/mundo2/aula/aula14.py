"""
laços de repetição. parte 02


for precisa de um limite

nesse caso, quando precisamos de algo que não tem limite, vamos usar o while
enquanto nao maça
    passo
pega
while not maça:
    passo
pega


while not maça:
    if chão:
    ande
    if buraco:
    pule
    if moeda:
    pegue
pega
"""

resposta = "S"
while resposta == "S":
    n = int(input("Digite um valor: "))
    resposta = str(input("Quer continuar? [S/N]")).upper()
print("Fim")