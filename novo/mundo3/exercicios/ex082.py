"""
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares
e os valores impares digitados. respectivamente.
ao final, mostre o contéudo das três listas geradas.
"""


pares = []
impares = []
numeros = []
opcoes = ["S", "N"]

while True:
    numero = int(input("Digite um número: "))
    numeros.append(numero)
    continuar = " "
    while continuar not in opcoes:
        continuar = input("Deseja continuar? [S/N]").strip().upper()
    if continuar == "N":
        break

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print(
    f"A lista digitada foi: {numeros}.\n"
    f"A lista de impares é: {impares}.\n"
    f"A lista de pares é: {pares}."
)
