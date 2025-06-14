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

if jokenpo == pc:
    print(f"Ambos tiraram: {opcao_pc}. Deu empate!!")
elif jokenpo == 0:
    if pc == 1:
        print(f"{opcao_pc} perde de Pedra. Você ganhou!!")
    elif pc == 2:
        print(f"{opcao_pc} ganha de Pedra. Você perdeu!!")
elif jokenpo == 1:
    if pc == 0:
        print(f"{opcao_pc} ganha de Tesoura. Você perdeu!!")
    elif pc == 2:
        print(f"{opcao_pc} perde de Tesoura. Você ganhou!!")
elif jokenpo == 2:
    if pc == 0:
        print(f"{opcao_pc} perde de Papel. Você ganhou!!")
    elif pc == 1:
        print(f"{opcao_pc} ganha de Papel. Você perdeu!!")
else:
    print("opcão invalida")
