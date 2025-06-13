"""
Elabore um programa que calcule o valor a ser pago por um produto, considerando
considerando o seu preço normal e condição de pagamento:

- a vista dinheiro/cheque: 10% de desconto
- a vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão 20% de juros.
"""


produto = float(input("Digite o preço do seu produto: R$"))

print("Escolha o metodo do pagamento abaixo, com base no número.")
print(
    "1 - a vista em cash/cheque,\n"
    "2 - a vista no cartao,\n"
    "3 - 2x no cartao,\n"
    "4 - 3x ou + no cartao"
)

metodo_pagamento = int(input("Digite o número referente ao metodo: "))

if metodo_pagamento == 1:
    preco = produto * .9
    print(f"Você irá pagar {preco:,.2f} uma vez em cash ou cheque.")
elif metodo_pagamento == 2:
    preco = produto * .95
    print(f"Você irá pagar {preco:,.2f} uma vez no cartão.")
elif metodo_pagamento == 3:
    parcela = produto / 2
    print(f"Você irá pagar duas parcelas de {parcela:,.2f}, pelo valor normal.")
elif metodo_pagamento == 4:
    preco = produto * 1.20
    print(f"Voce irá pagar {preco:,.2f}, e pode parcelar em 3 vezes ou mais.")
else:
    print(f"Você digitou o número errado.")
