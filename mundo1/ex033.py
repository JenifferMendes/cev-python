"""Faça um programa que leia três números e mostre qual é o maior e qual é o menor."""


numero_um = int(input('Digite um número: '))
numero_dois = int(input('Digite outro número: '))
numero_tres = int(input('Digite outro número: '))

menor = numero_um
if numero_dois < numero_um and numero_dois < numero_tres:
    menor = numero_dois
if numero_tres < numero_um and numero_tres < numero_dois:
    menor = numero_tres

maior = numero_um
if numero_dois > numero_um and numero_dois > numero_tres:   
    maior = numero_dois
if numero_tres > numero_um and numero_tres > numero_dois:
    maior = numero_tres
    
print(f'O menor número digitado foi {menor} e o maior foi {maior}')
