"""
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas
daqueles que forem pares.Se o valor digitado for impar.
"""


soma = 0
contador = 0
for c in range(0, 6):
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        soma += numero
        contador += 1
print(f"A soma dos {contador} números pares é: {soma}.")
