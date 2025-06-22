"""
Crie um programa onde o usuário digite uma expressão qualquer que use parenteses
seu aplicativo deverá analisar se a expressão passada está com os parênteses
abertos e fechados na ordem correta.
"""


expressao = input("Digite uma expressão: ")

parenteses = 0
for n in expressao:
    if n == ")":
        parenteses -= 1
    elif n == "(":
        parenteses += 1
    if parenteses < 0:
        break

if parenteses == 0:
    print("Sua expressão está certa.")
else:
    print("Sua expressão está errada.")
print("fim")
