"""
Faça um programa que jogue par ou impar com o computador. O jogo será
interrompido quando o jogador PERDER. Mostrando o total de vitórias
consecutivas que ele conquistou no final do jogo.
"""


from random import randint


quantidade = 0
dash = "\n" + "~" * 20 + "\n"

print(dash)
print("Preparado para jogar: PAR OU IMPAR?")

while True:
    print(dash)
    numero_pc = randint(0,10)
    numero_jogador = int(input("Digite um número: "))
    soma = numero_pc + numero_jogador
    opcao = input(
        "[P] para Par \n"
        "[I] para Impar \n"
        "Qual sua opção: "
    ).strip().upper()[0]
    print(f"Jogador: {numero_jogador}, PC: {numero_pc}, SOMA: {soma}")
    if opcao == "P":
        if soma % 2 == 0:
            print("Você ganhou - Par")
            quantidade += 1
            print(1)
        else:
            print("Você perdeu - Impar")
            print(2)
            break
    else: 
        if soma % 2 == 0:
            print("Você perdeu - Par")
            print(3)
            break
        else:
            print("Você ganhou - Impar")
            print(4)
            quantidade += 1
print(f"Você ganhou {quantidade} vezes. Porém perdeu a última. \nFim")
