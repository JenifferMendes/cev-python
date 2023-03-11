"""Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e
seu antecessor"""

num = int(input('Digite um número: '))
antecessor = num - 1
sucessor = num + 1
print(f'O número que você digitou foi {num}.', end=' ')
print(f'Seu antecessor é {antecessor}, o seu sucessor é {sucessor}!')