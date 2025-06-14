"""
Faça um programa que leia um número inteiro e diga se ele é ou não um número
primo.
primo : divisivel por 1 e por ele mesmo.
"""


numero = int(input("Digite um número: "))

eh_primo = True

for c in range(2, numero):
    if numero % c == 0:
        eh_primo = False

if eh_primo:
    print(f"{numero} é um número primo")
else:
    print(f"{numero} não é um número primo")
