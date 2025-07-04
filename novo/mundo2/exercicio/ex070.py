"""
Crie um programa que leia o nome e o preço de vários produtos. o programa deverá
perguntar se o usuário vai continuar. No final, mostre:
a) qual é o total gasto na compra.
b)quantos produtos custam mais de 1000.
c) qual é o nome do produto mais barato.
"""


n = 49
dash = "\n" + "~" * n
dash_espaco = "\n" + "=" * n + "\n"

print(dash_espaco, f"{'ATACADÃO K-JOTUME':^{n}}", dash_espaco)

nome_barato = " "
quantidade = soma = maior = barato = 0

while True:
    print(f"{'PASSANDO PRODUTO':^{n}}", dash)

    nome_produto = str(input("Digite o nome do produto: "))
    preco_produto = float(input("Digite o preço do produto: R$"))

    soma += preco_produto
    quantidade += 1

    if quantidade == 1 or preco_produto < barato:
        barato = preco_produto
        nome_barato = nome_produto

    if preco_produto > 1000:
        maior += 1

    continuar = ["S", "N"]
    opcao = " "
    while opcao not in continuar:
        opcao= input(
            "Deseja adicionar mais alguma coisa? [S/N]"
        ).strip().upper()
    if opcao == "N":
        break

    print(dash)

print(
    dash_espaco,
    (
        f"\bO total da compra foi de: {soma}.\n"
        f"O produto mais barato foi: {nome_barato}.\n"
        f"Foram {maior} produtos com mais de R$1000.\n"
        "Obrigada por comprar com Atacadão K-JOTUME.\n"
        "Volte sempre!"
    ),
    dash_espaco,
)
