"""
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em
uma lista composta. No final, mostre um boletim contendo a média de cada um e
permita que o usuário possa mostrar as notas de cada aluno individualmente.
"""


alunos = []
aluno = []
notas = []
opcoes = ["S", "N"]
dash = "\n" + "=" * 50 + "\n"
opcao = 0

while True:
    nome = input("Digite o nome do aluno: ")
    nota_um = float(input("Digite a nota 1: "))
    nota_dois = float(input("Digite a nota 2: "))
    media = (nota_um + nota_dois) / 2
    aluno.append(nome)
    notas.append(nota_um)
    notas.append(nota_dois)
    aluno.append(notas[:])
    aluno.append(media)
    alunos.append(aluno[:])
    aluno.clear()
    notas.clear()
    continuar = " "
    while continuar not in opcoes:
        continuar = input("Há mais alunos? [S/N]").strip().upper()
    if continuar == "N":
        break

print(dash)
print("No.  NOME               MÉDIA")
for pos, aluno in enumerate(alunos):
    print(f"{pos:<4} {aluno[0]:<18} {aluno[2]:>}")

while True:
    print(dash)
    nota = int(input("Mostrar notas de qual aluno? (999 interrompe): "))
    if nota == 999:
        print("FINALIZANDO...")
        break
    if nota <= len(alunos) - 1:
        print(f"Notas de {alunos[nota][0]} são: {alunos[nota][1]}")
