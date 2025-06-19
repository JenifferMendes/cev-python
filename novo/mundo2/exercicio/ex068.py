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
    tipo = ["P", "I"]
    opcao = " "
    while opcao not in tipo:
        opcao = input(
            "[P] para Par \n"
            "[I] para Impar \n"
            "Qual sua opção: "
        ).strip().upper()
    print(f"Jogador: {numero_jogador}, PC: {numero_pc}, SOMA: {soma}")
    if not (soma % 2 == 0 and opcao == "P" or soma % 2 == 1 and opcao == "I"):
        break
    print("Você ganhou, vamos jogar novamente!")
    quantidade += 1
print(f"Você ganhou {quantidade} vezes. Porém perdeu a última. \nFim")
