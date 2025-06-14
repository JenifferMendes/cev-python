"""
Crie um programa que faça o computador jogar jokenpo com voce.
"""


import random


pc = random.randint(0,2)

print("Vamos jogar jokenpo, escolha um dos números para me vencer.")

jokenpo = int(input(
    "Digite uma das opções abaixos\n" 
    "[ 0 ] pedra\n"
    "[ 1 ] tesoura\n"
    "[ 2 ] papel\n"
    ""
))

opcoes = ["Pedra", "Tesoura", "Papel"]
opcao_pc = opcoes[pc]

if jokenpo == 1 or jokenpo == 2 or jokenpo == 0:
    if pc == jokenpo:
        print(f"Ambos tiraram: {opcao_pc}. Deu empate!!")
    elif pc == 0:
        if jokenpo == 1:
            print(f"Tesoura perde para {opcao_pc}. Você perdeu!!")
        elif jokenpo == 2:
            print(f"Papel ganha de {opcao_pc}. Você ganhou!!")
    elif pc == 1:
        if jokenpo == 0:
            print(f"Pedra ganha de {opcao_pc}. Você ganhou!!")
        elif jokenpo == 2:
            print(f"Papel perde para {opcao_pc}. Você perdeu!!")
    elif pc == 2:
        if jokenpo == 0:
            print(f"Pedra perde para {opcao_pc}. Você perdeu!!")
        if jokenpo == 1:
            print(f"Tesoura ganha de {opcao_pc}. Você ganhou!!")
else:
    print("opcão invalida")
