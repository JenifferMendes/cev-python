"""
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa
cadastrada, o programa pergunta se o usuário quer ou não continuar.
No final, mostre:
a) quantas pessoas tem mais de 18 anos.
b) quantos homens foram cadastrados.
c) quantas mulheres tem menos de 20 anos.
"""

dash = "\n" + "=" * 20 + "\n"

total = maiores = homens = mulheres = 0

while True:
    print(dash)
    print( "CADASTRANDO NOVA PESSOA")
    nome = str(input("Digite o nome: ")).strip().capitalize()
    idade = int(input("Digite a idade: "))
    sexo = str(input(
        "Qual é o sexo da pessoa: [M/H]"
    )).strip().upper()
    print(nome, idade)
    total += 1
    if idade >= 18:
        maiores += 1
    if sexo == "H":
        homens += 1
    if sexo == "M" and idade < 20:
        mulheres += 1
        print(mulheres)
    opcao = input("Deseja continuar? [S/N]").strip().upper()[0]
    if opcao == "N":
        break
print(
    f"O total de pessoas cadastradas foi de: {total}. \n"
    f"A quantidade de pessoas maiores de 18 anos é: {maiores}. \n"
    f"A quantidade de homens cadastrados foi de: {homens}. \n"
    f"A quantidade de mulheres menores de 20 anos foi de: {mulheres}."
)