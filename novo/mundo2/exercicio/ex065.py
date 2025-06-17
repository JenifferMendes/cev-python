"""
Crie um programa que leia varios numeros inteiros pelo teclado. No final da
execução, mostre a media entre todos os valores e qual foi o maior e o menor
valor lido. o programa deve perguntar ao usuario se ele quer ou nao continuar a 
digitar valores.
"""


opcao = 0
soma = 0
quantidade = 0
maior = 0
menor = 0

while opcao != "N":
    numero = int(input("Digite um número: "))
    soma += numero
    quantidade += 1
    media = soma / quantidade
    if quantidade == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    opcao = input(
        "Deseja continuar?\n"
        "[S] sim para continuar\n"
        "[N] não para sair\n"
    ).upper()
    print(maior, menor)
print(
    f"Você digitou {quantidade} números.\n"
    f"A soma entre eles é {soma} e a média {media:.2f}.\n"
    f"O maior número que você digitou foi {maior} e o menor: {menor}.\n"
)
