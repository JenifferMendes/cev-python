"""
Desenvolva um programa que leia o comprimento de três retas e diga ao usuario
se elas podem ou não formar um triângulo.
"""


reta1 = float(input("Digite o comprimento da reta1:"))
reta2 = float(input("Digite o comprimento da reta2:"))
reta3 = float(input("Digite o comprimento da reta3:"))

if reta1 + reta2 > reta3 and reta2 + reta3 > reta1 and reta1 + reta3 > reta2:
    print("Pode formar uma triângulo")
else:
    print("Não pode formar um triângulo")
