"""
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o
maior valor que estão na tupla.
"""


from random import randint


numeros = (
    randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10)
)

print(f"Os números sorteados foram: ", end="")

for numero in numeros:
    print(f"{numero} ", end="" )

ordem = sorted(numeros)

print(
    f"\nO maior valor sorteado foi: {ordem[-1]}.\n"
    f"O menor valor sorteado foi: {ordem[0]}."
)
