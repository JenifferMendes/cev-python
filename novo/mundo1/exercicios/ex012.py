""" Faça um algoritmo que leia o preço de um produto e mostre seu novo preço,
com 5% desconto """

preco = float(input('Qual é o preço do produto? '))
precoDesconto = preco * 0.95
print(f'O preço do produto é {preco:.2f}, com desconto de 5% fica: {precoDesconto:.2f}')
