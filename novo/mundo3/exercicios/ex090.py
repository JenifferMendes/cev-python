"""
Faça um programa que leia nome e média de um aluno, guardando tambéma. situação
em um dicionário. no final mostre o conteudo da estrutura na tela.
"""


aluno = {}

nome = input("Nome: ")
aluno["Aluno"] = nome
media = float(input(f"Média de {nome}: "))
aluno["Média"] = media

if 100 > media > 70:
    aluno["Situação"] = "Aprovado"
elif 49 < media < 70:
    aluno["Situação"] = "Recuperação"
elif 0 <= media <= 49:
    aluno["Situação"] = "Reprovado"
else:
    print("Média inválida.")

for k, v in aluno.items():
        print(f"{k} é igual a {v}")
