"""Faça um programa que leia um número inteiro e mostre na tela o seu sucessor 
e seu antecessor."""

num = int(input('digite um número: '))
numAntecessor = num - 1
numSucessor = num + 1
print(f'O número que você digitou foi: {num}', end="")
print(f', o seu antecessor é: {numAntecessor}', end="")
print(f', o seu sucessor é: {numSucessor}.')
