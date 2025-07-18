"""
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e
cadastre-os (com idade)em um dicionário se por acaso a ctps for diferente de
zero, o dicionário receberá também o ano de contratação e o salario.
calcule a acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
35 anos de contribuição para aposentar.
"""


from datetime import date


ano = date.today().year

pessoa = {}

pessoa["nome"] = input("Digite o nome: ")
nascimento = int(input("Digite o ano nascimento: "))
pessoa["idade"] = ano - nascimento
pessoa["ctps"] = int(input("Carteira de trabalho [0 não tem]: "))

if pessoa["ctps"] != 0:
    pessoa["contratacao"] = int(input("Ano de contratação: "))
    pessoa["salario"] = float(input("Salário: "))
    pessoa["aposentadoria"] = pessoa["contratacao"] - nascimento + 35

print(pessoa)

for k,v in pessoa.items():
    print(f"{k} tem o valor {v}")
