"""
Crie um programa onde o usuário possa digitar sete valores númericos e cadastre
-os em uma lista única que mantenha separados os valores pares e impares.
No final, mostre os valores pares e impares em ordem crescente.
"""


numeros = [[],[]]
dash = "\n" + "=" * 50 + "\n"

for c in range(0, 7):
    numero = int(input(f"Digite o {c + 1}º valor: "))
    if numero % 2 == 0:
        numeros[0].append(numero)
    else:
        numeros[1].append(numero)

print(dash)
print(numeros)

numeros[0].sort()
numeros[1].sort()

print(
    f"Os valores pares digitados foram: {numeros[0]}.\n"
    f"Os valores impares digitados foram: {numeros[1]}."
)
