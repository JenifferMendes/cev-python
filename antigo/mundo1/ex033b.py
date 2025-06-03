"""Faça um programa que leia três números e mostre qual é o maior e qual é o menor."""


numero_um = int(input('Digite um número: '))
numero_dois = int(input('Digite outro número: '))
numero_tres = int(input('Digite outro número: '))

numeros = [numero_um, numero_dois, numero_tres]
numeros.sort()

print(f'O menor número digitado foi {numeros[0]} e o maior foi {numeros[2]}')
