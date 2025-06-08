"""
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do
seno, cosseno e tangente desse ângulo.
"""


from math import radians, sin, cos, tan


angulo = float(input("Digite um ângulo: "))

rad = radians(angulo)

sen = (sin(rad))
cos = (cos(rad))
tan = (tan(rad))


print(
    f"O angulo {angulo} tem o seno{sen:,.2f}, cosseno{cos:,.2f} e tangente {tan:,.2f}"
)