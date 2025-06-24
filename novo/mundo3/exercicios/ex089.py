"""
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em
uma lista composta. No final, mostre um boletim contendo a média de cada um e
permita que o usuário possa mostrar as notas de cada aluno individualmente.
"""


alunos = []
aluno = []
notas = []
opcao = ["S", "N"]


while True:
    nome = input("Digite o nome do aluno: ")
    nota_um = float(input("Digite a nota 1: "))
    nota_dois = float(input("Digite a nota 2: "))
    aluno.append(nome)
    notas.append(nota_um)
    notas.append(nota_dois)
    aluno.append(notas[:])
    alunos.append(aluno[:])
    aluno.clear()
    notas.clear()
    continuar = " "
    while continuar not in opcao:
        continuar = input("Deseja continuar? [S/N]").strip().upper()
    if continuar == "N":
        break

print("Fim", aluno, notas, alunos)
