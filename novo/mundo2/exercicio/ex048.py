"""
Faça um programa que calcule a soma entre todos os números
impares que são multiplos de tres e que se encontram no intervalo de 1 até 500.
"""


soma = 0

for c in range(1, 500, 2):
    if c % 3 == 0:
        soma = soma + c
        print(c)
print(f"Todos os números multiplos de 1 a 500. A soma {soma}.")
