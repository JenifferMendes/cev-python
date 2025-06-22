"""
Faça um programa que leia 5 valores númericos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas
posições na lista.
"""


dash = "=" * 50 + "\n"
numeros = []

for posicao in range(0,5):
    numero = int(input(f"Digite um valor para a posição {posicao}: "))
    numeros.append(numero)

maior = max(numeros)
menor = min(numeros)

posicoes_maior = []
posicoes_menor = []

for posicao, numero in enumerate(numeros):
    if numero == maior:
        posicoes_maior.append(posicao)
    if numero == menor:
        posicoes_menor.append(posicao)

print(
    dash,
    f"\bVocê digitou os valores: {numeros}.\n"
    f"O maior valor digitado foi {maior} na posicao: {posicoes_maior}.\n"
    f"O menor valor digitado foi {menor} nas posicão: {posicoes_menor}."
)
