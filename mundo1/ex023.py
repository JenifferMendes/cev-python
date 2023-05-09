"""Faça um programa que leia um número de 0 a 9999 e mostre na tela cada 
um dos dígitos separados"""


numero = int(input('Digite um número de 0 a 9999: '))

unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10

print(f'O número digitado foi {numero}')
print(f'A unidade: {unidade}  ')
print(f'A dezena: {dezena}')
print(f'A centena: {centena} ')
print(f'O milhar: {milhar}')
