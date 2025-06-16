"""
Crie um programa que leia dois valores e mostre um menu na tela
[1]somar
[2]multiplicar
[3]maior
[4]novos números
[5]sair do programa

seu programa devera realizar a operaçao solicitada em caada caso
"""


numero_um = int(input("Digite um número: "))
numero_dois = int(input("Digite outro número: "))

print("Escolha uma das opções abaixo")


opcao = 0
while opcao != 5:
    print(
        "[1] Somar\n"
        "[2] Multiplicar\n"
        "[3] Maior\n"
        "[4] Novos números\n"
        "[5] Sair do programa\n"
    )
    opcao = int(input("Digite sua opção: "))
    if opcao == 1:
        soma = numero_um + numero_dois
        print("=" * 20, "\n")
        print(f"A soma: {numero_um} + {numero_dois} = {soma}.\n")
        print("=" * 20)
    if opcao == 2:
        multiplicacao = numero_um * numero_dois
        print("=" * 20, "\n")
        print(
            f"A multiplicacao: {numero_um} x {numero_dois} = {multiplicacao}.\n"
        )
        print("="* 20)
    if opcao == 3:
        if numero_um > numero_dois:
            print("=" * 20, "\n")
            print(f"O número {numero_um} é maior que o número {numero_dois}.\n")
            print("="* 20)
        elif numero_um < numero_dois:
            print("=" * 20, "\n")
            print(f"O número {numero_dois} é maior que o número {numero_um}.\n")
            print("="* 20)
        else:
            print("=" * 20, "\n")
            print(f"os números são iguais.\n")
            print("="* 20)
    if opcao == 4:
            print("=" * 20, "\n")
            print("digite novamente")
            numero_um = int(input("Digite um número: "))
            numero_dois = int(input("Digite outro número: "))
            print("="* 20)
    if opcao < 5:
        print("Escolha uma nova opção")

print("Obrigado por usar o programa!")