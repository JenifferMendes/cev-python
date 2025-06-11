"""
Faça um programa que leia 3 números e mostre qual é o maior e qual é menor.
"""


numero_um = int(input("Digite o número1: "))
numero_dois = int(input("Digite o número2: "))
numero_tres = int(input("Digite um número3: "))

if numero_um > numero_dois > numero_tres:
    print(f"O número1: {numero_um} é o maior" )
    print(f"O número3: {numero_tres} é o menor" )
elif numero_um < numero_dois < numero_tres:
    print(f"O número3: {numero_tres} é o maior" )
    print(f"O número1: {numero_um} é o menor" )
elif numero_dois < numero_um < numero_tres:
    print(f"O número3: {numero_tres} é o maior" )
    print(f"O número2: {numero_dois} é o menor" )
elif numero_dois > numero_tres > numero_um:
    print(f"O número2: {numero_dois} é o maior" )
    print(f"O número1: {numero_um} é o menor" )
else:
    print("tem números iguais")
