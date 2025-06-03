"""Desenvolva um programa que leia o comprimento de três retas e diga ao usuário
se elas podem ou não formar um triângulo."""


reta_um = int(input('Digite o comprimento um: '))
reta_dois = int(input('Digite o comprimento dois: '))
reta_tres = int(input('Digite o comprimento tres: '))

if (
    (reta_um + reta_dois) > reta_tres 
    and (reta_dois + reta_tres) > reta_um 
    and (reta_um + reta_tres) > reta_dois
):
    print(f'Pode formar um triângulo')
else:
    print(f'Não pode formar um triângulo')
