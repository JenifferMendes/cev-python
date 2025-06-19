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
    nome = input("Digite o nome: ").strip().capitalize()
    idade = int(input("Digite a idade: "))
    opcao = ["F","M"]
    sexo = " "
    while sexo not in opcao:
        sexo = input(
            "Qual é o sexo da pessoa: [F/M]"
        ).strip().upper()
    total += 1
    if idade >= 18:
        maiores += 1
    if sexo == "M":
        homens += 1
    if sexo == "F" and idade < 20:
        mulheres += 1
    
    resposta = ["S","N"]
    continuar = " "
    while continuar not in resposta:
        continuar = input("Deseja continuar? [S/N]").strip().upper()
    if "N" in continuar:
        break
print(
    f"O total de pessoas cadastradas foi de: {total}. \n"
    f"A quantidade de pessoas maiores de 18 anos é: {maiores}. \n"
    f"A quantidade de homens cadastrados foi de: {homens}. \n"
    f"A quantidade de mulheres menores de 20 anos foi de: {mulheres}."
)
