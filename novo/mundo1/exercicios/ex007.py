"""
Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre
a sua média.
"""


nota1 = float(input("Digite sua nota: "))
nota2 = float(input("Digite sua segunda nota: "))

media = (nota1 + nota2) / 2

print(f"A média das notas {nota1} e {nota2} é igual a {media:.2f}")
