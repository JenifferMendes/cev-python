"""
faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma 
lista. no final mostre:
a) quantas pessoas foram cadastradas.
b) uma listagem com as pessoas mais pesadas.
c) uma listagem com as pessoas mais leves.
"""

pessoas_cadastradas = []
cadastro = []
posicoes_maior = []
posicoes_menor = []
opcoes = ["S", "N"]
maior_peso = menor_peso = quantidade_pessoas = 0
dash = "\n" + "=" * 40 + "\n"

while True:
    nome = input("Nome: ")
    peso = float(input("Peso: kg"))
    cadastro.append(nome)
    cadastro.append(peso)
    pessoas_cadastradas.append(cadastro[:])
    cadastro.clear()
    quantidade_pessoas += 1
    continuar = " "
    while continuar not in opcoes:
        continuar = input("Quer continuar? [S/N] ").strip().upper()
    if continuar == "N":
        break

for posicao, pessoa in enumerate(pessoas_cadastradas):
    if posicao == 0:
        menor_peso = maior_peso = pessoa[1] 
    if pessoa[1] > maior_peso:
        maior_peso = pessoa[1]
        print(maior_peso)
    elif pessoa[1] < menor_peso:
        menor_peso = pessoa[1]
        print(menor_peso)

for posicao, pessoa in enumerate(pessoas_cadastradas):
    if pessoa[1] == maior_peso:
        posicoes_maior.append(pessoa[0])
    if pessoa[1] == menor_peso:
        posicoes_menor.append(pessoa[0])

print(
    dash,
    f"\bAs pessoas cadastradas: {pessoas_cadastradas}.\n" 
    f"Ao todo, você cadastrou {quantidade_pessoas} pessoas.\n"
    f"O maior peso foi de {maior_peso:.2f}kg, peso de {posicoes_maior}.\n"  
    f"O menor peso foi de {menor_peso:.2f}kg, peso de {posicoes_menor}.\n"
    "fim"
)
