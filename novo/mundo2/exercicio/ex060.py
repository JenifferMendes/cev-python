"""
faça um programa que leia um número qualquer e mostre o seu fatorial.
5! = 5x4x3x2x1 = 120
tente fazer com for e while
"""


numero = numero_for = int(input("Digite um número: "))

fatorial = fatorial_for = 1
print(f"O fatorial de {numero} ", end="")
while numero != 1:
    fatorial *= numero
    numero -= 1
print(f"é igual a {fatorial} usando o while.")

for c in range(1, numero_for + 1):
    fatorial_for *= c
    #print(c,fatorial_for, numero_for)
print(f"Com o for, o fatorial de {numero_for} é {fatorial_for}.")
