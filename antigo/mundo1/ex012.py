"""Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com
5% de desconto"""


preco = float(input('Digite o preço do produto: '))

desconto = preco * 0.05
total = preco - desconto

print(f'O valor do produto é R${preco:.2f} e o seu valor com desconto de 5% é R${total:.2f}')
