"""
Faça um programa que leia nome e média de um aluno, guardando tambéma. situação
em um dicionário. no final mostre o conteudo da estrutura na tela.
"""


aluno = {}

aluno["Aluno"] = input("Nome: ")
aluno["Média"] = float(input(f"Média de {aluno["Aluno"]}: "))


if 100 > aluno["Média"] > 70:
    aluno["Situação"] = "Aprovado"
elif 49 < aluno["Média"] < 70:
    aluno["Situação"] = "Recuperação"
elif 0 <= aluno["Média"] <= 49:
    aluno["Situação"] = "Reprovado"
else:
    print("Média inválida.")

for k, v in aluno.items():
        print(f"{k} é igual a {v}")
