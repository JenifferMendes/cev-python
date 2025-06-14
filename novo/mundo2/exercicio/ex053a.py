"""
Crie um programa que leia uma frase qualquer e diga se ela é um palindromo,
desconsiderando os espaços.
"""


frase = input("Digite uma frase: ").strip().replace(" ", "")

contrario = frase[::-1]

print(f"A frase é um palindromo: {frase == contrario}")
