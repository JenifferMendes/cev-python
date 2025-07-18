"""
Faça um programa que leia nome e média de um aluno, guardando tambéma. situação
em um dicionário. no final mostre o conteudo da estrutura na tela.
"""


aluno = {}

aluno["Aluno"] = input("Nome: ")
aluno["Média"] = float(input(f"Média de {aluno["Aluno"]}: "))


if 10.0 > aluno["Média"] > 7.0:
    aluno["Situação"] = "Aprovado"
elif 4.9 < aluno["Média"] < 7.0:
    aluno["Situação"] = "Recuperação"
elif 0 <= aluno["Média"] <= 4.9:
    aluno["Situação"] = "Reprovado"
else:
    print("Média inválida.")

for k, v in aluno.items():
        print(f"{k} é igual a {v}")
