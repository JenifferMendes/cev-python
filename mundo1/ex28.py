"""Escreva um programa que faça o computador "pensar" em um número inteiro entre
0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo
computador.
O programa deverá escrever na tela se o usuário vencer ou perdeu."""


import random

numero = random.randint(0, 5)

numero_adivinhado = int(input('Tente adivinhar o numero entre 0 e 5: '))

if numero == numero_adivinhado:
    print(f'Acerto miseravi')
else:
    print(f'errooooooooou, o número foi {numero}')
