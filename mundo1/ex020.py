"""O mesmo professor do desafio anterior quer sortear a ordem de apresentação de 
trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre
a ordem sorteada"""


import random


aluno1 = str(input('Digite o nome do primeiro aluno: '))
aluno2 = str(input('Digite o nome do segundo aluno: '))
aluno3 = str(input('Digite o nome do terceiro aluno: '))
aluno4 = str(input('Digite o nome do quarto aluno: '))

alunos = [aluno1, aluno2, aluno3, aluno4]

alunos_sorteados = random.sample(alunos, 4)

print(f'A ordem dos alunos que foi sorteada é {alunos_sorteados}')
