"""Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre
a sua média"""

nota_um = int(input('Digite a primeira nota: '))
nota_dois = int(input('Digite a segunda nota: '))

media_aluno = (nota_um + nota_dois) / 2
print(f'A média do aluno é igual a {media_aluno}')