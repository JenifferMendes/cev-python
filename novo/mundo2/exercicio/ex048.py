"""
Faça um programa que calcule a soma entre todos os números
impares que são multiplos de tres e que se encontram no intervalo de 1 até 500.
"""


soma = 0
numeros = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        soma = soma + c
        numeros = numeros + 1
        #print(c, numeros)
print(f"Todos os {numeros} números multiplos de 1 a 500 tem a soma de: {soma}.")
