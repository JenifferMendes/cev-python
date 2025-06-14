"""
Crie um programa que leia uma frase qualquer e diga se ela é um palindromo,
desconsiderando os espaços.
"""


frase = input("Digite uma frase: ").strip().replace(" ", "")

tamanho = len(frase)
contrario = frase[tamanho::-1]

palindromo = True
for c in range(0, tamanho):
    if frase[c] != contrario[c]:
       palindromo = False

print(f"A frase é um palindromo: {palindromo}")
