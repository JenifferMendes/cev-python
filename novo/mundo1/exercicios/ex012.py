"""
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço,
com 5% desconto
"""


preco = float(input("Qual é o preço do produto? "))

preco_desconto = preco * .95

print(
    f"O preço do produto é {preco:.2f}"
    f", com desconto de 5% fica: {preco_desconto:.2f}"
)
