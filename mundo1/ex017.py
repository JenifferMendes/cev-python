"""Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
de um triângulo retângulo, calcule e mostre o comprimento da hiponetusa"""


cateto_oposto = float(input('Digite o comprimento do cateto oposto: '))
cateto_adjacente = float(input('Digite o comprimento do cateto adjacente: '))

soma_catetos = (cateto_oposto ** 2) + (cateto_adjacente ** 2)
hipotenusa = soma_catetos ** 0.5

print(f'O comprimento da hipotenusa é {hipotenusa:.2f}')
