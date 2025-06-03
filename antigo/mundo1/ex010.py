"""Crie um programa que leia quanto dinheiro uma pessoa tem a certeira e mostre 
quantos Dólares ela pode comprar"""


real = float(input('Digite a quantidade de reais que você possui: '))

dolar = 3.27
quantidade_dolar = real / dolar

print(f'A quantidade de dolar que você pode ter com R${real} é igual a U${quantidade_dolar:.2f}')
