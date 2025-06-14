"""
Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi
o maior e o menor peso lidos.
"""


for c in range(0, 5):
    peso = float(input("Digite o peso: (kg) "))
    if c == 0:
        maior = menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print(f"O maior peso foi: {maior:.2f}kg e o menor {menor:.2f}kg.")
