"""Faça um programa que leia uma frase pelo teclado e mostre:
- quantas vezes aparece a letra A
- em que posição ela aparece a primeira vez
- em que posição ela aparece a última vez"""


frase = input('digite uma frase: ').strip().lower()

letra_a = frase.count('a')
primeiro_a = frase.find('a')
ultimo_a = frase.rfind('a')

print(f'A frase digitada foi "{frase}"')
print(f'A frase contém {letra_a} a')
print(f'O primeiro a aparece na posição {primeiro_a}')
print(f'O ultimo a aparece na posição {ultimo_a}')
