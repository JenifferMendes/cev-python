"""Crie um algoritmo que leia um número e mostre o seu dobro, triplo e
raiz quadrada"""


num = int(input('Digite um número: '))

dobro_num = num * 2
triplo_num = num * 3
raiz_quadrada_num = num ** (1/2)

print(f'O número que você digitou foi {num}')
print(f'O dobro de {num} é igual a {dobro_num}')
print(f'O triplo de {num} é igual a {triplo_num}')
print(f'A raiz quadrada de {num} é igual a {raiz_quadrada_num}')
