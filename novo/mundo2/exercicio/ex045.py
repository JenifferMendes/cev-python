"""
Crie um programa que faça o computador jogar jokenpo com voce.
"""


import random


pc = random.randint(1,3)

print(pc)
print("Vamos jogar jokenpo, escolha um dos números para me vencer.")

jokenpo = int(input("Digite 1-pedra, 2-tesoura, 3-papel"))

if pc == jokenpo:
    print(f"Ambos tiraram: {jokenpo}. Deu empate!!")
elif pc == 1:
    escolha = "Pedra"
    if jokenpo == 2:
        print(f"Tesoura perde para {escolha}. Você perdeu!!")
    elif jokenpo == 3:
        print(f"Papel ganha de {escolha}. Você ganhou!!")
elif pc == 2:
    escolha = "Tesoura"
    if jokenpo == 1:
        print(f"Pedra ganha de {escolha}. Você ganhou!!")
    elif jokenpo == 3:
        print(f"Papel perde para {escolha}. Você perdeu!!")
elif pc == 3:
    escolha = "Papel"
    if jokenpo == 1:
        print(f"Pedra perde para {escolha}. Você perdeu!!")
    if jokenpo == 2:
        print(f"Tesoura ganha de {escolha}. Você ganhou!!")
