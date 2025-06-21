"""
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma
tupla. No final, mostre:

a) Quantas vezes apareceu o valor 9.
b) Em que posição foi digitado o primeiro valor 3.
c) Quais foram os números pares.
"""


numeros = (
    int(input("Digite um número: ")), int(input("Digite um número: ")),
    int(input("Digite um número: ")), int(input("Digite um número: ")),
)

print(f"Os números digitados foram: {numeros}.")

if numeros.count(9) == 0:
    print("Não teve número 9.")
elif numeros.count(9) == 1:
    print("O número nove aparece apenas uma vez.")
else:
    print(f"Teve {numeros.count(9)} números noves.")

if 3 in numeros:
    print(f"O primeiro 3 aparece na posição: numeros[{numeros.index(3)}].")
else:
    print("Não teve número 3.")

pares = 0
for numero in numeros:
    if numero % 2 == 0:
        pares += 1
if pares == 0:
    print("Não teve pares.")
elif pares == 1:
    print("Teve apenas um número par.")
else:
    print(f"Teve {pares} números pares.")

print("Fim")
