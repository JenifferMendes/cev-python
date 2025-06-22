"""
Crie um programa onde o usuário possa digitar varios valores númericos e
cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores unicos digitados, em ordem cescente.
"""


numeros = []

opcoes = ["S", "N"]
continuar = ""

while True:
    numero = int(input("Digite um número: "))
    if numero in numeros:
        print("Número duplicado, não foi adicionado a lista.")
    else:
        numeros.append(numero)
        print("Número adicionado com sucesso.")
    continuar = input("Deseja continuar? [S/N]").strip().upper()
    while continuar not in opcoes:
        continuar = input(
            "Tente novamente. Deseja continuar? [S/N]"
        ).strip().upper()
    if continuar == "N":
        break

numeros.sort()
print(f"Você digitou os valores: {numeros}")
