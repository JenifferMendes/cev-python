"""Faça um programa qeu leia um ângulo qualquer e mostre na tela o valor do seno,
cosseno e tangente desse ângulo"""


import math


angulo = float(input('Digite um ângulo: '))

cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
seno = math.sin(math.radians(angulo))

print(f'O ângulo é {angulo}')
print(f'O seu cosseno é {cosseno:.2f}')
print(f'O seu seno é {seno:.2f}')
print(f'A sua tangente é {tangente:.2f}')
