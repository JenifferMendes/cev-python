"""
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas
daqueles que forem pares.Se o valor digitado for impar.
"""


soma = 0
for c in range(0, 6):
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        soma = soma + numero
print(f"A soma dos números pares é: {soma}.")
