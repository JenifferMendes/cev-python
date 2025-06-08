"""
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
de um triângulo retângulo, calcule e mostre o comptimento  da hipotenusa.
"""


from math import hypot


cateto_oposto = int(input("Digite o cateto oposto: "))
cateto_adjacente = int(input("Digite o cateto adjacente: "))

hipotenusa_teste = hypot(cateto_oposto,cateto_adjacente)

print(
    f"O cateto adjacente é {cateto_adjacente},o cateto oposto {cateto_oposto}"
    f",e a hipotenusa é {hipotenusa_teste:.0f}"
)
