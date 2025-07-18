"""
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os
dados de cada pessoa em um dicionario e todos os dicionarios em uma lista.
no final, mostre:
a) quantas pessoas foram cadastradas.
b) a media de idade do grupo.
c) uma lista com todas as mulheres.
d) uma lista com todas as pessoas com idade acima da media.
"""

pessoas = []
mulher = []
soma = 0


while True:
    pessoa = {}
    pessoa["nome"] = input("Nome: ")
    sexo = ["F", "M"]
    pessoa["sexo"] = " "
    while pessoa["sexo"] not in sexo:
        pessoa["sexo"] = input("Sexo [F/M]: ").strip().upper()
        if pessoa["sexo"] not in sexo:
            print("ERRO! Por favor, digite apenas F ou M.")
    pessoa["idade"] = int(input("Idade: "))
    pessoas.append(pessoa.copy())
    opcao = ["S", "N"]
    continuar = " "
    while continuar not in opcao:
        continuar = input("Quer continuar? [S/N]").strip().upper()
        if continuar not in opcao:
            print("ERRO! Resposta apenas S ou N.")
    if continuar == "N":
        break
    
tamanho = len(pessoas)

for c in range(0, tamanho):
    soma += pessoas[c]["idade"]
    if pessoas[c]["sexo"] == "F":
        mulher.append(pessoas[c]["nome"])

media = soma / tamanho

print("=-" * 30)
print(f"A) O grupo tem {tamanho} pessoas.")
print(f"B) A média de idade é de {media:.2f} anos.")
print(f"C) As mulheres cadastradas foram: {mulher}")
print("D)Lista das pessoas que estão acima da média: ")

for i,v in enumerate(pessoas):
    for k,v in pessoas[i].items():
        if pessoas[i]["idade"] > media:
            print(f"{k} = {v};", end=" ")
    print()
print()
