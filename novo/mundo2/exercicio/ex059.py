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

dash = "\n" + "=" * 20 + "\n"

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
        print(dash)
        print(f"A soma: {numero_um} + {numero_dois} = {soma}.")
        print(dash)
    elif opcao == 2:
        multiplicacao = numero_um * numero_dois
        print(dash)
        print(
            f"A multiplicação: {numero_um} x {numero_dois} = {multiplicacao}."
        )
        print(dash)
    elif opcao == 3:
        if numero_um > numero_dois:
            print(dash)
            print(f"O número {numero_um} é maior que o número {numero_dois}.")
            print(dash)
        elif numero_um < numero_dois:
            print(dash)
            print(f"O número {numero_dois} é maior que o número {numero_um}.")
            print(dash)
        else:
            print(dash)
            print(f"Os números são iguais.")
            print(dash)
    elif opcao == 4:
        print(dash)
        print("Digite novamente")
        numero_um = int(input("Digite um número: "))
        numero_dois = int(input("Digite outro número: "))
        print(dash)
    if opcao < 5:
        print("Escolha uma nova opção: ")
    if opcao > 5:
        print("Opção invalida! Escolha uma opção abaixo: ")
print(dash)
print("Obrigado por usar o programa!")
print(dash)
