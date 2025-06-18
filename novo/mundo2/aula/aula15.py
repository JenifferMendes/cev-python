"""
laços de repetição parte 03
"""


soma = 0
while True:
    numero = int(input("Digite um número: "))
    if numero == 999:
        break
    soma += numero
print("Acabou", soma)
