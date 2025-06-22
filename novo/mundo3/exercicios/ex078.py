"""
Faça um programa que leia 5 valores númericos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas
posições na lista.
"""


dash = "=" * 30 + "\n"
numeros = []
for numero in range(0,5):
    numero = int(input(f"Digite um valor para a posição {numero}: "))
    numeros.append(numero)
print(dash)
print(f"Você digitou os valores: {numeros}")
maior = max(numeros)
menor = min(numeros)
print(f"O maior valor digitado foi {maior} na posicao: {numeros.index(maior)}")
print(f"O menor valor digitado foi {menor} nas posicão: {numeros.index(menor)}")