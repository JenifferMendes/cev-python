"""Escreva um programa que leia um valor em metros e o exiba convertido em 
centimentros e milimetros"""

metros = int(input('Digite um número: '))
centimetros = metros * 100
milimetros = metros * 1000

print(f'O valor digitado foi {metros}m que é igual a {centimetros}cm e {milimetros}mm')
